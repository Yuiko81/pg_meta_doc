FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /workspace

COPY . /tmp/project
RUN pip install --no-cache-dir /tmp/project

CMD ["python", "-m", "pg_meta_doc.cli", "--help"]
