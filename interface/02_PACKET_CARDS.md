# Interface · Packet Cards — two faces, both Presentation

A Packet ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)) becomes a small, durable, two-sided card
that slides into a Figure's Frame. The crucial rule:

> **The authoritative Packet Definition is the JSON in code. Both physical faces are Presentation.**

Printing the Kernel language onto plastic does **not** move authority into the plastic. A physical card
is **one two-sided Presentation artifact referencing one Packet Definition.**

```
Packet Definition   ← authoritative JSON, in code
     ├── front  →  play-facing Presentation view
     └── back   →  kernel-facing Presentation view
```

## Front — play-facing Presentation
Immediately usable at the table; the Frame's window may cover what isn't needed right now:

```
HEAL
Target:    adjacent ally (standing, wounded)
Roll:      3 dice · 4+
Effect:    restore 1 Wound
Cost:      1 AP
```

## Back — kernel-facing Presentation
The same Definition, rendered in Kernel language for a player who wants to see the machinery:

```json
{
  "id": "heal",
  "verb": "ACTION",
  "resolution": "graded",
  "targets": "one friendly figure in contact",
  "constraints": { "friendly": true },
  "cost": { "agency": 1 },
  "dice": 3,
  "success_number": 4,
  "grades": {
    "1": ["restore 1 Wound"],
    "2": ["restore 2 Wounds"],
    "3": ["restore 3 Wounds"]
  }
}
```

*(Valid current grammar — [Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md): `targets`, a `constraints`
object, a `cost`, and discrete `grades` that do not inherit. HEAL could equally be `automatic` if it
carried no uncertainty; here it rolls.)*

Pull out **HEAL**, flip it, read the Kernel rendering, flip it back, keep playing. Two Presentation
resolutions of one Definition — that is the whole trick, and it teaches the Kernel without forcing
anyone to read JSON during ordinary play.

## Authority
If a printed face — front *or* back — disagrees with the JSON in code, **the JSON wins**, and the card
is reprinted. Definitions are static referenced descriptions; Presentation is a mirror
([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)). This is exactly the same rule that makes a token defer
to the Instance — a card defers to its Definition.

*Next: [03_GEOMETRY.md](03_GEOMETRY.md) — when the card's *shape* itself does validation.*
