# Slice 3 · Walkthrough — the survivors make history

The testable artifact. It picks up **exactly where [Slice 2's walkthrough](../slice-2/04_WALKTHROUGH.md)
ended**, runs the Aftermath, marches one clock-turn, and starts the next battle — so you can watch a
battle's outcome walk into the next fight. Rolls are illustrative; the point is the loop **closes**
and history is *felt*, not just logged.

## Where Slice 2 left them

| Warband (Caravan roster) | End of battle 1 |
|---|---|
| **C** (Circle leader) | Steady, unhurt |
| **S1** (Square) | **Knocked Out** |
| **S2** (Square) | survived, ended Shaken — but **was Broken** mid-battle, then Rallied |
| **S3** (Square) | **Knocked Out**, felled far forward |

The Caravan carries a **Healer** facility (`+1 care`).

---

## Step 1 — the Aftermath (the battle→campaign boundary)

The Aftermath Procedure reads the battle's Transitions and rolls a graded packet per marked figure
([01_HARM_LIFECYCLE.md](01_HARM_LIFECYCLE.md)):

- **S1 — `felled`.** Body Aftermath, 1d6 `+1` (Healer): rolls `3` → **4** → Grade I → **Injury: *Lame*** (−1″ MOVE). Recovered but limping.
- **S3 — `felled`, far forward.** It fell where the line could not reach it before the enemy overran the ground: **−1 care.** Body Aftermath rolls `1` → **0** → **Dead.** S3 is removed from the roster.
- **S2 — `broke`** (rallied, but the crack happened). Morale check, 1d6 `+1` (its leader C rode on): rolls `1` → **2** → Grade I → **Rattle** (will start the next battle Shaken).
- **C** — never felled, never broke → no Aftermath roll.

> **The stakes landed:** S3 is gone. Not knocked out to pop back up next scenario — *gone*, and the
> roster is one Square lighter for the rest of the campaign.

## Step 2 — the reset

All `battle`-scoped State wipes: Wounds refill, the Mind track returns to Steady, Guard and armed
WAITs clear, positions forget. What the Aftermath just promoted **does not** wipe — it is
`campaign`/`permanent` now:

| after reset | durable State | scope |
|---|---|---|
| C | — (Hale) | — |
| S1 | Injury: *Lame* | `campaign` |
| S2 | *Rattle* | `campaign` |
| ~~S3~~ | **Dead** | `permanent` |

## Step 3 — load the Caravan, and march

Roster into the Caravan: **C (Hale) · S1 (Injured, Lame) · S2 (Recovering, Rattled)** — three where
there were four. S1's Lame is minor: it still walks, still takes a normal capacity slot.

**The decision — heal or hurry.** A Rest would advance the clock two steps (S1's Injury heals, S2's
Rattle clears) — but the enemy is closing. The warband **hurries**: a **March** (clock `+1`, no rest).
On the clock step:
- S1's **Lame** does **not** heal — no rest. It travels into the next battle.
- S2's **Rattle** does **not** clear.
- `Charge` stores top up from the wagons (a March still resupplies).
- Scars, had anyone one, would not move — but no one carries a permanent Scar yet. (S2's Morale check
  came up **Rattle, not Mind Scar**, only because C was there for the `+1`; alone, that `1` would have
  been a **Mind Scar** — a permanent Nerve-tier drop. The leader's presence was the difference between
  a bad week and a lasting wound.)

## Step 4 — the next battle begins, and history walks in

The next scenario instantiates the roster **with durable State intact** — not a blank slate:

| figure | starts battle 2 as | because |
|---|---|---|
| **C** | Steady, Hale, 3 AP | untouched |
| **S1** | **Lame** — MOVE range −1″ this battle | the Injury it hasn't rested off |
| **S2** | **Shaken** from turn one (−1 die on ACTIONs) until it clears | the Rattle it carried |
| **S3** | *absent* | it died |

And it **bites immediately**: on turn one S1 needs a 3″ run-up to charge and, at −1″, comes up
short — no charge, no Impact. S2, Shaken, rolls its first strike at −1 die. The unit that started
Slice 2 as four fresh Squares under a hero opens Slice 3's battle as **a limping veteran, a rattled
survivor, and a hole in the line where S3 used to stand.**

That is the whole thesis of the slice: **the `battle` world reset, but the `campaign`/`permanent`
remainder did not — and it changed the next fight.**

---

## Coverage check — did Slice 3 close?

| Beat | Exercised by | Rule source |
|---|---|---|
| Temporal scope on State | battle vs campaign vs permanent, per row | 00_PERSISTENCE |
| The Aftermath boundary Procedure | reads Transitions, rolls per figure | 00 + 01 |
| Body: Wound → Injury | S1's Lame | 01 |
| Body: Death (permanent) | S3 removed | 01 |
| Mind: the Morale check → Rattle | S2's roll (on `broke`, not end-state) | 01 · Ruling 11 |
| Aftermath rolls are graded PACKETs | 1d6 → Grade → Effect | 01 + Slice 1 · 03_GRAMMAR |
| The Caravan (nesting Entity, roster) | loading C/S1/S2; S3 gone | 02 |
| Capacity / facilities | the Healer's +1; S1 walks | 02 |
| The clock & March | heal-or-hurry; Lame/Rattle persist | 03 |
| History alters the next battle | S1 short of a charge, S2 opens Shaken | 03 |

**No undefined rule was reached, and no new Object kind was invented.** "Campaign" turned out to be
`battle`'s objects at a longer **scope**, plus one boundary Procedure (the Aftermath), plus a
containing Entity (the Caravan) that is a Formation grown up. **The object model held at the top of the
stack** — which was the real question Slice 3 asked.

## Open at the seam — Slice 4 and beyond
- **Recruitment** and the roster growing (the hole where S3 stood).
- The **map, travel events, factions, territory** — content on the campaign loop.
- The **Story module's Bonds** accruing across battles exactly the way Scars do — the same `campaign`-scope machinery pointed at relationships.
- The two **declared blanks** — Redemption, and how a figure goes **hollow** — remain unbuilt by design.
