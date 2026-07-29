# Slice 1 · Combat — the figure, the base, the exchange

The owned procedures (L5) for physical conflict, translated through the grammar. Combat is the
Kernel's **reference implementation, not its master**: everything here cites a primitive it
reads or writes.

## The Figure

A **Figure** is one independent agent / one piece. It owns its capability: Role · Tool · signature ·
PACKET references · stats. In Slice 1 every figure is a **Square**.

- **Square** — crew / rank-and-file. **Has a facing.** Has **2 AP**. May be flanked. *(The Circle — 3 AP, faceless, and its own rules — is Slice 2.)*
- A figure stays a complete agent at all times; nothing strips its Agency.

A Slice 1 figure profile (Definition — no runtime state):

```json
{
  "id": "spearman",
  "shape": "square",
  "agency": 2,
  "wounds": 2,
  "armour": "M",
  "tool": "Melee",
  "packets": ["spear_thrust"]
}
```

## The Base — the measuring instrument

State and geometry live on the **base**, read directly off the table. The base is the instrument;
no extra component is added for anything the base already tells you.

- **Facing** — a Square's base has a front arc. It answers threats to its **face** and concedes its **flanks**.
- **Engagement** — two bases in contact are **engaged**. An engaged figure's face is where it can strike and be struck.
- **Reach** — base-to-base contact is reach 0 (Slice 1 melee is contact only). Longer reach is a named field on a weapon packet, deferred.

Because Position is the cap, "who can I hit / who can hit me" is answered by **geometry**, never by
a spent resource.

## Movement and the Push

**MOVE** writes Position: choose a legal destination, pay 1 AP, move the base. A **Sprint** is just a
MOVE spent to cover ground.

When a moving base contacts another body, an owned procedure fires — the **Push**:

- **Push writes Position only.** A moving base continues along its straight trajectory and displaces contacted bases the **minimum** needed to clear its path. *[Ruling 12 — Push is the one displacement term; a weapon that displaces does so by writing a `Push` **Effect** on its packet, same primitive.]*
- **Larger plows smaller**, always. Same-size bodies: the mover stops on contact unless it arrived on a genuine charge (a clean run-up — an emergent case, not a defined term).
- If a wall prevents clearance, the mover **jams and stops**, and any strike that follows lands with the target pinned.
- Any Wound or state change from a collision comes from the **PACKET** the contact resolves — never from the Push itself.

## The strike (ACTION)

To strike, spend **1 AP** on an **ACTION** that resolves a melee PACKET against a figure in base
contact to your face:

1. Verify constraints (`not_in_contact:false` → must be in contact).
2. Roll the packet's dice, count Successes, resolve the highest **Grade**.
3. Apply that Grade's Effects: Wounds are resisted by the target's **Armour** save; each unsaved Wound steps the Body track.

## Overwatch (WAIT)

Spend **1 AP** on **WAIT** to arm a packet against a trigger window ("the first enemy that enters my
face"). The armed packet resolves when the trigger fires, on someone else's activation, at no
further cost. The AP bought a *better* armed packet than a bare Written Trigger would give — it buys
**quality, not permission**. An armed WAIT expires on the figure's next activation.

## The Counter (Written Trigger)

A **Counter** is one melee packet returned **free** by a figure struck in melee — a **Written
Trigger**, not a WAIT, and it costs nothing to resolve.

Four limits, all Position/authoring/death — never a budget:

- **Contact** — the counter-strike must reach its attacker (base contact, to face).
- **Facing** — a Square answers its **face** and concedes its **flanks**: strike a Square from the flank and it cannot Counter.
- **Authoring** — the striking packet decides whether it *provokes* a Counter (`provokes:true` by default for melee resolved in contact). A packet with `provokes:false` draws none.
- **Death** — a figure Knocked Out or Dead by the strike answers **once, on the way down** (a dying swing), and never again.

And the closure rule: **a Counter does not itself draw a Counter.** The exchange terminates.

## Guard (a defensive State)

Some Grades grant **Guard** — a State a figure holds until its **next activation**. While a figure
has Guard, strikes resolved against its **face** roll **−1 die**. Guard is spent by nothing; it
simply expires when the figure next activates. (It is State on the Instance, not a Resource.)

## Terminal states (Body channel)

```
Standing → Knocked Out (wounds_remaining = 0) → Dead (struck again while down; rolls no Armour)
```

Whether a felling Effect stops at Knocked Out or goes to Dead is a field on the Effect (Slice 1
default: a normal strike that reduces a figure to 0 leaves it **Knocked Out**; a strike on a downed
figure kills).

*Next: [05_WALKTHROUGH.md](05_WALKTHROUGH.md) — the whole thing, played out.*
