# Slice 3 · Walkthrough — the survivors make history

The testable artifact. It picks up **exactly where [Slice 2's walkthrough](../slice-2/04_WALKTHROUGH.md)
ended**, runs both persistence boundaries (Aftermath out, Battle-Start in), and marches one clock-turn
— so you can watch a battle's outcome walk into the next fight and *cost* something. Rolls are
illustrative; the point is the loop **closes** and history is *felt*.

## Where Slice 2 left them — and what the battle recorded

As figures fell and broke, the Body and Mind procedures wrote **battle-scoped history flags** (not
queryable Transitions — the flags are the stored proof, [Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)):

| Warband — the player's **Book** | End of battle 1 | Flag written |
|---|---|---|
| **C** (Circle leader) | Steady, unhurt | — |
| **S1** (Square) | Knocked Out | `was_felled` |
| **S2** (Square) | survived Shaken (Rallied back) | `was_broken` |
| **S3** (Square) | Knocked Out | `was_felled` |

The Caravan carries a **Healer** facility (`+1 care`) and — being a small expedition — **one bed slot.**

---

## Step 1 — the Aftermath (battle → campaign boundary)

The Aftermath reads the **flags** and resolves one **`table` packet** per marked figure
([01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md); resolver = `table`, [Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)):

- **S1** (`was_felled`) — Body Aftermath, `1d6 +1` (Healer): `3` → **4** → band `2..4` → **Injury**, a bad leg — **severe (cannot walk; needs a bed slot).**
- **S3** (`was_felled`) — Body Aftermath, `1d6 +1`: `2` → **3** → band `2..4` → **Injury**, also **severe (needs a bed slot).** *(A `≤1` would have been **Dead** outright — both survived the roll.)*
- **S2** (`was_broken`) — the Morale check, `1d6 +1` (leader C rode on): `1` → **2** → band `2..4` → **Rattle** (walks; will start next battle Shaken).
- **C** — no flags → no roll.

## Step 2 — the reset

All `battle`-scoped State wipes — Wounds refill, the Mind track returns to Steady, Guard clears,
positions forget, **and the `was_felled` / `was_broken` flags clear now that the Aftermath has read
them.** What the Aftermath *promoted* does not wipe:

| after reset | durable State | scope · `advance_rule` |
|---|---|---|
| C | — (Hale) | — |
| S1 | Injury: *severe leg* | `campaign` · heal on rest, else harden to Scar |
| S2 | *Rattle* | `campaign` · clears on a calm turn |
| S3 | Injury: *severe leg* | `campaign` · (but — see Step 3) |

## Step 3 — the Book rides in the Caravan, and capacity forces a choice

The Figures are the player's, held by `book_membership`; the **Book** rides in the shared Caravan
(`caravan_membership`, [02_THE_CARAVAN.md](02_THE_CARAVAN.md)). The Caravan's **shared bed slots** now
bite:

- **Walkers:** C (Hale) and S2 (Rattled) walk — walking slots, no problem.
- **Bed-cases:** **S1 and S3 both need a bed** — and the Caravan has **one bed slot.**

**Forced choice — whom to carry.** Two figures who cannot walk, one wagon bed. The warband beds the
veteran **S1** and **leaves S3.** S3's membership Relationship flips to `lost`: it is **removed from
the roster.** The death this campaign turn was not a die roll — it was a **decision**, made because a
wagon had one bed and two broken bodies in it.

## Step 4 — march (the clock), then Battle-Start

The enemy is closing, so the warband **hurries**: a **March** (clock `+1`, no Rest). Each `campaign`
State's `advance_rule` fires:

- **S1's severe Injury** — carried, not rested: it does not heal, but the bed keeps it alive, and it stabilises one step **severe → Lame** (walking-wounded). (A Rest would have healed it further; hurrying did not.)
- **S2's Rattle** — no calm turn, so it **does not clear.**
- `Charge` stores top up; Scars, had anyone had one, would not move. *(S2's Morale check came up Rattle, not a **Mind Scar**, only because C was there for the `+1`; alone, that `1` lands a permanent Nerve-tier drop. The leader's presence was the difference between a bad week and a lasting wound.)*

Then the next scenario begins, and the **Battle-Start Procedure**
([00_PERSISTENCE.md](00_PERSISTENCE.md)) — the entrance twin of the Aftermath — runs:

```
BATTLE-START
  1. defaults:  Wounds full, Mind Steady, positions placed, flags false
  2. read durable State:  S1 Lame · S2 Rattle · S3 absent (lost)
  3. apply init effects:   Lame → S1 MOVE −1″ ;  Rattle → S2 starts Shaken (−1 die)
  4. deploy the roster:    C · S1 · S2   (three where there were four)
```

## Step 5 — history walks in, and bites

The next battle opens on the Battle-Start output:

| figure | starts battle 2 as | because |
|---|---|---|
| **C** | Steady, Hale, 3 AP | untouched |
| **S1** | **Lame** — MOVE −1″ this battle | the leg it couldn't rest off |
| **S2** | **Shaken** from turn one (−1 die) until it clears | the Rattle it carried |
| **S3** | *absent* | left in the mud because the wagon had one bed |

On turn one it bites immediately: **S1**, at −1″, needs a 3″ run-up to charge and comes up short — no
charge, no Impact. **S2**, Shaken, rolls its first strike at −1 die. The warband that started Slice 2
as four fresh Squares under a hero opens Slice 3's second battle as **a lame veteran, a rattled
survivor, a hero, and a hole in the line.**

That is the whole thesis: **the `battle` world reset, but the `campaign`/`permanent` remainder did
not — and Battle-Start walked it back onto the table.**

---

## Coverage check — did Slice 3 close?

| Beat | Exercised by | Rule source |
|---|---|---|
| Scope **+ `advance_rule`** on State | the durable-State table | 00 |
| History **flags** (not Transitions) drive Aftermath | `was_felled` / `was_broken` read, then cleared | 00 + Slice 1 · 02_WORLD |
| Aftermath rolls are **`table`** PACKETs | 1d6 ± care → band → Effect | 01 + Slice 1 · 03_GRAMMAR |
| Body: Injury (severe) ; Mind: Rattle | S1/S3 legs ; S2 rattle | 01 |
| **Death** (permanent) | S3 lost | 01 + 02 |
| Roster membership as a **Relationship** | `caravan_membership`, queried | 02 |
| **Capacity — actually resolved** | 1 bed, 2 bed-cases → forced choice, S3 left | 02 |
| The clock & `advance_rule` (heal-or-hurry) | March; S1 severe→Lame, Rattle persists | 03 |
| **Battle-Start Procedure** (entrance boundary) | reads durable State, applies init effects | 00 + 03 |
| History alters the next battle | S1 short of a charge, S2 opens Shaken, S3 gone | 03 |

**No undefined rule was reached, and no new Object kind was invented.** "Campaign" is `battle`'s
objects at a longer **scope**, plus two owned boundary Procedures (**Aftermath** out, **Battle-Start**
in), plus a containing Entity (the Caravan) and `caravan_membership` Relationships. Every conversion
across the battle↔campaign line is owned. **The object model held at the top of the stack.**

## Open at the seam — Slice 4 and beyond
- **Recruitment** and the roster growing back (the hole where S3 stood).
- The **map, travel events, factions, territory** — content on the campaign loop.
- The **Story module's Bonds** accruing across battles exactly the way Scars do — the same `campaign`-scope machinery pointed at relationships.
- The two **declared blanks** — Redemption, and how a figure goes **hollow** — remain unbuilt by design.
