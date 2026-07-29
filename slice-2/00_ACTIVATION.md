# Slice 2 · Activation & the Round — the scheduler

*Foundation. Discovered in Slice 2, but it underpins Slice 1 too — Slice 1's "A activates (2 AP)"
was quietly assuming this. It is written down now.*

The scheduler answers one question the earlier slices left open: **in what order do figures act?**
Getting it wrong makes the Rout-before-Rally question undecidable, so it is a rule, not a vibe.

## The round

Play proceeds in **rounds**. Within a round, the two sides **alternate**, and on your turn you
activate **exactly one** of your figures that has not yet activated this round. Then your opponent
activates one. Back and forth until every figure has activated once; that ends the round, and a new
round begins with all figures un-activated.

- **One figure per activation.** You do not move your whole side at once.
- **One activation per figure per round.** A figure acts once, then waits for the next round.
- If one side has more figures, it keeps activating its remainder after the other side is spent.

## What an activation is

An activation is a figure spending its **Agency** on **MOVE · ACTION · WAIT**, exactly as
[Slice 1](../slice-1/01_PRIMITIVES.md) defines. It reaffirms Slice 1's law: **a figure spends Agency
only on its own activation.** There is no other window in which a figure pays AP.

**Out-of-turn answers are not activations.** A Counter, a Shock, an armed WAIT firing — these are
free **Written Triggers** ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)); they resolve on someone
else's activation, cost no Agency, and do not use up the answering figure's own activation.

## Formation MOVE and activation

A **Formation has no activation of its own.** Instead:

> On a figure's activation, if it is in a Formation it may declare a **Formation MOVE**. It and every
> coherent friendly figure **that has not yet activated this round** move together, keeping coherency,
> and **each mover spends 1 AP**. For each figure that joins, **that move is its activation for the
> round** — it does not activate again. The whole coordinated move counts as **one activation** in
> the alternation; then the other side goes.

This keeps two Slice 1 truths intact at once:

- **Agency is spent only on your own activation** — a joining figure is activating *now*, together with the others; it is not paying AP on someone else's turn.
- **One activation per figure per round** — joining a Formation MOVE *is* your activation; you don't also get a solo one.

A figure with AP left after the 1-AP move may spend it in the **same activation** (e.g. move up with
the block, then ACTION). A **Circle never joins a Formation MOVE** ([02_THE_CIRCLE.md](02_THE_CIRCLE.md),
Ruling 13) — it always takes its own separate activation on its own 3 AP.

## Why alternating

Alternating, one figure at a time, is what makes Slice 2's drama real: when a Square breaks, it may
get **its own (routing) activation before its leader's next turn comes around** — so the leader has
to *choose* to spend an activation chasing it down to Rally, while the rest of the line goes
unanswered. A side-based turn would let you Rally everything after the fact for free. The scheduler
is where tempo becomes a decision.

## Object-model note

"Has this figure activated this round?" is **State** at *(figure, Instance)* — a flag flipped
`false → true` when it activates and reset each round. That flip is a **Transition**
([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)); the round is its temporal scope.

*Next: [01_MIND_CHANNEL.md](01_MIND_CHANNEL.md).*
