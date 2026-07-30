# Composition · Signature Invariants — Charge, Channel, Cycle, and Reserve

> ⚠ **PROVISIONAL CONTENT MODEL.** This document corrects the naming seam between the finite Resource
> formerly called `Charge` and the Signature invariant **Charge**. It does not add a fifth primitive, a
> new Object kind, or a new resolution mode. It defines authoring vocabulary for content construction and
> **must later be ratified through the Concordance** (proposed **CON-0026**). Until then, treat the
> `Charge → Reserve` Resource rename and the invariant definitions here as pending, not settled canon.

## The correction

<!-- retired-lint: allow sustain reason: names the retired Sustain in order to correct it -->
**Charge** and **Channel** were previously inverted, while **Sustain** was introduced to cover what
Channel already means.

The corrected distinction is:

```text
CHARGE
Potential is accumulated before a discrete release.

CHANNEL
An application remains continuously active through commitment.

CYCLE
Repeated use alternates with forced restoration.

STRAIN
Use accumulates liability until restraint, venting, or failure.

RESERVE
Not an invariant: the finite Resource those loops may read and spend.
```

Preparation duration is an **Expression parameter of Charge**. Continuous duration is the essence of
**Channel**.

---

## Charge — accumulate, then release

> **Accumulate potential, then release it as a discrete burst.**

The recurring decision is:

> **When do I stop accumulating and cash the stored potential into one committed Expression?**

```text
ACCUMULATE → HOLD → RELEASE → RESET
```

Examples: draw and loose a greatbow; charge a lightning bolt; wind a siege engine; gather momentum for a
battlefield charge; build a combo and execute it; prepare a ritual, then invoke it; charge a capacitor,
then discharge it; aim patiently, then take the shot.

Its trade:

```text
delay · exposure · telegraphing
for
burst · reach · severity · reliability
```

Its counterplay:

```text
interrupt accumulation · force an early release · leave the threatened geometry
attack during accumulation · deny the required target or Position
```

The amount accumulated is **State or Resource read by the Expression**. It is not the Signature itself.

```text
Signature invariant: Charge
Expression: accumulate aiming progress
Packet: Perfect Shot
Release: consumes accumulated progress
Grades: determine how successfully the shot lands
```

---

## Channel — continuously apply while committed

> **Continuously apply an effect while remaining committed to it.**

```text
BEGIN → MAINTAIN → REDIRECT OR CONTINUE → END / INTERRUPT
```

The recurring decision is:

> **Is maintaining this continuous application still worth the commitment it occupies?**

Examples: continuous lightning beam; sustained healing; suppressive stream of fire; tractor beam;
magical barrier; flamethrower sweeping a lane; telepathic domination pressure; life-draining tether;
holding a portal open; maintaining a storm or hazardous zone.

Its trade:

```text
persistent application
for
continued attention · limited movement · occupied capability · ongoing Resource
```

Its counterplay:

```text
break contact · break line of sight · leave the area
interrupt the source · force the source to redirect · make continued maintenance too costly
```

**Sustain is redundant — it collapses into Channel.** Continuous application is exactly Channel's essence. <!-- retired-lint: allow sustain reason: states Sustain is retired into Channel -->

---

## Reserve — the finite Resource kind

The finite Resource formerly called `Charge` is renamed **Reserve** so the vocabulary no longer collides
with the Charge Signature invariant. (Calling ammunition and finite uses "Charge" stole a major causal
invariant and produced nonsense like *"the Charge Signature spends Charge to charge a charged attack."*)

```text
RESERVE decreases through use.
At zero, an action or event must restore it.
```

Reserve is neutral. Presentation may skin it as: Ammo · Arrows · Spell uses · Fuel · Supplies · Breath ·
Command capacity · Stored venom.

The Resource kinds are therefore ([Slice 1 · 01_PRIMITIVES](../slice-1/01_PRIMITIVES.md)):

```text
AGENCY   renewing:      refills every activation
RESERVE  finite:        spend → empty → restore
STRAIN   accumulating:  gain → danger → vent or punishment
```

`Reserve` is the carrier; a Signature such as **Cycle** builds the decision loop around it.

---

## Cycle — use, exhaust, restore

> **Alternate between productive and recovery states because capability periodically exhausts.**

```text
READY → SPEND RESERVE → EMPTY → RESTORE → READY
```

Cycle remains distinct from Charge:

```text
Charge   build before one amplified release
Cycle    manage repeated ordinary use and predictable downtime
```

Examples:

```text
Musket:               fire → empty → reload → fire
Railgun:              Charge the shot → release → Cycle through cooling or reloading
Sustained plasma:     Channel while accumulating Strain
```

---

## Clean combinations

| Construction | Signature(s) | Loop |
|---|---|---|
| Lightning bolt | **Charge** | accumulate power → release one burst |
| Lightning beam | **Channel** | maintain continuous contact and application |
| Plasma cannon | **Charge + Strain** | accumulate a burst while accepting instability |
| Machine gun | **Suppress** or **Channel** | expressed through a Reserve-driven **Cycle** |
| Flamethrower | **Channel + Zone** | maintain a continuous application while denying space |
| Healing beam | **Channel + Restore** | continuously reverse Body damage while committed |
| Greatbow sniper | **Charge + Focus** | invest preparation into one selected release |
| Ritual shield | **Charge → Radiate** | prepare, release, then the ward exists independently |
| Ritual shield (alt) | **Channel → Radiate** | the ward exists only while the caster maintains it |

The machine gun's *actual loop* decides its primary Signature: short bursts controlling a lane →
**Suppress**; a continuous stream held on target → **Channel**; an ammo/reload rhythm → **Cycle**.

---

## Authoring consequence

```text
Signature invariant   the recurring causal decision
Expression            how a Role × Tool construction realizes that invariant
Packet                one concrete attempt implementing the Expression
Grade                 how successfully that attempt expresses it
Resource              a carrier the Expression may read, spend, gain, restore, or vent
```

Therefore:

| Term | Kind |
|---|---|
| Charge | Signature invariant |
| Channel | Signature invariant |
| Cycle | Signature invariant |
| Strain | Resource kind (and a possible Signature invariant built around it) |
| Reserve | finite Resource kind — never a Signature |
| Sustain | retired into Channel <!-- retired-lint: allow sustain reason: summary row states Sustain is retired --> |

This document **reserves the terms**. Exact Packet procedures for accumulating, maintaining,
interrupting, releasing, restoring, and venting remain later content work.

---

*Prior: [03_UNIT_PROFILE.md](03_UNIT_PROFILE.md) — the flat Figure Definition. This document adds the
first provisional **Signature invariants**, the repeated causal decision a Signature specializes a
FrameSpec into.*
