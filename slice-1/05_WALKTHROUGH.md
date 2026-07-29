# Slice 1 · Walkthrough — a melee exchange, played out

The testable artifact. Two Squares fight to a decision using **only** what Slice 1 defines. Every
line cites the rule it exercises; every State change is shown on the Instance. Dice are illustrative
(one concrete roll of many) — the point is that the loop **closes** with no rule left undefined.

## The two figures

Both use the `spearman` Definition from [04_COMBAT.md](04_COMBAT.md):
`shape square · agency 2 · wounds 2 · armour M (save 5+) · packet spear_thrust`.

`spear_thrust` = **5 dice, success 4+**, grades: `1:Push · 2:1 Wound · 3:1 Wound + Guard · 4:2 Wounds`.

| Instance (start) | Position | wounds_remaining | Guard | AP |
|---|---|---|---|---|
| **A** (attacker) | 6″ from B, facing B | 2 | — | 2 / 2 |
| **B** (defender) | holding, facing A | 2 | — | 2 / 2 |

---

## Turn 1 — A activates (2 AP)

**① `MOVE` (1 AP)** — A sprints into base contact with B, front-to-front.
- *Writes Position* (Law: only MOVE writes Position). Same-size bodies meeting on contact → A **stops on contact**, no Push (not a charge). B is now **engaged** to A's face.

**② `ACTION` → `spear_thrust` vs B (1 AP)**
- Constraint check: `not_in_contact:false` → A is in contact ✓. Target is to A's face ✓.
- **Roll 5 dice (4+):** `6 · 5 · 4 · 2 · 1` → **3 Successes → Grade 3 → "1 Wound + Guard".**
- **B resolves Armour** (M = 5+): 1 save die per incoming Wound → `3` → **fails.** 1 unsaved Wound steps B's Body track.
- **A gains Guard.**
- **`provokes:true`** → B was struck, in contact, to its **face**, and is **Standing** → B **may Counter.**

**↳ Counter (Written Trigger, free)** — B returns one `spear_thrust` vs A.
- A has **Guard** → strike against A's face rolls **−1 die → 4 dice.**
- **Roll 4 dice (4+):** `5 · 4 · 2 · 1` → **2 Successes → Grade 2 → "1 Wound".**
- **A resolves Armour** (M = 5+): 1 die → `6` → **saves.** 0 Wounds to A.
- **A Counter does not draw a Counter** → the exchange terminates.

A has spent 2/2 AP. Turn ends.

| Instance (after Turn 1) | wounds_remaining | Guard | AP |
|---|---|---|---|
| **A** | 2 | ✅ (until A's next activation) | 0 / 2 |
| **B** | **1** | — | 2 / 2 |

*What just closed the loop:* perceive Position → choose intent → spend Agency → invoke PACKET →
world constrains (contact, facing) → Procedure resolves (roll → Grade → Effect) → State changes
(B −1 Wound, A +Guard) → the free Counter (a second, budget-less invocation) resolved and
terminated. Nothing referenced a rule outside Slice 1.

---

## Turn 2 — B activates (2 AP)

B is already engaged, so it spends both AP attacking.

**① `ACTION` → `spear_thrust` vs A (1 AP)**
- A still has **Guard** → B's strike rolls **−1 die → 4 dice.**
- **Roll 4 dice (4+):** `6 · 5 · 4 · 3` → **3 Successes → Grade 3 → "1 Wound + Guard".**
- **A resolves Armour:** 1 die → `2` → **fails.** A: 2 → **1**.
- **B gains Guard.** A is Standing, in contact, struck to face → **A may Counter.**

**↳ Counter (free)** — A returns `spear_thrust` vs B. (B just gained Guard → A's Counter rolls −1 die → 4 dice.)
- **Roll 4 dice (4+):** `4 · 4 · 2 · 1` → **2 Successes → Grade 2 → "1 Wound".**
- **B resolves Armour:** 1 die → `4` → **fails** (needs 5+). B: 1 → **0** → **Knocked Out.**
- Counter draws no Counter → exchange terminates.

**② B's second AP** — B is **Knocked Out**; it does not act. (Its activation ends with 1 AP unspent.)

| Instance (after Turn 2) | wounds_remaining | State | Guard | AP |
|---|---|---|---|---|
| **A** | 1 | Standing | — (expired on activation) | — |
| **B** | 0 | **Knocked Out** | — | — |

**Result:** B is down — felled by A's **free Counter**, not by A's own action. A survives on 1 Wound.
The fight was decided by *position and authoring* (B provoked a Counter it couldn't afford), exactly
as the architecture predicts: out-of-turn answers, capped by Position and death, carry the exchange.

---

## Variant — the flank erases the Counter

Rewind to Turn 1 ②, but A strikes B from the **flank** (A maneuvered around, or B was already
engaged elsewhere):

- Same Grade 3 → B takes its Wound…
- …but **B cannot Counter** — a Square answers its **face** and concedes its **flanks** (Position is the cap, not a budget). No die is spent to "deny" the Counter; the geometry simply doesn't permit it.

This is the whole thesis of the Kernel in one move: **a decision made through Position instead of a
number.**

---

## Coverage check — did the slice close?

| Loop step | Exercised by | Rule source |
|---|---|---|
| perceive Position | contact / facing / flank | 04_COMBAT · Base |
| choose intent | MOVE then ACTION | 03_GRAMMAR · verbs |
| spend Agency | 2 AP, one per verb | 01_PRIMITIVES · Agency (Ruling 2) |
| invoke Capability | `spear_thrust` via ACTION; Counter via Written Trigger | 03_GRAMMAR · invocations |
| world constrains | `not_in_contact`, `provokes`, facing | 03/04 · named fields (Law 15) |
| Procedure resolves | roll → Successes → Grade → Effect | 03_GRAMMAR · resolution |
| Save | Armour, 1 die per Wound | 03_GRAMMAR · Save |
| State changes | Wounds, Guard, Knocked Out | 01/04 · Body channel |
| out-of-turn | the free Counter, capped by Position/death | 04_COMBAT · Counter |

**No undefined rule was reached.** Nerve/Morale, the Circle, formation movement, and persistence
were never needed — confirming they belong to Slice 2, not Slice 1.

## Open at the seam (for Slice 2)
- What happens to a Knocked-Out figure *after* the battle → Persistence (Wounds → Injury → Scar).
- The Mind channel: Morale damage, the Nerve save, the **Morale check** recovery roll. *[Ruling 11]*
- The **Circle** (3 AP, faceless, breaks on its own meter) and why it does **not** move in formation. *[Rulings 10, 13]*
