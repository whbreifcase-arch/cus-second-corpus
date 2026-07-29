# Slice 2 · Walkthrough — a group breaks, Routs, and is held

The testable artifact. It runs on the real scheduler ([00_ACTIVATION.md](00_ACTIVATION.md)):
**sides alternate, one figure at a time.** That is what lets a broken figure take its own routing
activation *before* its leader can reach it — the thing the earlier draft glossed. Slice 1 melee is
compressed to results; the dice shown are the **new** Slice 2 rolls. Illustrative rolls; the point is
the loop **closes**.

## The board

**Player** — a Formation of three Squares **S1 · S2 · S3** (`wounds 2 · armour M(5+) · nerve M(5+)`),
in coherency, with a **Circle leader C** (`3 AP · faceless · nerve H(4+) · leadership 3″`) fighting
beside them (never *in* the Formation — [02_THE_CIRCLE.md](02_THE_CIRCLE.md)).

**Enemy** — two Squares **E1 · E2** (`wounds 2 · armour M`).

| Instance (start) | Mind | Body | in Formation? |
|---|---|---|---|
| **S1 · S2 · S3** | Steady *(Nerve M, 5+)* | 2 | yes (coherent) |
| **C** (Circle) | Steady *(Nerve H, 4+)* | 2 | never (fights beside) |

---

## Round 1 — activations alternate, one figure at a time

**① Enemy · E1** strikes **S1** (in contact), two ACTIONs → **S1 Knocked Out.**
- ⚡ The Body procedure writes S1 to Knocked Out and emits the **`felled` Transition.** The **Shock** Trigger fires: 1 Morale to each friendly within 3″, resolve Nerve —
  - **S2** `3` → **fail** → Steady → **Shaken**.
  - **S3** `6` → save → Steady.
  - **C** (H, 4+) `5` → save → Steady.

**② Player · C** (3 AP) — the leader acts on its **own** activation (a Circle is never in the Formation): **MOVE** into contact with E1; **ACTION → strike** → Grade 3 → 1 Wound + Guard; E1 Armour `2` → fails → **E1: 2 → 1**. (Third AP held.)

**③ Enemy · E2** **MOVE**s to **S3** and strikes, two ACTIONs → **S3 Knocked Out.**
- ⚡ `felled` again → **Shock** within 3″:
  - **S2** *(already Shaken)* `2` → **fail** → **Shaken → Broken.**
  - **C** (H, 4+) `6` → save → Steady.

**④ Player · S2 — Broken, and it takes its own activation.** This is the beat the scheduler makes real: it is S2's turn, and a Broken figure **Routs**. S2 **MOVE**s directly away from the nearest enemy (spending its AP to flee), makes **no offensive ACTION**, and **drops out of the Formation** — coherency broken. S2 ends ~6″ off, alone, still **Broken.**

*Round 1 ends* — E1, C, E2, S2 have activated; S1 and S3 are down.

> **The Rout actually happened.** S2 was not conveniently caught before it could run. It spent a
> whole activation fleeing and left the line, because the leader had already activated and could not
> be two places at once. The panic cost ground — which is the whole point of alternating activation.

| after R1 | Mind | Body | note |
|---|---|---|---|
| S1 | — | Knocked Out | |
| S2 | **Broken** | 2 | **Routing · left Formation** |
| S3 | — | Knocked Out | |
| C | Steady | 2 | |

---

## Round 2 — the leader pays a turn to hold

**① Player · C** (3 AP): **MOVE** after the routing S2 (up to within 3″ — its own Agency, never carried by a Formation); **ACTION → Rally** — the `automatic` Rally packet ([03_THE_GROUP.md](03_THE_GROUP.md)) applies with no roll: **S2 Broken → Shaken, and S2 stops Routing.** Third AP: reface toward the enemy.

**② Enemy · E2** repositions **behind C** and strikes its **rear.**
- **Faceless:** a Square struck from behind could not answer — but **C has no flanks.** C **Counters from the rear** (free Written Trigger, Slice 1): `6 · 5 · 4 · 3` → Grade 3 → 1 Wound + Guard on E2. The hero cannot be caught from behind.

**③ Player · S2 — Shaken, no longer Routing.** It takes a normal activation, **MOVE**ing back toward the line (it may ACTION at **−1 die** while Shaken). The unit is reforming.

**④ Enemy · E1** presses, but the line has stabilised.

| after R2 | Mind | Body | note |
|---|---|---|---|
| S2 | **Shaken** | 2 | **Rallied — rejoining** |
| C | Steady | 2 | held the line |

**Result:** the honest version costs a **turn.** The Rout happened; S2 ran; and the leader spent an
entire activation — a move and the Rally — reversing *one* figure while the rest of the field went
unanswered. The Circle held the line not by immunity (it took the same shocks, and saved on its
Heavy Nerve) and not by a bonus, but by being **more resistant** and **choosing** to spend its tempo
on the break. Alternating activation is what turned "hold the line" into a decision instead of a
free clean-up.

---

## Coverage check — did Slice 2 close?

| Beat | Exercised by | Rule source |
|---|---|---|
| Activation scheduler | alternating, one figure at a time, explicit | 00_ACTIVATION |
| Transition + Trigger | Body emits `felled`; Shock watches it | 01 + Slice 1 · 02_WORLD |
| Morale as channel damage / Nerve save | Shock's 1 Morale, Nerve dice | 01 · Ruling 1 |
| Mind track steps | Steady → Shaken → Broken | 01 |
| **Rout — actually performed** | S2 flees a full activation, leaves Formation | 03 |
| Rally as an `automatic` PACKET | leader's no-roll ACTION steps the track up | 03 + Slice 1 · 03_GRAMMAR |
| Circle: 3 AP · faceless · same Mind channel | rear Counter; took shock, saved on Nerve | 02 · Rulings 2, 10 (rev.) |
| Circle: not in formation | C moved on its own AP both rounds | 02 · Ruling 13 |
| Formation & coherency (`flank_covered`) | the screened unit; S2 dropping out on Rout | 03 |

**No undefined rule was reached, and nothing was added to the three-axis object model** — Morale/Nerve
are State, Shock is a Trigger on a Transition, the Formation is a nesting Entity, Rally is a PACKET.
The one genuinely new *foundation* piece — the **activation scheduler** — was a gap in Slice 1 too,
and is now written down where it belongs.

## Open at the seam — Slice 3, "a battle makes history"
- **S1 and S3 are Knocked Out**, **S2 ended Shaken** (Rallied down from Broken). Does breaking leave a mark? The **Morale check** decides whether a figure that broke carries a **Mind Scar** forward. *[Ruling 11 — the Morale check is the aftermath roll; it is Persistence, and Persistence is Slice 3.]*
- Wounds → Injury → Scar, the **Caravan**, and the campaign clock: Slice 3.
