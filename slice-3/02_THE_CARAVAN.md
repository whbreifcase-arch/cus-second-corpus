# Slice 3 · The Caravan

If Persistence is *which State survives*, the **Caravan** is *where it survives*. It is the
persistent expedition — the body of people, beasts, wagons and materiel that travels between
battles and carries the roster. It is the **physical representation of the persistence axis**: an
actual model on the table, not a spreadsheet.

## The Caravan is an Entity

The Caravan is a new **Entity** ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)) — and, exactly like a
**Formation**, it is an Entity that **contains** other Entities without stripping their agency. The
containment is the *same nesting rule*, at a longer temporal scope:

- a **Formation** contains Figures for the length of a **battle**;
- a **Caravan** contains Figures for the length of a **campaign**.

A figure in the Caravan is still a complete Entity with its own durable record (its Injuries, Scars,
name). The Caravan adds carrying and coordination, not control.

> This is the Slice 3 ontology payoff in one line: **a campaign roster is a Formation with a
> `campaign` scope.** Nothing new in kind — the same container, viewed at a longer scope.

## What the Caravan holds

The Caravan's Instance holds the **roster** — every figure between battles, in one of a few durable
conditions (all `campaign`/`permanent` State on each figure, per [00_PERSISTENCE.md](00_PERSISTENCE.md)):

- **Hale** — uninjured, ready.
- **Injured** — carrying a `campaign` Injury; healing or worsening on the clock.
- **Recovering** — Rattled or bed-bound; cannot fight this coming battle, or fights impaired.
- **Scarred** — permanently marked, but ready.
- (and the ones who are simply *gone* — the Dead the Caravan no longer carries.)

## Capacity

The Caravan has a **capacity** — how many it can carry. The catch is that **the wounded cost more**:
a figure too injured to walk (`Injured`, severe) takes a wagon slot that a hale figure does not.
Capacity is `campaign` State on the Caravan Entity; exceeding it forces a choice — leave someone
behind (which worsens their Aftermath, −1 care) or slow the March. This is where persistence
becomes a *decision* rather than bookkeeping.

## Facilities

A Caravan carries **facilities** — referenced Definitions that modify the campaign Procedures. Slice 3
defines the concept and one facility:

- **The Healer** — `+1 care` to Body Aftermath rolls, and heals `campaign` Injuries one step faster on the clock. A referenced Definition on the Caravan; owned once, read by the Aftermath and the March.

Facilities are content: a Forge, a Chapel, a Quartermaster follow the same pattern (a Definition the
campaign Procedures read). None of them is a new mechanic — each is a modifier on an existing roll or
clock step.

## On the table

Per the interface commitment ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md), Presentation), the Caravan
is a **model** — the persistence axis you can see and move. Its roster and clock live in the companion
app (campaign bookkeeping is the one place the corpus commits to an app), but the *thing* is physical:
the wagon on the map is the Caravan Entity, and where it stands is Position at campaign scale.

*Next: [03_THE_CAMPAIGN_LOOP.md](03_THE_CAMPAIGN_LOOP.md) — how time passes between battles.*
