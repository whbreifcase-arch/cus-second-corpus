# Slice 1 · The World — the Object Model of CUS

What kinds of things exist, where they exist, and who is authoritative for each fact. This is the
**object model**: the root ontology the whole corpus reads against.
[01_PRIMITIVES.md](01_PRIMITIVES.md) gave the four *substances* (Position, Force, State, Resource);
this file gives the **Objects** those substances live in, and the three orthogonal axes that
describe every one of them. Read it before the grammar — once you know what an Object is and where
its state lives, every later document reads as instruction rather than invention.

It is slice-independent. Slice 1 supplies the examples.

---

## The world is Objects

**The world consists of Objects.** Every Object:

- is **authoritative for its own facts**, and duplicates no other Object's — *ownership*;
- **exists across four layers** — Definition · Procedure · Instance · Presentation;
- **may reference other Objects**, but never copies them;
- **specializes into a kind.**

```
Object
├── Entity ── Figure · Formation · Caravan · Kingdom · Nest · …
├── Packet
└── Relationship
```

That is the whole root ontology. There is one universal noun — **Object** — and everything else in
the corpus is a kind of Object or a fact owned by one. You never have to say "a Packet is an object
too"; a Packet simply *is* an Object.

---

## Three orthogonal axes

Every Object is described by three axes that **do not overlap**. Keeping them separate is the single
most important structural commitment in the corpus — most contradictions the First Corpus suffered
came from tangling two of them together.

| Axis | Question | Values |
|---|---|---|
| **1 · Ontology** | *What is it?* | Object → Entity · Packet · Relationship |
| **2 · Layer** | *Where does it exist?* | Definition · Procedure · Instance · Presentation |
| **3 · Ownership** | *Who is authoritative for a fact?* | exactly one **(Object × Layer)** cell |

Axis 3 is not a third list — it is the **rule** that Axis 1 crossed with Axis 2 has exactly one
authoritative cell per fact. Ownership is a *coordinate*, not a column.

---

## Axis 1 — Ontology: what exists

Three specializations of Object. (More Entity kinds arrive in later slices; the model does not
change, only the content.)

- **Entity** — a thing that *acts*. It owns capability (its packet references, its axes Role/Tempo/Tool/Temperament, its stats) and holds state, and it always has a **Position**. Entities **nest** — a Figure is a complete Entity inside a Formation that is itself an Entity — and nesting never strips agency (a contained Object keeps its own). Slice 1's only Entity kind is the **Figure**.
- **Packet** — a *resolvable effect*, one universal stateless data object. It is reached by an invocation and produces Effects. It never acts on its own; it is invoked. (Full grammar in [03_GRAMMAR.md](03_GRAMMAR.md).)
- **Relationship** — an *edge between agents*, holding its own state. It is a first-class Object because some facts live **between** two entities and belong to neither alone (the design razor's "relationship between agents"). Slice 1 shows the shape transiently — "A is **engaged** to B" is a symmetric edge; "B **may Counter** A" is a directed one — and later slices make edges persist and accrue: Bonds, grudges, oaths. Because Relationship is an Object *here*, the Story module later adds content, not a parallel mechanic.

---

## Axis 2 — Layer: where an Object exists

A layer is a **perspective**, not a thing. Every Object is viewed through the same four layers; an
Object simply may be empty at some of them. If you think in code, the mapping is exact:

| Layer | The facet it is | Runtime state? | Code analogy |
|---|---|---|---|
| **Definition** | The static, referenced description — a figure profile, a packet's grade table, a Base spec. | **Never** | the class / schema |
| **Procedure** | The one owned method that resolves a Statement — movement, the strike, the Counter, an aftermath roll. | No | the method |
| **Instance** | What is true **right now** — current Position, `wounds_remaining`, an armed WAIT, triggers already fired. | **Only here** | the heap object |
| **Presentation** | What the player sees and touches — the model, the card, the base, tokens, colour + shape. It **translates**; it never forks a mechanic. | No (mirrors the Instance) | the rendered view |

Two laws fall straight out of this, load-bearing everywhere:

- **No state in Definitions.** A Definition is identical at the end of a battle and at the start. The `spearman` profile in [04_COMBAT.md](04_COMBAT.md) is a Definition — every `spearman` on the table shares it. A **Packet's Instance facet is always empty**; that *is* what "stateless" means.
- **Runtime state lives only in the Instance.** When a `spearman` takes a Wound, `wounds_remaining` drops **on that figure's Instance** — never on the shared Definition, never (authoritatively) on the card.

Presentation is a **mirror, not a source.** If the base, a token, and the Instance ever disagree,
the Instance is right — Presentation may only display what some other layer already owns.

---

## Axis 3 — Ownership: one fact, one authoritative cell

**Every fact is authoritative at exactly one (Object × Layer) coordinate. No layer keeps a second
authoritative copy of another's fact.** This is the rule that makes the other two axes safe. To
place any fact, ask both coordinates:

| A fact… | is owned by Object… | at Layer… |
|---|---|---|
| a figure's packet references, axes, stats | the **Entity** (Definition) | Definition |
| a packet's grades, constraints, targeting | the **Packet** | Definition |
| `wounds_remaining`, current Position, an armed WAIT | the **Entity** | Instance |
| the state of an edge (engaged, a grudge's heat) | the **Relationship** | Instance |
| whether a strike may draw a Counter | the **striking Packet** (`provokes`) | Definition |
| anything shown on a card, base, or token | *(nobody — mirrors)* | Presentation owns nothing |

So a felled **Champion**'s wounds live on **tokens beside the model** — a Presentation *mirror* of a
fact owned at *(that Champion Entity, Instance)*. They are never written on the card, because the
card is that Entity's **Definition** facet, and Definitions hold no state. One fact, one owner.

When you add any mechanic, the first question is always both coordinates. If a fact seems to want
two owners, the mechanic is wrong — not clever.

---

## Reference — Objects point, they never copy

Objects are **referenced, not copied.** A Packet is defined once and pointed to by every card,
figure, and procedure that uses it; nothing is transcribed, because a copy is a second owner waiting
to drift (Axis 3). Two rules keep referencing safe:

- **Neutral identity.** An Object's primary ID never encodes its *kind*. `spear_thrust` is a name, not a category. Kind, tool, tags, and targeting live in a separate **sidecar registry** (`packet_index`) that is additive — an Object with no index entry is still valid; the index aids retrieval, never resolution.
- **One-way references.** References point from the specific to the general (Figure → Packet → primitive), which is also the build order of the documents that follow.

This is why the corpus can add a hundred weapons without touching the grammar: each is a new
**Definition** of a Packet Object that *references* the same machinery.

---

## Transitions — how change is observed

State is *what is true*. But some objects react to *what just changed* — a Counter fires when a
strike lands, Shock fires when a figure falls, an armed WAIT fires when an enemy enters a band. What
they watch is not a State; it is a **Transition** — the moment a State crosses a value
(`Standing → Knocked Out`, `Steady → Shaken`, `has_activated: false → true`). Four terms, kept
distinct, cover all causal propagation **without inventing an Event object**:

- **State** — what is true now (owned at one Instance cell).
- **Transition** — the fact that a State just changed. It is **emitted by the Procedure that owns the State it changes** — e.g. the Body procedure, on writing a figure to Knocked Out, emits the `felled` transition. A Transition is not a stored object; it is a named moment.
- **Trigger** — a clause on a **Definition** that watches for a named Transition (a Written Trigger). *"On a friendly `felled` within 3″, deal 1 Morale"* watches `felled`.
- **Invocation** — what the Trigger does when it fires: it **invokes a PACKET** ([03_GRAMMAR.md](03_GRAMMAR.md)) — free, once per occurrence, gated by Position and authoring.

So a causal chain — *a strike fells a figure, which shocks its neighbours, one of whom breaks* — is
just: **a Procedure writes State → emits a Transition → a Trigger watching it invokes a PACKET → that
Effect writes State → which may emit the next Transition.** No Entity is skipped, no event object is
smuggled in, and every step is owned. Naming this is what keeps Written Triggers honest — it is the
machinery Slice 2 leans on.

**Ephemeral vs recorded.** A Transition is a *moment*: a Trigger observes it **as it happens**, then
it is gone. If a *later* Procedure needs to know a Transition occurred — the Aftermath, at battle's
end, asking *"was this figure felled?"* — the emitting Procedure also **writes a scoped history flag**:
ordinary stored State (`was_felled_this_battle = true`), owned exactly where the changed State is
owned, expiring with its scope. The Transition stays ephemeral; the flag is its stored proof. Two
owned flags are **not** an event log — reach for a log only if you actually want log architecture.

---

## The object model in one breath

> The world is **Objects**. Each is described by three orthogonal axes: it **is** a kind (Entity ·
> Packet · Relationship), it **exists across** four layers (Definition · Procedure · Instance ·
> Presentation), and every fact it holds is **owned** at exactly one (Object × Layer) cell.
> Objects reference each other and never duplicate authority.

Hold that, and the grammar next is just: *how one Packet is written down and resolved.*

*Next: [03_GRAMMAR.md](03_GRAMMAR.md) — the PACKET, resolution, and the three verbs.*
