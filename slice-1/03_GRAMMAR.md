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
  "resolution": "graded",
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

## Resolution — every packet resolves, by dice or automatically

Every capability resolves **through a PACKET** — there is no second execution path in the corpus.
A packet is either **`automatic`** (no roll) or **uncertain**; an uncertain packet declares its
**resolver** — `graded` (count successes) or `table` (a modified roll onto a result band). Three
modes, **one grammar**.

### `graded` — roll for it
The default for anything with uncertainty (a strike, a shot):

1. **Roll the PACKET's dice.**
2. **Count Successes** — each die that meets or beats the `success_number`.
3. **Resolve the highest Grade achieved.** Grade *N* fires **only** the Effects written at Grade *N* — a higher Grade does **not** inherit lower Grades' (discrete grading).

So with `spear_thrust`: 3 Successes → **Grade 3 → "1 Wound + Guard"** (not Grade 1's Push as well).
Each Grade line is a complete, self-contained outcome.

- **Success** — a die that meets the packet's success number.
- **Grade** — how well the whole roll succeeded.
- **Effect** — what resolving that Grade changes (a Wound, a Push, Guard…). Effects write State or Position, nothing else.

### `automatic` — it just resolves
Some capabilities carry no uncertainty — a Rally, a heal, opening a door, issuing a command. An
`automatic` packet **applies its Effect with no roll and no Grade.** It still targets, still checks
its constraints, still costs Agency; it only skips the dice.

```json
{ "id": "rally", "verb": "ACTION", "resolution": "automatic",
  "targets": "one coherent friendly Formation", "constraints": { "range": 3, "friendly": true },
  "cost": { "agency": 1 }, "effects": ["recover 1 Morale stage"] }
```

Automatic and graded are **the same grammar with the dice step optional** — not two engines. And a
normally-automatic effect may be given a **graded** version when the moment deserves it: a graded
Rally whose Grade decides how many figures steady, a graded heal whose Grade decides how much mends.
Nothing here is a new verb or a stray Procedure — Rally resolves exactly the way a strike does, minus
the roll.

### `table` — roll onto a result band
Some uncertain outcomes are not "how many successes" but "which band did one roll land in" — an
injury result, a scatter, an exploration event. A `table` packet rolls a single die (plus named
modifiers) and applies the Effect of the band it lands in:

```json
{ "id": "body_aftermath", "resolution": "table",
  "roll": "1d6", "modifier": "care",
  "results": { "<=1": ["Dead"], "2..4": ["Injury"], ">=5": ["Recovered"] } }
```

`table` is the **third resolver, not a new engine**: like `graded` it maps a roll to an Effect — it
just maps a *modified single roll to a band* instead of a *success count to a Grade*. Campaign,
injury, and scatter tables all use it, so it earns a first-class place in the grammar rather than
living as prose in each module.

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
