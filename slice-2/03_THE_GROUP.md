# Slice 2 · The Group — Formation, the Leader, Rout & Rally

One figure that can break is a tragedy; a **group** that can break is a battle. This document adds
the smallest set of rules that let Squares act together and hold — or fail to.

## The Formation — a group Entity

A **Formation** is an Entity that **contains** Figures ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md),
nesting). Per the object model, containing them never strips their agency: each Square inside a
Formation is still a complete Entity that spends its own Agency. The Formation adds *coordination*,
not control.

- **Members** are **Squares** in **coherency** — each within **1″** (or base contact) of another
  member. A figure that leaves coherency **drops out** of the Formation.
- A **Circle never joins a Formation** ([02_THE_CIRCLE.md](02_THE_CIRCLE.md), Ruling 13). It may
  fight *beside* one and lead it, but it is never a member and is never dressed into the rank.

### Form Up
On its activation, a Square in base contact with a friendly Square may **Form Up** — a **MOVE** (1 AP)
that **ends in a legal Formation relationship**: it dresses into an existing Formation, or founds one.
Form Up is not a new verb and not a "MOVE-class" anything; it is a MOVE with a coherency requirement
on where it ends.

### What the Formation is *for* (its benefit)
Formation is not free movement — it earns its keep two ways:

- **The screen.** Interior members present a shared **front**. A Square's flank is **covered** when a
  coherent, **unbroken** member of the *same* Formation is in **base contact** on that side and
  overlaps its flank arc — the predicate **`flank_covered(figure, side)`**. A figure struck on a
  `flank_covered` side is **treated as struck to its face** (it may Counter; it is not flanked). Only
  the Formation's **exposed edges** — sides with no covering neighbour — carry open flanks. This is
  pure Position — a benefit the base *shows*, not a bonus number; Presentation can teach a player to
  read `flank_covered` by eye.
- **Rallied as one.** A leader's Rally reaches **every member in coherency at once** (below), instead
  of one figure at a time.

### Group MOVE
A Formation moves as a block on **one activation** ([00_ACTIVATION.md](00_ACTIVATION.md)). A member
declares a **Formation MOVE**; it and every coherent member **that has not yet activated this round**
move together, keeping coherency, and **each spends 1 AP**. For each figure, moving with the block
**is its activation for the round** — so the whole coordinated move is a **single activation** in the
alternation, and Agency is still spent only by its owner, on its own (now shared) turn. Break
coherency and the stragglers drop out. A member with AP to spare may spend it in the same activation
(move up with the block, then ACTION).

## The Leader

A **Leader** is an Entity that can **Rally** a unit — normally the **Circle** Champion, but a Square
may carry a **Sergeant** signature that makes it one too. Leadership reaches members within **3″**.
Being a leader is a **Procedure** the Entity owns, not a property of its shape — which is why it lives
here and not in [02_THE_CIRCLE.md](02_THE_CIRCLE.md).

## Rout — what Broken does

A figure stepped to **Broken** on the Mind track ([01_MIND_CHANNEL.md](01_MIND_CHANNEL.md)) **Routs**:

- on its activation it must **MOVE directly away** from the nearest enemy (it spends its AP fleeing);
- it may make **no offensive ACTION**;
- it **drops out of its Formation** (a routing figure breaks coherency);
- it keeps routing every activation until it is **Rallied** or it flees the table edge and is gone.

*Temperament* flavours *how* a figure routs (a Cowardly figure bolts for cover; a Ravenous one may
peel toward the nearest prey instead) — but the Slice 2 mechanic is uniform: **flee, no offense,
until Rallied.** The Temperament-specific rout behaviours are content for a later pass.

## Rally — the only way back up

**A leader can Rally.** *[Ruling 9 — the "a leader cannot Rally" line is struck.]*

**Rally is a PACKET** — an `automatic` one ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)). A Leader
spends **1 AP on an ACTION** to resolve it; it applies its Effect with no roll. It is not a stray
Procedure — it goes through the same grammar as a strike, minus the dice.

```json
{ "id": "rally", "verb": "ACTION", "resolution": "automatic",
  "targets": "one coherent friendly Formation (or one figure)",
  "constraints": { "range": 3, "friendly": true }, "cost": { "agency": 1 },
  "effects": ["recover 1 Morale stage"] }
```

- It steps the Mind track **up one** — **Broken → Shaken**, or **Shaken → Steady** — for each figure affected. A figure Rallied out of Broken **stops Routing** (now Shaken, it may act next turn at −1 die).
- Because a Formation is targeted **as one**, a single Rally steadies the whole coherent unit — the mechanical meaning of "the leader held the line."
- **Only Rally steps the track up.** No passive recovery; the will comes back because someone leads it back.
- Rally is also the clean case for a **graded** capability when you want one: a bigger authored packet — a *Rousing Speech* — could resolve `graded`, its Grade deciding how many stages, or how much of the field, it steadies. Slice 2's default Rally is the simple automatic one above.

The classic figure is the **Circle** — steadier than the levy (a high Nerve tier) though not immune —
spending an ACTION to Rally the Squares dying around it. That is the whole loop of Slice 2 in one
image, and the next document plays it out.

*Next: [04_WALKTHROUGH.md](04_WALKTHROUGH.md) — a group takes shock, breaks, and is held.*
