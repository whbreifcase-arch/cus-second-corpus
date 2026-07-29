# Design note — the capture pipeline & the big world loop

**Status: UNRATIFIED DIRECTION — a captured idea, not canon.** Author: William, 2026-07-29.
Recorded verbatim-in-spirit; to be designed, not yet built.

---

## 1. The capture pipeline (the interface to Persistence)

The physical→digital bridge that *feeds* the two persistence boundaries
([slice-3/00_PERSISTENCE.md](../slice-3/00_PERSISTENCE.md): Battle-Start reads durable State,
Aftermath records it). William's shape:

- **Snap pics of the game board** — and **the end state** especially. The photo is the record of what
  the table looked like when the battle ended.
- **QR codes on the mini bases** — each figure's base carries a code. (Fits the existing rule that the
  **base is the measuring instrument / the state-bearer**, Slice 1 · 02_WORLD Presentation. The base
  already *shows* shape/facing; now it also *identifies*.)
- **An app to fast-scan and quick-digest** — sweep the board, read the bases, and the companion app
  reconstructs who was where, who fell, who broke → hands the Aftermath its `was_felled` / `was_broken`
  inputs without hand-entry.

> "That is just the **capture**." — i.e. this is the *input* layer only: it turns a finished table into
> the durable-State deltas the campaign loop already knows how to consume. It does not decide anything;
> it observes. (Mirrors of the Instance, per the Presentation layer — capture never *owns* state, it
> *reports* it into the boundary Procedure.)

Open questions to design here: what exactly the QR encodes (identity only, vs identity + last known
condition), how much the photo does vs the scan, reconciliation when the scan and the players disagree
(the Instance is authoritative — capture proposes, the app confirms).

## 2. The big world loop (open thread)

> "Hmmm lets think about how we want the big world loop."

Separate, larger thread — the campaign **meta** above a single Battle→Aftermath→March→Battle turn.
This is Slice 4+ territory (the campaign loop's `## What is not here` seam):
- recruitment and the roster growing back;
- the **map**, travel, territory, factions;
- Story's **Bonds** accruing across battles the way Scars do;
- and how a whole **world** advances between the warband's battles (other forces marching, the clock at
  world scale) — the top of the recursion.

**To pick up:** design the world loop deliberately, same as the slices — one closed, testable loop at a
time. The capture pipeline (above) is the sensory organ that keeps the world loop fed with ground truth.
