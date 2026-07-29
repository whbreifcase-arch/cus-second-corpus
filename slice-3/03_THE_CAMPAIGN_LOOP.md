# Slice 3 · The Campaign Loop

The Aftermath ([01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md)) turned a battle into durable State. The
Caravan ([02_THE_CARAVAN.md](02_THE_CARAVAN.md)) carries it. The **campaign loop** is what happens
*between* battles — and it is the same decision loop as combat, one scale up.

## It is the decision loop, recursed

[Slice 1 · 02_WORLD](../slice-1/02_WORLD.md) named recursion: every layer is a complete game and a
component of the one above (Law 4). The campaign loop is the proof at the top of the stack — the same
*perceive → choose → act → consequence → persist* loop, with the **Caravan as the acting Entity** and
the **map as its Position:**

```
BATTLE  →  AFTERMATH  →  MARCH  →  (arrive)  →  next BATTLE
   │          │           │                        │
   │      harm becomes   the clock            survivors carry
   │      history        advances             their scars in
   └────────────────── one campaign turn ──────────────────┘
```

## The clock

The campaign runs on a **clock** — the `campaign` temporal scope made countable. Each turn of the
loop is a **March**: the Caravan MOVEs across the map (Position at campaign scale), and the clock
advances one step. Advancing the clock fires each `campaign` State's owned **`advance_rule`**
([00_PERSISTENCE.md](00_PERSISTENCE.md)):

- **Injuries heal** — one step per calm clock-turn (two with a Healer). A fully healed Injury clears; a neglected one **hardens into a Scar** ([01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md)).
- **Rattle clears** — a Rattled mind steadies after a calm turn.
- **Finite Resources replenish** — `Charge` refills from the Caravan's stores.
- **Scars do not move** — `permanent` is permanent; the clock does nothing to them.

The clock is also **pressure**: resting to heal costs time, and time is not free — supplies dwindle,
and the enemy is marching too. Slice 3 keeps that pressure minimal (a March advances one step; a Rest
heals but advances two), enough to make "heal or hurry" a real choice. Richer campaign pressure is
later content, not new architecture.

## How history feeds the next battle

This is the payoff — the reason any of it was worth recording. When the next battle begins, the
**Battle-Start Procedure** ([00_PERSISTENCE.md](00_PERSISTENCE.md)) — the owned, entrance-side twin of
the Aftermath — reads each figure's durable State and applies its initialization effect. Nothing "just
carries over"; Battle-Start carries it. So each figure is instantiated **with its durable State
intact:**

- a **Scarred** figure carries its Scar's hook (a lower Nerve tier, a fear trigger, a limp);
- an **Injured** figure fights impaired until it heals;
- the **Dead** are simply absent — the roster is smaller, and the gap is felt.

The next battle's opening Instance is not a blank slate; it is **last battle's Aftermath, plus the
clock**. That is the whole meaning of "a battle makes history": the `battle`-scoped world resets, but
the `campaign`/`permanent` remainder walks into the next fight and changes it. History is not a
separate ledger — it is the State that refused to reset.

## What is *not* here (Slice 4+)
The campaign loop as built is the **spine**. Richer content hangs off it later: recruitment and the
roster growing, the map and travel events, factions and territory, the Story module's Bonds accruing
across battles the way Scars do. All of it is content on this loop — none of it changes the
architecture, which is done: **scope + Aftermath + the Caravan + the clock.**

*Next: [04_WALKTHROUGH.md](04_WALKTHROUGH.md) — the Slice 2 survivors live through a campaign turn.*
