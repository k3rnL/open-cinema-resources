#!/usr/bin/env python3
"""Ranked local search for the Open Cinema reference system."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


TEXT_SUFFIXES = {
    ".md", ".txt", ".csv", ".tsv", ".json", ".yaml", ".yml", ".toml",
    ".ini", ".cfg", ".c", ".h", ".cpp", ".hpp", ".ino", ".py", ".js",
    ".ts", ".sh",
}
SKIP_PARTS = {".agents", ".git", ".venv", "node_modules", "__pycache__"}


@dataclass
class Result:
    path: str
    title: str
    score: int
    matches: list[str]


def path_weight(relative: Path) -> int:
    value = relative.as_posix()
    if value == "docs/reference/INDEX.md":
        return 8
    if value.startswith("docs/reference/topics/"):
        return 6
    if value.startswith("docs/decisions/"):
        return 5
    if value == "ROADMAP.md":
        return 5
    if value.startswith("docs/worklog/"):
        return 4
    if relative.name == "README.md":
        return 2
    return 1


def title_for(text: str, path: Path) -> str:
    metadata = re.search(r"(?m)^title:\s*[\"']?(.+?)[\"']?\s*$", text)
    if metadata:
        return metadata.group(1).strip()
    heading = re.search(r"(?m)^#\s+(.+?)\s*$", text)
    return heading.group(1).strip() if heading else path.stem.replace("-", " ").title()


def candidate_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        relative = path.relative_to(root)
        if any(part in SKIP_PARTS for part in relative.parts):
            continue
        if path.name.startswith("0000-template"):
            continue
        yield path, relative


def search(root: Path, query: str, limit: int = 10) -> list[Result]:
    terms = [term.casefold() for term in re.findall(r"[\w.-]+", query)]
    if not terms:
        return []

    results: list[Result] = []
    for path, relative in candidate_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue

        folded = text.casefold()
        if not all(term in folded for term in terms):
            continue

        title = title_for(text, path)
        header = "\n".join(text.splitlines()[:20]).casefold()
        base = path_weight(relative)
        score = base + sum(folded.count(term) for term in terms)
        score += 5 * sum(term in title.casefold() for term in terms)
        score += 3 * sum(term in header for term in terms)

        snippets: list[str] = []
        for number, line in enumerate(text.splitlines(), start=1):
            folded_line = line.casefold()
            if any(term in folded_line for term in terms):
                snippets.append(f"L{number}: {line.strip()}")
            if len(snippets) == 4:
                break
        results.append(Result(relative.as_posix(), title, score, snippets))

    results.sort(key=lambda item: (-item.score, item.path))
    return results[:limit]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Words that must all occur in a result")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Repository root")
    parser.add_argument("--limit", type=int, default=10, help="Maximum results")
    parser.add_argument("--json", action="store_true", help="Emit JSON")
    args = parser.parse_args()

    root = args.root.resolve()
    results = search(root, args.query, max(1, args.limit))
    if args.json:
        print(json.dumps([asdict(item) for item in results], indent=2))
    elif not results:
        print("No matching project knowledge found.")
    else:
        for item in results:
            print(f"{item.path} — {item.title} (score {item.score})")
            for match in item.matches:
                print(f"  {match}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

