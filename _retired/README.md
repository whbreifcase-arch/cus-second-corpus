# The Retired-Claim Register (the graveyard)

> **This register owns no ruling. It indexes authoritative Concordance entries. Where this summary and
> its cited ruling disagree, the ruling wins.**

It answers one question: *"I found this term in old material — is it still real, renamed, rejected, or
transformed?"* It is the continuity tool that lets the corpus **name the dead, cite its death, and make
recurrence mechanically detectable** — rather than relying on anyone to "remember not to say that."

## Two layers: terms vs claims
Drift comes in two shapes, and each has its own source of truth and its own lint:

- **Terms** — dead *words/phrases* (`Shove`, `Ladder`, `Nerve test`, `MOVE-class`). Lexical: a word is
  either live or retired. These live in the top-level **[`glossary.tsv`](../glossary.tsv)** (LIVE and
  RETIRED together — the live rows double as the canonical hyperlink target for each term) and are swept
  by **[`glossary_lint.py`](../glossary_lint.py)**, which also checks **link integrity** (every relative
  markdown link resolves to a real file and heading). A retired term is caught structurally, and a live
  term earns a definition to link to.
- **Claims** — dead *relationships* between valid words (*"Reaction is a Resource," "Frame contains
  Archetypes," "Archetype is executable"*). Here every word is fine; the **proposition** is retired.
  A link can't express "these two valid nouns may not stand in this relation," so these need contextual
  patterns. They live in **`registry.tsv`** and are swept by **`sweep.py`**.

That split is deliberate: it is why the sweep matches **contextual patterns, never bare words**, and why
`glossary_lint` can afford exact term matching. (Structuring the *claims* as machine-checkable relations —
so they stop living in prose at all — is the next step, and overlaps the "Definition vs Presentation"
model.)

## How the lints work
- **`registry.tsv`** — the machine-readable list of retired *claims* (`id · pattern · scope · authority · message`); source of truth for `sweep.py` and the table below.
- **`glossary.tsv`** — the machine-readable list of *terms* (`term · status · id · ref · ruling · note`); source of truth for `glossary_lint.py`. LIVE rows point at a term's canonical home; RETIRED rows name the live replacement.
- **`sweep.py`** / **`glossary_lint.py`** — both scan the canonical docs (`README.md`, `composition/`, `interface/`, `slice-1..3/`), report `file:line · id · authority · remediation`, and **exit nonzero on any unallowed match.** Run: `python3 _retired/sweep.py` and `python3 glossary_lint.py`.
- **Allowances** are inline, not line-numbered (lines move): a deliberate historical callback in canon carries `<!-- retired-lint: allow <id> reason: … -->` on its own line or the line above. Both lints honor the same marker, so an `id` from either source works. Every exception is thus a *named, visible field* — very CUS.
- Both lints **ignore** `_retired/` itself, `.git/`, and `notes/`.

## The register of retired *claims* (`registry.tsv`)
Each row cites the ruling that retired the claim. Statuses are verified against those rulings, not guessed.

| Retired claim / meaning | Surface term | Status | Current treatment | Authority | Lint id |
|---|---|---|---|---|---|
| Archetype is executable / operative / compiled / derived / stored / authored | Archetype | SUPERSEDED | Archetype is a **rendered Presentation view** | CON-0023 | archetype-operative, archetype-author |
| A Frame *contains* Archetypes / is a layer / is a root Object | Frame | CORRECTED | **FrameSpec** (authoring schema) + **physical Frame**; not a hierarchy | CON-0023 | frame-hierarchy, frame-layer |
| The FrameSpec *owns* fields | FrameSpec | CORRECTED | FrameSpec owns no fact; the **Figure Definition** owns `role`/`tool` | CON-0023 | framespec-owns |
| Nerve resolves as a **3-dice test** | Nerve | SUPERSEDED | Nerve is a **tiered save**; the aftermath roll is the **Morale check** | CON-0001 | nerve-3dice |
| Reaction is a Resource / pool / budget / economy | Reaction | REJECTED (struck) | Out-of-turn answers are **free Written Triggers**, capped by Position | First Corpus `reaction-struck` | reaction-resource |
| There is a Reaction / Support **Packet category** | Reaction / Support | REJECTED | Packet **Tools** are Melee/Ranged/Hybrid; no such category | CON-0023 | reaction-category |
| AP = 3 for all / universal AP | AP | SUPERSEDED | AP by **Rank** — Square 2, Circle 3 | CON-0002 | universal-ap |
| A Circle is immune to Morale / breaks by a written trigger / has its own break meter / never breaks | Circle | SUPERSEDED | A Circle breaks **like a Square** via the Mind channel; resilience = high Nerve tier | CON-0010 (rev.) | circle-immune |
| Support or Control is a **Role** | Support / Control | MERGED → Utility | Roles are **Pressure / Anchor / Utility** | First Corpus A | support-role |
| Tempo is speed / movement rate | Tempo | CORRECTED | Tempo is the **cadence of the decision loop**, not movement | CON-0022 | tempo-speed |
| A Packet card's **back** is the Definition | (card back) | CORRECTED | **Both faces are Presentation**; the JSON in code is the Definition | CON-0023 | packet-back-def |
| The Caravan carries / owns "the roster" of Figures | Caravan / roster | CORRECTED | Caravan carries **Books**; the roster is **membership Relationships** | CON-0023 | caravan-roster |

## The register of retired *terms* (`glossary.tsv`)
Dead vocabulary — matched exactly, replaced by a live term. (The glossary also carries the LIVE
vocabulary; those rows are the hyperlink target for each term.)

| Retired term(s) | Status | Current term | Authority | Lint id |
|---|---|---|---|---|
| Shove | RENAMED → Push | Displacement is a **Push** (a Push Effect on a packet) | CON-0012 | shove |
| Ladder / Rungs / Outcome Track | RENAMED → Success Grade | The result of a roll is a **Success Grade** | First Corpus D | grade-ladder |
| Nerve test / Nerve roll / Nerve check | SUPERSEDED | **Morale check** / tiered **Nerve save** | CON-0001; CON-0011 | nerve-check |
| MOVE-class | CORRECTED | Only three verbs; **Form Up is a MOVE** | Slice-1 03_GRAMMAR | move-class |
| one-way ratchet | CORRECTED | Steps down on unsaved Morale; **only Rally steps up** in-battle | Slice-2 01_MIND_CHANNEL | one-way-ratchet |

## Authority for the register *process*
The retired-claim register, the glossary, and both lints are ratified by **[CON-0024]** — which owns only
the *mechanism*, not the substantive rulings above. Each substantive claim's or term's authority is the
ruling in its own row.
