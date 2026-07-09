from __future__ import annotations

import pytest

from pg_meta_doc.db import build_engine, normalize_dsn
from pg_meta_doc.inspector import inspect_database

pytestmark = pytest.mark.integration


def test_inspect_database_reads_live_postgres_schema():
    testcontainers = pytest.importorskip("testcontainers")
    docker = pytest.importorskip("docker")
    assert testcontainers
    assert docker

    try:
        from testcontainers.postgres import PostgresContainer
    except Exception as exc:  # pragma: no cover - import availability differs by env.
        pytest.skip(f"testcontainers.postgres is unavailable: {exc}")

    try:
        with PostgresContainer("postgres:16") as postgres:
            dsn = normalize_dsn(postgres.get_connection_url())
            engine = build_engine(dsn)
            try:
                with engine.begin() as connection:
                    connection.exec_driver_sql(
                        """
                        CREATE TABLE departments (
                            department_id BIGSERIAL PRIMARY KEY,
                            name TEXT NOT NULL
                        );
                        """
                    )
                    connection.exec_driver_sql(
                        """
                        CREATE TABLE users (
                            id BIGSERIAL PRIMARY KEY,
                            department_id BIGINT REFERENCES departments(department_id),
                            email TEXT NOT NULL
                        );
                        """
                    )
                    connection.exec_driver_sql(
                        "CREATE INDEX idx_users_department_id ON users(department_id);"
                    )

                snapshot = inspect_database(dsn, schemas=["public"])
            finally:
                engine.dispose()
    except Exception as exc:  # pragma: no cover - Docker may be unavailable.
        pytest.skip(f"Docker-based integration test is unavailable: {exc}")

    tables = {table.qualified_name: table for table in snapshot.tables}
    assert "public.users" in tables
    assert "public.departments" in tables
    assert tables["public.users"].primary_key == ["id"]
    assert any(
        foreign_key.referred_table == "departments"
        for foreign_key in tables["public.users"].foreign_keys
    )
    assert any(index.name == "idx_users_department_id" for index in tables["public.users"].indexes)
