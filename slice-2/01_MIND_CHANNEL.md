# Slice 2 · The Mind Channel

Slice 1 built the **Body** channel: damage `Wounds`, save `Armour`, a terminal at 0. The Mind
channel is its **symmetric twin** — and reuses every piece of Slice 1's grammar. Nothing new is
invented; a second channel is instantiated.

```
BODY   damage = Wounds    save = Armour    track: Standing → Knocked Out → Dead   (Slice 1)
MIND   damage = Morale    save = Nerve     track: Steady   → Shaken       → Broken (Slice 2)
```

Both are **State**, owned at *(Entity, Instance)* — see [Slice 1 · 02_WORLD](../slice-1/02_WORLD.md).
An Entity now carries two independent channels: toughness in one says nothing about the other. A
heavy knight has high Armour and may have low Nerve; a barefoot fanatic, the reverse.

## Morale — damage on the Mind

**Morale** is damage dealt to the Mind, exactly the way Wounds are dealt to the Body: as a grade-line
Effect on a PACKET (see [Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)). A frightening strike writes
`1 Morale` on a grade line the same way another writes `1 Wound`.

> **Fear is not a special procedure. It is damage on a channel.** There is no separate "fear test,"
> no morale subsystem — a terror effect simply deals Morale, and the Mind channel resolves it with
> the same machinery the Body uses for Wounds.

## Nerve — the save

**Nerve is psychic Armour.** It is the **tiered save** on the Mind channel — the *same shape* as
Armour, applied to Morale. *[Ruling 1: Nerve is a tiered save rolled per incoming Morale point.
There is no 3-dice Nerve test.]*

```
NERVE  (Mind channel)   tiers:  None · L6+ · M5+ · H4+
```

Resolve it exactly like Armour: **roll one Nerve save die per incoming Morale point**; a
Light-Nerve figure saves on 6, Medium on 5+, Heavy on 4+. Each **unsaved** Morale steps the Mind
track one state.

## The Mind track — Steady → Shaken → Broken

The Mind track is a **one-way ratchet** of three states. Each unsaved Morale steps it **down** one;
**only Rally** ([03_THE_GROUP.md](03_THE_GROUP.md)) steps it back up.

| State | Meaning | Effect |
|---|---|---|
| **Steady** | default | none |
| **Shaken** | rattled | the figure's ACTIONs roll **−1 die**, and it **cannot gain Guard** |
| **Broken** | will gone | the figure **Routs** (see [03_THE_GROUP.md](03_THE_GROUP.md)) |

Two unsaved Morale takes a Steady figure to Broken. Note the deliberate **asymmetry with the Body**,
and it is a feature, not an oversight: the Body track is *depth* (a `wounds_remaining` pool — flesh
soaks a variable number of hits), while the Mind track is *stages* (a will cracks in visible steps:
steady, then shaky, then gone). Naming the asymmetry is required by Slice 1's Law 15 — it is a real
distinction between flesh and will, not a modelling accident.

## Shock — where Morale comes from in Slice 2

Slice 2's main Morale source falls straight out of Slice 1's melee: **when a figure is Knocked Out
or Dead, every *friendly* figure within 3″ takes 1 Morale** (a shock) and rolls Nerve. A unit does
not break because its own bodies are tough — it breaks because it watches its neighbours fall.

- Shock is a **Written Trigger** ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)) carried by the *felling* event: "on a friendly KO/Dead within 3″, deal 1 Morale." Free, fires once per occurrence, gated by Position (the 3″).
- A **Circle never takes shock** — it has no Nerve and does not use this channel at all (see [02_THE_CIRCLE.md](02_THE_CIRCLE.md)).

## The Morale check — named here, built in Slice 3

The **Morale check** is the *aftermath* recovery roll — what happens to a figure that ended the
battle **Broken**: does its will recover clean, or does it carry a **Mind Scar** into the next
battle? *[Ruling 11: "Nerve" is the in-battle save; the "Morale check" is the aftermath roll — two
names, never one word for two resolvers.]*

The Morale check is **Persistence**, and Persistence is Slice 3. Slice 2 names it so the vocabulary
is clean, and stops at the battle's edge: in-battle, the only way off the Mind track is **Rally**.

*Next: [02_THE_CIRCLE.md](02_THE_CIRCLE.md) — the figure that plays by different rules.*
