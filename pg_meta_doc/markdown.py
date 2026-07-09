from __future__ import annotations

from collections import defaultdict

from pg_meta_doc.db import Issue, SchemaSnapshot, TableSpec
from pg_meta_doc.mermaid import render_mermaid


def render_markdown(snapshot: SchemaSnapshot, issues: list[Issue]) -> str:
    issues_by_table: dict[str, list[Issue]] = defaultdict(list)
    for issue in issues:
        issues_by_table[issue.table].append(issue)

    lines = [
        "# PostgreSQL Schema Report",
        "",
        f"- Generated at: `{snapshot.generated_at}`",
        f"- Source: `{snapshot.source or 'unknown'}`",
        f"- Tables: `{len(snapshot.tables)}`",
        f"- Issues: `{len(issues)}`",
        "",
        "## ERD",
        "",
        "```mermaid",
        render_mermaid(snapshot),
        "```",
        "",
        "## Problems",
        "",
    ]

    if issues:
        for issue in issues:
            lines.append(
                f"- `{issue.severity.upper()}` `{issue.code}` in `{issue.table}`: {issue.message}"
            )
    else:
        lines.append("- No issues found.")

    for table in snapshot.tables:
        lines.extend(
            [
                "",
                f"## {table.qualified_name}",
                "",
                f"- Estimated rows: `{table.estimated_rows if table.estimated_rows is not None else 'unknown'}`",
                f"- Primary key: `{', '.join(table.primary_key) if table.primary_key else 'none'}`",
                "",
                "### Columns",
                "",
                "| Column | Type | Nullable | Default | Notes |",
                "| --- | --- | --- | --- | --- |",
            ]
        )
        for column in table.columns:
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{column.name}`",
                        f"`{column.data_type}`",
                        "yes" if column.nullable else "no",
                        f"`{column.default}`" if column.default is not None else "",
                        _column_notes(table, column.name),
                    ]
                )
                + " |"
            )

        lines.extend(["", "### Foreign Keys", ""])
        if table.foreign_keys:
            for foreign_key in table.foreign_keys:
                columns = ", ".join(f"`{name}`" for name in foreign_key.columns)
                target_columns = ", ".join(f"`{name}`" for name in foreign_key.referred_columns)
                target_table = (
                    f"{foreign_key.referred_schema or table.schema}.{foreign_key.referred_table}"
                )
                lines.append(f"- {columns} -> `{target_table}` ({target_columns})")
        else:
            lines.append("- None")

        lines.extend(["", "### Indexes", ""])
        if table.indexes:
            for index in table.indexes:
                lines.append(f"- {_format_index(index)}")
        else:
            lines.append("- None")

        lines.extend(["", "### Problems", ""])
        table_issues = issues_by_table.get(table.qualified_name, [])
        if table_issues:
            for issue in table_issues:
                lines.append(f"- `{issue.code}`: {issue.message}")
        else:
            lines.append("- None")

    return "\n".join(lines).strip() + "\n"


def _column_notes(table: TableSpec, column_name: str) -> str:
    notes: list[str] = []
    if column_name in table.primary_key:
        notes.append("PK")
    for foreign_key in table.foreign_keys:
        if column_name in foreign_key.columns:
            target = f"{foreign_key.referred_schema or table.schema}.{foreign_key.referred_table}"
            notes.append(f"FK -> {target}")
    if any(column_name in index.columns for index in table.indexes):
        notes.append("Indexed")
    return ", ".join(notes)


def _format_index(index) -> str:
    flags: list[str] = []
    if index.is_primary:
        flags.append("primary")
    if index.is_unique:
        flags.append("unique")
    prefix = f"`{index.name}`"
    if flags:
        prefix += f" ({', '.join(flags)})"

    if index.columns:
        columns = ", ".join(f"`{name}`" for name in index.columns)
        return f"{prefix} on {columns}"

    if index.definition:
        return f"{prefix} using `{index.definition}`"

    return prefix
