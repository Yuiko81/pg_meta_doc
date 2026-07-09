from __future__ import annotations

import argparse
from pathlib import Path

from pg_meta_doc.db import load_snapshot, save_snapshot
from pg_meta_doc.inspector import inspect_database
from pg_meta_doc.markdown import render_markdown
from pg_meta_doc.rules import lint_schema

DEFAULT_SNAPSHOT_PATH = Path(".dbdoc/schema.json")
DEFAULT_REPORT_PATH = Path("docs/schema.md")


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    return args.handler(args)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="dbdoc",
        description="Inspect PostgreSQL schemas and generate Markdown documentation.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser("scan", help="Scan a live PostgreSQL database.")
    scan.add_argument("--dsn", required=True, help="PostgreSQL DSN.")
    scan.add_argument(
        "--schema",
        action="append",
        help="Schema to inspect. Pass multiple times to include several schemas.",
    )
    scan.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_SNAPSHOT_PATH,
        help=f"Snapshot output path. Default: {DEFAULT_SNAPSHOT_PATH}",
    )
    scan.set_defaults(handler=_handle_scan)

    report = subparsers.add_parser(
        "report",
        help="Render documentation from a saved schema snapshot.",
    )
    report.add_argument(
        "--format",
        choices=["markdown"],
        default="markdown",
        help="Output format. Only markdown is currently supported.",
    )
    report.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_SNAPSHOT_PATH,
        help=f"Snapshot input path. Default: {DEFAULT_SNAPSHOT_PATH}",
    )
    report.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_REPORT_PATH,
        help=f"Report output path. Default: {DEFAULT_REPORT_PATH}",
    )
    report.set_defaults(handler=_handle_report)

    lint = subparsers.add_parser(
        "lint",
        help="Validate a saved snapshot or scan a live database and lint it.",
    )
    lint.add_argument(
        "--input",
        type=Path,
        default=DEFAULT_SNAPSHOT_PATH,
        help=f"Snapshot input path. Default: {DEFAULT_SNAPSHOT_PATH}",
    )
    lint.add_argument("--dsn", help="Optional DSN to lint a live database.")
    lint.add_argument(
        "--schema",
        action="append",
        help="Schema to inspect when --dsn is supplied.",
    )
    lint.set_defaults(handler=_handle_lint)

    return parser


def _handle_scan(args: argparse.Namespace) -> int:
    snapshot = inspect_database(args.dsn, schemas=args.schema)
    path = save_snapshot(snapshot, args.output)
    print(
        f"Scanned {len(snapshot.tables)} table(s) from {snapshot.source} "
        f"and wrote {path}"
    )
    return 0


def _handle_report(args: argparse.Namespace) -> int:
    snapshot = load_snapshot(args.input)
    issues = lint_schema(snapshot)
    report = render_markdown(snapshot, issues)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Wrote Markdown report with {len(snapshot.tables)} table(s) to {args.output}")
    return 0


def _handle_lint(args: argparse.Namespace) -> int:
    snapshot = (
        inspect_database(args.dsn, schemas=args.schema)
        if args.dsn
        else load_snapshot(args.input)
    )
    issues = lint_schema(snapshot)
    if not issues:
        print("No issues found.")
        return 0

    for issue in issues:
        columns = f" [{', '.join(issue.columns)}]" if issue.columns else ""
        print(f"{issue.severity.upper()} {issue.code} {issue.table}{columns}: {issue.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
