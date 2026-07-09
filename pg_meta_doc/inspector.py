from __future__ import annotations

from datetime import datetime, timezone

from pg_meta_doc.db import (
    ColumnSpec,
    ForeignKeySpec,
    IndexSpec,
    SchemaSnapshot,
    TableSpec,
    build_engine,
    mask_dsn,
)

DEFAULT_EXCLUDED_SCHEMAS = {"information_schema", "pg_catalog"}

INDEX_QUERY = """
SELECT
    idx.relname AS index_name,
    ix.indisunique AS is_unique,
    ix.indisprimary AS is_primary,
    pg_get_indexdef(ix.indexrelid) AS definition,
    COALESCE(
        array_agg(att.attname ORDER BY ord.ordinality)
            FILTER (WHERE att.attname IS NOT NULL),
        ARRAY[]::text[]
    ) AS columns
FROM pg_class tbl
JOIN pg_namespace ns ON ns.oid = tbl.relnamespace
JOIN pg_index ix ON ix.indrelid = tbl.oid
JOIN pg_class idx ON idx.oid = ix.indexrelid
LEFT JOIN unnest(ix.indkey) WITH ORDINALITY AS ord(attnum, ordinality) ON TRUE
LEFT JOIN pg_attribute att
    ON att.attrelid = tbl.oid
   AND att.attnum = ord.attnum
WHERE ns.nspname = :schema
  AND tbl.relname = :table
GROUP BY idx.relname, ix.indisunique, ix.indisprimary, ix.indexrelid
ORDER BY idx.relname;
"""

ROW_ESTIMATE_QUERY = """
SELECT c.reltuples::bigint
FROM pg_class c
JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = :schema
  AND c.relname = :table;
"""


def inspect_database(
    dsn: str,
    schemas: list[str] | None = None,
    excluded_schemas: set[str] | None = None,
) -> SchemaSnapshot:
    try:
        from sqlalchemy import inspect
    except ModuleNotFoundError as exc:
        raise RuntimeError(
            "SQLAlchemy is not installed. Run `pip install -e .[dev]` first."
        ) from exc

    engine = build_engine(dsn)
    skip_schemas = excluded_schemas or DEFAULT_EXCLUDED_SCHEMAS

    try:
        with engine.connect() as connection:
            inspector = inspect(connection)
            available_schemas = sorted(
                name for name in inspector.get_schema_names() if name not in skip_schemas
            )
            selected_schemas = _resolve_schemas(available_schemas, schemas)

            tables: list[TableSpec] = []
            for schema in selected_schemas:
                for table_name in sorted(inspector.get_table_names(schema=schema)):
                    tables.append(
                        TableSpec(
                            schema=schema,
                            name=table_name,
                            columns=_load_columns(inspector, schema, table_name),
                            primary_key=_load_primary_key(inspector, schema, table_name),
                            foreign_keys=_load_foreign_keys(inspector, schema, table_name),
                            indexes=_load_indexes(connection, schema, table_name),
                            estimated_rows=_load_row_estimate(connection, schema, table_name),
                        )
                    )

            return SchemaSnapshot(
                generated_at=datetime.now(timezone.utc).isoformat(),
                source=mask_dsn(dsn),
                tables=sorted(tables, key=lambda table: table.qualified_name),
            )
    finally:
        engine.dispose()


def _resolve_schemas(
    available_schemas: list[str],
    requested_schemas: list[str] | None,
) -> list[str]:
    if not requested_schemas:
        return available_schemas

    missing = sorted(set(requested_schemas) - set(available_schemas))
    if missing:
        joined = ", ".join(missing)
        raise ValueError(f"Requested schemas were not found: {joined}")

    ordered = [schema for schema in available_schemas if schema in requested_schemas]
    return ordered


def _load_columns(inspector, schema: str, table_name: str) -> list[ColumnSpec]:
    columns: list[ColumnSpec] = []
    for raw in inspector.get_columns(table_name, schema=schema):
        default = raw.get("default")
        columns.append(
            ColumnSpec(
                name=raw["name"],
                data_type=str(raw["type"]),
                nullable=bool(raw.get("nullable", False)),
                default=None if default is None else str(default),
            )
        )
    return columns


def _load_primary_key(inspector, schema: str, table_name: str) -> list[str]:
    payload = inspector.get_pk_constraint(table_name, schema=schema)
    return list(payload.get("constrained_columns") or [])


def _load_foreign_keys(inspector, schema: str, table_name: str) -> list[ForeignKeySpec]:
    foreign_keys: list[ForeignKeySpec] = []
    for raw in inspector.get_foreign_keys(table_name, schema=schema):
        foreign_keys.append(
            ForeignKeySpec(
                name=raw.get("name"),
                columns=list(raw.get("constrained_columns") or []),
                referred_schema=raw.get("referred_schema") or schema,
                referred_table=raw["referred_table"],
                referred_columns=list(raw.get("referred_columns") or []),
            )
        )
    return foreign_keys


def _load_indexes(connection, schema: str, table_name: str) -> list[IndexSpec]:
    from sqlalchemy import text

    rows = connection.execute(
        text(INDEX_QUERY),
        {"schema": schema, "table": table_name},
    ).mappings()

    indexes: list[IndexSpec] = []
    for row in rows:
        indexes.append(
            IndexSpec(
                name=row["index_name"],
                columns=list(row["columns"] or []),
                is_unique=bool(row["is_unique"]),
                is_primary=bool(row["is_primary"]),
                definition=row["definition"],
            )
        )
    return indexes


def _load_row_estimate(connection, schema: str, table_name: str) -> int | None:
    from sqlalchemy import text

    row = connection.execute(
        text(ROW_ESTIMATE_QUERY),
        {"schema": schema, "table": table_name},
    ).first()
    if row is None or row[0] is None:
        return None
    return int(row[0])
