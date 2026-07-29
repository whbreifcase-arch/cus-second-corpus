# Slice 1 · The World — the object model of CUS

What kinds of things exist, what owns what, and what may reference what. This is the **object
model**: the container structure the whole corpus reads against. [01_PRIMITIVES.md](01_PRIMITIVES.md)
gave the four *substances* (Position, Force, State, Resource); this file gives the *objects* those
substances live in. Read it before the grammar — once you know what an Entity is and where state
lives, every later document reads as instructions rather than invention.

It is slice-independent: nothing here is specific to Slice 1's melee. Slice 1 supplies the examples.

---

## 1. Entity

An **Entity** is one thing the world treats as a unit — something that can own capability and hold
state.

- It **owns capability**: the packets it can invoke, the axes that describe it (Role · Tempo · Tool · Temperament), its stats.
- It **holds state**: what is currently true of it, on its Instance.
- It **has a Position**: it stands somewhere relative to other entities. (Even a purely social entity has Position — its standing in a room is Position, not a stat.)

Entities nest, and nesting never strips agency: a **Figure** is a complete Entity even inside a
formation that is itself an Entity. Slice 1 has one entity kind — the **Figure** (one piece / one
agent). Later slices add the **Caravan**, the **Formation**, the **Nest**, the **Kingdom** — each a
complete game at its scale and a component of the one above. The same object model describes all of
them; only the content differs.

> **Entities are not the only objects.** A **PACKET** is an object too, and so is a **Relationship**
> (§5). "Entity" names the things that *act*; the rest of this file names the things that *describe,
> resolve, or connect* them.

---

## 2. The four layers — where an object lives

Every object in CUS lives across four layers. This is the corpus's separation of concerns; it is
what stops rules from bleeding into one another. If you think in code, the analogy is exact:

| Layer | Holds | Runtime state? | Code analogy |
|---|---|---|---|
| **Definition** | The static, referenced description — a figure profile, a PACKET, a Formation, a Base spec. | **Never** | the class / the schema |
| **Procedure** | The one owned method that resolves a Statement — movement, the strike, the Counter, an aftermath roll. | No | the method |
| **Instance** | What is true **right now** — current Position, `wounds_remaining`, an armed WAIT, triggers already fired. | **Only here** | the heap object |
| **Presentation** | What the player sees and touches — the model, the card, the base, tokens, colour + shape. It **translates** the Kernel; it never forks a mechanic. | No (mirrors the Instance) | the rendered view |

Two laws fall directly out of this table and are load-bearing everywhere:

- **No state in Definitions.** A Definition is the same at the end of a battle as at the start. A PACKET holds no per-use result; a card holds no wound total. The `spearman` profile in [04_COMBAT.md](04_COMBAT.md) is a Definition — every `spearman` on the table shares it.
- **Runtime state lives only in the Instance.** When the `spearman` takes a Wound, `wounds_remaining` drops **on that figure's Instance** — never on the shared Definition, never (authoritatively) on the card.

Presentation is a *mirror*, not a *source*. The base shows facing; a token beside the model shows a
Wound; the card shows capability. If the mirror and the Instance ever disagree, the Instance is
right — Presentation may only display what some layer already owns.

---

## 3. Ownership — one fact, one owner

**Every fact has exactly one authoritative owner. No layer keeps a second authoritative copy of
another's information.** This is the single most important rule in the object model, because every
contradiction the corpus has ever suffered was two places claiming the same fact.

Ownership answers two questions for every fact:

1. **Which layer owns it?** `wounds_remaining` is owned by the **Instance**. The list of grades a
   packet can produce is owned by its **Definition**. Whether a strike may draw a Counter is owned
   by the **striking packet** (its `provokes` field), not by the defender.
2. **Where does it physically live at the table?** This is Presentation's assignment, and it must be
   singular. Slice 1's example: a felled **Champion**'s wounds live on **tokens beside the model** —
   *not* written on the Champion's card, because the card is a Definition and Definitions hold no
   state. One fact, one home.

When you add any new mechanic, the first question is always: *what single thing owns this?* If the
answer is "two things," the mechanic is wrong, not clever.

---

## 4. Reference — defined once, pointed to everywhere

Objects are **referenced, not copied.** A PACKET is defined one time and referred to by every card,
figure, and procedure that uses it. Nothing is transcribed onto each card, because a copy is a
second owner waiting to drift out of sync (see §3).

Two rules make referencing safe:

- **Neutral identity.** An object's primary ID never encodes what *kind* of thing it is. `spear_thrust` is just a name; it does not say "melee" or "attack." Kind, tool, tags, and targeting live in a **separate sidecar registry** (`packet_index`), which is additive — an object with no index entry is still valid; the index only aids retrieval, never resolution.
- **One-way references.** A card references a packet; the packet does not know which cards hold it. References point from the specific to the general (figure → packet → primitive), which is also the build order in [03_GRAMMAR.md](03_GRAMMAR.md) and beyond.

This is why the corpus can add a hundred weapons without touching the grammar: each is a new
Definition that *references* the same PACKET machinery.

---

## 5. Relationship — the fourth kind of object

Some facts are not owned by any single entity because they live **between** two of them. A
**Relationship** is a first-class object: an edge connecting agents, holding its own state.

The design razor names five things a mechanic may read or write: *Position, Force, State, a
Resource,* **or a relationship between agents.** The first four are covered by the primitives; the
fifth is why Relationship is part of the object model rather than an afterthought.

- Slice 1 uses no persistent relationships — a melee exchange is resolved and gone. But it already
  shows the *shape*: "A is **engaged** to B" is a transient relationship (a symmetric edge that both
  figures read), and "B may **Counter** A" is a directed one the striking packet authors.
- Later slices make relationships persist and accrue: a **Bond**, a **grudge**, an **oath**, a
  reputation. Those are the raw material of the Story module — and because Relationship is an object
  here, Story adds *content*, not a parallel mechanic.

A Relationship obeys the same object model as everything else: it has a Definition (what kind of
edge), an Instance (its current state), and — where the table needs to see it — a Presentation.

---

## Summary — the object model in one breath

> The world is made of **Entities** that own capability and hold **State**, standing at a
> **Position**, connected by **Relationships**. Every object lives across four **layers** —
> Definition, Procedure, Instance, Presentation — with runtime state only ever in the Instance.
> Every fact has **one owner**. Objects are **referenced, never copied**, under neutral IDs.

Hold that, and the grammar next is just: *how one capability is written down and resolved.*

*Next: [03_GRAMMAR.md](03_GRAMMAR.md) — the PACKET, resolution, and the three verbs.*
