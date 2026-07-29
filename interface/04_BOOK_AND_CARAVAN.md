# Interface · The Book & the Caravan

Two persistent objects at two scales. Their **data model** (the Book Entity, the membership
Relationships, the topology) is defined in [../slice-3/02_THE_CARAVAN.md](../slice-3/02_THE_CARAVAN.md);
this doc is their **physical embodiment** and the one rule that governs both: *containment is not
ownership.*

## The Book — personal
Each player has their own **Book**: a fold-out physical object that is that player's bounded, portable
piece of the campaign. Opening it says *"my people, my capabilities, my history, my place in the
world."* It may unfold into a play surface / component station, not mere storage. Physically it holds
and presents:

- the player's Figures (Champion, Retinue), their miniature bays and Frames;
- their Packet cards and optional loadouts;
- their personal equipment;
- their personal persistent history — injuries, Scars, advancement, personally-owned records.

**But the Book carries these without owning them.** The **Book Entity** owns only *Book-specific*
facts — personal resources, capacity, selections, Book-level persistent state. Each **Figure still
owns its own** name, Injuries, Scars, Wounds, advancement, capabilities; the **Book–Figure
Relationship** owns the personal membership ([../slice-3](../slice-3/02_THE_CARAVAN.md)). The physical
Book *displays and transports* all of it; it is not a bucket of authoritative copies.

## The Caravan — shared
The **Caravan** is the party's shared persistent object and physical vehicle — shared supplies,
facilities, capacity, location, obligations, campaign records, world-facing state. It is a **model on
the table** (the persistence axis you can move).

## The nook — containment, not ownership
The Caravan has a **Book nook**: a physical bay where the players stow their Books for transport. The
nook is the material form of the `Caravan → Book` expedition-membership Relationship.

> A Book is **sheltered by** the Caravan while remaining **personally owned.** The Caravan transports
> and coordinates the Books; it does not absorb their facts. *Containment is not ownership.*

```
CARAVAN            shared state  (+ the nook)
   └── nook        Caravan → Book  (containment)
         └── BOOK  personal state  (still the player's)
               └── Figures, Frames, Packet cards  (each Figure still owns its own condition)
```

## The slogan
**Each player carries a Book. Together, their Books travel in the Caravan.** The personal and the
shared are different scales with different owners — the nook lets them ride together without one
swallowing the other.

*Next: [05_LAYER_MAP.md](05_LAYER_MAP.md).*
