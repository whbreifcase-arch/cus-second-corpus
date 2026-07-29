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
| 1 | [01_MIND_CHANNEL.md](01_MIND_CHANNEL.md) | The **Mind channel** — Morale (damage) · **Nerve** (the tiered save) · the Steady→Shaken→Broken track · Shock · Fear-as-damage. The symmetric twin of the Body channel. |
| 2 | [02_THE_CIRCLE.md](02_THE_CIRCLE.md) | The **Circle** — 3 AP · faceless (no facing, never flanked) · breaks only by a **written trigger**, on its own meter, never by a Nerve test · never moves in formation. |
| 3 | [03_THE_GROUP.md](03_THE_GROUP.md) | The **Formation** as a group Entity · Form Up · group MOVE (Squares only) · coherency · the **leader** · **Rout & Rally**. |
| 4 | [04_WALKTHROUGH.md](04_WALKTHROUGH.md) | A worked group action — a Square unit under a Circle leader takes shock, one breaks and Routs, the leader Rallies it — closing the new loop with no undefined rule. |

## Where this sits in the object model (Slice 1 · 02_WORLD)
Slice 2 is the first real test of whether the three-axis ontology holds when the corpus grows:
- **Morale · Nerve · the Mind track** are new **State** on the Body-and-Mind Entity — owned at *(Entity, Instance)*, exactly like Wounds. No new machinery.
- The **Circle** is a new **Entity** kind; its break condition is a **Written Trigger** on its *Definition* — the same invocation as Slice 1's Counter.
- The **Formation** is a new **Entity** that *contains* Figures without striping their agency (nesting, per 02_WORLD).
- **Rally** is a new **Procedure**; **Rout** is a state consequence. Nothing invents a parallel system.

If the ontology needed patching to fit any of this, that would be the finding. It did not.

## Deliberately deferred to Slice 3 — "a battle makes history"
All **Persistence**: the **Morale check** (the *aftermath* recovery roll — whether a Broken figure
carries a **Mind Scar** into the next battle), Wounds → Injury → Scar, the Caravan, campaign state.
Slice 2 is still **one battle only** — it covers the *in-battle* mind and group; what survives the
battle is Slice 3. *[Ruling 11 keeps "Nerve" = the in-battle save and "Morale check" = the aftermath
roll; Slice 2 builds the first, names the second, and defers it.]*

## Rulings honored
- **Nerve** is a tiered save, rolled per incoming Morale point; there is **no 3-dice Nerve test**. *[Ruling 1]*
- **Circle** = 3 AP, faceless; **breaks by a written trigger, never by dice**, on its own meter; **never moves in formation**. *[Rulings 2, 10, 13]*
- **A leader can Rally.** *[Ruling 9]*
