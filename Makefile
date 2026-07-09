PYTHON ?= python3
DSN ?= postgresql://dbdoc:dbdoc@localhost:54329/dbdoc
SNAPSHOT ?= .dbdoc/schema.json
REPORT ?= docs/schema.md

.PHONY: install test scan report lint compose-up compose-down demo-report

install:
	$(PYTHON) -m pip install -e .[dev]

test:
	$(PYTHON) -m pytest

scan:
	$(PYTHON) -m pg_meta_doc.cli scan --dsn $(DSN) --output $(SNAPSHOT)

report:
	$(PYTHON) -m pg_meta_doc.cli report --input $(SNAPSHOT) --output $(REPORT)

lint:
	$(PYTHON) -m pg_meta_doc.cli lint --input $(SNAPSHOT)

compose-up:
	docker compose up -d postgres

compose-down:
	docker compose down -v

demo-report: scan report
