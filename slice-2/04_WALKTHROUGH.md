# Slice 2 · Walkthrough — a group breaks, and is held

The testable artifact. A Square unit under a Circle leader takes casualties, wavers, and one figure
Routs — until the leader Rallies it. Slice 1 melee is compressed to its results; the dice shown are
the **new** Slice 2 rolls (Nerve saves, Morale steps, Rally). Illustrative rolls; the point is the
loop **closes**.

## The board

**Player** — a Formation of three Squares **S1 · S2 · S3** (each `wounds 2 · armour M(5+) · nerve M(5+)`),
in coherency, with a **Circle leader C** (`3 AP · faceless · immune to Morale · leadership 3″`) fighting
beside them (never *in* the Formation — [02_THE_CIRCLE.md](02_THE_CIRCLE.md)).

**Enemy** — two Squares **E1 · E2** (`wounds 2 · armour M`).

| Instance (start) | Mind | Body | in Formation? |
|---|---|---|---|
| **S1 · S2 · S3** | Steady | 2 | yes (coherent) |
| **C** (Circle) | — *(no Mind channel)* | 2 | never |

---

## Round 1

### Enemy activates
- **E1 fells S1.** Two strikes, Slice 1 melee procedure → **S1 Knocked Out.**
- **⚡ Shock (Written Trigger).** S1's KO deals **1 Morale** to every friendly within 3″. Roll one Nerve die each (M = 5+):
  - **S2** → `3` → **fails** → Steady → **Shaken**.
  - **S3** → `6` → **saves** → stays **Steady**.
  - **C** → **immune** — a Circle has no Nerve and takes no shock. Unmoved.
- **E2 strikes S2** → Grade 2 → 1 Wound. S2's Armour → `4` → fails → **S2: 2 → 1**.
  *(Note: S2 is Shaken, but Shaken only penalises a figure's **own** ACTIONs — its Armour save is unaffected.)*

### Player activates
- **S2 (Shaken) strikes E1** — demonstrating the penalty: its `spear_thrust` rolls **−1 die → 4 dice**: `5 · 4 · 2 · 1` → 2 Successes → Grade 2 → 1 Wound on E1. The rattled soldier still fights, just worse.
- **C and S3** press E1 (compressed). The line holds — for now.

| after R1 | Mind | Body |
|---|---|---|
| S1 | — | **Knocked Out** |
| S2 | **Shaken** | 1 |
| S3 | Steady | 2 |
| C | — | 2 |

---

## Round 2 — the break

### Enemy activates
- **E2 fells S3.** Slice 1 melee → **S3 Knocked Out.**
- **⚡ Shock.** S3's KO deals 1 Morale to friendlies within 3″:
  - **S2** is **already Shaken** → Nerve `2` → **fails** → **Shaken → Broken.**
    → **S2 Routs:** next activation it must flee, may make no offensive ACTION, and **drops out of the Formation.** The unit is coming apart.
  - **C** → immune again.
- **E2 repositions behind C** and strikes it in the **rear**.
  - **Faceless:** a Square struck in the flank could not answer — but **C has no flanks.** C **Counters from the rear** (a free melee packet, Slice 1): `6 · 5 · 4 · 3` → 3 Successes → Grade 3 → 1 Wound + Guard on E2. The hero cannot be caught from behind.

### Player activates — the leader holds the line
**C (3 AP)** — a Circle moves and acts on **its own Agency**, never carried by the Formation:
1. **MOVE** to within 3″ of the routing **S2** (its own AP).
2. **ACTION → Rally S2** — steps the Mind track **up one: Broken → Shaken.** **S2 stops Routing;** Shaken, it may act again next turn (at −1 die). *[Ruling 9 — a leader can Rally.]*
3. **ACTION → strike E2** (Slice 1 melee), finishing what the rear-Counter started.

| after R2 | Mind | Body | note |
|---|---|---|---|
| S1 | — | Knocked Out | |
| S2 | **Shaken** | 1 | **Rallied — stopped Routing** |
| S3 | — | Knocked Out | |
| C | — | 2 | held the line |

**Result:** the unit that was one failed save from routing off the table is still fighting, because
a single Entity immune to the panic spent one ACTION to reverse it. Two Squares are down, but the
line did not break — the Circle broke the **Rout**, not by a bonus, but by being the one thing on the
field the Mind channel cannot touch.

---

## Coverage check — did Slice 2 close?

| New beat | Exercised by | Rule source |
|---|---|---|
| Morale as channel damage | Shock deals 1 Morale | 01_MIND_CHANNEL |
| Nerve as a tiered save | 1 save die per Morale point (M 5+) | 01 · Ruling 1 |
| Mind track steps | Steady → Shaken → Broken | 01 |
| Shaken penalty | S2's −1-die strike | 01 |
| Shock (Written Trigger) | KO within 3″ → 1 Morale | 01 (reuses Slice 1 grammar) |
| Circle: 3 AP | C's three acts | 02 · Ruling 2 |
| Circle: faceless | the rear Counter | 02 |
| Circle: immune / no Nerve | took no shock | 02 · Ruling 10 |
| Circle: not in formation | C moved on its own AP | 02 · Ruling 13 |
| Formation & coherency | the screened unit, S2 dropping out on Rout | 03 |
| Rout | Broken S2 flees, leaves Formation | 03 |
| Rally | leader steps the track up | 03 · Ruling 9 |

**No undefined rule was reached.** Every new object slotted into the Slice 1 ontology — Morale/Nerve
are State, Shock/the Circle-break are Written Triggers, the Formation is a nesting Entity, Rally is a
Procedure. **The three-axis object model held with nothing added to it.** That was the real test of
Slice 2, and it passed.

## Open at the seam — Slice 3, "a battle makes history"
- **S1 and S3 are Knocked Out** — what becomes of them after the battle? Wounds → Injury → Scar.
- **S2 ended Shaken** (Rallied down from Broken) — does that leave a mark? The **Morale check** decides whether a figure that broke carries a **Mind Scar** forward. *[Ruling 11 — the Morale check is the aftermath roll; it is Persistence, and Persistence is Slice 3.]*
- The **Caravan**, the campaign clock, and everything that turns a battle into a history: Slice 3.
