# Slice 1 · Primitives, State, and the Laws that bind them

The bottom of the stack (L0–L2). Nothing above may contradict this file.

## The four primitives

The operative kernel reads and writes **exactly four things — no more.** Everything else reduces
to them.

| Primitive | Kind | One line |
|---|---|---|
| **Position** | substrate | Where an entity stands relative to other entities, objects, boundaries, and threats. You **change** it; you never spend it. |
| **Force** | substrate | An entity's capacity to produce, resist, or alter consequential change. **Non-numerical** — there is no Force stat. Read through an entity's axes; expressed by writing State, Position, or a Resource. |
| **State** | carrier | What is currently true of an entity. Written by Effects; stored only in the Instance. |
| **Resource** | carrier | A limited quantity an entity spends to act. Classified by how it replenishes. |

**Position and Force are substrates** — everything the Kernel touches ultimately reads or writes
one of them. **State and Resource are carriers** — how a substrate is stored and spent.

> These four are the whole operative ontology. A **reserved constitutional space** exists
> *outside* the executable kernel — referenced by nothing in it, instantiated never — see
> [Appendix Ω · Reserved Constitutional Space](APPENDIX_OMEGA_RESERVED.md). Slice 1 touches it
> nowhere.

## Position (substrate)

Position is physical and relational. In Slice 1 it is the location and facing of a figure's
**base** on the table (see [04_COMBAT.md](04_COMBAT.md) for how the base carries it).

- **Only `MOVE` writes Position directly.** One owned procedure — the Push — also writes it, as a consequence of movement.
- Position is the **cap** on what a figure can reach, strike, or answer. Where a rule wants to limit a figure, it denies it the *geometry*, not a budget.
- If a decision can be created through Position instead of a number, it is.

## State (carrier)

State is what is true right now. In Slice 1 the only State track is the **Body channel**:

```
BODY   damage = Wounds     save = Armour     terminal:  Standing → Knocked Out → Dead
```

- **Wounds are a number, not a track** — the punishment a figure absorbs before it goes down (`wounds_remaining`). At 0 the figure is **Knocked Out**; struck again while down, it is **Dead**.
- The Mind channel (Morale / Nerve) is **out of scope** for Slice 1.

## Resource (carrier)

A Resource is a limited quantity spent to produce change, typed by replenishment:

| Kind | Colour | Behaviour | In Slice 1 |
|---|---|---|---|
| **Agency** | 🟢 renewing | Refills every activation | ✅ the only Resource in the slice |
| **Charge** | 🟡 finite | Depletes; an action/event restores | deferred (ranged) |
| **Strain** | 🔴 accumulating | Rises with use; vents or punishes | deferred |

### Agency

**Agency (AP) is the only pool a figure spends to act, and only on its own activation.**

- **A Square has 2 AP.** (A Circle has 3 — deferred to Slice 2.) *[Ruling 2]*
- `1 AP → one MOVE, one ACTION, or one WAIT.`
- There is **no second pool** for acting on someone else's activation. Out-of-turn answers cost nothing to resolve — they are limited by Position, authoring, and death, never by a budget.
- Any deviation from 2 AP exists **only as a named, owned field** a tool can read — never as a sentence buried in prose. *[Kernel Law 15]*

> **Where these live.** A primitive is a *substance*; the *containers* it lives in — the Entity,
> the four layers (Definition · Procedure · Instance · Presentation), ownership, and reference —
> are the object model, defined next in [02_WORLD.md](02_WORLD.md). Every live value in Slice 1
> (current Position, `wounds_remaining`, an armed WAIT) is runtime state, and runtime state lives
> only on the **Instance**.

## The binding laws (the ones Slice 1 relies on)

1. **One owner.** Every fact has exactly one owner; no layer keeps a second authoritative copy.
2. **No state in Definitions.** Runtime state lives only in Instances.
3. **Intent vs. resolution.** The player chooses intent; an owned Procedure resolves the outcome. A procedure never makes the choice.
4. **Primitives are atomic; composites reduce.** Every mechanic reduces to Position / Force / State / Resource / a relationship between agents, with no unexplained remainder.
5. **An exception is a named field, never prose.** A deviation from a default may exist only as a named, owned field a tool can read. If it can't be a field, it's a missing layer — not a special sentence.

*Next: [02_WORLD.md](02_WORLD.md) — the object model: what kinds of things exist, and what owns state.*
