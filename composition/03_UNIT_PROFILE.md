# Composition · The Unit Profile

The Archetype ([02_ARCHETYPE](02_ARCHETYPE.md)) is only the figure's *rendered function.* A whole
figure is **authored** as one flat **Figure Definition** — field groups, each owning **one** concern,
none collapsing into another. (These are **field groups**, *not* Layers — `Layer` is reserved for
Definition · Procedure · Instance · Presentation.)

```
FIGURE DEFINITION
    = CHASSIS FIELDS                    # hardware:  Move · Armour · Wounds · Nerve · base shape (Rank) · Creature Type
    + ROLE · TOOL · SIGNATURE · TEMPO   # the four authored composition fields
    + TEMPERAMENT                       # fallback psychology (independent of function)
    + DEFAULT_DOCTRINE                  # the starting policy (a Figure field)
    + PACKET REFERENCES
    + OVERLAYS · FACTION KNOBS          # explicit optional fields
```

Then, **separately, Presentation renders** the **Archetype** (and the Frame view, the card, the
physical package) *from* that Figure — the Archetype is never an authored ingredient.

## The field groups

- **Chassis fields — the hardware.** `Move`, `Armour` tier (Body save), `Wounds` (Body depth), `Nerve` tier (Mind save), **Rank** (Square/Circle base shape → Agency + geometry), **Creature Type**. Slices 1–2's stats. Chassis *groups* body fields the **Figure Definition owns**; the rendered Archetype describes behaviour — they never overlap.
- **The four composition fields — Role · Tool · Signature · Tempo.** What Presentation reads to render the Frame view and the Archetype ([02_ARCHETYPE](02_ARCHETYPE.md)). The **Figure owns them; the Archetype owns nothing** (it is rendered).
- **Temperament — fallback psychology.** The lean a figure reverts to when unled or Broken. A Figure field, independent of the rendered Archetype (an Aggressive Guard is still rendered a *Guard*).
- **Doctrine.** `default_doctrine` is a **Figure Definition** field (the starting stance). The **current** stance in play — `current_doctrine` — is **Instance** State, not a Definition field. A doctrine *assigned by an order* is later Order/Mission authoring, **potentially Relationship-owned; exact owner unresolved.**
- **Overlays — decorators.** Additive optional modifiers: keywords, kit/equipment, veterancy. *(A **Scar is not an Overlay** — it is durable **Figure State** ([Slice 3](../slice-3/01_HARM_LIFECYCLE.md)); its physical piece is only a Presentation mirror.)* Bounded here; content later.
- **Faction Knobs — explicit configuration.** Per-faction settings that tune the same Figure to a faction's feel. Bounded here; content later.

## The authoritative Definition

A figure Definition stores the **authored** fields, **flat**; Presentation *renders* the human-facing
Archetype from them (never the reverse):

```json
{
  "id": "guard_pinning_gunner",

  "chassis": { "rank": "square", "creature_type": "Man", "move": 5, "wounds": 2, "armour": "M", "nerve": "M" },

  "role": "Anchor",
  "tool": "Ranged",
  "signature": "Suppress",
  "tempo": "Slow",

  "temperament": "Resolute",
  "default_doctrine": "Hold",

  "overlays": ["heavy_weapon", "veteran"],
  "faction_knobs": { "supply": "line" },

  "packets": ["suppressing_fire", "brace_weapon", "reposition"]
}
```

- The four composition fields sit **flat at the top level** — no `archetype_inputs` wrapper. `archetype` is **absent by construction**: Presentation *renders* it, it is never stored, so it can never drift from the fields.
- The **FrameSpec** is *not* stored in the figure — it is the authoring schema that guided construction ([02_ARCHETYPE](02_ARCHETYPE.md) / [../interface/01_FRAME.md](../interface/01_FRAME.md)).
- `packets` are the figure's capabilities, referenced by ID ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)); a FrameSpec sets *socket expectations* — the packets themselves are separate Definitions.

## Why this holds

Each field group answers a different question, and each authoritative fact has a single
**(Object × Layer)** owner — so nothing leaks:

| Question | Authoritative owner |
|---|---|
| What can its body take/do? | Figure Definition — Chassis fields |
| What is it functionally for? | *rendered* from the composition fields — the Archetype owns nothing |
| How does it behave unled? | Figure Definition — Temperament |
| What stance did it start with? | Figure Definition — `default_doctrine` |
| What is it doing right now? | **Instance** — `current_doctrine` |
| What extra is bolted on? | Figure Definition — Overlays |
| How does its faction tune it? | Figure Definition — Faction Knobs |

Compose a figure by filling these fields; Presentation shows you a **Pinning Gunner** — but the truth
of the figure is the authored fields, and the label is just the recognizable shadow they cast.

---
*Back to [README](README.md) · axes in [01_AXES](01_AXES.md) · the pipeline in [02_ARCHETYPE](02_ARCHETYPE.md).*
