# PROJECT ARCHAEOLOGY — DISCOVERY PHASE REPORT

**Status: UNRATIFIED FINDING — a discovery document, not canon.**
Filed in `notes/` per this corpus's own convention: nothing here is authority, and
`_model/check.py` does not govern it. No summary outranks its cited source.

**Director:** temporary multidisciplinary research studio, seven independent teams.
**Corpus examined:** 5 uploaded artifacts + 4 GitHub repositories (`cus-second-corpus`,
`cus-concordance`, `cus-kernel-rebuild`, `cus-rules`) + the `CUS_Rulebook_Vault v0.5`
Obsidian vault. ~1.5M characters, 219 git commits, 2026-07-01 → 2026-08-03.
**Date of report:** 2026-08-04.

---

## 0 · HOW EVIDENCE WAS WEIGHTED

Every team applied the same ladder, and stated the tier behind each finding.

| Tier | Kind of evidence |
|---|---|
| **W5** | Measured play or simulation output |
| **W4** | Decisions that survived multiple revisions, or were independently re-derived in a later line |
| **W3** | Signed / locked rulings (`CON-####`, `Locked Decisions`, "SIGNED (William, date)") |
| **W2** | Current authored canon, unrevised |
| **W1** | Brainstorming, rationale essays, notes, `PARKED`/`◇ draft` items |

**Three Director amendments,** adopted after seeing the reports:

- **W4½ — computed, not measured.** The Table Companion's per-hero defence math and
  Team C's binomial audits are real closed-form analysis, but they are not play data.
  They sit above signed rulings and below simulation. This distinction turned out to
  matter enormously: **the corpus contains a great deal of correct arithmetic and
  almost no observation.**
- **Convergence outranks signature.** A commitment independently re-derived in two
  lines that do not cite each other outranks a signed ruling in one line. Signed
  rulings in this corpus have a documented half-life of about 48 hours; convergent
  commitments have held for five weeks across three incompatible engines.
- **Negative evidence is evidence.** A thing built repeatedly and abandoned every
  time, and a thing planned repeatedly and never begun, are both strong findings.
  Several of the most important conclusions below rest on exhaustive `grep` returning
  nothing.

---

# 1 · EXECUTIVE SUMMARY

**This project has already produced its game. Twice. It is now three rebuilds deep
into producing the conditions under which it could produce its game.**

That is the finding. Everything else is detail.

Between roughly 1 and 14 July 2026 the designer assembled **The Campaign — Core
Rulebook, First Edition**: 27 rule sections, ~14 hero paths, a warband, a complete
first scenario, a one-page summary, and an opening promise it keeps — *"This book is
the whole game… A table that has never seen it can play tonight."* Shortly after, he
re-engined the same game into the **Table Companion**, which added five warbands, 24
enemy profiles with printed brains, a full enemy-AI grammar, two scenarios, and
per-unit balance mathematics that I checked and found correct to the decimal.

On 23 July he began again, from first principles, under a different name. In the
eleven days since, four successive architectures have been built — CUS v0.6 (with a
1.3-million-game simulation and a working Tabletop Simulator implementation), the
Concordance, the Second Corpus, and the Rulebook Vault v0.5. Those eleven days have
produced **zero playable warbands, zero figures, zero scenarios, and zero recorded
games.** On 29 July, commit `e140a09` deleted 160 files and 50,240 lines, including
every simulator, the entire software build, and all nine factions.

The most recent artifact — the Vault, issued 3 August — was manufactured in **seven
hours and forty-one minutes**, and contains a constitution, an authority chain, a
version procedure, three "immutable" kernel snapshots, an archive of packets
superseded the same afternoon, a validation report reading `PASS`, and 179 SHA-256
hashes. It also contains a locked Morale rule that cannot be executed, a locked
Packet Schema that none of its 39 packets obey, and one-fifth of its headline feature
implemented as a single unused word.

**The mechanism is not laziness or indecision.** Each rebuild diagnosed a real
defect and fixed it well. The problem is structural: **the only feedback channel this
project has ever used is the designer re-reading his own documents, and re-reading
always returns the same verdict — the vocabulary is wrong.** Defects that documents
can surface get fixed brilliantly and repeatedly. Defects that only a table can
surface accumulate untouched into every new baseline. Five separate apparatuses for
capturing play have been built across three lines. All five are empty.

**What is genuinely here, and is worth five years:** a coherent, unusually specific
design philosophy, re-derived so many times and in so many vocabularies that it must
be treated as intent rather than preference. The table is the memory. Committing
forecloses something. The battlefield decides, not the character sheet. Nobody is the
referee. Down is not dead, and who lives is the story's business. Nothing scores a
kill. The animals always come home.

**What should be discarded:** the charter that forbids copying work forward; the
636,000-word inventory layer built to serve a rebuild that was itself abandoned five
days later; the composition and interface layers, which by their own documents decide
nothing at a table; the multi-setting requirement, which has produced two abstractions
and no content; and the ceremony — hashes, lock statements, immutability regimes —
that guarantees integrity over material never checked for meaning.

**The highest-leverage action available is one evening long.** Play *At the
Den-Mouth* — the one complete play package in the corpus, in which every profile named
is fully statted in the same file — and write four sentences into a folder that has
been empty in every incarnation of this project. The designer wrote the diagnosis
himself on 1 July, and then did the opposite for five weeks:

> **"The clock is one of the two judges, and it does not exist on paper."**

---

# 2 · DIRECTOR'S INITIAL OBSERVATIONS

Recorded before the teams reported, so their independence can be judged.

1. **There are two lines, not one, and they never cite each other.** "The Campaign"
   and "CUS" share no vocabulary, no resolution engine, and no cross-reference in
   either direction. They share a great deal of DNA.
2. **There are more engine states than artifacts.** `cus-rules/index.html` (23 July,
   "CODEX v0.5") is a sixth state and turned out to be the most useful single document
   for dating resurrections.
3. **The corpus is AI-assisted throughout.** 117 of 130 commits across the CUS repos
   carry `Co-Authored-By: Claude Opus 4.8 / Opus 5`. William is author-of-record and
   signs the rulings. This is context, not criticism — but it explains the velocity
   (32 commits in one day), and it makes the *transition between artifacts* the
   fragile joint, because a fresh session does not remember the last rebuild.
4. **The trend is legible from the file listing alone.** Playability peaks in
   mid-July and again on 27 July. Everything after 28 July is architecture.
5. **The designer's own rationale register, `G_WHY_NOT.md`, names the project's
   thesis outright** — a fact no team had to infer:
   > *"They are **one idea found six times**. Every one of them says: **you get one
   > commitment, and committing forecloses something.** … Treat this as the design's
   > thesis and use it as a test."*

---

# 3 · INDEPENDENT TEAM REPORTS

Seven teams worked in isolation on the same corpus with the same weighting rules and
no access to one another's findings. Full reports are held in the research record;
their load-bearing conclusions follow.

### Team A — Systems Archaeologists
Traced every major mechanic across all six engine states. Found **three things never
questioned** (alternating activation; base shape = rank = AP; position modifies dice,
not numbers) and **eleven resurrections** — ideas killed in one line that return in a
later one under another name. Built the cross-line synonym table. Classified every
rules change by its stated trigger and found that **roughly two-thirds are caused by
the corpus arguing with itself**, and four by measured output, all from one weekend.

### Team B — Tabletop Designers
Reconstructed the physical room. Found that **exactly one artifact in the corpus
describes a table** and the rest describe a system. Counted **five full independent
constructions of a printed enemy brain** — the most re-derived idea in the corpus.
Discovered that on 25 July the designer built a playable guided tutorial, a
print-and-play field guide and a 36-card deck, and reverted all of it seven minutes
to three hours later with the message *"wrong target."* Measured the
teaching-to-specifying ratio falling from ~40% to 0% to 7%.

### Team C — Tactical Wargamers
Re-ran the simulation. **All six headline findings reproduce.** Also found that
`crush` — the terminal state of the charge cascade, listed in the capstone as
validated — **fired zero times in 1,296,000 games** because the study harness never
built a wall. Computed the positional payoff in every line and found it worth ×3.1 in
the Corebook, ×2.64 in the Table Companion, and **+5% to +47% in the Vault**, which
arithmetically falsifies the Vault's own Design Law 8. Found the Table Companion's
"bad spot" is a **no-op against every ATK-1 model — roughly 85% of the printed
roster**. Found one dominated weapon, one null Grade band, and the exact
non-monotonicity bug the designer's own rationale register predicted and told him to
lint for.

### Team D — Narrative Designers
Identified 26 mechanics whose only function is to manufacture a specific story beat,
and showed that the beats survive total engine replacement while the mechanics do not.
Established that **5 of 5 starter warbands are authored as mercy dilemmas** and that
the moral cost of killing is treated as a balance term. Separated the deliberate
absences into three tiers — argued and disciplined (`Redemption`, `hollow`'s trigger),
asserted and self-sealing (`SOUL`), and merely scheduled and never written (the
"membrane", the Child marker, `The Sword & the Light`). Found the narrative layer
thins monotonically to **zero in the newest artifact**.

### Team E — Cognitive Psychology & UX
Counted **nine independent derivations** of one rule — *the table is the memory, and
the only thing held in a head is the current activation's action points* — across two
mechanically unrelated games. Then found three clean violations of it, all in the
newest artifact, all clustering where state spans more than one figure or more than
one activation. Measured the architecture's cost to a *player* as close to zero (a
real achievement) and its cost to a *future collaborator* as severe: five vocabularies
in five weeks with one machine-checked bridge, pointed at the wrong artifact.

### Team F — Production & Engineering
Counted the artifacts. Established by zip-timestamp forensics that **the entire Vault
— 165 files, three kernel/build versions, an immutability regime, and an archive of
superseded packets — was produced between 07:10 and 14:51 on a single day.** Measured
Concordance governance at **2.31 : 1 against the text it governs**, and the Second
Corpus retaining **5.5% of its own line history**. Verified that the Vault cites no
prior artifact anywhere in 165 files. Named the highest-leverage decision and the
largest sunk-cost trap.

### Team G — Adversarial Critics
Prosecuted seven charges. Upheld five, split one, dismissed one. Verified all 179
build hashes (**179 match, 0 mismatches** — the one control in the corpus that is
exactly as good as it claims). Audited all 39 Vault packets programmatically: **0 of 39
obey the locked Packet Schema; the locked Effect Lexicon's five core verbs appear in
zero packets; 9 undefined tags in 30 uses.** Ran the Second Corpus's continuity
checker and found it reports `clean` while the exact retired claim it was built to
catch sits verbatim in the flagship walkthrough — the regex wanted `own break meter`
and the prose says `on its own meter`.

---

# 4 · CROSS-TEAM CONSENSUS MATRIX

| # | Finding | Teams | Tier | Confidence |
|---|---|---|---|---|
| C1 | **No record exists of any human ever playing any version of this game.** Five capture apparatuses across three lines; all empty. | **A B C D E F G (7/7)** | W2 negative, exhaustive | **Very high** |
| C2 | **The project restarts rather than iterates.** Five to six full vocabulary resets in five weeks; each keeps the ideas and discards the artifacts. | **A B D E F G (6/7)** | W2 | **Very high** |
| C3 | **Governance and architecture grow monotonically; playable content declines monotonically.** | **A B D E F G (6/7)** | W2 measured | **Very high** |
| C4 | **"The table is the memory"** is the single most stable commitment in the corpus. | **A B C E F (5/7)** | **W4** × 9 derivations | **Very high** |
| C5 | **Position over numbers is the stated thesis of every line — and is only load-bearing in Line 1.** | **A C E G (4/7)** | W2 arithmetic | **High** |
| C6 | **Base shape = rank = action points; alternating single-figure activation; the flank and rear matter.** Present in all six engine states. | **A C E (3/7)** | **W4** × 6 | **Very high** |
| C7 | **The enemy must run itself from a printed card, with no referee.** Built five times in Line 1; absent from both CUS lines. | **A B C D (4/7)** | **W4** | **High** |
| C8 | **Nothing scores a kill; the aftermath is the game.** Survives two total engine replacements and a cross-line reconstruction. | **A C D (3/7)** | **W4** | **High** |
| C9 | **The Vault is a restart, not a successor.** It cites no prior artifact and re-locks at least one claim a machine-enforced graveyard forbids. | **A E F G (4/7)** | W2/W3 conflict | **High** |
| C10 | **The corpus contains a great deal of correct arithmetic and almost no observation.** Every W5 datum targets an engine superseded at least twice. | **C F G (3/7)** | W5 self-retracting | **High** |
| C11 | **Deliberate absences are real design.** `Redemption`, `hollow`'s trigger, `SOUL` — re-honoured across a rebuild that deleted 70 other files. | **A D (2/7)** | W3 | **High** |
| C12 | **The commitment economy is the design's thesis**, and the designer says so in writing. | **A C E (3/7)** | W1 stated / W4 observed | **High** |

**Unanimity is rare and worth naming.** Seven teams, working blind, in seven
disciplines, all independently arrived at C1. That is the strongest signal this
investigation produced.

---

# 5 · CROSS-TEAM DISAGREEMENTS, AND THE DIRECTOR'S RESOLUTION

Disagreements are resolved by evidence, not by averaging.

### D1 — Does maintaining two lines guarantee neither ships?
**Team B** implies divided attention. **Team G** says the inference is unsupported:
the Campaign has had no dated revision since ~14 July; it is not a competing
workstream but an abandoned one.
**RESOLVED FOR G.** Attention is not being split; it is being serially and totally
reallocated. This matters because it changes the prescription: the cure for split
attention is to choose. The cure for serial reallocation is to *stop reallocating* —
and to go back and pick up what was dropped. **Confidence: high.**

### D2 — Did the Vault descend from CUS or from The Campaign?
**Team A** argues vocabulary transmission from Line 1 (`Threat`, `Hearts`,
`Fine/Hurt`, reach bands, stacking modifiers — all Line-1 or CODEX-v0.5 words that the
CUS line explicitly retired). **Teams F and G** emphasise that it descends
architecturally from CUS while citing nothing.
**RESOLVED: both, and this is a discovery rather than a conflict.** The Vault takes
CUS's *architecture* (an authority chain, layers, Packets, Grades, Square/Circle) and
Line 1's *table vocabulary*. The decisive single link is Team A's: the **Threat
keyword** was scoped-but-undrafted in the Campaign manifest on 1 July — *"Register
lists them; do not invent them"* — appears drafted in the Table Companion, appears
**zero times** in the First and Second Corpus, and becomes the constitutional centre of
the Vault on 3 August. **The Vault is the first artifact that tries to merge the two
lines, and it merges them by taking Line 2's governance and Line 1's words.**
**Confidence: medium-high.**

### D3 — Is `SOUL` discipline or decoration?
**Team D** splits the refusals into three tiers and calls `SOUL` "asserted,
self-sealing" but genuinely meant. **Team G** calls it decoration, and its evidence is
sharp: the primitive marked *"Do not define or alter it under any circumstances, ever"*
was not altered — it was **restarted out of existence**, absent from all 165 Vault
files, with no ruling.
**RESOLVED BY SEPARATING INTENT FROM IMPLEMENTATION.** The *intent* — that the system
must never claim to have modelled the whole of a person — is genuine, is stated four
times across three repos, and is re-honoured after a rebuild that deleted seventy other
files. The *implementation* — a formal blank primitive with a tripwire, an appendix
slot, a glossary entry and custodial protection in a second repository — is decoration:
it guarded against the one threat that never materialised (someone defining it) and was
silent against the one that did (someone starting over). **Intent: keep. Mechanism:
discard.** See §12, False Constraint 6. **Confidence: high.**

### D4 — Is the Vault's emptiness sequencing or abandonment?
Raised as a live alternative by **A, F and G**, each of whom took it seriously.
**RESOLVED BY THE PATTERN, NOT THE INSTANCE.** The same six-step order — build the
law, build the grammar, build the content, *then* playtest — appears in the Campaign
build order (1 July), the First Corpus's closing note (25 July), and the Vault's
production order (3 August). It has reached step one every time. A plan restated three
times in five weeks and executed to step one on each occasion is not a schedule; it is
a preference. **Confidence: high.**

### D5 — Is the composition / Signature layer depth or filing?
**Team C** calls it fake depth. **Team G** grants that it is honestly labelled
authoring infrastructure and narrows the charge.
**RESOLVED FOR G's NARROWER FORM, which is the more damaging one.** The documents say
of themselves that they decide nothing at a table — Tempo is *"read by humans, never
by the resolver"*; `archetype` is *"never a stored field"*; the Signature invariants
document closes by admitting it *"reserves the terms"* and defines no procedure. That
is not a lie and it is not fake depth. It is a filing system, correctly labelled, that
consumed the documentation budget the packet linter never received. **Confidence: high.**

### D6 — Is `reaction-struck` a correct ruling?
**Team C** shows a measured report named chaff sequencing as one of three counterplays
a horde needs, and a signed ruling deleted it three days later on architectural
grounds, reasoning that envelopment covers it — when envelopment was already on the
list. **Team A** records the strike as one of the corpus's cleanest pieces of
reasoning.
**RESOLVED: the ruling is right and the consequence was never paid for.** The
architectural argument is correct — a Reaction pool really was restating what the front
arc already says, and the Champion's "2 Reactions" really was facelessness written
badly. But the mechanic's *job* — giving cheap bodies a role that is not damage — was
not reassigned. And the Campaign line independently rebuilt that exact job as a
centrepiece (`Overwhelm`), which under this report's convergence rule is W4 evidence
that the job is real even though the implementation was wrong. **Confidence: high.**

---

# 6 · EVOLUTION TIMELINE

### Era 0 — before the record (≤ 2026-07-01)
Two independent lines already exist and both are mature: **The Campaign** at Master
Codex v2.3 → Errata v2.4 ("Soul Merge") → v2.5 Register, and **CUS** at Kernel v0.6 /
How-to-Play v1.3. Neither's origin is in the corpus.

### 2026-07-01 — the Campaign states its own diagnosis
`00_MANIFEST` and `Playtest Doc Architecture v1.1`. Four document classes, a one-owner
rule, a module contract, a rewrite inbox, a build order.
- **Kept:** supersession by errata, never by rewrite. *"One owner per rule… A rule
  stated twice will fork."*
- **Known gaps, honestly logged:** CORE unassembled, PERSIST a three-page stub, four
  v2.5 items undrafted.
- **The lesson, written and not taken:** *"Run Mill Road solo, twice, with a timer…
  **Then the family.** Everything after is playtest data, not specification. The clock
  is one of the two judges, and it does not exist on paper."*

### ~07-01 → 07-14 — the productive period
**The Core Rulebook is assembled** and it is the corpus's one completed product.
- **Why it worked, and this is the single most actionable fact in this report:** the
  Architecture scoped it as **"assembly, not design"** and it copied forward. The one
  period that produced a finished game is the one period the designer forbade himself
  from designing.
- **Retained:** everything.
- **Tradeoff:** none visible.

### 2026-07-14 — Parry is cut
*"6+ plus a save out-walled the Knight."* The only content deletion in the corpus
justified by a computed number about a specific character. **Correct call, correctly
reasoned** — Parry negated 70.4% of incoming hits with a 25.9% riposte.

### post-07-14 — the Table Companion re-engine
The same game, a different engine: `ATK dice ≥ DEF`, *"no number is ever added to any
die"*, Winded, the Status Die, Knocked Out.
- **Problem solved:** arithmetic at the table. The new modifier (±1 die) is
  DEF-independent, which the d20 keep-best version was not. Genuinely better engineering.
- **Ideas retained:** the enemy card, postures, the mercy ledger, the backstab, the
  banner, base shape as rank.
- **Ideas abandoned:** the d20 engine, Parry, ~8 hero paths, and **morale — marked
  ASLEEP with its hooks left printed.** This is the most intellectually honest handling
  of an unfinished subsystem anywhere in the corpus.
- **Cost, unnoticed:** the "never below one die" floor makes the bad spot a no-op
  against every ATK-1 model — which is the entire non-boss roster.
- **Lesson available:** you may ship a game with a subsystem switched off and its
  sockets visible. Nobody has to rebuild the world to defer a feature.

### 2026-07-14 → 07-23 — the undocumented nine days
Nothing in the corpus covers this gap. **It is the moment the project changed
direction and it is unexplained.** Ranked #1 in Open Questions.

### 2026-07-23 → 07-28 — CUS v0.6, the First Corpus
75 commits in six days. A–N law documents, 125 unit profiles, 90 packets, a Tabletop
Simulator implementation in 9,272 lines of Lua, and a simulator.
- **07-24:** twelve open decisions signed; v0.6 declared *closed*, *"no open
  constitutional questions remain."*
- **07-25 (32 commits, the corpus's peak day):** `F_CLASH_RESOLUTION`; ~1.3M simulated
  charges; `CHARGE_FINDINGS` — *"The clash system is **done**"*; `G_WHY_NOT.md`,
  which moves the arguing out of the rules and names the design's thesis; the harm
  tables; `hollow` hardened with no way out and its trigger deliberately withheld.
- **07-25, 12:25 → 15:46:** a playable guided tutorial verified by 300 headless runs,
  a print-and-play field guide, a 36-card deck, a machine-readable ruleset and a
  landing site are built — and reverted. *"Revert this session's web work; wrong
  target."* **The most diagnostic three hours in the corpus.**
- **07-25, 22:08:** the AI Director, which beat the greedy AI 52–87% in testing, is
  killed after 21 hours. *"Nothing salvaged."*
- **07-27:** the Reaction economy is struck. *"Position was already answering that
  question."* Architecturally right; the measured cost was named, accepted, and never
  re-tested.
- **07-28:** Morale becomes a channel; AP by rank; the First Corpus is frozen and the
  repository archived read-only.

### 2026-07-28 → 07-30 — the Concordance and the Second Corpus
- **The Concordance** is genuinely valuable in one respect: it found ten real
  contradictions nobody had noticed, and compressed them into 24 signed rulings. It is
  also 128,904 words of governance over 55,742 words of governed text, of which 102,563
  words are per-document inventories that governed one rebuild, which was superseded,
  and were then never cited again.
- **The Second Corpus** is rebuilt in vertical slices and is, in places, excellent:
  ownership as an (Object × Layer) coordinate resolves a real contradiction and produces
  a concrete table ruling; the activation scheduler makes Rally a genuine tempo cost and
  is the best-argued design in the corpus; persistence-as-scope-plus-`advance_rule` is
  sound architecture.
- **07-29, `e140a09`:** *"prune First Corpus lineage from the tree."* **160 files,
  50,240 lines** — every simulator, the whole software build, all nine factions, every
  playable HTML page. The tree now retains 5.5% of its own line history.
- **Tradeoff accepted:** the corpus's only empirical instruments were deleted before
  they were used a second time. The Vault would later specify *"Simulation fields —
  record at minimum…"* for a simulator that had been deleted eight days earlier.

### 2026-08-03, 07:10 → 14:51 — the Rulebook Vault v0.5
Seven hours and forty-one minutes. A new authority chain, a new vocabulary, three
kernel/build versions issued in one afternoon, an archive of packets superseded the
same day, 179 SHA-256 hashes, and a validation report reading `PASS`.
- **The real idea, and it is a good one:** *"CAPABILITY IS PUBLIC. INTENT MAY BE
  UNCERTAIN."* Face-up preparation, the Equipment Promise, minimum-Reach dead zones,
  Threat Words. This is the first idea in eleven days that is about what the game feels
  like at a table rather than about how the documents relate.
- **What it cost:** persistence, the campaign, the Caravan, scars, `SOUL`, the
  Signature layer, the object model, the Concordance rulings and `_model/` — all
  dropped without a ruling. Morale regressed to a stub that cannot execute. And
  position, the constitutional thesis, fell to +5–47%.

### The shape of the curve
Playability peaks around 14 July and again on 27 July. Every artifact after 28 July is
architecture. **Each rebuild kept the same ideas and changed the words.**

---

# 7 · DESIGN DNA

Ten immutable principles. Each is philosophy, not mechanism; each is supported by
convergent evidence across lines that do not cite one another.

1. **The table is the memory.** Nothing persistent lives in a head. The only thing a
   player holds is the current activation.
   *Nine independent derivations across two mechanically unrelated games. The single
   most secure finding in this investigation.*

2. **Committing forecloses something.** Every good mechanic in this corpus is one
   idea wearing a costume: you get one commitment, and taking it closes a door.
   *The designer's own named thesis, and his own proposed test: "Does this create a
   commitment with a real foreclosure — or is it just a modifier?"*

3. **The battlefield decides, not the character sheet.** Where a rule wants to limit a
   figure, deny it the geometry, not a budget. If a decision can be created through
   position instead of a number, it is.
   *Stated in all six engine states. Load-bearing in two of them — see §10.*

4. **Nobody at the table is the referee.** The enemy runs itself off a printed card:
   first true line, meanest legal form, and a coin at the bottom of everything.
   *Constructed five separate times. The most re-derived idea in the corpus.*

5. **Judged by eye, settled in seconds.** Looks reachable, it's reachable. Looks
   flanked, it's flanked. Five minutes on one activation is a fault, not diligence.
   Unclear rule → the bad guys get the luck → coin → the table decides.

6. **A rule is wrong if it fails the youngest player or the clock.** These are the two
   judges, and the second one does not exist on paper.

7. **Loss must be bearable and it must be real.** Down is not dead; who lives is the
   story's business. Dead is permanent, and that is what makes surviving mean anything.
   The animals always come home; the spearman may not.

8. **The enemy is a person, and killing is a choice the rules refuse to score.**
   Every warband in the starter set is authored as a mercy dilemma. Nothing scores a
   kill. Letting it go is mercy; what hunting it down makes of you is a question for a
   darker book.

9. **Being alone is the worst thing that can happen to someone.** Body heals with care
   and time; mind heals with relationships. A figure with no bonds does not recover
   from what he saw. *"He is not a villain. He is a man nobody sat with."*

10. **Depth comes from the board, never from a table of combinations.** Say what a
    thing *is*, never what it is *for*. If a use fits what the thing is, it works.
    The mirror is a bridge because it is hard and flat, not because a rule says so.

---

# 8 · PLAYER PROMISE

**Who this is for.** A family table. Two to four players on a coffee table or a
two-foot square, for about an hour, with miniatures already in the house and coins for
wound tokens. At least one player is a child young enough that the Necromancer is kept
back for older players, and that child holds constitutional veto over any rule too slow
or too confusing. A second adult — named once, as Courtney — plays half the heroes and
reads the other warband's cards, because there is no referee and nobody should have to
sit out.

**The fantasy being delivered.** Not conquest and not tactical mastery. **Stewardship
and its cost.** You take people out on a green road that used to be a trade route, and
you bring some of them back changed, and what happened to them was partly your fault.

**The emotions that should dominate.** Dread that is bearable. Relief that is earned.
Complicity — the feeling that the death was your arithmetic, not the dice. Affection
for people the rules insist are people and not equipment.

**The moments players should remember years later.**
- The first time a spearman did not come home, and the animals did.
- The evening the wagon had one bed and two broken bodies in it.
- The argument about the Pale Sexton — the gravedigger with a spade, tagged as a
  living man in an undead warband — that the designer engineered on purpose and whose
  success criterion is that the table argues. *"The table will argue. Good."*
- Sending a helper in first, knowing he eats the answer, so the hero's blade lands
  unanswered.
- Writing one sentence about a scar, and finding that sentence is the mechanic.

**The frustrations being eliminated, repeatedly and across every line.** Arithmetic at
the table. Stacked modifiers. Looking anything up mid-fight. Arguing about geometry.
Analysis paralysis. Bookkeeping that yields no decision. A referee. Points values. A
rule you cannot see on the table.

**The experiences being created, repeatedly.** A fight that is decided by where you
stand. An enemy that behaves without anyone deciding for it. A roster that grows by
mercy and is limited by bread. A record of the campaign that is written in sentences,
not numbers.

---

# 9 · EMOTIONAL GOALS

1. **Loss reversible enough to bear, permanent enough to matter.** *(W4 — survives two
   engine replacements)*
2. **A death should be a decision someone made, not a number that came up.** *(W3/W4 —
   the bed-slot forced choice; "the execution read, watched every time")*
3. **The enemy should be someone.** *(W4 — 6 of 6 warbands)*
4. **Being alone should be the worst outcome.** *(W3/W4 — the most consistently
   re-derived emotional law in the corpus)*
5. **Play should generate a written record, and the record should be the mechanic.**
   *(W4 — "one sentence, no numbers"; "that line is the whole difficulty system")*
6. **A veteran should be visibly changed, not merely worse.** *("Every entry takes
   something and gives something, because that is what surviving does.")*
7. **The room should have to argue out loud about something the rules refuse to
   settle.** *(W3 — "if a group works something out at their own table, what they
   worked out is theirs")*
8. **A young player should be safe here, and should be able to grow out of it without
   leaving.** *(Widest gap in the corpus between how often it is stated and how much
   of it is built.)*

---

# 10 · CURRENT PROJECT EVALUATION

Effort invested is not a reason to keep anything.

### Strongly supports design intent — keep, defend, build on
| Item | Why |
|---|---|
| **The Campaign Core Rulebook** | The corpus's one completed product. Missing 24 art files and nothing else. |
| **The Table Companion** | The most complete play package in existence here: 6 heroes, 5 warbands, 24 printed brains, 2 scenarios, correct balance math. Already an HTML reference app. |
| **The enemy-card engine** (first true line, meanest legal form; the queue; the fall-through ladder; the downgrade rule; posture) | The most finished subsystem in the corpus. "Killing the spotter makes the artillery dumb with zero rules" is first-class emergent design. |
| **The posture dial** | One word, three fights, ~2.6× swing in enemy output, bounded by an anti-analysis clause. Cheapest good idea here. |
| **The activation scheduler** (Second Corpus) | Makes Rally a real tempo cost. Best-argued design in the corpus. |
| **Persistence as scope + `advance_rule` + Battle-Start/Aftermath** | Sound architecture. Line 1 lacks it and needs it. |
| **Ownership as an (Object × Layer) coordinate** | Resolves a real contradiction and produces a concrete table ruling. |
| **"Capability is public; intent may be uncertain"** + face-up WAIT + minimum-Reach bands | The Vault's one genuine contribution, and a good re-derivation of the simulation's cleanest result by an entirely different route. |
| **`G_WHY_NOT.md` as a document type** | Separate the rule from its defence; cite by slug. Original, effective, solved a measured problem — and was not carried forward. |
| **The `_model` insight** (dead words and dead claims are different failure modes) | Correct and non-obvious. The tool failed; the distinction is right. |
| **The Table Companion's per-unit design logs** | The only place in the corpus where a number changed a piece of content. This is what balance reasoning should look like. |

### Weakly supports intent — keep, but stop investing
The Vault Kernel v0.2.0 (coherent, but see below); the Threat Word vocabulary (4 of 6
backed by content); Grade discreteness (a distribution choice, not a decision);
`BALANCE_REPORT.md` as a method (excellent method, superseded conclusions).

### Neutral
The Concordance's 24 signed rulings — genuinely useful compression, now orphaned. The
BUILD MANIFEST: I verified all 179 hashes and they match. It does exactly what it
claims; what it claims is not currently worth anything.

### Probably accidental
- **The 3-AP Circle's free hit-and-run** in the Second Corpus. Deleting melee
  stickiness without noticing the third action point now buys disengagement.
- **"Modifiers stack freely"** in the Vault — a symptomatic fix for weak modifiers,
  which repealed the non-stacking law that made "one state" a principle.
- **The Grade-ceiling saturation.** Four individually reasonable decisions — flat
  damage, Grades topping at 3, a 2-Heart standard figure, a 2-AP Square — multiply into
  base lethality exceeding the health pool. Nobody did the multiplication.
- **The bad-spot no-op** against ATK-1 models.

### Probably harmful
- **The re-derivation charter** — *"Nothing migrates merely because it existed."* See §12.
- **Validation that verifies presence, never conformance.** `PASS` on a build with a
  dominated weapon, a non-monotonic baseline packet, a locked schema no content obeys,
  and a Morale rule that cannot execute.
- **`Great Weapon — Cleave`**, dominated ~2.4×, and the only packet that generates
  retaliation — so a rational player never takes it, so retaliation never fires.
- **The Vault's Morale channel**: one source, no save, an inert middle state, an
  undefined terminal, shipped `locked`.

### Needs experimentation before another line is built
Winded (the designer parked a hero ability specifically to test it — the one place the
corpus asked the table a question); Reach bands; REACT as opt-in retaliation; the
posture dial; counter-charge (the one untested defensive option, and the one that most
directly threatens the simulation's central thesis — roughly a day's work on a working,
reproducible harness).

### Should likely be removed
| Item | Reason |
|---|---|
| **The Concordance inventory layer** (102,563 words) | Served one rebuild, which was superseded five days later, and has been cited zero times since. |
| **The composition / Signature layer** | By its own documents it decides nothing at a table and *"reserves the terms."* Its ratifying body had already stopped meeting when its ratification was proposed. |
| **The interface / physical component ecosystem** | 2,047 words, two `PROVISIONAL / UNRESOLVED` markers on its load-bearing details, no CAD, no quote, no cost — and it contradicts the corpus's own signed "play is analog, no screen at the table." |
| **The multi-setting requirement** | Two independent attempts, two elegant abstractions, zero cross-setting content. Setting-neutrality is *why* no figure exists. |
| **`SOUL` as a formal reserved primitive** | Intent keep; mechanism discard. See §12. |
| **The Vault's immutability ceremony** | Hashes, lock statements and immutable snapshots over material produced the same afternoon and never checked for meaning. |

---

# 11 · CONTRADICTIONS

### 11.1 Simplicity vs the architecture that serves it — **GENUINE, and resolvable**
The stated goal is that a player holds one number in their head. The delivered
architecture is five vocabularies, four layers, three axes, five invocations, three
resolvers, an ownership coordinate system and two authority chains.
**Evidence favours:** simplicity, overwhelmingly. Team E measured the architecture's
cost to a *player* as near zero — that is a real achievement and the architecture is
not the villain. The cost lands on a future collaborator, and there it is severe.
**Resolution:** the architecture is not too complex; it is *uncited* and *unbounded*.
Cap it: one vocabulary, one bridge document, and a rule that no new layer may be
authored while the content folders are empty.

### 11.2 Determinism vs "the bad guys get the luck" — **GENUINE, and already resolved in practice**
CUS declares *"determinism as trust — after resolution, nobody negotiates the result"*
and forbids drawn cards. The Campaign settles unclear rules with a coin and a
thumb-on-the-scale for the enemy.
**Resolution:** these are answering different questions. Determinism governs
*resolution*; the coin governs *adjudication*. They are compatible and both should be
kept. The corpus has never noticed they are not in conflict.

### 11.3 "Position is the primary modifier" vs the arithmetic — **GENUINE, and the most consequential in the report**
| Line | Maximum positional payoff |
|---|---|
| Corebook | **×3.1** (Edge ≈ +5 Skill, plus a critical, plus no return blow) |
| Table Companion | **×2.64**, unanswered, blind to the defence number |
| Second Corpus | binary counter-denial; no arc dice at all |
| **Vault** | **+5% to +47%**; +7.2 percentage points of kill chance for walking behind an enemy; **+5% for a spear** |
**The law is loudest exactly where it is least true.** Evidence favours Line 1's
magnitudes. The Vault's own Design Law 8 is arithmetically falsified by its own
packets.

### 11.4 "The table is the memory" vs the designer's own content — **GENUINE, narrow, fixable**
`FORM UP` leaves participants "Unactivated with 1 AP" — carried, invisible, per-figure,
for the rest of the round — in the same artifact that says AP refreshes on activation
and is the only thing held in memory. The Table Companion solved this exact problem and
gave it a dedicated token: *"Winded is its own token, never a face."*

### 11.5 Accessibility vs the component ecosystem — **GENUINE**
*"Any miniatures you own or can borrow; coins do fine"* against dual-diameter magnet
wells booleaned into printed bases, keyed frames, and QR codes on every base.
**Evidence favours accessibility**, by W4: it is stated in the line that shipped.

### 11.6 "Play is analog / no screen at the table" vs both lines' behaviour — **GENUINE**
The signed law forbids screens; the Table Companion *is* a web app with a search box
and a theme toggle, and the campaign layer is declared to *require* a companion
application.
**Resolution available and already latent in the corpus:** the app belongs to downtime,
never between two players in a fight. Say so once and the contradiction dissolves.

### 11.7 The refusal to define, vs the refusal to build — **GENUINE, and the most delicate**
Three tiers, which behave differently and must not be conflated:
- **Argued and disciplined** — `Redemption`, `hollow`'s trigger. The designer deleted
  his own working causal chain and even his own protective clause, because *"a line
  that guards the door also nods at the door."* That is real discipline, and it earns
  its blank because forty lines of specification stand beside it.
- **Asserted and self-sealing** — `SOUL`. See §5 D3.
- **Merely scheduled** — the membrane, the Child marker, `The Sword & the Light`. Given
  the strongest ownership language in the Campaign architecture and never written.
**The grammatical tell:** tier one says *"write no procedure"* — an instruction. Tier
three says *"remains its home"* — a filing decision.

---

# 12 · FALSE CONSTRAINTS

Assumptions that look like laws and are not. Challenging these is the point of the
exercise.

**FC1 — "Nothing migrates merely because it existed."**
*The single most expensive assumption in the corpus.* It is intellectually admirable
and it is the machine that guarantees each rebuild costs more and yields less. Measured:
the First Corpus produced 125 profiles and a working build in six days; the Second
Corpus produced zero content in 2.4 days and retains 5.5% of its own history; the Vault
produced zero figures in one afternoon. **The one period that produced a finished game
scoped itself as "assembly, not design" and copied forward.**
*Replace with:* nothing migrates merely because it existed — **but nothing is rebuilt
merely because it is old.** Migration is the default for anything that has been played;
re-derivation must be justified, not assumed.

**FC2 — "The vocabulary must be correct before content can exist."**
Five vocabularies, zero figures. Content is what generates the pressure that makes a
vocabulary correct. Reverse the order once and see.

**FC3 — "Persistence requires the companion application."**
Declared *"a deliberate architectural commitment, not a fallback."* Yet the only
persistence mechanic that has survived every rebuild is one d6 and one written sentence
— *"1–3 takes a narrative Scar (one sentence, no numbers)"*. The three-page PERSIST
stub has been outstanding for five weeks. **The feasible campaign layer is three pages
and has never been attempted.**

**FC4 — "This must carry politics, trade, logistics and exploration as peers."**
The CUS Constitution requires it. In five weeks, Combat is the only module ever
discharged; Story was drafted, never signed, and deleted. Two modules became one in
practice. The kernel does not need to be universal to be good.

**FC5 — "Multi-setting from the start."**
Two independent attempts have produced two elegant cross-setting abstractions and zero
cross-setting content — and the abstraction is now *causing* the content gap, because
setting-neutral packets have no figure to sit on.

**FC6 — "`SOUL` must be a formal reserved primitive."**
The intent is real and should be kept forever. The mechanism — a blank node in the
dependency graph, a tripwire, an appendix, a glossary entry, custodial protection in a
second repository — protected against a threat that never occurred and was silent
against the one that did: it simply vanished in the next restart, without a ruling.
**A principle in the constitution does this work. A primitive does not.**

**FC7 — "The enemy brain needs its own symbol grammar."**
The commitment to a refereeless enemy is genuine and should never be dropped. But the
Corebook did the same job in plain English — *"read its card top to bottom and do the
first line that's true, in its meanest legal form"* — and the 30-glyph replacement
introduced four position-dependent symbol collisions, which the corpus's own poka-yoke
doctrine forbids. The three load-bearing rules are the queue, the fall-through ladder
and the downgrade rule. The other 27 tokens are notation.

**FC8 — "An exception is a named field, never prose."**
A genuinely good law that licensed a field explosion. The Vault ships nine undefined
tags in thirty uses, six undefined effects, and a locked Effect Lexicon whose five core
verbs appear in zero packets. *Add the missing half:* a field that nothing reads is not
an exception — it is a note.

**FC9 — "Integrity is validation."**
179 SHA-256 hashes, a lock statement, an immutability regime, and a `PASS` report that
checks whether files exist. Ten lines of Python over the packet frontmatter would have
caught the dominated weapon, the null Grade, the undefined effects and the
non-monotonic baseline in one pass. **The corpus lints its words and not its numbers.**

**FC10 — "Each artifact must be internally perfect before the next begins."**
The Table Companion disproves this in the corpus's own hand: it shipped a complete,
playable game with **morale switched off and its hooks left printed**. You may defer a
subsystem without rebuilding the world.

---

# 13 · DESIGN CONSTITUTION

> ## THE CAMPAIGN — DESIGN CONSTITUTION
> *One page. The permanent north star. Everything else is implementation.*
>
> ### Mission
> A miniatures game that a family can play tonight on a coffee table, in about an
> hour, with figures they already own and no referee — and that remembers what
> happened.
>
> ### Player Promise
> You take people out, you bring some of them back changed, and what happened to them
> was partly your fault. Nothing here scores a kill. The animals always come home.
>
> ### Core Fantasy
> Stewardship on a green road, and the cost of it.
>
> ### Core Loop
> **Read the board → commit → live with where you are standing → write one line about
> it → carry it to the next fight.**
>
> ### Design Values
> 1. The table is the memory.
> 2. Committing forecloses something.
> 3. The battlefield decides, not the character sheet.
> 4. Judged by eye, settled in seconds.
> 5. Say what a thing *is*, never what it is *for*.
> 6. Depth comes from the board, never from a table of combinations.
>
> ### Non-Negotiable Principles
> - **Two judges rule every fight: the youngest player at the table, and the clock.**
>   Any rule too slow or too confusing for either is wrong, and is simplified on the spot.
> - **Nobody at the table is the referee.** The enemy runs itself off a printed card.
> - **No number is ever added to a die at the table.**
> - **Down is not dead. Dead is permanent.**
> - **A rule you cannot see on the table is not a rule.**
> - **The system never claims to have modelled the whole of a person.**
>
> ### Acceptable Tradeoffs
> - Precision, wherever it costs time. Honest judgment and a coin beat measurement.
> - Simulation fidelity, wherever it costs a decision.
> - Universality. This is a skirmish game that remembers, not a grammar for all
>   organised action.
> - Internal perfection. A subsystem may ship switched off with its hooks printed.
>
> ### Explicit Non-Goals
> - Cross-faction points balance. Asymmetry is content; the scenario balances the match.
> - A referee, an AI director, or any second scripted mind.
> - Bespoke components as a requirement to play.
> - A rules corpus that is correct before it is played.
> - Cross-setting content before one setting is finished.
> - Any procedure for redemption, or for what a person is worth.

---

# 14 · OPEN QUESTIONS

Ranked by importance. **Not answered here, by instruction — and several cannot be
answered from the corpus at all.**

1. **What happened between 14 and 23 July?** Nine days separate the last Campaign
   artifact from the first CUS one. It is the moment the project changed direction and
   nothing in 1.5M characters covers it.
2. **Has any version of this ever been played by a human?** Seven teams found no
   record. If notes exist outside the corpus, this report's central finding weakens
   substantially and the Director should be told.
3. **Which line is the product?** The corpus never says. Every recommendation in this
   report depends on the answer.
4. **Is the Vault a decision or a context loss?** It cites nothing prior and re-locks a
   claim a machine-enforced graveyard forbids. A deliberate reversal is a decision; a
   fresh session without the previous artifact in view is a process defect with a cheap fix.
5. **Do the named Campaign artifacts exist?** `Final_campaign.pdf`, the Resolved
   Statlines, the 14-deck Build Plan, Battle Doctrine v1.3, and Module 0 are all listed
   as canon and none is in the corpus. If Module 0 and the Deck Plan are real, the
   finished-output inventory is significantly understated.
6. **Was Mill Road ever run, solo, twice, with a timer?** The corpus specifies the
   experiment precisely and records no result.
7. **What is in `The Sword & the Light`?** The declared home of the entire moral
   economy, granted cross-cutting authority above every other document, and absent.
8. **Is `Winded` survivable at the table?** The one place the corpus explicitly asked
   the table a question — and parked a hero ability pending the answer.
9. **Does counter-charging break the "denial is the strongest defence" thesis?** The
   one untested defensive option, on a working and reproducible harness.
10. **Was `reaction-struck`'s cost ever paid?** The measured report flagged shield and
    counter behaviour for re-testing; the re-test was never run, and the simulator was
    deleted three days later.
11. **Where did the enemy-card engine go?** The most finished subsystem in the corpus
    was dropped by both CUS lines with no rejection note, in a project that maintains a
    52,000-word register of rejected ideas.
12. **What is the Child marker, concretely?** An age gate, a content warning, or an
    in-fiction protection rule? A Mind Scar named `never_again` triggers on *"a child —
    or a thing wearing a child"*, which implies children may be board pieces.
13. **Why does the continuity checker lint words and not numbers?** The harness exists,
    works, and is pointed at vocabulary while the packets go unaudited.
14. **Is there a losing condition?** *"There is advancement and harm here, and still no
    way to lose the whole thing."* Unaddressed in every rebuild since.
15. **Who is Courtney, and does she play?** The only second human in the corpus. If she
    plays, the gap may be a recording gap rather than a play gap — which changes the
    prescription from "play it" to "write it down."

---

*Section 15 — Creative Phase Handoff — is filed separately as
`01_CREATIVE_PHASE_HANDOFF.md`, because Phase 12 requires it to be self-contained for a
team that has not seen any source material.*

*Section 16 — Appendix of Supporting Evidence — is filed as `02_APPENDIX_EVIDENCE.md`.*
