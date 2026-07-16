# PostgreSQL Schema Report

- Generated at: `2026-07-16T08:15:07.309038+00:00`
- Source: `postgresql+psycopg://dbdoc:***@localhost:5432/dbdoc`
- Tables: `4`
- Issues: `10`

## ERD

```mermaid
graph LR
  public_audit_logs["public.audit_logs\nevent_id\nuser_id\nentity_id\ncreated_at\npayload"]
  public_departments["public.departments\ndepartment_id (PK)\nname\ncode"]
  public_profiles["public.profiles\nid\nuser_id (PK, FK)\ndisplay_name\nbio"]
  public_users["public.users\nid (PK)\ndepartment_id (FK)\nname\nemail\ncreated_at\n..."]
  public_profiles -->|user_id| public_users
  public_users -->|department_id| public_departments
```

## Problems

- `ERROR` `LARGE_TABLE_UNINDEXED_FK` in `public.audit_logs`: Large table is missing an index on identifier-like column `entity_id`.
- `ERROR` `LARGE_TABLE_UNINDEXED_FK` in `public.audit_logs`: Large table is missing an index on identifier-like column `event_id`.
- `ERROR` `LARGE_TABLE_UNINDEXED_FK` in `public.audit_logs`: Large table is missing an index on identifier-like column `user_id`.
- `ERROR` `MISSING_PRIMARY_KEY` in `public.audit_logs`: Table does not define a primary key.
- `WARNING` `NO_INDEXES` in `public.audit_logs`: Table has no indexes, including implicit primary key indexes.
- `WARNING` `SUSPICIOUS_NULLABLE_COLUMN` in `public.audit_logs`: Nullable column `created_at` looks business-critical.
- `WARNING` `NON_PRIMARY_ID_COLUMN` in `public.profiles`: Column `id` exists but is not part of the primary key.
- `WARNING` `SIMILAR_IDENTIFIER_COLUMNS` in `public.users`: Columns look like duplicated identifier variants for `user_id`: `users_id`, `usr_id`
- `WARNING` `SUSPICIOUS_NULLABLE_COLUMN` in `public.users`: Nullable column `created_at` looks business-critical.
- `WARNING` `SUSPICIOUS_NULLABLE_COLUMN` in `public.users`: Nullable column `name` looks business-critical.

## public.audit_logs

- Estimated rows: `1200`
- Primary key: `none`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `event_id` | `BIGINT` | no |  |  |
| `user_id` | `BIGINT` | yes |  |  |
| `entity_id` | `BIGINT` | yes |  |  |
| `created_at` | `TIMESTAMP` | yes |  |  |
| `payload` | `JSONB` | no | `'{}'::jsonb` |  |

### Foreign Keys

- None

### Indexes

- None

### Problems

- `LARGE_TABLE_UNINDEXED_FK`: Large table is missing an index on identifier-like column `entity_id`.
- `LARGE_TABLE_UNINDEXED_FK`: Large table is missing an index on identifier-like column `event_id`.
- `LARGE_TABLE_UNINDEXED_FK`: Large table is missing an index on identifier-like column `user_id`.
- `MISSING_PRIMARY_KEY`: Table does not define a primary key.
- `NO_INDEXES`: Table has no indexes, including implicit primary key indexes.
- `SUSPICIOUS_NULLABLE_COLUMN`: Nullable column `created_at` looks business-critical.

## public.departments

- Estimated rows: `3`
- Primary key: `department_id`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `department_id` | `BIGINT` | no |  | PK, Indexed |
| `name` | `TEXT` | no |  |  |
| `code` | `TEXT` | no |  | Indexed |

### Foreign Keys

- None

### Indexes

- `departments_code_key` (unique) on `code`
- `departments_pkey` (primary, unique) on `department_id`

### Problems

- None

## public.profiles

- Estimated rows: `3`
- Primary key: `user_id`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `id` | `BIGINT` | yes |  |  |
| `user_id` | `BIGINT` | no |  | PK, FK -> public.users, Indexed |
| `display_name` | `TEXT` | yes |  |  |
| `bio` | `TEXT` | yes |  |  |

### Foreign Keys

- `user_id` -> `public.users` (`id`)

### Indexes

- `profiles_pkey` (primary, unique) on `user_id`

### Problems

- `NON_PRIMARY_ID_COLUMN`: Column `id` exists but is not part of the primary key.

## public.users

- Estimated rows: `4`
- Primary key: `id`

### Columns

| Column | Type | Nullable | Default | Notes |
| --- | --- | --- | --- | --- |
| `id` | `BIGINT` | no |  | PK, Indexed |
| `department_id` | `BIGINT` | yes |  | FK -> public.departments, Indexed |
| `name` | `TEXT` | yes |  |  |
| `email` | `TEXT` | no |  | Indexed |
| `created_at` | `TIMESTAMP` | yes |  |  |
| `usr_id` | `BIGINT` | yes |  |  |
| `users_id` | `BIGINT` | yes |  |  |

### Foreign Keys

- `department_id` -> `public.departments` (`department_id`)

### Indexes

- `idx_users_department_id` on `department_id`
- `users_pkey` (primary, unique) on `id`
- `ux_users_email` (unique) on `email`

### Problems

- `SIMILAR_IDENTIFIER_COLUMNS`: Columns look like duplicated identifier variants for `user_id`: `users_id`, `usr_id`
- `SUSPICIOUS_NULLABLE_COLUMN`: Nullable column `created_at` looks business-critical.
- `SUSPICIOUS_NULLABLE_COLUMN`: Nullable column `name` looks business-critical.
