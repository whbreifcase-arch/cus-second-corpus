#!/usr/bin/env python3
"""CUS glossary lint — the term layer + link integrity.

The companion to _retired/sweep.py. Where the sweep polices retired *claims*
(relational assertions between valid terms), this polices the *term* layer:

  1. Link integrity — every relative markdown link in the canonical docs must
     resolve to a real file (and, if it carries a #anchor, to a real heading).
     Broken cross-doc links are drift; this catches them structurally, which a
     regex over prose never could.

  2. Retired terms — any RETIRED term in glossary.tsv appearing in canon is a
     failure unless it carries an inline allowance (same convention as the
     sweep), on the matching line or the line directly above it:

         <!-- retired-lint: allow <id> reason: ... -->

glossary.tsv is the single source of truth for terms (LIVE and RETIRED).
_retired/registry.tsv remains the source for retired *claims*. The split is the
point: a term is lexical (a link resolves it); a claim is relational (only a
schema can). See _retired/README.md.

Run:  python3 glossary_lint.py
Exit: 0 = clean, 1 = problem(s) found, 2 = glossary error.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))   # glossary.tsv lives at repo root
GLOSSARY = os.path.join(ROOT, "glossary.tsv")

# Canonical docs governed (globs, relative to ROOT) — same scope as the claim sweep.
CANON_GLOBS = [
    "README.md",
    "composition/**/*.md",
    "interface/**/*.md",
    "slice-1/**/*.md",
    "slice-2/**/*.md",
    "slice-3/**/*.md",
]
IGNORE_TOP = {"_retired", ".git", "notes"}

ALLOW_RE = re.compile(r"retired-lint:\s*allow\s+([\w,\-\s]+?)\s*(?:reason:|-->)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.*?)\s*#*\s*$")


def load_glossary():
    live, retired = [], []
    try:
        with open(GLOSSARY, encoding="utf-8") as f:
            for n, raw in enumerate(f, 1):
                line = raw.rstrip("\n")
                if not line or line.startswith("#"):
                    continue
                parts = line.split("\t")
                if len(parts) < 6:
                    print(f"glossary.tsv:{n}: expected 6 tab-separated fields, got {len(parts)}", file=sys.stderr)
                    return None
                term, status, tid, ref, ruling, note = (p.strip() for p in parts[:6])
                if status == "RETIRED":
                    rx = re.compile(r"\b" + re.escape(term) + r"\b")
                    retired.append((tid, term, rx, ref, ruling, note))
                elif status == "LIVE":
                    live.append((tid, term, ref))
                else:
                    print(f"glossary.tsv:{n}: status must be LIVE or RETIRED, got '{status}'", file=sys.stderr)
                    return None
    except FileNotFoundError:
        print(f"glossary not found: {GLOSSARY}", file=sys.stderr)
        return None
    return live, retired


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


def slugify(text):
    s = text.strip().lower()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s


def headings(path):
    slugs = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = HEADING_RE.match(line)
            if m:
                slugs.add(slugify(m.group(1)))
    return slugs


def check_links(files):
    problems = []
    heading_cache = {}
    for path in files:
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        base = os.path.dirname(path)
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            for target in LINK_RE.findall(line):
                t = target.strip()
                if t.startswith(("http://", "https://", "mailto:")):
                    continue
                filepart, sep, anchor = t.partition("#")
                dest = path if filepart == "" else os.path.normpath(os.path.join(base, filepart))
                if not os.path.isfile(dest):
                    problems.append((rel, i + 1, t, "file not found"))
                    continue
                if anchor:
                    if dest not in heading_cache:
                        heading_cache[dest] = headings(dest)
                    if slugify(anchor) not in heading_cache[dest]:
                        problems.append((rel, i + 1, t, f"no heading matching '#{anchor}'"))
    return problems


def check_terms(files, retired):
    hits = []
    for path in files:
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            allow = allowed_ids(lines, i)
            for tid, term, rx, ref, ruling, note in retired:
                if tid in allow:
                    continue
                if rx.search(line):
                    hits.append((rel, i + 1, tid, term, ref, ruling, note, line.strip()))
    return hits


def main():
    g = load_glossary()
    if g is None:
        return 2
    live, retired = g
    files = canon_files()

    links = check_links(files)
    terms = check_terms(files, retired)

    if links:
        print(f"link integrity: {len(links)} broken link(s)\n")
        for rel, ln, t, why in links:
            print(f"  {rel}:{ln}  ({t})  — {why}")
        print()
    if terms:
        print(f"retired-term sweep: {len(terms)} unallowed match(es)\n")
        for rel, ln, tid, term, ref, ruling, note, text in terms:
            print(f"  {rel}:{ln}  [{tid}]  '{term}' -> {ref}  ({ruling})")
            print(f"      {note}")
            print(f"      > {text}\n")
        print("Fix the term, or (for a deliberate historical callback) add on the line or the one above:")
        print("  <!-- retired-lint: allow <id> reason: ... -->")

    if links or terms:
        return 1
    print(f"glossary lint: clean — {len(live)} live terms, {len(retired)} retired terms; "
          f"links + terms OK across {len(files)} canonical files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
