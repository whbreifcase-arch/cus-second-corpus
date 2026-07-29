# Composition · The Archetype Pipeline

An **Archetype** is *function made playable through identity and cadence* — and it is **rendered, not
authored.** The *Figure* is authored — the four composition fields (Role · Tool · Signature · Tempo)
plus Chassis and Packets; the Archetype is the **Presentation view** the constructor renders from them:

```
ARCHETYPE = Tempo( Signature( Role × Tool ) )
```

or, evocatively, **`(Role × Tool) ▷ Signature @ Tempo = Archetype`** — where each operator does a
different job:

- `×` — **locate** the functional cell (the Frame)
- `▷` — **specialize** that cell into a repeated decision loop (the Signature)
- `@` — **express** that loop at a cadence (the Tempo)

(These are Presentation-composition operators. `▷` is **specialize**, deliberately *not* "resolve" —
`resolve` is a formal Packet term (`automatic`/`graded`/`table`), a different thing.)

Read it as a pipeline, not a product:

```
PURPOSE + MEDIUM  →  FUNCTIONAL FRAME  →(Signature)→  DECISION LOOP  →(Tempo)→  PLAYABLE ARCHETYPE
```

---

## Stage 1 · FrameSpec = Role × Tool  (locate the socket)

`Role × Tool` locates a **FrameSpec** — a *socket contract*, **not** a taxonomic parent that "contains"
archetypes. It is the **build-a-soldier authoring schema** for that functional cell: which sockets a
Figure there must fill and may fill. It is **parameterized by Role and Tool** and specifies **socket
expectations** — it **owns no fact**: the Figure Definition owns its authored `role`/`tool`, and
body/equipment/personality live in Chassis / Overlays / Temperament. A FrameSpec is **not a root
Object** beside Entity/Packet/Relationship — it is authoring/interface tooling, and its *physical*
embodiment (a housing with keyed slots) lives in [../interface/01_FRAME.md](../interface/01_FRAME.md).
(Its exact required/optional sockets are ⚠ **PROVISIONAL** — see that doc.)

The nine cells give recognizable *names* for the socket you are building in:

| Role \ Tool | **Melee** | **Ranged** | **Hybrid** |
|---|---|---|---|
| **Pressure** (applies) | Assault | Shooter | Raider |
| **Anchor** (prevents) | Guard | Gunner | Warden |
| **Utility** (changes) | Disruptor | Controller | Operator |

*(Names ⚠ PROVISIONAL — reconcile against the frozen `ARCHETYPES.md`.)* A FrameSpec is **abstract**:
`Anchor × Ranged` (a Gunner socket) says *"denies space through ranged interaction"* and lists sockets
to fill — but not yet *what the player repeatedly does.* That is the author's next choice: the Signature.

## Stage 2 · Signature specializes the Frame  (▷)

**Signature is a specializer, not a fourth coordinate.** It does not sit beside Role and Tool — it acts
on their **combination:** `Signature(Role × Tool)`. It answers: *what recognizable, repeated decision
loop realizes this function through this tool?*

The deep consequence: **the same Signature means something different on a different Frame.** Take
`Suppress`:

| Frame ▷ Suppress | Specializes to |
|---|---|
| **Pressure × Ranged** ▷ Suppress | forces the enemy to react so the attacker can **advance** |
| **Anchor × Ranged** ▷ Suppress | **denies a lane** and prevents passage |
| **Utility × Ranged** ▷ Suppress | manipulates Morale / options / positioning **for someone else** |

Same Signature; three different specialized behaviours — because it acts on Role *and* Tool together. Two
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

## Authored, then rendered — never inferred

The authored fields are **authoritative**; the Archetype label is what **Presentation renders** from
them for humans. A Figure stores the inputs (flat — [03_UNIT_PROFILE](03_UNIT_PROFILE.md)):

```json
{ "role": "Anchor", "tool": "Ranged", "signature": "Suppress", "tempo": "Slow" }
```

…and Presentation renders the recognizable name (here: a *Pinning Gunner* / *Machine-Gun Nest*).
`archetype` is **never a stored field**, so contradictory data is not merely wrong — it is
**unrepresentable:**

```json
{ "role": "Utility", "tool": "Melee", "signature": "Heal", "tempo": "Fast", "archetype": "Sniper" }
```

You cannot set `archetype`; and those inputs render a *fast melee medic*, not a sniper.

**The pipeline runs one way only — construction, not inference. Each role is fixed:**

```
Author       constructs :  Role · Tool · Signature · Tempo      (explicit, authoritative)
FrameSpec    validates  :  socket legality · capacity · packet/Tool compatibility · references exist
Presentation renders    :  the Archetype package (name · card · silhouette)
Engine       resolves   :  Packets   (never an "Archetype")
```

Nothing runs backward. The system **never infers** Role, Tool, Signature, Tempo, or Archetype from a
figure's packets, effects, or costs. Validation confirms a construction is *legal*; it never *authors
identity.*

## The hidden-Tempo leak this fixes

The frozen reference sometimes smuggled Tempo *inside* an archetype's description — e.g. **Piercer** was
`Shooter + Pierce`, but its text also said *"slow."* That "slow" was doing architectural work without
its own field. The pipeline extracts it:

```
Old:  Piercer = Shooter + Pierce + (secretly) slow
New:  Role Pressure · Tool Ranged · Frame Shooter · Signature Pierce · Tempo Slow  →  Piercer
```

Now **Pierce** means *how the attack defeats protection* and **Slow** means *how often, and with what
commitment, the loop fires* — two different knobs, each its own field, no hidden state.

*Next: [03_UNIT_PROFILE.md](03_UNIT_PROFILE.md) — the Archetype stacked into a whole figure.*
