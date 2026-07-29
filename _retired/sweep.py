#!/usr/bin/env python3
"""CUS retired-claim sweep.

Reads _retired/registry.tsv (the single list of retired *claims*, as contextual regexes) and scans the
canonical Second-Corpus docs for any match. A match is a failure unless it carries an inline allowance:

    <!-- retired-lint: allow <id> reason: ... -->

on the matching line or the line directly above it (allowances move with the text — no line numbers).

Run:  py _retired/sweep.py   (or  python3 _retired/sweep.py)
Exit: 0 = clean, 1 = unallowed match(es) found, 2 = registry error.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # repo root (parent of _retired/)
REGISTRY = os.path.join(HERE, "registry.tsv")

# Canonical docs the sweep governs (globs, relative to ROOT).
CANON_GLOBS = [
    "README.md",
    "composition/**/*.md",
    "interface/**/*.md",
    "slice-1/**/*.md",
    "slice-2/**/*.md",
    "slice-3/**/*.md",
]
# Never scanned (the graveyard names retired claims on purpose; notes are drafts).
IGNORE_TOP = {"_retired", ".git", "notes"}

ALLOW_RE = re.compile(r"retired-lint:\s*allow\s+([\w,\-\s]+?)\s*(?:reason:|-->)")


def load_registry():
    rules = []
    try:
        with open(REGISTRY, encoding="utf-8") as f:
            for n, raw in enumerate(f, 1):
                line = raw.rstrip("\n")
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) < 5:
                    print(f"registry.tsv:{n}: expected 5 tab-separated fields, got {len(parts)}", file=sys.stderr)
                    return None
                rid, pat, scope, auth, msg = (p.strip() for p in parts[:5])
                try:
                    rx = re.compile(pat)
                except re.error as e:
                    print(f"registry.tsv:{n}: bad regex for '{rid}': {e}", file=sys.stderr)
                    return None
                rules.append((rid, rx, auth, msg))
    except FileNotFoundError:
        print(f"registry not found: {REGISTRY}", file=sys.stderr)
        return None
    return rules


def canon_files():
    files = set()
    for g in CANON_GLOBS:
        for p in glob.glob(os.path.join(ROOT, g), recursive=True):
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel.split("/")[0] in IGNORE_TOP:
                continue
            if os.path.isfile(p):
                files.add(p)
    return sorted(files)


def allowed_ids(lines, i):
    ids = set()
    for j in (i, i - 1):
        if 0 <= j < len(lines):
            for grp in ALLOW_RE.findall(lines[j]):
                ids.update(t for t in re.split(r"[^\w-]+", grp) if t)
    return ids


def main():
    rules = load_registry()
    if rules is None:
        return 2
    hits = []
    for path in canon_files():
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            allow = allowed_ids(lines, i)
            for rid, rx, auth, msg in rules:
                if rid in allow:
                    continue
                if rx.search(line):
                    hits.append((rel, i + 1, rid, auth, msg, line.strip()))
    if hits:
        print(f"retired-claim sweep: {len(hits)} unallowed match(es)\n")
        for rel, ln, rid, auth, msg, text in hits:
            print(f"  {rel}:{ln}  [{rid}]  ({auth})")
            print(f"      {msg}")
            print(f"      > {text}\n")
        print("Fix the claim, or (for a deliberate historical callback) add on the line or the one above:")
        print("  <!-- retired-lint: allow <id> reason: ... -->")
        return 1
    print(f"retired-claim sweep: clean — 0 unallowed matches across {len(canon_files())} canonical files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
