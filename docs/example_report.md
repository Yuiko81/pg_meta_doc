# PostgreSQL Schema Report

- Generated at: `2026-01-01T00:00:00+00:00`
- Source: `postgresql://dbdoc:***@localhost:54329/dbdoc`
- Tables: `4`
- Issues: `7`

## ERD

```mermaid
graph LR
  public_departments["public.departments\ndepartment_id (PK)\nname"]
  public_users["public.users\nid (PK)\nname\ndepartment_id (FK)\ncreated_at\nusr_id"]
  public_profiles["public.profiles\nid\nuser_id (PK, FK)\ndisplay_name"]
  public_audit_logs["public.audit_logs\nevent_id\nuser_id\nentity_id\ncreated_at\npayload"]
  public_users -->|department_id| public_departments
  public_profiles -->|user_id| public_users
```

## Problems

- `WARNING` `SUSPICIOUS_NULLABLE_COLUMN` in `public.users`: Nullable column `name` looks business-critical.
- `WARNING` `SUSPICIOUS_NULLABLE_COLUMN` in `public.users`: Nullable column `created_at` looks business-critical.
- `WARNING` `SIMILAR_IDENTIFIER_COLUMNS` in `public.users`: Columns look like duplicated identifier variants for `user_id`: `usr_id`, `users_id`
- `WARNING` `NON_PRIMARY_ID_COLUMN` in `public.profiles`: Column `id` exists but is not part of the primary key.
- `ERROR` `MISSING_PRIMARY_KEY` in `public.audit_logs`: Table does not define a primary key.
- `WARNING` `NO_INDEXES` in `public.audit_logs`: Table has no indexes, including implicit primary key indexes.
- `ERROR` `LARGE_TABLE_UNINDEXED_FK` in `public.audit_logs`: Large table is missing an index on identifier-like column `user_id`.
