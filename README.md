# pg-meta-doc

CLI-инструмент для PostgreSQL, который сканирует структуру базы, сохраняет снапшот схемы, генерирует Markdown-документацию и подсвечивает базовые проблемы в модели данных.

Проект сделан как небольшая инженерная утилита для ситуаций, когда база уже существует, а актуальной документации по ней нет.

## Возможности

* сканирование схем PostgreSQL
* сохранение снапшота в JSON
* генерация Markdown-отчёта
* Mermaid ERD-диаграмма
* lint-проверки по структуре БД
* работа как с live-базой, так и с сохранённым снапшотом

## Что проверяет lint

* таблицы без primary key
* колонка `id`, которая не является primary key
* nullable-поля с важными названиями вроде `name`, `email`, `created_at`
* таблицы без индексов
* похожие identifier-колонки вроде `user_id`, `users_id`, `usr_id`
* большие таблицы с неиндексированными fk-подобными полями

## Установка

```bash
python3 -m pip install -e .[dev]
```

## Использование

Скан базы и создание снапшота:

```bash
dbdoc scan --dsn postgresql://user:pass@localhost:5432/db
```

По умолчанию снапшот сохраняется в:

```text
.dbdoc/schema.json
```

Генерация Markdown-отчёта:

```bash
dbdoc report --format markdown
```

По умолчанию отчёт сохраняется в:

```text
docs/schema.md
```

Lint сохранённого снапшота:

```bash
dbdoc lint
```

Lint live-базы:

```bash
dbdoc lint --dsn postgresql://user:pass@localhost:5432/db
```

## Пример workflow

```bash
dbdoc scan --dsn postgresql://user:pass@localhost:5432/db
dbdoc report --format markdown
```

После этого можно закоммитить актуальное состояние схемы:

```bash
git add .dbdoc/schema.json docs/schema.md
git commit -m "update database schema documentation"
```

## Структура проекта

```text
pg_meta_doc/
├── cli.py          # CLI-команды
├── inspector.py    # сканирование PostgreSQL
├── rules.py        # lint-правила
├── markdown.py     # генерация Markdown
├── mermaid.py      # генерация Mermaid ERD
└── db.py           # модели и работа со снапшотами
```

## Тесты

```bash
make test
```