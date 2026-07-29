# `_model/` — the canon's machine-readable brain

This folder is the small, boring, dependable core that keeps the corpus honest.
You don't have to understand the whole system to use it. Here it is in plain terms.

## The one idea

The docs are prose, and prose drifts. Over time a sentence creeps back in that
says something the corpus has already decided is wrong. There are exactly **two
ways** that happens, and this folder guards both:

1. **A dead word comes back.** Someone writes "Shove" when the word is now
   "Push", or "Ladder" when it's "Success Grade". This is about *vocabulary*.
2. **A dead idea comes back.** Someone writes "the Frame contains the Archetype"
   — every word is fine, but the *relationship* between them is one we retired.
   This is about *how things relate*.

A link can fix the first (a word either points at a real definition or it
doesn't). It can't fix the second, because the words are all valid — only the
sentence is wrong. So the two are stored differently.

## The three files

| File | Holds | In plain terms |
|---|---|---|
| **`glossary.tsv`** | the **words** | the protected vocabulary + where each term is defined, and every retired word + what to say instead |
| **`model.tsv`** | the **relationships** | short "A relates-to B" statements: the true ones, and the retired ones |
| **`check.py`** | the **guard** | one command that reads both files and checks the docs |

From those two data files, `check.py` also writes **[`GLOSSARY.md`](../GLOSSARY.md)**
at the top of the repo — a clean, clickable, always-up-to-date glossary you can
just read. You never edit that file; you edit the two `.tsv` files and let the
tool rewrite it.

## Using it

```
python3 _model/check.py           # check the whole corpus, report any drift
python3 _model/check.py --write   # rebuild GLOSSARY.md from the data, then check
```

It exits quietly with `0` when everything is clean, and prints exactly what and
where when something drifted. What it checks:

- **Links** — every link between docs actually goes somewhere real.
- **Retired words** — no dead vocabulary slipped into the docs.
- **Retired claims** — no dead relationship slipped in.
- **Itself** — every entry cites a ruling, every live term's home really exists,
  and `GLOSSARY.md` matches the data.

## When you *mean* to name a dead thing

Sometimes a doc has to say "we do **not** use 'Shove' anymore" — which means the
dead word appears on purpose. Mark that line (or the line above it) so the guard
knows it's deliberate:

```
<!-- retired-lint: allow <id> reason: says why the retired thing is wrong -->
```

The `<id>` is the little code in the last column of `GLOSSARY.md`'s retired
tables (e.g. `shove`, `frame-hierarchy`).

## Adding to it

- **A new word?** Add a `LIVE` row to `glossary.tsv` (term, its home doc, a
  one-line meaning). Run `check.py --write`.
- **Retiring a word?** Add a `RETIRED` row (the dead word + what replaces it +
  the ruling).
- **A new rule about how things relate?** Add a `canonical` row to `model.tsv`.
  Retiring a relationship? Add a `forbidden` row with a pattern that catches it
  in prose.

## Where the authority actually lives

This folder **indexes**; it does not **rule**. Every row cites a Concordance
ruling (the `CON-####` codes), and where a row and its ruling ever disagree, the
ruling wins. The register *mechanism* was ratified under **CON-0024** for the
earlier `_retired/` tooling; this consolidated `_model/` form (glossary +
relation model + one checker) still needs its own ruling — **proposed as
CON-0025, pending in the Concordance**. Until that lands the mechanism is
provisional; the substantive term and claim rulings it cites are unaffected.

> The long-term direction (noted here so it isn't lost): the retired *claims*
> still carry a regex to catch them in prose. The deeper version lifts the
> relationships fully out of prose, so `model.tsv` becomes the source and the
> docs are checked against it — the same "the structure is the truth, the prose
> is a view" idea the corpus already uses for Definition vs Presentation. Not
> today's job; a signpost for later.
