# Slice 3 · Persistence — the architecture

*Foundation. Persistence is **Kernel architecture, not a module*** ([CON-0005]). This document is
the whole of it; everything else in Slice 3 is content built on the idea defined here.

Persistence answers one question: **what survives when the battle ends?** The answer is not a new
system. It is a property every piece of State already has but the earlier slices never named — its
**temporal scope.**

## Every State has a scope

State ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)) is *what is true now*. Slice 3 adds *how long
"now" lasts* — the **scope** at which a fact resets:

| Scope | Resets… | Examples |
|---|---|---|
| `instant` | immediately | a die result mid-resolution |
| `activation` | end of the figure's activation | an armed WAIT that didn't fire |
| `round` | end of the round | `has_activated` |
| `battle` | **at battle end** | `wounds_remaining`, the Mind track, Guard, current Position |
| `campaign` | on the **clock**, over time | an **Injury** (heals or worsens as the campaign advances) |
| `permanent` | never | a **Scar**, a figure's name and identity, the dead staying dead |

Scope is a field on the State, owned exactly where the State is owned (`(Object × Layer)`). Nothing
about *where* state lives changes; Slice 3 only writes down *when* it changes. But scope alone answers
only *which temporal domain owns this State* — not *how* a particular fact expires. So the
constitutional rule is **two-part:**

> **Every State declares its temporal `scope`. Every non-`permanent` State also declares an owned
> `advance_rule`** — how it resets, heals, clears, or hardens. (An Injury: *on a calm clock-turn, heal
> one step; if neglected, harden to a Scar.* Guard: *clear at the figure's next activation.*)

Scope *plus* `advance_rule` is what actually closes the Wave-2 "state without an expiry rule" risk —
scope alone would only half-answer it.

## The battle-end reset

A **battle** is a temporal scope. When it ends, all `battle`-scoped State is **reset** — the board
is wiped, Wounds refill, the Mind track returns to Steady, Guard and armed WAITs clear, positions
are forgotten. This is why Slice 1–2 could treat each battle as a closed world: everything they
wrote was `battle`-scoped.

What does **not** reset is `campaign` and `permanent` State. That surviving remainder — a figure's
injuries, scars, name, and the fact that it is alive at all — **is** the figure's persistent record.
Persistence is simply: *the reset skips the durable scopes.*

## The Aftermath — the boundary Procedure

Between "battle ends" and "durable state persists" sits one owned **Procedure**: the **Aftermath**.
It runs once, at the battle→campaign boundary, and it is where `battle`-scoped harm is **converted**
into durable State before the reset wipes it:

```
BATTLE ENDS
   ↓
AFTERMATH  (the boundary Procedure — reads the battle's history flags)
   ├─ each figure with was_felled  → Body aftermath  (table) → Dead / Injury / Recovered
   ├─ each figure with was_broken  → the Morale check (table) → Mind Scar / Rattle / Steeled
   └─ promote results to campaign/permanent State on the figure's record
   ↓
RESET  (wipe all battle-scoped State — including the history flags)
   ↓
CAMPAIGN  (the Caravan carries the durable records onward)
```

The Aftermath **cannot read a Transition** — a Transition is an ephemeral moment, long gone by
battle's end ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)). Instead it reads the **battle-scoped
history flags** the Body and Mind Procedures wrote *alongside* those Transitions — `was_felled`,
`was_broken` — resolves the matching packet, **promotes** the result across the scope boundary, and
only then does the reset clear the `battle` scope, flags included. Details of each roll are in
[01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md).

## The entrance boundary — Battle-Start

Aftermath is the *exit* from a battle. It has a twin at the *entrance*, because durable State does
not apply itself — a Procedure must read it and set the scene. **Battle-Start** runs when a scenario
begins:

```
BATTLE-START  (the entrance boundary Procedure)
   1. instantiate battle-scoped defaults   (Wounds full, Mind Steady, positions placed, flags false)
   2. read each surviving figure's durable campaign/permanent State
   3. apply each condition's initialization effect   (Rattle → start Shaken; Lame → −1″ MOVE; a Mind Scar → its Nerve-tier drop)
   4. deploy the roster
```

The two boundaries are symmetric, and together they *are* the persistence loop:

```
Battle-Start :  durable State  → battle initialization
Battle-End   :  battle history → durable State        (Aftermath)
```

Every conversion across the battle↔campaign line is owned by one of these two Procedures. Nothing
"just carries over": **Battle-Start carries it, explicitly.**

## Why this is architecture, not a module

A module (Combat, Story) *owns mechanics*. Persistence owns **no mechanic of its own** — it owns a
*rule about State*: which scopes survive a reset, and the one Procedure that bridges the boundary.
That is why it is Kernel architecture. Combat writes Wounds; the Mind channel writes the track;
Story will write Bonds — and Persistence decides, uniformly, which of those survive the night. It
sits *under* every module, not beside them. **Do not cite Persistence as a domain** — cite the scope.

*Next: [01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md) — what a battle leaves on a body and a mind.*
