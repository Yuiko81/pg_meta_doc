# pg-meta-doc

`pg-meta-doc` scans a PostgreSQL schema, flags structural issues, and writes a Markdown report with a Mermaid ERD.

## Features

- inspects tables, columns, types, nullability, defaults, primary keys, foreign keys, and indexes
- flags missing primary keys, suspicious nullable columns, duplicate identifier variants, missing indexes, and large-table FK-like columns without indexes
- saves a JSON schema snapshot and renders `docs/schema.md`
- exposes a CLI: `dbdoc scan`, `dbdoc report`, `dbdoc lint`
- ships with a demo schema, Docker Compose setup, and pytest coverage

## Install

```bash
python3 -m pip install -e .[dev]
```

## CLI

Scan a database and save the snapshot:

```bash
dbdoc scan --dsn postgresql://user:pass@localhost:5432/db
```

Render Markdown from the saved snapshot:

```bash
dbdoc report --format markdown
```

Lint the saved snapshot:

```bash
dbdoc lint
```

You can also lint a live database directly:

```bash
dbdoc lint --dsn postgresql://user:pass@localhost:5432/db
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
├── examples/
├── docs/
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── pyproject.toml
└── README.md
```

## Demo

Start PostgreSQL with the demo schema:

```bash
docker compose up -d postgres
```

Generate the snapshot and report:

```bash
make demo-report
```

The example output lives in `docs/example_report.md`.
