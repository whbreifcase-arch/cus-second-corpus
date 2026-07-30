#!/usr/bin/env python3
"""CUS canon check — one command for the whole model.

Two kinds of drift, one checker:

  TERMS   — dead *words* (Shove, Ladder, Nerve test). Lexical: a word is live or
            retired. Source of truth: glossary.tsv.
  CLAIMS  — dead *relationships* between valid words (Frame contains Archetype).
            Relational: every word is fine, the sentence is not. Source of truth:
            model.tsv, where each claim is a subject-predicate-object statement.

What it checks over the canonical docs (README + composition/ interface/ slice-1..3):
  1. Link integrity  — every relative markdown link resolves to a real file
                       (and, if anchored, a real heading).
  2. Retired terms   — no RETIRED glossary term appears unallowed.
  3. Retired claims  — no forbidden model relation's pattern matches unallowed.

Plus model self-consistency (not over prose):
  4. every row cites a ruling; every forbidden pattern compiles; every id is
     unique; every LIVE term's home doc exists; the living GLOSSARY.md is in sync.

Deliberate historical callbacks carry an inline allowance on the matching line
or the line above (same marker for terms and claims):
    <!-- retired-lint: allow <id> reason: ... -->

Run:   python3 _model/check.py           # check everything
       python3 _model/check.py --write   # regenerate ../GLOSSARY.md, then check
Exit:  0 = clean, 1 = drift found, 2 = model/config error.
"""
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)                       # repo root (parent of _model/)
GLOSSARY_TSV = os.path.join(HERE, "glossary.tsv")
MODEL_TSV = os.path.join(HERE, "model.tsv")
GLOSSARY_MD = os.path.join(ROOT, "GLOSSARY.md")

# Canonical docs governed: every markdown doc except the ignored areas below. Using a
# broad glob (not an enumerated slice list) means future slices — Slice 4 and beyond —
# are scanned automatically, with no edit here.
CANON_GLOBS = ["README.md", "**/*.md"]
IGNORE_TOP = {"_model", "_retired", ".git", "notes"}
# Files skipped even at a non-ignored path: the generated glossary names dead terms on purpose.
IGNORE_FILES = {"GLOSSARY.md"}

ALLOW_RE = re.compile(r"retired-lint:\s*allow\s+([\w,\-\s]+?)\s*(?:reason:|-->)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^\s*#{1,6}\s+(.*?)\s*#*\s*$")


def die(msg):
    print(f"config error: {msg}", file=sys.stderr)
    return None


def load_glossary():
    live, retired = [], []
    with open(GLOSSARY_TSV, encoding="utf-8") as f:
        for n, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 6:
                return die(f"glossary.tsv:{n}: expected 6 fields, got {len(parts)}")
            term, status, tid, ref, ruling, note = (p.strip() for p in parts[:6])
            if status == "LIVE":
                live.append({"term": term, "id": tid, "home": ref, "ruling": ruling, "note": note})
            elif status == "RETIRED":
                rx = re.compile(r"\b" + re.escape(term) + r"\b")
                retired.append({"term": term, "id": tid, "use": ref, "ruling": ruling, "note": note, "rx": rx})
            else:
                return die(f"glossary.tsv:{n}: status must be LIVE or RETIRED, got '{status}'")
    return {"live": live, "retired": retired}


def load_model():
    canonical, forbidden = [], []
    with open(MODEL_TSV, encoding="utf-8") as f:
        for n, raw in enumerate(f, 1):
            line = raw.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 8:
                return die(f"model.tsv:{n}: expected 8 fields, got {len(parts)}")
            rid, kind, subj, pred, obj, ruling, pat, stmt = (p.strip() for p in parts[:8])
            row = {"id": rid, "subject": subj, "predicate": pred, "object": obj,
                   "ruling": ruling, "statement": stmt}
            if kind == "canonical":
                canonical.append(row)
            elif kind == "forbidden":
                if not pat:
                    return die(f"model.tsv:{n}: forbidden row '{rid}' has no detection pattern")
                try:
                    row["rx"] = re.compile(pat)
                except re.error as e:
                    return die(f"model.tsv:{n}: bad regex for '{rid}': {e}")
                forbidden.append(row)
            else:
                return die(f"model.tsv:{n}: kind must be canonical or forbidden, got '{kind}'")
    return {"canonical": canonical, "forbidden": forbidden}


def canon_files():
    files = set()
    for g in CANON_GLOBS:
        for p in glob.glob(os.path.join(ROOT, g), recursive=True):
            rel = os.path.relpath(p, ROOT).replace("\\", "/")
            if rel.split("/")[0] in IGNORE_TOP or rel in IGNORE_FILES:
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
    return re.sub(r"\s+", "-", s)


def headings(path):
    slugs = set()
    with open(path, encoding="utf-8") as f:
        for line in f:
            m = HEADING_RE.match(line)
            if m:
                slugs.add(slugify(m.group(1)))
    return slugs


def check_links(files):
    problems, cache = [], {}
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
                filepart, _, anchor = t.partition("#")
                dest = path if filepart == "" else os.path.normpath(os.path.join(base, filepart))
                if not os.path.isfile(dest):
                    problems.append((rel, i + 1, t, "file not found"))
                    continue
                if anchor:
                    if dest not in cache:
                        cache[dest] = headings(dest)
                    if slugify(anchor) not in cache[dest]:
                        problems.append((rel, i + 1, t, f"no heading matching '#{anchor}'"))
    return problems


def sweep(files, rules, key):
    """Generic prose sweep: rules is a list of dicts each with 'id' and 'rx'."""
    hits = []
    for path in files:
        rel = os.path.relpath(path, ROOT).replace("\\", "/")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            allow = allowed_ids(lines, i)
            for rule in rules:
                if rule["id"] in allow:
                    continue
                if rule["rx"].search(line):
                    hits.append((rel, i + 1, rule, line.strip()))
    return hits


def model_consistency(gloss, model):
    errs = []
    seen = {}
    for r in gloss["retired"] + model["canonical"] + model["forbidden"]:
        rid = r["id"]
        # ids may legitimately repeat within a group (e.g. grade-ladder x3); only flag
        # a collision across DIFFERENT rulings, which would be a real inconsistency.
        if rid in seen and seen[rid] != r["ruling"]:
            errs.append(f"id '{rid}' used with conflicting rulings: '{seen[rid]}' vs '{r['ruling']}'")
        seen[rid] = r["ruling"]
    for t in gloss["live"]:
        if t["home"] and not os.path.isfile(os.path.join(ROOT, t["home"])):
            errs.append(f"live term '{t['term']}' home doc not found: {t['home']}")
    for t in gloss["retired"]:
        if not t["use"]:
            errs.append(f"retired term '{t['term']}' names no replacement")
    for r in gloss["retired"] + model["canonical"] + model["forbidden"]:
        if not r["ruling"]:
            errs.append(f"row '{r['id']}' cites no ruling")
    return errs


def render_glossary(gloss, model):
    def rul(x):
        return x if x else "—"
    out = []
    out.append("# CUS — Living Glossary")
    out.append("")
    out.append("> _Generated from [`_model/glossary.tsv`](_model/glossary.tsv) + "
               "[`_model/model.tsv`](_model/model.tsv) by `_model/check.py`. "
               "Do not edit by hand — run `python3 _model/check.py --write`._")
    out.append("")
    out.append("The canonical vocabulary and how it relates. Two kinds of drift are guarded "
               "automatically: **dead words** (*Retired vocabulary*) and **dead claims** "
               "(*Retired claims*). Each entry cites the ruling behind it.")
    out.append("")
    out.append("## Live vocabulary")
    out.append("")
    out.append("| Term | Meaning | Ruling |")
    out.append("|---|---|---|")
    for t in gloss["live"]:
        link = f"[{t['term']}]({t['home']})" if t["home"] else t["term"]
        out.append(f"| {link} | {t['note']} | {rul(t['ruling'])} |")
    out.append("")
    out.append("## How the vocabulary relates (canonical)")
    out.append("")
    out.append("| Subject | relation | Object | Ruling |")
    out.append("|---|---|---|---|")
    for r in model["canonical"]:
        out.append(f"| {r['subject']} | {r['predicate']} | {r['object']} | {rul(r['ruling'])} |")
    out.append("")
    out.append("## Retired vocabulary — use the live term instead")
    out.append("")
    out.append("| Retired | Use instead | Ruling | id |")
    out.append("|---|---|---|---|")
    for t in gloss["retired"]:
        out.append(f"| {t['term']} | {t['use']} | {rul(t['ruling'])} | `{t['id']}` |")
    out.append("")
    out.append("## Retired claims — statements the corpus has struck")
    out.append("")
    out.append("| Struck claim | Correction | Ruling | id |")
    out.append("|---|---|---|---|")
    for r in model["forbidden"]:
        claim = f"{r['subject']} {r['predicate']} {r['object']}"
        out.append(f"| {claim} | {r['statement']} | {rul(r['ruling'])} | `{r['id']}` |")
    out.append("")
    return "\n".join(out) + "\n"


def main(argv):
    write = "--write" in argv[1:]
    gloss = load_glossary()
    model = load_model()
    if gloss is None or model is None:
        return 2

    errs = model_consistency(gloss, model)
    if errs:
        print("model consistency: %d problem(s)\n" % len(errs))
        for e in errs:
            print(f"  - {e}")
        print()
        return 2

    desired = render_glossary(gloss, model)
    if write:
        with open(GLOSSARY_MD, "w", encoding="utf-8") as f:
            f.write(desired)
        print("wrote GLOSSARY.md")

    files = canon_files()
    links = check_links(files)
    terms = sweep(files, gloss["retired"], "term")
    claims = sweep(files, model["forbidden"], "claim")

    stale = False
    if not write:
        current = open(GLOSSARY_MD, encoding="utf-8").read() if os.path.isfile(GLOSSARY_MD) else ""
        stale = current.rstrip("\n") != desired.rstrip("\n")

    if links:
        print(f"link integrity: {len(links)} broken link(s)\n")
        for rel, ln, t, why in links:
            print(f"  {rel}:{ln}  ({t})  — {why}")
        print()
    if terms:
        print(f"retired terms: {len(terms)} unallowed match(es)\n")
        for rel, ln, r, text in terms:
            print(f"  {rel}:{ln}  [{r['id']}]  '{r['term']}' -> {r['use']}  ({r['ruling']})")
            print(f"      > {text}\n")
    if claims:
        print(f"retired claims: {len(claims)} unallowed match(es)\n")
        for rel, ln, r, text in claims:
            print(f"  {rel}:{ln}  [{r['id']}]  {r['subject']} {r['predicate']} {r['object']}  ({r['ruling']})")
            print(f"      {r['statement']}")
            print(f"      > {text}\n")
    if stale:
        print("GLOSSARY.md is out of sync with the model — run: python3 _model/check.py --write\n")

    if links or terms or claims:
        print("Fix it, or (for a deliberate historical callback) add on the line or the one above:")
        print("  <!-- retired-lint: allow <id> reason: ... -->")
    if links or terms or claims or stale:
        return 1

    print(f"canon check: clean — {len(gloss['live'])} live terms, {len(gloss['retired'])} retired terms, "
          f"{len(model['canonical'])} canonical + {len(model['forbidden'])} forbidden relations; "
          f"links, terms, claims OK across {len(files)} docs; GLOSSARY.md in sync.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
