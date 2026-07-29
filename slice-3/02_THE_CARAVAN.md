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

> This is the Slice 3 ontology payoff: a Caravan uses the **same containment *pattern*** as a Formation
> — nesting Entities — but its **membership persists at `campaign` scope** rather than `battle`. (Scope
> is a property of the membership State, not of the Entity's taxonomic kind: a Caravan and a Formation
> are different Entity kinds that happen to share a pattern.)

## What the Caravan holds

Roster **membership** is not a list the Caravan owns — it is a **Relationship**
([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)), the very object Slice 1 built for a fact that lives
*between* two Entities:

```
Relationship: caravan_membership
  from: Caravan A   to: Figure S1   scope: campaign   state: active
```

The Caravan **queries** its members through these edges; it keeps no second authoritative copy (that
would be two owners for one fact). Each figure's *condition* — its Injuries, Scars, Rattle — remains
durable **State on that figure** (per [00_PERSISTENCE.md](00_PERSISTENCE.md)). Between battles a member
sits in one of a few conditions:

- **Hale** — uninjured, ready.
- **Injured** — carrying a `campaign` Injury; healing or worsening on the clock.
- **Recovering** — Rattled or bed-bound; cannot fight this coming battle, or fights impaired.
- **Scarred** — permanently marked, but ready.
- (and the ones who are simply *gone* — the Dead the Caravan no longer carries.)

## Capacity

The Caravan has a **capacity**, and the catch is that **the wounded cost more.** Two slot kinds:

- **walking slots** — a hale, Lame, or Rattled figure walks alongside and takes a walking slot;
- **bed slots** — a figure too hurt to walk (a *severe* Injury) needs a **bed slot** in a wagon, and beds are few.

Capacity is `campaign` State on the Caravan Entity. When bed-cases outnumber bed slots, the Caravan
**cannot carry everyone** — a **forced choice**: whom to bed, and whom to leave. A figure left behind
is **lost** — removed from the roster; the abandonment is, in effect, a death. This is where
persistence stops being bookkeeping and becomes a decision with a body count.

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
