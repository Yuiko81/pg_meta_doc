from pg_meta_doc.db import ColumnSpec, IndexSpec, SchemaSnapshot, TableSpec
from pg_meta_doc.rules import lint_schema


def test_lint_schema_finds_expected_issues():
    snapshot = SchemaSnapshot(
        generated_at="2026-01-01T00:00:00+00:00",
        source="postgresql://user:***@localhost:5432/app",
        tables=[
            TableSpec(
                schema="public",
                name="profiles",
                columns=[
                    ColumnSpec(name="id", data_type="BIGINT", nullable=False),
                    ColumnSpec(name="user_id", data_type="BIGINT", nullable=False),
                    ColumnSpec(name="usr_id", data_type="BIGINT", nullable=True),
                    ColumnSpec(name="name", data_type="TEXT", nullable=True),
                    ColumnSpec(name="created_at", data_type="TIMESTAMP", nullable=True),
                ],
                primary_key=["user_id"],
                foreign_keys=[],
                indexes=[IndexSpec(name="profiles_pkey", columns=["user_id"], is_primary=True)],
                estimated_rows=5_000,
            ),
            TableSpec(
                schema="public",
                name="audit_logs",
                columns=[
                    ColumnSpec(name="event_id", data_type="BIGINT", nullable=False),
                    ColumnSpec(name="user_id", data_type="BIGINT", nullable=False),
                ],
                primary_key=[],
                foreign_keys=[],
                indexes=[],
                estimated_rows=50,
            ),
        ],
    )

    issues = lint_schema(snapshot)
    codes = {(issue.table, issue.code) for issue in issues}

    assert ("public.profiles", "NON_PRIMARY_ID_COLUMN") in codes
    assert ("public.profiles", "SIMILAR_IDENTIFIER_COLUMNS") in codes
    assert ("public.profiles", "SUSPICIOUS_NULLABLE_COLUMN") in codes
    assert ("public.profiles", "LARGE_TABLE_UNINDEXED_FK") in codes
    assert ("public.audit_logs", "MISSING_PRIMARY_KEY") in codes
    assert ("public.audit_logs", "NO_INDEXES") in codes
