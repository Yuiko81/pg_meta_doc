from pg_meta_doc.db import (
    ColumnSpec,
    ForeignKeySpec,
    IndexSpec,
    Issue,
    SchemaSnapshot,
    TableSpec,
)
from pg_meta_doc.markdown import render_markdown


def test_render_markdown_contains_table_sections_and_mermaid():
    snapshot = SchemaSnapshot(
        generated_at="2026-01-01T00:00:00+00:00",
        source="postgresql://user:***@localhost:5432/app",
        tables=[
            TableSpec(
                schema="public",
                name="users",
                columns=[
                    ColumnSpec(name="id", data_type="BIGINT", nullable=False),
                    ColumnSpec(name="department_id", data_type="BIGINT", nullable=True),
                ],
                primary_key=["id"],
                foreign_keys=[
                    ForeignKeySpec(
                        name="users_department_id_fkey",
                        columns=["department_id"],
                        referred_schema="public",
                        referred_table="departments",
                        referred_columns=["department_id"],
                    )
                ],
                indexes=[
                    IndexSpec(name="users_pkey", columns=["id"], is_primary=True),
                    IndexSpec(name="idx_users_department_id", columns=["department_id"]),
                ],
                estimated_rows=42,
            ),
            TableSpec(
                schema="public",
                name="departments",
                columns=[ColumnSpec(name="department_id", data_type="BIGINT", nullable=False)],
                primary_key=["department_id"],
                foreign_keys=[],
                indexes=[
                    IndexSpec(
                        name="departments_pkey",
                        columns=["department_id"],
                        is_primary=True,
                    )
                ],
                estimated_rows=3,
            ),
        ],
    )
    issues = [
        Issue(
            code="SUSPICIOUS_NULLABLE_COLUMN",
            severity="warning",
            table="public.users",
            message="Nullable column `department_id` looks business-critical.",
            columns=["department_id"],
        )
    ]

    rendered = render_markdown(snapshot, issues)

    assert "# PostgreSQL Schema Report" in rendered
    assert "## public.users" in rendered
    assert "```mermaid" in rendered
    assert "public_users -->|department_id| public_departments" in rendered
    assert "`SUSPICIOUS_NULLABLE_COLUMN`" in rendered
