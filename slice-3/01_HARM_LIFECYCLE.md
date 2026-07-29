# Slice 3 · The Harm Lifecycle

What a battle leaves on a figure. Both channels follow the same shape — **battle harm → an Aftermath
roll → a durable mark** — and both Aftermath rolls are **`table`-resolution PACKETs**
([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)): a modified 1d6 onto a result band. No new
resolution engine — this is the third resolver the grammar already declares.

```
BODY   Wound (battle)  →  Body Aftermath   →  Injury (campaign)  →  Scar (permanent)
MIND   Morale (battle) →  the Morale check →  Rattle (campaign)  →  Mind Scar (permanent)
```

The numbers below are **⚠ PROVISIONAL** — Definition-layer content to tune in play. The *structure*
is the ratified part.

## Body — Wound → Injury → Scar

During battle, unsaved Wounds drop `wounds_remaining`; at 0 a figure is **Knocked Out**, and the Body
procedure writes the battle-scoped flag **`was_felled`** ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md),
Transitions). At the **Aftermath**, every figure flagged `was_felled` rolls the Body Aftermath — a
**`table` packet**, 1d6 modified by **care** (a Healer facility, safe ground: +1; abandoned on the
field, no Caravan: −1):

| Roll (1d6 ± care) | Grade | Result |
|---|---|---|
| ≤ 1 | — | **Dead.** Removed from the roster, permanently. |
| 2–4 | I | **Injury** — a durable `campaign` Body State (e.g. *Lame* −1″ MOVE, *Maimed* −1 die on strikes). |
| 5+ | II | **Recovered** — a hard night, no lasting mark. |

- An **Injury** is `campaign`-scoped, with an owned **`advance_rule`**: *on a calm clock-turn, heal one step; if neglected (or on a second Injury to the same place), harden into a Scar* ([03_THE_CAMPAIGN_LOOP.md](03_THE_CAMPAIGN_LOOP.md)). It travels with the figure until it clears or hardens.
- A **Scar** is `permanent` — it never clears. It is the durable record of what a figure survived, and it may carry a small mechanical hook or be purely a mark of identity. A figure is a history of its Scars.

## Mind — the Morale check → Mind Scar

*[Ruling 11: "Nerve" is the in-battle save; the **Morale check** is the aftermath roll. One word never
names two resolvers.]* At the Aftermath, every figure that **was Broken at any point** in the battle
([Slice 2 · 01_MIND_CHANNEL](../slice-2/01_MIND_CHANNEL.md)) rolls the **Morale check** — a **`table`
packet**, 1d6 modified by **a leader's presence in the Caravan** (+1) or isolation (−1). (The Mind
procedure sets the flag **`was_broken`** the first time a figure hits Broken; the Aftermath reads that
flag, not the end-state — breaking is the trauma even if a Rally brought the figure back, which is
what connects Slice 2's Rally to a lasting mark.)

| Roll (1d6 ± support) | Grade | Result |
|---|---|---|
| ≤ 1 | — | **Mind Scar** — a `permanent` Mind State (e.g. Nerve tier drops one step, or a fear trigger: *on the first shock each battle, auto-fail the Nerve save*). |
| 2–4 | I | **Rattle** — a `campaign` Mind State: starts the next battle **Shaken**, then clears with a calm clock-turn. |
| 5+ | II | **Steeled** — recovered clean; a veteran of the terror. |

The Mind lifecycle mirrors the Body's exactly — the same interface, at campaign scope: a temporary
durable condition (Rattle ~ Injury) that either heals or hardens into a permanent mark (Mind Scar ~
Scar).

## Death

**Dead is `permanent` and real.** A figure that dies is removed from the roster; the Caravan carries
one fewer. This is the stake that makes the rest matter — Injuries and Scars are the *survivable*
outcomes, and they are survivable precisely because the alternative is on the table.

## The Aftermath is one Procedure over `table` packets

Every roll above is a **`table` PACKET** resolved by the **Aftermath** Procedure
([00_PERSISTENCE.md](00_PERSISTENCE.md)). It reads the battle's **history flags** (`was_felled`,
`was_broken`) — *not* ephemeral Transitions — resolves the matching packet, and **promotes** its
band's Effect to `campaign`/`permanent` State before the reset wipes the `battle` scope. Nothing here
is a bespoke subsystem; it is the grammar's `table` resolver
([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)) pointed at the battle boundary.

## Declared blanks at the seam
Two things live just past Scar and are **deliberately not built** here — the First Corpus keeps them
blank on purpose (Slice 1 · Appendix Ω discipline): **Redemption** (there is a place where the
correct rules text is an *absence*), and how a figure becomes **hollow** (its trigger is unpublished).
Slice 3 records their existence and stops. Nothing in the harm lifecycle reads, writes, or defines
**SOUL**.

*Next: [02_THE_CARAVAN.md](02_THE_CARAVAN.md) — where the survivors travel.*
