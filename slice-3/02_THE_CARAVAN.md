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
- a **Caravan** contains each player's **Book** for the length of a **campaign** — and the Books carry the Figures.

A Figure remains a complete Entity with its own durable record (Injuries, Scars, name), and so does a
Book; the Caravan adds carrying and coordination, not control. **Containment is not ownership** at
either step.

> This is the Slice 3 ontology payoff: a Caravan uses the **same containment *pattern*** as a Formation
> — nesting Entities — but its **membership persists at `campaign` scope** rather than `battle`. (Scope
> is a property of the membership State, not of the Entity's taxonomic kind: a Caravan and a Formation
> are different Entity kinds that happen to share a pattern.)

## Two scales of membership — the Book and the Caravan

Membership is a **Relationship** ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)) — never a list an Entity
owns — but it runs at **two scales**, because a warband is a player's *personal* Figures travelling in
a *shared* expedition:

```
Book    ──book_membership───────▶ Figure     (a player's own Figures)
Caravan ──caravan_membership────▶ Book        (the shared expedition carries the Books)
Caravan ──(direct)──────────────▶ communal    (hirelings, pack animals, NPC escorts — only if genuinely shared)
```

- A **Book** is a player's personal persistence Entity (physical form: [../interface/04_BOOK_AND_CARAVAN.md](../interface/04_BOOK_AND_CARAVAN.md)). It owns **only Book-specific** facts — personal resources, capacity, selections, Book-level state — and relates to its Figures by `book_membership`. **It does not own their Injuries or Scars.**
- Each **Figure** still owns its own durable condition — name, Injuries, Scars, Rattle, advancement — as **State on that figure** ([00_PERSISTENCE.md](00_PERSISTENCE.md)). Unchanged.
- The **Caravan** relates to the **Books**, not directly to most Figures, and **queries travelling Figures transitively through the Books.** Direct `Caravan → Figure` is reserved for genuinely **communal** assets that belong to no one player. The Caravan keeps **no roster copy** — no second authoritative owner, exactly as before.

Between battles a member Figure sits in one of a few conditions:

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
