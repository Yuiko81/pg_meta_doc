from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

_POSTGRES_SCHEME_RE = re.compile(r"^postgres(?:ql)?(?:\+[a-z0-9_]+)?://", re.IGNORECASE)


@dataclass(slots=True)
class ColumnSpec:
    name: str
    data_type: str
    nullable: bool
    default: str | None = None


@dataclass(slots=True)
class ForeignKeySpec:
    columns: list[str]
    referred_table: str
    referred_columns: list[str]
    name: str | None = None
    referred_schema: str | None = None


@dataclass(slots=True)
class IndexSpec:
    name: str
    columns: list[str]
    is_unique: bool = False
    is_primary: bool = False
    definition: str | None = None


@dataclass(slots=True)
class TableSpec:
    schema: str
    name: str
    columns: list[ColumnSpec]
    primary_key: list[str]
    foreign_keys: list[ForeignKeySpec]
    indexes: list[IndexSpec]
    estimated_rows: int | None = None

    @property
    def qualified_name(self) -> str:
        return f"{self.schema}.{self.name}"

    def column_names(self) -> list[str]:
        return [column.name for column in self.columns]


@dataclass(slots=True)
class Issue:
    code: str
    severity: str
    table: str
    message: str
    columns: list[str] = field(default_factory=list)


@dataclass(slots=True)
class SchemaSnapshot:
    generated_at: str
    tables: list[TableSpec]
    source: str | None = None
    warnings: list[str] = field(default_factory=list)


def normalize_dsn(dsn: str) -> str:
    if "://" not in dsn:
        return dsn
    return _POSTGRES_SCHEME_RE.sub("postgresql+psycopg://", dsn, count=1)


def build_engine(dsn: str):
    try:
        from sqlalchemy import create_engine
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "SQLAlchemy is not installed. Run `pip install -e .[dev]` first."
        ) from exc

    return create_engine(normalize_dsn(dsn), future=True, pool_pre_ping=True)


def mask_dsn(dsn: str) -> str:
    try:
        from sqlalchemy.engine import make_url
    except ModuleNotFoundError:
        normalized = normalize_dsn(dsn)
        parts = urlsplit(normalized)
        if "@" not in parts.netloc:
            return normalized

        credentials, host = parts.netloc.rsplit("@", 1)
        if ":" in credentials:
            username, _password = credentials.split(":", 1)
            safe_netloc = f"{username}:***@{host}"
        else:
            safe_netloc = f"{credentials}@{host}"

        return urlunsplit((parts.scheme, safe_netloc, parts.path, parts.query, parts.fragment))

    return make_url(normalize_dsn(dsn)).render_as_string(hide_password=True)


def save_snapshot(snapshot: SchemaSnapshot, path: str | Path) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(asdict(snapshot), indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return target


def load_snapshot(path: str | Path) -> SchemaSnapshot:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    return snapshot_from_dict(payload)


def snapshot_from_dict(payload: dict[str, Any]) -> SchemaSnapshot:
    return SchemaSnapshot(
        generated_at=payload["generated_at"],
        source=payload.get("source"),
        warnings=list(payload.get("warnings", [])),
        tables=[
            TableSpec(
                schema=table["schema"],
                name=table["name"],
                primary_key=list(table.get("primary_key", [])),
                estimated_rows=table.get("estimated_rows"),
                columns=[ColumnSpec(**column) for column in table.get("columns", [])],
                foreign_keys=[
                    ForeignKeySpec(
                        columns=list(fk.get("columns", [])),
                        referred_table=fk["referred_table"],
                        referred_columns=list(fk.get("referred_columns", [])),
                        name=fk.get("name"),
                        referred_schema=fk.get("referred_schema"),
                    )
                    for fk in table.get("foreign_keys", [])
                ],
                indexes=[
                    IndexSpec(
                        name=index["name"],
                        columns=list(index.get("columns", [])),
                        is_unique=bool(index.get("is_unique", False)),
                        is_primary=bool(index.get("is_primary", False)),
                        definition=index.get("definition"),
                    )
                    for index in table.get("indexes", [])
                ],
            )
            for table in payload.get("tables", [])
        ],
    )
