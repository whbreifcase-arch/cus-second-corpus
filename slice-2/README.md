# Vertical Slice 2 — A group acts, and can break

Slice 1 gave one figure a body it could lose. Slice 2 gives figures a **will** they can lose, and
lets them act as a **group** with a leader who can hold them together. It closes a genuinely new
loop:

```
an ally falls → the shock deals Morale → figures test Nerve → the Mind track steps
   → a figure breaks and Routs → a leader spends an ACTION to Rally → the track steps back
```

Everything is built on Slice 1 (the object model, the PACKET grammar, the Body channel) and the
signed rulings in `cus-concordance`. Nothing here is copied from the frozen First Corpus.

## What Slice 2 adds

| # | Doc | Adds |
|---|---|---|
| 0 | [00_ACTIVATION.md](00_ACTIVATION.md) | **The scheduler** (foundation, also underpins Slice 1) — the round · **alternating activation, one figure at a time** · how a Formation MOVE rides one activation. |
| 1 | [01_MIND_CHANNEL.md](01_MIND_CHANNEL.md) | The **Mind channel** — Morale (damage) · **Nerve** (the tiered save) · the Steady→Shaken→Broken track · **Shock** (a Trigger on the `felled` Transition). Same channel *interface* as Body. |
| 2 | [02_THE_CIRCLE.md](02_THE_CIRCLE.md) | The **Circle** — differs from a Square in exactly three ways: 3 AP · faceless (no facing, never flanked) · never moves in formation. Its Mind channel (Morale/Nerve/break/Rout) is **identical to a Square's**. |
| 3 | [03_THE_GROUP.md](03_THE_GROUP.md) | The **Formation** as a group Entity · Form Up · group MOVE · coherency & `flank_covered` · the **leader** · **Rout** · **Rally** (an `automatic` PACKET). |
| 4 | [04_WALKTHROUGH.md](04_WALKTHROUGH.md) | A worked group action on the real scheduler — a Square breaks, **actually Routs a full activation**, and the leader spends a turn to Rally it. Closes the loop with no undefined rule. |

> **Foundation changes that flowed back to Slice 1** (from the Slice 2 review): the **activation
> scheduler** (above), an **`automatic` resolution mode** so Rally and kin resolve *through* a PACKET
> with no dice (Slice 1 · 03_GRAMMAR), and the **Transition** boundary — State / Transition / Trigger
> / Invocation — so Written Triggers observe change without smuggling in an "event" object
> (Slice 1 · 02_WORLD). Recorded as CON-0015…0017.

## Where this sits in the object model (Slice 1 · 02_WORLD)
Slice 2 is the first real test of whether the three-axis ontology holds when the corpus grows:
- **Morale · Nerve · the Mind track** are new **State** on the Body-and-Mind Entity — owned at *(Entity, Instance)*, exactly like Wounds. No new machinery.
- The **Circle** is a new **Entity** kind that differs only in Agency, facing, and formation — its Mind channel is ordinary State, identical in kind to a Square's (no new machinery).
- The **Formation** is a new **Entity** that *contains* Figures without stripping their agency (nesting, per 02_WORLD).
- **Rally** is a **PACKET** (`automatic` resolution — no dice); **Rout** is a state consequence of Broken; **Shock** is a **Trigger** on the `felled` **Transition**. Nothing invents a parallel system.

If the ontology needed patching to fit any of this, that would be the finding. It did not.

## Deliberately deferred to Slice 3 — "a battle makes history"
All **Persistence**: the **Morale check** (the *aftermath* recovery roll — whether a Broken figure
carries a **Mind Scar** into the next battle), Wounds → Injury → Scar, the Caravan, campaign state.
Slice 2 is still **one battle only** — it covers the *in-battle* mind and group; what survives the
battle is Slice 3. *[Ruling 11 keeps "Nerve" = the in-battle save and "Morale check" = the aftermath
roll; Slice 2 builds the first, names the second, and defers it.]*

## Rulings honored
- **Nerve** is a tiered save, rolled per incoming Morale point; there is **no 3-dice Nerve test**. *[Ruling 1]* <!-- retired-lint: allow nerve-check, nerve-3dice reason: states the retired 3-dice Nerve test to reject it -->
- **Circle** = 3 AP, faceless, **never moves in formation**; **breaks via the standard Mind channel, exactly like a Square** (more resilient only by a higher Nerve tier). *[Rulings 2, 10 (rev.), 13]*
- **A leader can Rally.** *[Ruling 9]*
