FROM postgres:16-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV POSTGRES_DB=dbdoc
ENV POSTGRES_USER=dbdoc
ENV POSTGRES_PASSWORD=dbdoc
ENV PATH="/opt/dbdoc-venv/bin:$PATH"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip \
        python3-venv \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /workspace

COPY . /tmp/project

RUN python3 -m venv /opt/dbdoc-venv \
    && /opt/dbdoc-venv/bin/pip install --no-cache-dir --upgrade pip \
    && /opt/dbdoc-venv/bin/pip install --no-cache-dir /tmp/project \
    && rm -rf /tmp/project

COPY demo_db.sql /docker-entrypoint-initdb.d/10-demo-db.sql

EXPOSE 5432

CMD ["postgres"]