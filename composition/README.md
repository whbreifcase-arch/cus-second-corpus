# Composition — how a figure is built

The definition-layer. Slices 1–3 built the **engine** (act → fight → break → persist); this is how you
**author a figure** to run on it. It is not a gameplay slice (it closes no new loop) — it is the
authoring model that turns the four axes, named in [Slice 1 · 02_WORLD](../slice-1/02_WORLD.md), into a
composable figure.

## The one idea: the Figure is authored; the Archetype is rendered

An **Archetype** is not a thing you author, and not an object the engine resolves. You author explicit
fields + Packet references — that is the whole truth of the Figure. The **Archetype is a
Presentation *view*** the system **renders** from that truth; there is no Archetype object between the
Figure and its Packets. The constructor below is a **build-order**, never solved backward from packets:

```
        PURPOSE  +  MEDIUM
                 ↓                          Role × Tool          ×  = locate the functional cell
          FUNCTIONAL FRAME
                 ↓  Signature               ▷ Signature          ▷  = specialize that cell into a loop
           DECISION LOOP
                 ↓  Tempo                    @ Tempo              @  = express that loop at a cadence
        PLAYABLE ARCHETYPE
```

One expression:

```
ARCHETYPE = Tempo( Signature( Role × Tool ) )
```

Evocative form: **`(Role × Tool) ▷ Signature @ Tempo = Archetype`**. The operators are not arithmetic —
each has a different grammatical job (**locate / specialize / express**). Details in
[02_ARCHETYPE.md](02_ARCHETYPE.md).

## The complete figure

A figure is **authored** as one flat **Figure Definition** — it is *not* assembled from an
"Archetype." The authored field groups, each a distinct concern:

```
FIGURE DEFINITION
    = CHASSIS FIELDS                    # the hardware: Move, Armour, Wounds, Nerve, base shape (Rank), Creature Type
    + ROLE · TOOL · SIGNATURE · TEMPO   # the four authored composition fields
    + TEMPERAMENT                       # the fallback psychology (independent of function)
    + DEFAULT_DOCTRINE                  # the starting policy (a Figure field; current_doctrine is Instance)
    + PACKET REFERENCES
    + OVERLAYS · FACTION KNOBS          # explicit optional fields
```

Then, **separately, Presentation renders** — it never contributes an authored ingredient:

```
PRESENTATION renders
    the Frame view   from  Role × Tool
    the Archetype    from  Role × Tool ▷ Signature @ Tempo
    the whole card / physical package  from the Figure
```

(These are **field groups**, not *Layers* — `Layer` is reserved for Definition · Procedure · Instance ·
Presentation.)

The computational reading (the "small operating system" lens):

| Piece | Is like |
|---|---|
| Role × Tool | the **interface** |
| Signature | the **implementation** |
| Tempo | the **scheduler** |
| Figure (fields + packets) | the **executable truth** |
| Archetype | the **rendered identity** — a Presentation view, *not* executable <!-- retired-lint: allow archetype-operative reason: row explicitly states Archetype is NOT executable --> |
| Chassis | the **hardware** |
| Temperament | **fallback psychology** |
| Doctrine | **operating policy** |
| Overlays | **decorators** |
| Faction Knobs | **explicit configuration** |

## Docs
- **[01_AXES.md](01_AXES.md)** — the four axes with their *values* (Role · Tool · Tempo · Temperament) + the Rank & Creature-Type classifications. Fleshes out what Slice 1 only named.
- **[02_ARCHETYPE.md](02_ARCHETYPE.md)** — the constructor: `Role × Tool` (a **FrameSpec** socket) ▷ Signature @ Tempo → Archetype (rendered). Authored, never inferred.
- **[03_UNIT_PROFILE.md](03_UNIT_PROFILE.md)** — the full stack and the flat, authoritative figure Definition.

The **FrameSpec** here is the *digital* authoring schema; its *physical* embodiment (housing, keyed
slots), two-sided Packet cards, and the Book ⁄ Caravan objects live in **[../interface/](../interface/README.md)** —
the same architecture at a material resolution. (Physical is not a new layer; it is Presentation,
Position, and containment made of plastic.)

## Status
Ratified structure (William, 2026-07-29; **[CON-0023]**, which supersedes the layer-status framing of
[CON-0022]). **Chassis · the four composition fields · Temperament** are specified here; **Doctrine ·
Overlays · Faction Knobs** are *named and bounded* but their full content is later work. Specific
Frame/Archetype *names* and FrameSpec sockets are `⚠ PROVISIONAL`, to be reconciled against the frozen
`ARCHETYPES.md` and tuned in play.
