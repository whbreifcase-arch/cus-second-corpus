# Composition — how a figure is built

The definition-layer. Slices 1–3 built the **engine** (act → fight → break → persist); this is how you
**author a figure** to run on it. It is not a gameplay slice (it closes no new loop) — it is the
authoring model that turns the four axes, named in [Slice 1 · 02_WORLD](../slice-1/02_WORLD.md), into a
composable figure.

## The one idea: Archetype is compiled, not chosen

An **Archetype** is not a thing you author. It is the recognizable identity the system **derives** from
a few authoritative primitives, through a pipeline:

```
        PURPOSE  +  MEDIUM
                 ↓                          Role × Tool          ×  = locate the functional cell
          FUNCTIONAL FRAME
                 ↓  Signature               ▷ Signature          ▷  = resolve that cell into a loop
           DECISION LOOP
                 ↓  Tempo                    @ Tempo              @  = express that loop at a cadence
        PLAYABLE ARCHETYPE
```

One expression:

```
ARCHETYPE = Tempo( Signature( Role × Tool ) )
```

Evocative form: **`(Role × Tool) ▷ Signature @ Tempo = Archetype`**. The operators are not arithmetic —
each has a different grammatical job (locate / resolve / express). Details in
[02_ARCHETYPE.md](02_ARCHETYPE.md).

## The complete figure

Archetype is only the *functional identity*. A whole figure stacks it with the rest, each layer owning
its own concern:

```
UNIT PROFILE
    = CHASSIS          # the hardware: Move, Armour, Wounds, Nerve, base shape, Creature Type
    + ARCHETYPE        # the function: Tempo(Signature(Role × Tool))
    + TEMPERAMENT      # the fallback psychology (independent of function)
    + DOCTRINE         # the current operating policy
    + OVERLAYS         # decorators (keywords, kit, veterancy)
    + FACTION KNOBS    # explicit configuration
```

The computational reading (the "small operating system" lens):

| Layer | Is like |
|---|---|
| Role × Tool | the **interface** |
| Signature | the **implementation** |
| Tempo | the **scheduler** |
| Archetype | the **executable gameplay identity** |
| Chassis | the **hardware** |
| Temperament | **fallback psychology** |
| Doctrine | **operating policy** |
| Overlays | **decorators** |
| Faction Knobs | **explicit configuration** |

## Docs
- **[01_AXES.md](01_AXES.md)** — the four axes with their *values* (Role · Tool · Tempo · Temperament) + the Rank & Creature-Type classifications. Fleshes out what Slice 1 only named.
- **[02_ARCHETYPE.md](02_ARCHETYPE.md)** — the compilation pipeline: Frame → Signature → Tempo → Archetype, derived not authored.
- **[03_UNIT_PROFILE.md](03_UNIT_PROFILE.md)** — the full stack and the authoritative figure Definition.

## Status
Ratified structure (William, 2026-07-29; [CON-0022]). The **Chassis / Archetype / Temperament**
layers are specified here; **Doctrine · Overlays · Faction Knobs** are *named and bounded* but their
full content is later work. Specific Frame/Archetype *names* are `⚠ PROVISIONAL` content, to be
reconciled against the frozen `ARCHETYPES.md` and tuned in play.
