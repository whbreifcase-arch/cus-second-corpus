# Slice 1 · The Grammar — PACKET, resolution, verbs

The executable middle of the stack (L3–L4). This is the one grammar every capability speaks.

## The PACKET

A **PACKET** is a stateless, named, referenced definition of a resolvable effect — one universal
data object. It:

- has a **neutral ID** (the ID never encodes what kind of packet it is);
- holds **no runtime state** — a Packet is an Object whose Instance facet is always empty; per-use results live on the acting Entity's Instance ([02_WORLD.md](02_WORLD.md));
- is **defined once, referenced everywhere** — never copied onto each card;
- carries **only** what its resolution needs;
- does **not** encode whether it is "good" or "bad" — the Kernel carries no alignment tag.

A packet reaches the resolver through one of five **invocations**. Slice 1 uses three:

| Invocation | Who pays | In Slice 1 |
|---|---|---|
| **ACTION** (verb) | actor's Agency | a strike |
| **WAIT** (verb) | actor's Agency (arms it) | Overwatch |
| **WRITTEN_TRIGGER** | nobody | the Counter |
| MOVE (verb) | actor's Agency | writes Position (no packet) |
| OWNED_PROCEDURE | the procedure | the Push (fired by a MOVE collision) |

### Packet shape (Slice 1 schema)

The owning module decides which fields its packets require. For Slice 1's Combat packets:

```json
{
  "id": "spear_thrust",
  "verb": "ACTION",
  "targets": "one figure in contact",
  "constraints": { "not_in_contact": false, "provokes": true },
  "cost": { "agency": 1 },
  "dice": 5,
  "success_number": 4,
  "grades": {
    "1": ["Push"],
    "2": ["1 Wound"],
    "3": ["1 Wound", "Guard"],
    "4": ["2 Wounds"]
  }
}
```

Every constraint is a **named field** (`not_in_contact`, `provokes`, `los`, `path`, `range`) —
never prose. A bullet is `los:true`; a lobbed grenade is `los:false, path:true`. Slice 1 melee
uses `not_in_contact:false` (must be in base contact) and `provokes:true` (this strike may draw a
Counter — see [04_COMBAT.md](04_COMBAT.md)).

## Resolution — Success → Grade → Effect

One resolver, used by every packet:

1. **Roll the PACKET's dice.**
2. **Count Successes** — each die that meets or beats the `success_number`.
3. **Resolve the highest Grade achieved.** Grade *N* fires **only** the Effects written at Grade *N* — a higher Grade does **not** inherit lower Grades' Effects (discrete grading).

So with the `spear_thrust` above: 3 Successes → **Grade 3 → "1 Wound + Guard"** (not Grade 1's Push
as well). Each Grade line is a complete, self-contained outcome. If a designer wants an Effect on
every line, they write it on every line.

- **Success** — a die that meets the packet's success number.
- **Grade** — how well the whole roll succeeded.
- **Effect** — what resolving that Grade changes (a Wound, a Push, Guard…). Effects write State or Position, nothing else.

## The Save

Some Effects are resisted by a **Save** — a tiered dice save owned by the target's channel. Slice 1
has one save:

```
ARMOUR  (Body channel)   tiers:  None · L6+ · M5+ · H4+
```

Read it as "roll one save die per incoming Wound; a Light-armour figure saves on 6, Medium on 5+,
Heavy on 4+." Each **unsaved** Wound steps the Body track (reduces `wounds_remaining` by 1).

> The Mind channel's save — **Nerve** — and its recovery roll, the **Morale check**, are Slice 2.
> *In this corpus "Nerve" names only the combat save; the aftermath roll is the "Morale check."* *[Ruling 11]*

## The three verbs

The player has **exactly three verbs**, forever. Everything else is an alias that reduces to one.

| Verb | Acts on | Writes | Cost |
|---|---|---|---|
| **MOVE** | the acting figure | Position | 1 AP |
| **ACTION** | a legal target | resolves a PACKET → Grade → Effect | 1 AP |
| **WAIT** | a trigger window | arms one PACKET to resolve later | 1 AP |

- **MOVE** stays its own verb because Position is a substrate, not an effect — it is never collapsed into ACTION.
- **ACTION** resolves a packet *now*. The packet decides what happens.
- **WAIT** changes *when* a packet resolves; it does not create a second reaction system. It is the only AP-priced out-of-turn capability, and the AP buys **quality**, not permission.

The engine adds two more invocations (Written Trigger, Owned Procedure) that fire packets without a
verb — but **the player still has only three verbs.**

*Next: [04_COMBAT.md](04_COMBAT.md) — the figure, the base, and the melee procedures.*
