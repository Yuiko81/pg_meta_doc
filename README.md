# pg-meta-doc

`pg-meta-doc` scans a PostgreSQL schema, flags structural issues, and writes a Markdown report with a Mermaid ERD.

## Features

- inspects tables, columns, types, nullability, defaults, primary keys, foreign keys, and indexes
- flags missing primary keys, suspicious nullable columns, duplicate identifier variants, missing indexes, and large-table FK-like columns without indexes
- saves a JSON schema snapshot and renders `docs/schema.md`
- exposes a CLI: `dbdoc scan`, `dbdoc report`, `dbdoc lint`
- includes an optional Docker wrapper and pytest coverage

## Install

```bash
python3 -m pip install -e '.[dev]'
```

## CLI

Scan a database and save the snapshot:

```bash
dbdoc scan --dsn 'postgresql://user:pass@db-host:5432/dbname'
```

Render Markdown from the saved snapshot:

```bash
dbdoc report --input .dbdoc/schema.json --output docs/schema.md
```

Lint the saved snapshot:

```bash
dbdoc lint --input .dbdoc/schema.json
```

You can also lint a live database directly:

```bash
dbdoc lint --dsn 'postgresql://user:pass@db-host:5432/dbname'
```

Typical workflow:

```bash
dbdoc scan --dsn 'postgresql://user:pass@db-host:5432/dbname'
dbdoc report --input .dbdoc/schema.json --output docs/schema.md
dbdoc lint --input .dbdoc/schema.json
```

## Docker

If you do not want to install Python dependencies on the host, you can run the CLI in Docker:

```bash
docker compose run --rm dbdoc scan --dsn 'postgresql://user:pass@db-host:5432/dbname' --output /workspace/.dbdoc/schema.json
docker compose run --rm dbdoc report --input /workspace/.dbdoc/schema.json --output /workspace/docs/schema.md
```

## Project Layout

```text
pg_meta_doc/
├── pg_meta_doc/
│   ├── cli.py
│   ├── db.py
│   ├── inspector.py
│   ├── markdown.py
│   ├── mermaid.py
│   └── rules.py
├── tests/
├── docs/
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── pyproject.toml
└── README.md
```
