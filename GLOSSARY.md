# CUS — Living Glossary

> _Generated from [`_model/glossary.tsv`](_model/glossary.tsv) + [`_model/model.tsv`](_model/model.tsv) by `_model/check.py`. Do not edit by hand — run `python3 _model/check.py --write`._

The canonical vocabulary and how it relates. Two kinds of drift are guarded automatically: **dead words** (*Retired vocabulary*) and **dead claims** (*Retired claims*). Each entry cites the ruling behind it.

## Live vocabulary

| Term | Meaning | Ruling |
|---|---|---|
| [Object](slice-1/02_WORLD.md) | The root noun; everything is an Object on three axes (Ontology/Layer/Ownership). | — |
| [Figure](composition/03_UNIT_PROFILE.md) | The authored unit definition; you author the Figure, Presentation renders the Archetype. | CON-0023 |
| [Archetype](composition/02_ARCHETYPE.md) | The rendered identity label — a Presentation view, never authored/stored/resolved. | CON-0023 |
| [FrameSpec](composition/02_ARCHETYPE.md) | Role x Tool socket schema; owns no fact. | CON-0023 |
| [Frame](interface/01_FRAME.md) | The physical face (FrameSpec + physical Frame); not a layer or root Object. | CON-0023 |
| [Signature](composition/02_ARCHETYPE.md) | Specializes the Frame; does not resolve it. | CON-0023 |
| [Tempo](composition/02_ARCHETYPE.md) | Cadence of the decision loop, not movement speed. | CON-0022 |
| [Role](composition/01_AXES.md) | Pressure / Anchor / Utility. | — |
| [Tool](composition/01_AXES.md) | Melee / Ranged / Hybrid. | — |
| [Packet](slice-1/03_GRAMMAR.md) | The unit of action in the grammar (PACKET). | — |
| [Morale](slice-2/01_MIND_CHANNEL.md) | The Mind channel's incoming pressure. | — |
| [Nerve](slice-2/01_MIND_CHANNEL.md) | A tiered SAVE rolled per incoming Morale point. | CON-0001;CON-0011 |
| [Circle](slice-2/02_THE_CIRCLE.md) | Breaks like a Square via the Mind channel; differs by +Agency / faceless / no formation. | CON-0010 |
| [Square](slice-2/02_THE_CIRCLE.md) | The rank-and-file figure with Morale/Nerve. | — |
| [Formation](slice-2/03_THE_GROUP.md) | A coherency relationship; Form Up is a MOVE that ends in it. | — |
| [Persistence](slice-3/00_PERSISTENCE.md) | Temporal scope on State. | — |
| [Aftermath](slice-3/00_PERSISTENCE.md) | The boundary Procedure that records durable State. | — |
| [Scar](slice-3/01_HARM_LIFECYCLE.md) | Figure State (Wounds->Injury->Scar; Mind Scar); not an Overlay. | CON-0023 |
| [Book](interface/04_BOOK_AND_CARAVAN.md) | Personal container; membership Relationship Book->Figure. | — |
| [Caravan](interface/04_BOOK_AND_CARAVAN.md) | Shared container; carries Books, not the roster directly. | CON-0023 |
| [Push](slice-1/04_COMBAT.md) | The one displacement Effect (replaces the retired 'Shove'). | CON-0012 |

## How the vocabulary relates (canonical)

| Subject | relation | Object | Ruling |
|---|---|---|---|
| Author | authors | Figure | CON-0023 |
| Presentation | renders | Archetype | CON-0023 |
| FrameSpec | socketsFrom | Role x Tool | CON-0023 |
| Signature | specializes | Frame | CON-0023 |
| Tempo | paces | Figure | CON-0022 |
| Figure | owns | role/tool | CON-0023 |
| Caravan | carries | Book | CON-0023 |
| Book | contains | Figure | CON-0023 |
| Scar | isStateOf | Figure | CON-0023 |
| Nerve | savesAgainst | Morale | CON-0001;CON-0011 |
| AP | scalesWith | Rank | CON-0002 |
| Packet | hasTool | Melee/Ranged/Hybrid | CON-0023 |
| Object | standsOn | Ontology/Layer/Ownership | Slice-1 02_WORLD |
| PacketCard | presents | both faces | CON-0023 |

## Retired vocabulary — use the live term instead

| Retired | Use instead | Ruling | id |
|---|---|---|---|
| Shove | Push | CON-0012 | `shove` |
| Ladder | Success Grade | First-Corpus D | `grade-ladder` |
| Rungs | Success Grade | First-Corpus D | `grade-ladder` |
| Outcome Track | Success Grade | First-Corpus D | `grade-ladder` |
| Nerve test | Morale check / tiered Nerve save | CON-0001;CON-0011 | `nerve-check` |
| Nerve roll | Morale check / tiered Nerve save | CON-0001;CON-0011 | `nerve-check` |
| Nerve check | Morale check / tiered Nerve save | CON-0001;CON-0011 | `nerve-check` |
| MOVE-class | a MOVE (one of the three verbs) | Slice-1 03_GRAMMAR | `move-class` |
| one-way ratchet | Mind steps down on unsaved Morale; Rally steps up | Slice-2 01_MIND_CHANNEL | `one-way-ratchet` |

## Retired claims — statements the corpus has struck

| Struck claim | Correction | Ruling | id |
|---|---|---|---|
| Archetype is executable/operative/stored | Archetype is a rendered Presentation view — never operative/authored/stored. | CON-0023 | `archetype-operative` |
| (someone) authors/stores/resolves Archetype | You author the Figure; Presentation renders the Archetype (never authored/stored/resolved). | CON-0023 | `archetype-author` |
| Frame contains Archetype | Frame does not contain Archetypes; FrameSpec is a socket schema. | CON-0023 | `frame-hierarchy` |
| Frame isA layer/rootObject | Frame is a FrameSpec (schema) + physical Frame — not a layer or root Object. | CON-0023 | `frame-layer` |
| FrameSpec owns (a fact) | FrameSpec owns no fact; the Figure Definition owns role/tool. | CON-0023 | `framespec-owns` |
| Nerve resolvesAs 3-dice test | The 3-dice Nerve test is retired; Nerve is a tiered save. | CON-0001 | `nerve-3dice` |
| Reaction isA Resource | Reaction-as-Resource is struck; out-of-turn = free Written Triggers, capped by Position. | First-Corpus reaction-struck | `reaction-resource` |
| Reaction/Support isA PacketCategory | No Reaction/Support Packet category; Tools are Melee/Ranged/Hybrid. | CON-0023 | `reaction-category` |
| AP equals 3-for-all | AP is by Rank — Square 2, Circle 3; 'AP=3 for all' is struck drift. | CON-0002 | `universal-ap` |
| Circle immuneTo Morale | A Circle breaks like a Square via the Mind channel; resilience = high Nerve tier. | CON-0010 | `circle-immune` |
| Support/Control isA Role | Roles are Pressure/Anchor/Utility; Control/Support were merged into Utility. | First-Corpus A | `support-role` |
| Tempo isA speed | Tempo is the cadence of the decision loop, not movement. | CON-0022 | `tempo-speed` |
| PacketBack isA Definition | Both Packet-card faces are Presentation; the JSON in code is the Definition. | CON-0023 | `packet-back-def` |
| Caravan owns roster | Caravan carries Books; the roster is membership Relationships (Book->Figure, Caravan->Book). | CON-0023 | `caravan-roster` |

