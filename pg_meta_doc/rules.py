from __future__ import annotations

from collections import defaultdict

from pg_meta_doc.db import Issue, SchemaSnapshot, TableSpec

SUSPICIOUS_NULLABLE_NAMES = {
    "code",
    "created_at",
    "email",
    "name",
    "slug",
    "title",
    "updated_at",
}
IDENTIFIER_ALIASES = {
    "acct": "account",
    "addr": "address",
    "org": "organization",
    "usr": "user",
    "users": "user",
}
LARGE_TABLE_THRESHOLD = 1_000


def lint_schema(snapshot: SchemaSnapshot) -> list[Issue]:
    issues: list[Issue] = []
    for table in snapshot.tables:
        issues.extend(_check_missing_primary_key(table))
        issues.extend(_check_non_primary_id(table))
        issues.extend(_check_nullable_business_columns(table))
        issues.extend(_check_missing_indexes(table))
        issues.extend(_check_similar_identifier_columns(table))
        issues.extend(_check_large_table_identifier_indexes(table))

    severity_order = {"error": 0, "warning": 1, "info": 2}
    return sorted(
        issues,
        key=lambda issue: (
            severity_order.get(issue.severity, 99),
            issue.table,
            issue.code,
            issue.columns,
        ),
    )


def _check_missing_primary_key(table: TableSpec) -> list[Issue]:
    if table.primary_key:
        return []
    return [
        Issue(
            code="MISSING_PRIMARY_KEY",
            severity="error",
            table=table.qualified_name,
            message="Table does not define a primary key.",
        )
    ]


def _check_non_primary_id(table: TableSpec) -> list[Issue]:
    issues: list[Issue] = []
    for column in table.columns:
        if column.name == "id" and column.name not in table.primary_key:
            issues.append(
                Issue(
                    code="NON_PRIMARY_ID_COLUMN",
                    severity="warning",
                    table=table.qualified_name,
                    message="Column `id` exists but is not part of the primary key.",
                    columns=[column.name],
                )
            )
    return issues


def _check_nullable_business_columns(table: TableSpec) -> list[Issue]:
    issues: list[Issue] = []
    for column in table.columns:
        if column.nullable and column.name in SUSPICIOUS_NULLABLE_NAMES:
            issues.append(
                Issue(
                    code="SUSPICIOUS_NULLABLE_COLUMN",
                    severity="warning",
                    table=table.qualified_name,
                    message=f"Nullable column `{column.name}` looks business-critical.",
                    columns=[column.name],
                )
            )
    return issues


def _check_missing_indexes(table: TableSpec) -> list[Issue]:
    if table.indexes:
        return []
    return [
        Issue(
            code="NO_INDEXES",
            severity="warning",
            table=table.qualified_name,
            message="Table has no indexes, including implicit primary key indexes.",
        )
    ]


def _check_similar_identifier_columns(table: TableSpec) -> list[Issue]:
    groups: dict[str, list[str]] = defaultdict(list)
    for column in table.columns:
        family = _identifier_family(column.name)
        if family is not None:
            groups[family].append(column.name)

    issues: list[Issue] = []
    for family, members in groups.items():
        unique_members = sorted(set(members))
        if len(unique_members) < 2:
            continue
        issues.append(
            Issue(
                code="SIMILAR_IDENTIFIER_COLUMNS",
                severity="warning",
                table=table.qualified_name,
                message=(
                    f"Columns look like duplicated identifier variants for `{family}`: "
                    + ", ".join(f"`{name}`" for name in unique_members)
                ),
                columns=unique_members,
            )
        )
    return issues


def _check_large_table_identifier_indexes(table: TableSpec) -> list[Issue]:
    if table.estimated_rows is None or table.estimated_rows < LARGE_TABLE_THRESHOLD:
        return []

    indexed_columns = {
        column_name
        for index in table.indexes
        for column_name in index.columns
    }
    issues: list[Issue] = []
    for column in table.columns:
        if not _looks_like_foreign_key_name(column.name):
            continue
        if column.name in indexed_columns:
            continue
        issues.append(
            Issue(
                code="LARGE_TABLE_UNINDEXED_FK",
                severity="error",
                table=table.qualified_name,
                message=(
                    f"Large table is missing an index on identifier-like column "
                    f"`{column.name}`."
                ),
                columns=[column.name],
            )
        )
    return issues


def _identifier_family(column_name: str) -> str | None:
    if not column_name.endswith("_id"):
        return None

    raw_base = column_name[:-3]
    normalized_tokens: list[str] = []
    for token in raw_base.split("_"):
        mapped = IDENTIFIER_ALIASES.get(token, token)
        if mapped.endswith("s") and len(mapped) > 3:
            mapped = mapped[:-1]
        normalized_tokens.append(mapped)

    return "_".join(normalized_tokens) + "_id"


def _looks_like_foreign_key_name(column_name: str) -> bool:
    return column_name.endswith("_id")
