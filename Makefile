PYTHON ?= python3
DSN ?= postgresql://user:pass@localhost:5432/db
SNAPSHOT ?= .dbdoc/schema.json
REPORT ?= docs/schema.md

.PHONY: install test scan report lint

install:
	$(PYTHON) -m pip install -e .[dev]

test:
	$(PYTHON) -m pytest

scan:
	$(PYTHON) -m pg_meta_doc.cli scan --dsn "$(DSN)" --output $(SNAPSHOT)

report:
	$(PYTHON) -m pg_meta_doc.cli report --input $(SNAPSHOT) --output $(REPORT)

lint:
	$(PYTHON) -m pg_meta_doc.cli lint --input $(SNAPSHOT)
