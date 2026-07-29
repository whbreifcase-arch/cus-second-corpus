# Composition · The Unit Profile

The Archetype ([02_ARCHETYPE](02_ARCHETYPE.md)) is only the figure's *function.* A whole figure stacks
it with five more layers, each owning **one** concern, none collapsing into another:

```
UNIT PROFILE
    = CHASSIS          # hardware:  Move · Armour · Wounds · Nerve · base shape (Rank) · Creature Type
    + ARCHETYPE        # function:  Tempo(Signature(Role × Tool))
    + TEMPERAMENT      # fallback psychology (independent of function)
    + DOCTRINE         # current operating policy
    + OVERLAYS         # decorators: keywords, kit, veterancy
    + FACTION KNOBS    # explicit configuration
```

## The layers

- **Chassis — the hardware.** The physical stats: `Move`, `Armour` tier (Body save), `Wounds` (Body depth), `Nerve` tier (Mind save), **Rank** (Square/Circle base shape → Agency + geometry), **Creature Type**. This is where Slices 1–2's stats live. *Chassis owns the body; Archetype owns the behaviour — they never overlap.*
- **Archetype — the function.** `Tempo(Signature(Role × Tool))`, *rendered* (02) — never stored on the Figure.
- **Temperament — fallback psychology.** The lean the figure reverts to when unled or Broken. Independent of Archetype (an Aggressive Guard is still a Guard).
- **Doctrine — operating policy.** The *current* stance the figure/unit is operating under (e.g. hold / press / screen). Policy, not identity — it can change mid-campaign. *Named and bounded here; full definition is later work.*
- **Overlays — decorators.** Additive modifiers: keywords, kit/equipment, veterancy, a Scar's hook ([Slice 3](../slice-3/01_HARM_LIFECYCLE.md)). They wrap the profile without changing its core. *Bounded here; content later.*
- **Faction Knobs — explicit configuration.** The per-faction settings that tune the same profile to a faction's feel. *Bounded here; content later.*

## The authoritative Definition

A figure Definition stores the **primitive, authoritative** fields, **flat**; Presentation *renders*
the human-facing Archetype from them (never the reverse):

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

- The four primitives sit **flat at the top level** — no `archetype_inputs` wrapper. `archetype` is **absent by construction**: it is *rendered* by Presentation, never stored, so it can never drift from the primitives.
- The **FrameSpec** is *not* stored in the figure — it is the authoring schema that guided this construction, and it lives in [02_ARCHETYPE](02_ARCHETYPE.md) / [../interface/01_FRAME.md](../interface/01_FRAME.md).
- `packets` are the figure's actual capabilities, referenced by ID ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)); a FrameSpec sets *socket expectations* for what packets a figure carries — the packets themselves are separate Definitions.

## Why this stack holds

Each layer answers a different question, so nothing leaks:

| Question | Owned by |
|---|---|
| *What can its body take/do?* | Chassis |
| *What is it functionally for?* | Archetype (Role × Tool ▷ Signature @ Tempo) |
| *How does it behave unled?* | Temperament |
| *What is it doing right now?* | Doctrine |
| *What extra is bolted on?* | Overlays |
| *How does its faction tune it?* | Faction Knobs |

Compose a figure by filling these fields; the system presents you a **Pinning Gunner** — but the truth
of the figure is the primitives, and the label is just the recognizable shadow they cast.

---

*Back to [README](README.md) · axes in [01_AXES](01_AXES.md) · the pipeline in [02_ARCHETYPE](02_ARCHETYPE.md).*
