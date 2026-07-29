# Composition · The Archetype Pipeline

An **Archetype** is *function made playable through identity and cadence.* It is **compiled**, not
authored, from four authoritative primitives:

```
ARCHETYPE = Tempo( Signature( Role × Tool ) )
```

or, evocatively, **`(Role × Tool) ▷ Signature @ Tempo = Archetype`** — where each operator does a
different job:

- `×` — **locate** the functional cell (the Frame)
- `▷` — **resolve** that cell into a repeated decision loop (the Signature)
- `@` — **express** that loop at a cadence (the Tempo)

Read it as a pipeline, not a product:

```
PURPOSE + MEDIUM  →  FUNCTIONAL FRAME  →(Signature)→  DECISION LOOP  →(Tempo)→  PLAYABLE ARCHETYPE
```

---

## Stage 1 · Frame = Role × Tool  (locate the cell)

Crossing the two functional axes gives a **Frame** — a nine-cell space of *functional sockets.* A
Frame owns **Role, Tool, and basic packet expectations** — **not** body, equipment, or personality
(those are Chassis / Overlays / Temperament).

| Role \ Tool | **Melee** | **Ranged** | **Hybrid** |
|---|---|---|---|
| **Pressure** (applies) | Assault | Shooter | Raider |
| **Anchor** (prevents) | Guard | Gunner | Warden |
| **Utility** (changes) | Disruptor | Controller | Operator |

*(Frame names ⚠ PROVISIONAL — reconcile against the frozen `ARCHETYPES.md`.)* A Frame is still
**abstract**: `Anchor × Ranged` (Gunner) says *"denies space through ranged interaction"* — but not yet
*what the player repeatedly does.*

## Stage 2 · Signature resolves the Frame  (▷)

**Signature is a resolver, not a fourth coordinate.** It does not sit beside Role and Tool — it acts on
their **combination:** `Signature(Role × Tool)`. It answers: *what recognizable, repeated decision loop
realizes this function through this tool?*

The deep consequence: **the same Signature means something different on a different Frame.** Take
`Suppress`:

| Frame ▷ Suppress | Resolves to |
|---|---|
| **Pressure × Ranged** ▷ Suppress | forces the enemy to react so the attacker can **advance** |
| **Anchor × Ranged** ▷ Suppress | **denies a lane** and prevents passage |
| **Utility × Ranged** ▷ Suppress | manipulates Morale / options / positioning **for someone else** |

Same Signature; three different resolved behaviours — because it acts on Role *and* Tool together. Two
figures can share a Frame yet feel different because different Signatures produce different loops
(Marksman's *Precision* vs Grenadier's *Blast*, both in the Shooter frame).

## Stage 3 · Tempo gives the loop cadence  (@)

Tempo ([01_AXES](01_AXES.md)) is **not** movement — it is the **cadence of the decision loop**: its
planning horizon, exposure, commitment, and counterplay. It acts on the *whole resolved loop:*

```
Pressure × Ranged ▷ Precision @ Fast    →  a mobile sharpshooter picking exposed targets, often
Pressure × Ranged ▷ Precision @ Normal  →  the ordinary Marksman
Pressure × Ranged ▷ Precision @ Slow    →  the Sniper: acquire, prepare, fire decisively, relocate
```

Same functional cell, same central decision — but **not the same archetype**, because cadence changes
the planning horizon. That is why Tempo belongs *after* Signature, and why the pipeline's output is the
Archetype.

---

## Archetype is derived, not authored

The primitive fields are **authoritative**; the Archetype label is what the composer **computes and
presents to humans.** A figure Definition stores the inputs:

```json
{ "role": "Anchor", "tool": "Ranged", "signature": "Suppress", "tempo": "Slow" }
```

…and the composer resolves the recognizable name (here: a *Pinning Gunner* / *Machine-Gun Nest*). This
makes contradictory data **impossible to write** — you can no longer author:

```json
{ "role": "Utility", "tool": "Melee", "signature": "Heal", "tempo": "Fast", "archetype": "Sniper" }
```

because "Sniper" is not a field you set — it is the *output* of the pipeline, and that input compiles to
a fast melee medic, not a sniper.

## The hidden-Tempo leak this fixes

The frozen reference sometimes smuggled Tempo *inside* an archetype's description — e.g. **Piercer** was
`Shooter + Pierce`, but its text also said *"slow."* That "slow" was doing architectural work without
owning a layer. The pipeline extracts it:

```
Old:  Piercer = Shooter + Pierce + (secretly) slow
New:  Role Pressure · Tool Ranged · Frame Shooter · Signature Pierce · Tempo Slow  →  Piercer
```

Now **Pierce** means *how the attack defeats protection* and **Slow** means *how often, and with what
commitment, the loop fires* — two different knobs, each in its own layer, no hidden state.

*Next: [03_UNIT_PROFILE.md](03_UNIT_PROFILE.md) — the Archetype stacked into a whole figure.*
