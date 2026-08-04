# APPENDIX OF SUPPORTING EVIDENCE

Companion to `00_DISCOVERY_REPORT.md`. Every major conclusion in that report should be
traceable to a row here. Where a claim rests on evidence not present in this corpus,
that is stated rather than smoothed over.

---

## A · THE CORPUS EXAMINED

| Artifact | Location | Date evidence |
|---|---|---|
| The Campaign — `00_MANIFEST` | uploaded PDF | 2026-07-01, "rules at v2.5 (partial)" |
| The Campaign — Playtest Doc Architecture v1.1 | uploaded PDF | 2026-07-01, supersedes v1.0 |
| The Campaign — Core Rulebook (print), 1st Ed. | uploaded HTML | after 07-01 (the Architecture lists CORE as PENDING); still prints Parry, which was cut 07-14 |
| The Campaign — Table Companion 2 | uploaded HTML, 559,771 B | Doctrine v1.4 (v1.3 was canon on 07-01); records "Parry was CUT (07-14)" |
| `cus-rules` | GitHub, 1 commit | 2026-07-23, "How to Play v1.3", rules source "CODEX v0.5" |
| `CuscoSauce` | GitHub, 1 commit | 2026-07-23 — a LICENSE file, nothing else, ever |
| First Corpus `cus-kernel-rebuild` | GitHub, 75 commits, archived | 2026-07-23 → 07-28 |
| `cus-concordance` | GitHub, 89 commits | → 2026-07-29 |
| Second Corpus `cus-second-corpus` | GitHub, 55 commits | 2026-07-25 → 07-30 (rebuild proper from 07-28) |
| `CUS_Rulebook_Vault v0.5` | uploaded zip, 165 md files | **2026-08-03, zip timestamps 07:10 → 14:51** |

**Authorship.** 117 of 130 CUS-line commits carry `Co-Authored-By: Claude Opus 4.8` or
`Claude Opus 5 (1M context)`. Human identities across all four repos — `William`,
`whbreifcase-arch`, `mitchdevano` — resolve to a single email address. There are no
co-authors, no reviewers, and no issue reporters.

---

## B · THE LOAD-BEARING QUOTATIONS

### B1 — The design's thesis, in the designer's own words
> *"They are **one idea found six times**. Every one of them says: **you get one
> commitment, and committing forecloses something.** Face one enemy and concede the
> other three arcs. One clean run, or the charge fumbles on the chaff… **Treat this as
> the design's thesis and use it as a test.** Does this proposal create a commitment
> with a real foreclosure — or is it just a modifier? If it is just a modifier, it
> probably does not belong."*
> — `G_WHY_NOT.md`, `the-commitment-economy`

Its Line-1 counterpart, in player-facing prose:
> *"**Attack is always last.** You cannot strike and then reposition — committing is
> the cost, and it makes where you end the round standing matter more than the damage
> you dealt."* — Core Rulebook §6

### B2 — The diagnosis the designer wrote and did not take
> *"4. **Run Mill Road solo, twice, with a timer** — once Rabble, once Cunning. Same
> cards, both rooms. 5. **Then the family.** Everything after is playtest data, not
> specification. **The clock is one of the two judges, and it does not exist on
> paper.**"* — Playtest Doc Architecture v1.1 §5, 2026-07-01

### B3 — The two judges (W4: stated four times across two lines)
> *"**Two judges rule every fight: the youngest player at the table, and the clock.**
> Any rule too slow or too confusing for either of them is wrong — **simplify it on the
> spot.** … For unclear facts on the table — 'is that a flank?' — **flip a coin. No
> argument survives longer than that.**"* — Core Rulebook, "The table laws"

### B4 — The memory budget (nine independent derivations)
> *"**The state of the fight lives on the table, not in anyone's head.**"* — Core Rulebook §17
> *"**READ TEST.** Does an opponent need to read this when it is NOT my activation?
> yes → hardware on the model. **no → it lives in your head.**"* — `J_COMPONENTS.md`, SIGNED 2026-07-27
> *"State and geometry live on the **base**, read directly off the table. The base is
> the instrument."* — `slice-1/04_COMBAT.md`
> *"**AP is the only ordinary short-term value held in memory.**"* — Vault, `01 CONSTITUTION/Design Laws.md`, Law 4

### B5 — No referee (W4: five independent constructions)
> *"There is **no referee in this game. The storyteller is a player: a card reader with
> a tape measure.** Every enemy carries its own card, and the card decides."* — Core Rulebook, Part Three
> *"**Who puppets the enemies? Both of you, and the trees decide — no GM.**"* — Table Companion, Scenario G2
> *"**AI generates · Doctrine is printed · players execute.** … **The enemy never gets
> smarter; the room does.**"* — Table Companion, Doctrine v1.4

### B6 — The emotional core (W4: survives two engine replacements)
> *"**Down is not dead.** Who lives is the story's business, after the fight."* — Core Rulebook §4
> *"Roll a **d6 for every Downed figure: 4–6, back on their feet. 1–3, a scar — write
> one line about it.** **The animals always come home.**"* — Core Rulebook §22
> *"**There are no points in this game.** Your roster is limited by bread… and grown by
> story: **spare someone, feed him, and he stays.**"* — Core Rulebook §8
> *"When bed-cases outnumber bed slots, the Caravan **cannot carry everyone** — a
> **forced choice**… **This is where persistence stops being bookkeeping and becomes a
> decision with a body count.**"* — `slice-3/02_THE_CARAVAN.md`
> *"**A figure is a history of its Scars.**"* — `slice-3/01_HARM_LIFECYCLE.md`
> *"**He is not a villain. He is a man nobody sat with.**"* — `H_PERSISTENCE.md`, on `hollow`

### B7 — The refusals
> *"The moment there is a procedure, there is a **checklist**, and **the most important
> thing one person can do for another becomes a line item you tick** on the way to a
> stat correction… **This is the one place where the correct rules text is an absence**
> — and if a group works something out at their own table, what they worked out is
> theirs."* — `G_WHY_NOT.md`, `there-is-no-redemption-rule`

Commit `a3985f5`, on removing even the protective clause: *"a line that guards the door
also nods at the door."*

### B8 — The Vault's one genuine contribution
> *"**CAPABILITY IS PUBLIC. INTENT MAY BE UNCERTAIN.**"*
> *"**SILHOUETTE PREDICTS THE THREAT. POSITION SHOWS THE FORMATION. THE FACE-UP PACKET
> CONFIRMS THE RULE. THE GRADE DETERMINES THE RESULT.**"*
> — `01 CONSTITUTION/Readable Threats and Formations.md`, status `locked`

---

## C · THE MEASURED EVIDENCE (W5), AND ITS LIMITS

### C1 — The charge study reproduces
648 configurations × 2,000 seeds = **1,296,000 games**. All six ranked findings were
independently reproduced from `study_results.json` and by re-running `holdtest.py`:

| Finding | Reproduction |
|---|---|
| "Run-up is king… ~81% hold" | deny-runup: hold **81%**, breakthrough 9%, halt 100% |
| "Depth punishes… roughly doubles" | charger losses 0.169 → 0.536 → 0.845; reach-strikes 0.91 → 2.55 → 3.77 |
| "Spears are defensive only" | as defender **1.231** charger-kills/game vs sword 0.147 (**8.4×**); as charger **0.467**, worst of three |
| "Shape by intent" | column breakthrough 83.7% (max); wedge kills 1.321 + flank/rear 3.019 (max); line lowest on both |
| "Angle" | flank losses 0.389 vs front 0.644; flank/rear hits 3.057 vs 1.362 |

### C2 — What the study could not have measured
- **`crush` fired zero times in all 1,296,000 games.** The terminal state of the
  push→indent→crush cascade requires a wall; the study harness never built one. The
  capstone lists that cascade among the rules the sim validated.
- **The study's "breakthrough" metric is unreliable** — at runup 2.0 with a line
  formation it reads 59.5% while halt reads 99.8%, because wing figures walking around
  an unbounded flank count as a breakthrough. `holdtest.py`'s 9% is the sound figure.
- **The two empirical documents ran under different reaction economies** — the charge
  study under "1 reaction/figure", the balance run under uncapped counters. Current
  canon matches only one of them.
- **The capstone carries its own retraction:** *"⚠ Superseded in part, 2026-07-27 — the
  Reaction economy is struck… the shield and counter behaviour it measured… is exactly
  the behaviour flagged for re-testing."* The re-test was never run; the simulator was
  deleted three days later.
- **"Lance/impact is the terror piece"** is ranked fourth among measured findings, and
  the same document concedes *"the lancer wins on its stat line alone."* That is a
  pricing observation, not a mechanic finding.

### C3 — The balance report's method (worth preserving even though its conclusions are not)
3,000-game round-robin; **seats swapped every game**; three rotating terrain sets; an
auditable pricing model; a documented tuning journey 60.0% → 56.0% → 55.8% → 56.5%; a
convergence check at two sample sizes (*"56.5% at 3000, 56.6% at 4000 — the estimate is
tight"*). Better than most published wargame balance work.

### C4 — Analytic evidence (W4½), verified
All six of the Table Companion's per-hero "defence math" lines check out exactly:
Knight (3+1 shrug) ÷ (2 × ⅓) = **6.0**; Rogue 2 ÷ (2 × ⅙) = **6.0**, and 2 ÷ (3 × ⅙) =
**4.0** against a gang; Berserker 3 ÷ (2 × ⅔) = **2.25**; Ranger/Mage/Muse 2 ÷ 1.0 =
**2.0**; Great Bear 3 × ½ × Deadly(2) = **3.0**.

The Parry cut is the one content deletion in the corpus justified by a computed number:
three green d6 blocking on 5+ negates 1 − (4/6)³ = **70.4%** of incoming hits, with
P(≥2) = **25.9%** riposte. *"6+ plus a save out-walled the Knight."*

---

## D · THE ARITHMETIC THAT FALSIFIES A CONSTITUTIONAL LAW

Every line asserts that position is the primary modifier. Computed payoffs:

| Line | Mechanism | Payoff |
|---|---|---|
| Core Rulebook | Edge = 2d20 keep best/worst | ≈ **+4.2 to +5.0 Skill**, against an authored Skill range of 3 pips. Backstab total ≈ **×3.1** (damage ×2.02, plus no return blow) |
| Table Companion | Edge = ±1 die | good spot **×1.33–×2.00**, DEF-independent. Backstab **×2.64** and unanswered, blind to the defence number |
| Second Corpus | no arc dice at all | binary: the flank denies the Counter |
| **Vault** | flank +1 die, rear +2 dice | **+5% to +47%**, mostly +8–20%. Spear **+5%**. Walking behind an enemy buys **+7.2 percentage points** of kill chance |

**Cause of the Vault's collapse.** Four individually reasonable decisions multiply:
flat small-integer damage; a Grade ladder that stops at 3; a 2-Heart standard figure; a
2-AP Square with a 1-AP attack. Two Sword Cuts kill a standard figure **91.8% of the
time from the front**. There is nothing left for position to buy.

**Corroborating defects found by two teams independently:**

| Defect | Detail |
|---|---|
| Top-Grade probability spread | 3 dice at 5+ → **3.7%**; 6 dice at 4+ → **65.6%**. An 18× spread across one Arsenal, undocumented, all `untested` |
| Null band | `Bow — Quick Shot` Grade 1 and Grade 2 are identical |
| Dominated weapon | `Great Weapon — Cleave`: 2 AP for E=1.78 Hearts *and* it prints REACT at every band; two Sword Cuts are 2 AP for E=2.50 with no REACT. Dominated ~**2.4×** |
| Non-monotonic band | `Sword — Cut` Grade 2 = 1 Heart + Push; Grade 3 = 2 Hearts. Against a target on its last Heart, **rolling better is worse.** Same bug in the Second Corpus's own example packet |
| Bad spot is a no-op | "never below one die" + a roster where every non-boss unit is ATK 1 ⇒ cover, Grease, Blinded, Prone and Brace do **nothing** against ~85% of the printed models |

The designer predicted the monotonicity bug himself and prescribed the fix:
> *"Because higher Grades do not inherit, a designer can accidentally write a Grade 3
> that is worse than Grade 2. That is an authoring bug, not a rules question — **lint
> for it.**"* — `G_WHY_NOT.md`, `grade-is-not-a-tier`

The lint was never written.

---

## E · THE NEGATIVE EVIDENCE

Several of this report's central findings rest on exhaustive searches returning nothing.

| Search | Result |
|---|---|
| Any record of a game being played — `we played`, `at my table`, `session log`, `first playtest`, post-fight notes | **Three hits, all false positives.** No commit message in any repo describes a game being played |
| Vault `06 PLAYTESTS/Sessions|Issues|Proposed Changes` | Three folders containing one README each. Both dashboard queries return nothing |
| Vault `balance_status:` | **50 of 50 read `untested`** |
| Vault figures / warbands / scenarios, both settings | Six folders, six 3-line READMEs, zero content |
| Second Corpus playable content | Zero figures, zero packets, zero factions, zero scenarios |
| Vault references to any prior artifact (`Corpus`, `Concordance`, `CON-00`, `slice`) | **Zero across 165 files** |
| `Nerve`, `Strain`, `Agency`, `Caravan`, `Shove`, `Knocked Out`, `SOUL` in the Vault | **Zero occurrences each** |
| `counter-attack`, `strike back`, `riposte`, `retaliat` in the Vault | **Zero** — automatic melee retaliation, the Corebook's stated thesis, does not exist in the newest artifact |
| `Temperament` values, `Route Packet` content in the Vault | The locked Morale rule invokes both; **neither exists** |
| `PURSUE` (a locked Threat Word) in Vault content | **Zero implementing packets** |
| Cross-citation between the two lines, either direction | **Zero** |
| Vault packets obeying the locked Packet Schema | **0 of 39** |
| Locked Effect Lexicon's five core verbs in content | **Zero uses**; 74 distinct effect strings in play instead; 9 undefined tags in 30 uses |

---

## F · THE FORENSIC FINDINGS

### F1 — The Vault was built in 7 hours 41 minutes
Zip-internal timestamps, four batches on one day: `07:10:16` (47 entries), `13:21:40`
(19), `14:41:52` (35), `14:51:54` (125). All 165 markdown files carry a 2026-08-03
mtime. `Change Log.md` records **three releases on that date** — Kernel v0.1.0, build
v0.4.0, Kernel v0.2.0 / build v0.5.0. The `99 ARCHIVE/Superseded Packets/v0.4 Arsenal/`
folder preserves versions that were hours old.

### F2 — `e140a09` deleted 160 files and 50,240 lines
Every simulator, the entire Tabletop Simulator build, all nine faction datasets, every
playable HTML page, and all fourteen A–N law documents. Commit message: *"No rebuild
content lost; the vertical-slice-* branches are kept as a safety net."* The Second
Corpus tree now retains **5.5%** of its own repository's line history (3,181 surviving
against 57,755 inserted).

### F3 — The onboarding suite lived three hours
2026-07-25: `12:25` a playable guided tutorial (821 lines, *"verified by 300 headless
playthroughs… 300/300 reached the end card"*); `15:38` a print-and-play field guide and
a **36-card deck**; `15:45` — *"Revert this session's web work; wrong target"*, −5,047
lines across 13 files. The print kit lived **seven minutes**. The revert message itself
names `rules.js` as *"the only machine-readable v0.6 ruleset"* and prints the recovery
command. It was never recovered.

### F4 — The AI Director lived 21 hours
Built 2026-07-25 01:04 with a measured result (*"beats the greedy AI 52–87%, games
staying 5–9 rounds"*); killed 22:08 — *"kill the AI Director — stale, nothing
salvaged."* Later argued against retroactively in the rationale register.

### F5 — The continuity checker is blind to the claim it was written to catch
`slice-1/05_WALKTHROUGH.md` still asserts *"the Circle… breaks on its own meter"* and
cites Ruling 10 — the very ruling that reversed it. The forbidden-claim row exists and
its regex requires the literal string `own break meter`; the prose says `on its own
meter`. Running the tool:

```
$ python3 _model/check.py
canon check: clean — 39 live terms, 10 retired terms, 18 canonical + 15 forbidden
relations; links, terms, claims OK across 31 docs; GLOSSARY.md in sync.
EXIT=0
```

### F6 — The Vault re-locks a machine-forbidden claim
`03 GRAMMAR/Archetype Grammar.md`, status `locked`: `FRAME = ARCHETYPE + STYLE`. The
Second Corpus's graveyard, four days earlier, ratified as CON-0023: *"Frame does not
contain Archetypes; FrameSpec is a socket schema."* The Vault also demotes Tempo into
`Style` — re-committing precisely the "hidden-Tempo leak" the Second Corpus wrote a
section to diagnose and fix.

### F7 — Two law-numbering schemes coexist in one repository
Eight citations to "Law 15", "Law 10" and "Law 4" point at a fifteen-law list in a
document `e140a09` deleted, while the repository's own list has five laws — in which
Law 4 names something different. One citation hyperlinks "Law 15" to a file whose list
stops at 5.

### F8 — The one control that is exactly as good as it claims
All **179 SHA-256 hashes in the BUILD MANIFEST verify: 179 match, 0 mismatches, 0
missing.** The criticism is not that it is dishonest — it is that integrity is not
conformance, the vault is not under version control, and the manifest hashes the
editor's colour scheme.

---

## G · THE RATIOS

| Measure | Value |
|---|---|
| Concordance governance : text governed | **2.31 : 1** (128,904 words vs 55,742), of which 102,563 words are inventories cited zero times since |
| Second Corpus playable content | **zero**, against 23,915 words of architecture |
| Vault teaching output : specification | **~7% by size, 3.6% by file count** — and the Quickstart is an 11-line table of contents |
| Teaching-to-specifying ratio over time | Campaign **~40%+** → First Corpus **~16%** → Second Corpus **0%** → Vault **~7%** |
| Vault stub ratio | 65 of 165 files are ≤25 lines; 16 are exactly 3 lines |
| Rules changes triggered by internal inconsistency or document review | **~2 in 3** |
| Rules changes triggered by measured output | **4, all from one weekend**, all targeting an engine since superseded twice |
| Rules changes triggered by observed table play | **0** |
| Playable warbands produced per rebuild | Core Rulebook 1 → Table Companion 5+2 → First Corpus 7 (as data) → Second Corpus **0** → Vault **0** |

---

## H · WHAT THIS INVESTIGATION COULD NOT ESTABLISH

Stated plainly, because a report that hides its limits is worth less than one that
does not.

1. **Whether the game has been played.** Seven teams found no record. Absence of a
   record is not proof of absence of play. If sessions happened and were not written
   down, the central finding of this report weakens from "never tested" to "never
   recorded" — which is a different problem with a much cheaper fix.
2. **Whether several named Campaign artifacts exist.** `Final_campaign.pdf`, the
   Resolved Statlines, the 14-deck Build Plan, Battle Doctrine v1.3, and a built
   Module 0 are all listed as canon and none is in the corpus. If Module 0 and the Deck
   Plan are real and complete, the finished-output inventory here is materially understated.
3. **Whether the Vault's omissions are a decision or a context loss.** These have
   opposite implications and no document distinguishes them.
4. **Anything about how the game feels.** Every W5 datum in the corpus concerns
   tactics. None concerns pace, clarity, tension, or whether a table enjoys it.
5. **What happened between 14 and 23 July.**
6. **How much effort has actually been spent.** Commit volume is a poor proxy in an
   AI-assisted corpus. The allocation estimate (roughly half to architecture and
   governance, a fifth each to tooling and content, and a small remainder to empirical
   work) is a considered judgment, not a measurement.

---

## I · THE FINDING THIS REPORT WOULD MOST LIKE TO BE WRONG ABOUT

That the game has never been played.

It rests entirely on negative evidence. It is the load-bearing fact under most of the
report's recommendations. And it is the single easiest thing in the world to overturn:
one file, in a folder that has been empty in every incarnation of this project.
