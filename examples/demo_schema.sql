CREATE TABLE departments (
    department_id BIGSERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    name TEXT,
    email TEXT NOT NULL,
    department_id BIGINT REFERENCES departments(department_id),
    created_at TIMESTAMPTZ,
    usr_id BIGINT,
    users_id BIGINT
);

CREATE INDEX idx_users_department_id ON users(department_id);

CREATE TABLE profiles (
    id BIGINT,
    user_id BIGINT PRIMARY KEY REFERENCES users(id),
    display_name TEXT
);

CREATE TABLE audit_logs (
    event_id BIGSERIAL,
    user_id BIGINT,
    entity_id BIGINT,
    created_at TIMESTAMPTZ,
    payload JSONB NOT NULL DEFAULT '{}'::jsonb
);
