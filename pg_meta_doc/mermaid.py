from __future__ import annotations

import re

from pg_meta_doc.db import SchemaSnapshot, TableSpec

_NON_ALNUM_RE = re.compile(r"[^a-zA-Z0-9_]")


def render_mermaid(snapshot: SchemaSnapshot) -> str:
    lines = ["graph LR"]

    for table in snapshot.tables:
        lines.append(f'  {node_id(table)}["{_node_label(table)}"]')

    for table in snapshot.tables:
        for foreign_key in table.foreign_keys:
            target_name = (
                f"{foreign_key.referred_schema or table.schema}.{foreign_key.referred_table}"
            )
            label = ", ".join(foreign_key.columns) or "fk"
            lines.append(
                f"  {node_id(table)} -->|{_escape_label(label)}| {node_id_from_name(target_name)}"
            )

    return "\n".join(lines)


def node_id(table: TableSpec) -> str:
    return node_id_from_name(table.qualified_name)


def node_id_from_name(name: str) -> str:
    return _NON_ALNUM_RE.sub("_", name)


def _node_label(table: TableSpec) -> str:
    field_lines = []
    for column in table.columns[:5]:
        tags: list[str] = []
        if column.name in table.primary_key:
            tags.append("PK")
        if any(column.name in foreign_key.columns for foreign_key in table.foreign_keys):
            tags.append("FK")
        suffix = f" ({', '.join(tags)})" if tags else ""
        field_lines.append(f"{column.name}{suffix}")

    if len(table.columns) > 5:
        field_lines.append("...")

    payload = [table.qualified_name, *field_lines]
    return _escape_label("\\n".join(payload))


def _escape_label(value: str) -> str:
    return value.replace('"', "'")
