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
about *where* state lives changes; Slice 3 only writes down *when it expires*. This also closes the
Wave-2 "state without an expiry rule" risk — **every State now declares its scope.**

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
AFTERMATH  (the boundary Procedure)
   ├─ for each figure that ended Knocked Out → Body aftermath  → Dead / Injury / Recovered
   ├─ for each figure that ended Broken      → the Morale check → Mind Scar / Rattle / Steeled
   └─ promote the results to campaign/permanent State on the figure's record
   ↓
RESET  (wipe all battle-scoped State)
   ↓
CAMPAIGN  (the Caravan carries the durable records onward)
```

The Aftermath reads a **Transition** the battle already recorded — *this figure was felled*, *this
figure broke* ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md), Transitions) — and resolves the
consequence. It does not invent state; it **promotes** it across the scope boundary, then lets the
reset clear the rest. Details of each roll are in [01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md).

## Why this is architecture, not a module

A module (Combat, Story) *owns mechanics*. Persistence owns **no mechanic of its own** — it owns a
*rule about State*: which scopes survive a reset, and the one Procedure that bridges the boundary.
That is why it is Kernel architecture. Combat writes Wounds; the Mind channel writes the track;
Story will write Bonds — and Persistence decides, uniformly, which of those survive the night. It
sits *under* every module, not beside them. **Do not cite Persistence as a domain** — cite the scope.

*Next: [01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md) — what a battle leaves on a body and a mind.*
