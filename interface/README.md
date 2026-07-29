# Interface — the physical face

CUS is **code all the way down and physical all the way up.** This module documents the *physical*
components — cards, sleeves, Frames, Books, the Caravan, tokens, models — and how they map onto the
system that already exists.

## Physical is not a new layer

There is **no fifth "physical layer."** The Kernel has four ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)):

```
Definition · Procedure · Instance · Presentation
```

Every physical component is a **manifestation inside** that architecture — overwhelmingly
**Presentation**, plus **Position** and **containment**. Presentation *translates and mirrors*; it is
**never authoritative.** A printed card, a sleeve, a token: if any of them disagrees with the object
they represent, the object in code wins. Plastic never holds authority.

> The physical interface is the **material implementation of Presentation, Position, and
> containment** — not a new Kernel layer.

## The physical hierarchy

Each level has a distinct owner and job; containment never transfers ownership:

```
CARAVAN                         shared persistent state  +  the Book nook   (a party owns this)
   └── BOOK NOOK                a containment Relationship  (Caravan → Book)
         └── BOOK               one player's personal persistent object     (a player owns this)
               └── FIGURE FRAME the assembly & play interface for one Figure
                     └── PACKET CARDS  individual executable capabilities (two-sided)
```

## Docs
- **[01_FRAME.md](01_FRAME.md)** — the **FrameSpec** (digital authoring schema) and its material embodiment, the **physical Frame** (housing, keyed slots, windows). Same design, two resolutions.
- **[02_PACKET_CARDS.md](02_PACKET_CARDS.md)** — the two-sided card. **Both faces are Presentation**; the JSON in code is the Definition.
- **[03_GEOMETRY.md](03_GEOMETRY.md)** — keyed shapes, notches, slot capacity: physical validation. *"An exception is a named, **visible component** — not a remembered sentence."*
- **[04_BOOK_AND_CARAVAN.md](04_BOOK_AND_CARAVAN.md)** — the physical **Book** (personal) sheltered in the Caravan's **nook** (shared). Containment ≠ ownership. (The Book *Entity* + topology live in [../slice-3](../slice-3/02_THE_CARAVAN.md).)
- **[05_LAYER_MAP.md](05_LAYER_MAP.md)** — which physical thing manifests each of the four layers.

## Slogans (ratified, [CON-0023])
- The Figure is authored; the Archetype is rendered.
- The FrameSpec constrains construction; the physical Frame embodies it.
- Both faces of a Packet card are Presentation; the JSON is Definition.
- The Book carries the personal; the Caravan carries the shared.
- Containment is not ownership.
