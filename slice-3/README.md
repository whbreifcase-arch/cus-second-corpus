# Vertical Slice 3 — A battle makes history

Slices 1–2 built a battle: figures act, oppose, break, and are held. But when the dust settles the
board is wiped and nothing remembers. Slice 3 gives the game a **memory** — it is where a battle
stops being an isolated event and becomes a link in a **campaign**.

The new loop is not a combat loop; it is the loop *around* combat:

```
        ┌──────────────────────────────────────────────┐
        │                                                │
   →  BATTLE  →  AFTERMATH  →  the CARAVAN marches  →  next BATTLE  →
        │        (harm becomes      (the clock         (survivors carry
        │         history)           advances)          their scars)
        └──────────────────────────────────────────────┘
```

Built on Slices 1–2 (the object model, the two channels, the scheduler) and the signed rulings.

## The one big claim

**Persistence is not a module. It is Kernel architecture** *(CON-0005)*. Slice 3's job is to prove
that claim by building the whole campaign layer from **one idea already in the object model —
temporal scope on State** — plus one boundary Procedure, the **Aftermath**. No new Object kind is
invented for "campaign"; a battle and a campaign are the same objects viewed at different scopes.

## What Slice 3 adds

| # | Doc | Adds |
|---|---|---|
| 0 | [00_PERSISTENCE.md](00_PERSISTENCE.md) | **The architecture** — temporal **scope** on every piece of State (battle / campaign / permanent) · the battle-end **reset** · the **Aftermath** boundary. Foundation. |
| 1 | [01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md) | **Wound → Injury → Scar** (Body) and **Morale → the Morale check → Mind Scar** (Mind) · death · the Aftermath rolls as **`table`** PACKETs, read from **history flags**. |
| 2 | [02_THE_CARAVAN.md](02_THE_CARAVAN.md) | The **Caravan** — the persistent expedition Entity that carries the roster between battles · capacity · facilities (the Healer) · the model on the table. |
| 3 | [03_THE_CAMPAIGN_LOOP.md](03_THE_CAMPAIGN_LOOP.md) | The **loop** and the **clock** — the March, recovery over time, and how a figure's history feeds the next battle. |
| 4 | [04_WALKTHROUGH.md](04_WALKTHROUGH.md) | The Slice 2 battle's survivors run the Aftermath, load the Caravan, march a clock-turn, and **start the next battle carrying their scars** — the make-history loop, closed. |

## Where this sits in the object model (Slice 1 · 02_WORLD)
The real test of the slice: does "campaign" fit the three-axis ontology, or does it force a new kind of thing?
- **Persistence is a temporal *scope* on State**, not a new Object. Every State fact already lived at `(Object × Layer)`; Slice 3 adds *when it resets*. Battle-scoped State (Wounds, the Mind track, Position, Guard) resets at battle end; **campaign/permanent** State (Injuries, Scars, the roster) survives.
- The **Caravan** is a new **Entity** that *contains* figures between events (nesting, per 02_WORLD) — the same containment the Formation used, at a longer scope.
- The **Aftermath** is a **Procedure** at the battle→campaign boundary; a **Scar** is durable **State**; the **clock** is the campaign temporal scope. Nothing new in kind.

If "make a campaign" had required a parallel game, that would be the finding. It does not — it required naming *scope*.

## Rulings honored
- The **Morale check** is the *aftermath* roll (not the in-battle Nerve save). *[Ruling 11]*
- **SOUL is untouched** — the harm lifecycle stops at Scar and never reads, writes, or defines SOUL.

## Deferred (declared, not built)
The First Corpus keeps two deliberate blanks near here — **Redemption** and how a figure becomes
**hollow**. Slice 3 records them as **declared absences at the seam** and does not operationalize
them (Slice 1 · Appendix Ω discipline).
