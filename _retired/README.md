# The Retired-Claim Register (the graveyard)

> **This register owns no ruling. It indexes authoritative Concordance entries. Where this summary and
> its cited ruling disagree, the ruling wins.**

It answers one question: *"I found this term in old material — is it still real, renamed, rejected, or
transformed?"* It is the continuity tool that lets the corpus **name the dead, cite its death, and make
recurrence mechanically detectable** — rather than relying on anyone to "remember not to say that."

## It registers *claims*, not words
Words like **Reaction, Support, Frame, layer, compiled, derived, Archetype** are valid English in many
sentences and are **not** banned. What is retired is a specific **semantic claim** — e.g.
*"Reaction is a Resource," "Support is a Role," "Archetype is executable," "Frame contains Archetypes."*
The lint therefore matches **contextual patterns**, never bare words.

## How the sweep works
- **`registry.tsv`** — the single machine-readable list of retired claims (`id · pattern · scope · authority · message`). It is the source of truth for both the lint and the table below.
- **`sweep.py`** — scans the canonical docs (`README.md`, `composition/`, `interface/`, `slice-1..3/`), reports `file:line · id · authority · remediation`, and **exits nonzero on any unallowed match.** Run it anytime: `py _retired/sweep.py` (or `python3`).
- **Allowances** are inline, not line-numbered (lines move): a deliberate historical callback in canon carries `<!-- retired-lint: allow <id> reason: … -->` on its own line or the line above. Every exception is thus a *named, visible field* — very CUS.
- The sweep **ignores** `_retired/` itself, `.git/`, and `notes/`.

## The register
Each row cites the ruling that retired the claim. Statuses are verified against those rulings, not guessed.

| Retired claim / meaning | Surface term | Status | Current treatment | Authority | Lint id |
|---|---|---|---|---|---|
| Archetype is executable / operative / compiled / derived / stored | Archetype | SUPERSEDED | Archetype is a **rendered Presentation view** | CON-0023 | archetype-operative, archetype-author |
| A Frame *contains* Archetypes / is a layer / is a root Object | Frame | CORRECTED | **FrameSpec** (authoring schema) + **physical Frame**; not a hierarchy | CON-0023 | frame-hierarchy, frame-layer |
| The FrameSpec *owns* fields | FrameSpec | CORRECTED | FrameSpec owns no fact; the **Figure Definition** owns `role`/`tool` | CON-0023 | framespec-owns |
| Nerve resolves as a 3-dice test / "Nerve check" | Nerve | SUPERSEDED | Nerve is a **tiered save**; the aftermath roll is the **Morale check** | CON-0001; CON-0011 | nerve-check, nerve-3dice |
| Reaction is a Resource / pool / budget / economy | Reaction | REJECTED (struck) | Out-of-turn answers are **free Written Triggers**, capped by Position | First Corpus `reaction-struck` | reaction-resource |
| There is a Reaction / Support **Packet category** | Reaction / Support | REJECTED | Packet **Tools** are Melee/Ranged/Hybrid; no such category | CON-0023 | reaction-category |
| "Shove" is a distinct mechanic | Shove | RENAMED → Push | Displacement is **Push** (a Push Effect on a packet) | CON-0012 | shove |
| AP = 3 for all / universal AP | AP | SUPERSEDED | AP by **Rank** — Square 2, Circle 3 | CON-0002 | universal-ap |
| The Mind track is a "one-way ratchet" | ratchet | CORRECTED | Steps down on unsaved Morale; **only Rally steps up** in-battle | Slice-2 01_MIND_CHANNEL | one-way-ratchet |
| "MOVE-class" (a fourth verb category) | MOVE-class | CORRECTED | Only three verbs; **Form Up is a MOVE** | Slice-1 03_GRAMMAR | move-class |
| A Circle is immune to Morale / breaks by a written trigger / has its own break meter / never breaks | Circle | SUPERSEDED | A Circle breaks **like a Square** via the Mind channel; resilience = high Nerve tier | CON-0010 (rev.) | circle-immune |
| Support or Control is a **Role** | Support / Control | MERGED → Utility | Roles are **Pressure / Anchor / Utility** | First Corpus A | support-role |
| Grades use a Ladder / Rungs / Outcome Track | Ladder / Rungs | RENAMED → Success Grade | The result of a roll is a **Success Grade** | First Corpus D | grade-ladder |
| Tempo is speed / movement rate | Tempo | CORRECTED | Tempo is the **cadence of the decision loop**, not movement | CON-0022 | tempo-speed |
| A Packet card's **back** is the Definition | (card back) | CORRECTED | **Both faces are Presentation**; the JSON in code is the Definition | CON-0023 | packet-back-def |
| The Caravan carries / owns "the roster" of Figures | Caravan / roster | CORRECTED | Caravan carries **Books**; the roster is **membership Relationships** | CON-0023 | caravan-roster |

## Authority for the register *process*
The retired-claim register and the sweep discipline are ratified by **[CON-0024]** — which owns only
the *mechanism*, not the substantive rulings above. Each substantive claim's authority is the ruling in
its own row.
