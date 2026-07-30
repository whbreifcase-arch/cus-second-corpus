# CUS — Living Glossary

> _Generated from [`_model/glossary.tsv`](_model/glossary.tsv) + [`_model/model.tsv`](_model/model.tsv) by `_model/check.py`. Do not edit by hand — run `python3 _model/check.py --write`._

The canonical vocabulary and how it relates. Two kinds of drift are guarded automatically: **dead words** (*Retired vocabulary*) and **dead claims** (*Retired claims*). Each entry cites the ruling behind it.

## Live vocabulary

| Term | Meaning | Ruling |
|---|---|---|
| [Object](slice-1/02_WORLD.md) | The root noun; everything is an Object on three axes (Ontology/Layer/Ownership). | — |
| [Entity](slice-1/02_WORLD.md) | An Ontology kind of Object — a unit that acts and persists; holds its facts across the four Layers. | — |
| [Relationship](slice-1/02_WORLD.md) | A first-class Object holding facts *between* Entities (an engaged edge, a grudge's heat); its runtime truth lives in its Instance facet. | — |
| [Definition](slice-1/02_WORLD.md) | A Layer: the static, shared, referenced description (the class/schema). Holds no runtime state. | — |
| [Instance](slice-1/02_WORLD.md) | A Layer: what is true right now (Position, wounds_remaining, fired triggers). Runtime State lives only here. | — |
| [Procedure](slice-1/02_WORLD.md) | A Layer: the one owned method that resolves a Statement. | — |
| [Presentation](slice-1/02_WORLD.md) | A Layer: what the player sees and touches (model, card, base, tokens). A mirror, never a source. | — |
| [State](slice-1/02_WORLD.md) | What is true now, owned at exactly one Instance cell. | — |
| [Transition](slice-1/02_WORLD.md) | The named moment a State changes; emitted by the Procedure that owns that State. | — |
| [Trigger](slice-1/02_WORLD.md) | A clause on a Definition that watches for a named Transition (a Written Trigger). | — |
| [Invocation](slice-1/02_WORLD.md) | A watched Transition firing a PACKET through a Trigger. | — |
| [Agency](slice-1/01_PRIMITIVES.md) | Renewing Resource (AP) — refills every activation; the only pool a figure spends to act, on its own activation. | — |
| [Reserve](slice-1/01_PRIMITIVES.md) | Finite Resource — spend -> empty -> restore. Renamed from the old 'Charge' Resource so the name no longer collides with the Charge invariant. Skins: ammo, arrows, fuel, spell uses... | PROVISIONAL |
| [Strain](slice-1/01_PRIMITIVES.md) | Accumulating Resource — rises with use; vents or punishes. | — |
| [Packet](slice-1/03_GRAMMAR.md) | The unit of action in the grammar (PACKET). | — |
| [Grade](slice-1/03_GRAMMAR.md) | How well a roll succeeded — the graded outcome (the Success Grade; replaces the retired Ladder/Rungs). | First-Corpus D |
| [Effect](slice-1/03_GRAMMAR.md) | What resolving a Grade changes — a Wound, a Push, Guard. Writes State or Position, nothing else. | — |
| [Push](slice-1/04_COMBAT.md) | The one displacement Effect (replaces the retired 'Shove'). | CON-0012 |
| [Figure](composition/03_UNIT_PROFILE.md) | The Entity for a unit, existing across all four Layers: shared authored capability is its Figure Definition; the specific persistent person (wounds, history, State) is its Figure Instance. You author the Definition; Presentation renders the Archetype. | CON-0023 |
| [Archetype](composition/02_ARCHETYPE.md) | The rendered identity label — a Presentation view, never authored/stored/resolved. | CON-0023 |
| [FrameSpec](composition/02_ARCHETYPE.md) | The Role x Tool socket schema — the *functional* frame Signature specializes. Owns no fact. | CON-0023 |
| [Frame](interface/01_FRAME.md) | The *physical* face — FrameSpec plus the physical Frame housing. Not a layer or root Object. (The functional frame Signature specializes is the Role x Tool cell — see FrameSpec.) | CON-0023 |
| [Signature](composition/02_ARCHETYPE.md) | Specializes the functional frame into a decision loop; does not resolve it. A Signature carries a recurring causal invariant (see 04_SIGNATURE_INVARIANTS). | CON-0023 |
| [Tempo](composition/02_ARCHETYPE.md) | Cadence of the decision loop, not movement speed. | CON-0022 |
| [Role](composition/01_AXES.md) | Pressure / Anchor / Utility. | — |
| [Tool](composition/01_AXES.md) | Melee / Ranged / Hybrid. | — |
| [Charge](composition/04_SIGNATURE_INVARIANTS.md) | Signature invariant: accumulate potential, then release it as a discrete burst (ACCUMULATE->HOLD->RELEASE->RESET). Not the finite Resource (that is Reserve), not lowercase 'charge' (a run-up). | PROVISIONAL |
| [Channel](composition/04_SIGNATURE_INVARIANTS.md) | Signature invariant: continuously apply an effect while remaining committed (BEGIN->MAINTAIN->END/INTERRUPT). Absorbs the retired 'Sustain'. | PROVISIONAL |
| [Cycle](composition/04_SIGNATURE_INVARIANTS.md) | Signature invariant: alternate productive and recovery states as capability periodically exhausts (READY->SPEND Reserve->EMPTY->RESTORE). | PROVISIONAL |
| [Morale](slice-2/01_MIND_CHANNEL.md) | The Mind channel's incoming pressure. | — |
| [Nerve](slice-2/01_MIND_CHANNEL.md) | A tiered SAVE rolled per incoming Morale point. | CON-0001;CON-0011 |
| [Circle](slice-2/02_THE_CIRCLE.md) | Breaks like a Square via the Mind channel; differs by +Agency / faceless / no formation. | CON-0010 |
| [Square](slice-2/02_THE_CIRCLE.md) | The rank-and-file figure with Morale/Nerve. | — |
| [Formation](slice-2/03_THE_GROUP.md) | A coherency relationship; Form Up is a MOVE that ends in it. | — |
| [Persistence](slice-3/00_PERSISTENCE.md) | Temporal scope on State. | — |
| [Aftermath](slice-3/00_PERSISTENCE.md) | The boundary Procedure that records durable State. | — |
| [Scar](slice-3/01_HARM_LIFECYCLE.md) | Figure Instance State (Wounds->Injury->Scar; Mind Scar); not an Overlay. | CON-0023 |
| [Book](interface/04_BOOK_AND_CARAVAN.md) | Personal container; membership is a Relationship, Book->Figure Instance. | — |
| [Caravan](interface/04_BOOK_AND_CARAVAN.md) | Shared container; carries Books, not the roster directly. | CON-0023 |

## How the vocabulary relates (canonical)

| Subject | relation | Object | Ruling |
|---|---|---|---|
| Author | authors | Figure Definition | CON-0023 |
| Presentation | renders | Archetype | CON-0023 |
| FrameSpec | socketsFrom | Role x Tool | CON-0023 |
| Signature | specializes | FrameSpec (functional frame) | CON-0023 |
| Tempo | paces | Figure | CON-0022 |
| Figure Definition | owns | role/tool | CON-0023 |
| Caravan | carries | Book | CON-0023 |
| Book | hasMember | Figure Instance | CON-0023 |
| Scar | isStateOf | Figure Instance | CON-0023 |
| Nerve | savesAgainst | Morale | CON-0001;CON-0011 |
| AP | scalesWith | Rank | CON-0002 |
| Packet | hasTool | Melee/Ranged/Hybrid | CON-0023 |
| Object | standsOn | Ontology/Layer/Ownership | Slice-1 02_WORLD |
| PacketCard | presents | both faces | CON-0023 |
| Charge | accumulatesThenReleases | a discrete burst | PROVISIONAL |
| Channel | continuouslyApplies | while committed | PROVISIONAL |
| Cycle | alternates | use and restoration | PROVISIONAL |
| Reserve | isA | finite Resource | PROVISIONAL |

## Retired vocabulary — use the live term instead

| Retired | Use instead | Ruling | id |
|---|---|---|---|
| Shove | Push | CON-0012 | `shove` |
| Ladder | Grade | First-Corpus D | `grade-ladder` |
| Rungs | Grade | First-Corpus D | `grade-ladder` |
| Outcome Track | Grade | First-Corpus D | `grade-ladder` |
| Nerve test | Morale check / tiered Nerve save | CON-0001;CON-0011 | `nerve-check` |
| Nerve roll | Morale check / tiered Nerve save | CON-0001;CON-0011 | `nerve-check` |
| Nerve check | Morale check / tiered Nerve save | CON-0001;CON-0011 | `nerve-check` |
| MOVE-class | a MOVE (one of the three verbs) | Slice-1 03_GRAMMAR | `move-class` |
| one-way ratchet | Mind steps down on unsaved Morale; Rally steps up | Slice-2 01_MIND_CHANNEL | `one-way-ratchet` |
| Sustain | Channel | PROVISIONAL | `sustain` |

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
| Charge isA (finite) Resource | The finite Resource is 'Reserve', not 'Charge'; capital Charge is a Signature invariant. | PROVISIONAL | `charge-resource` |

