# CUS — Second Corpus

**The rebuilt canonical architecture and implementation.** Authoritative for *current system
behavior*.

> **Status: REBUILD IN PROGRESS.** Rebuilt in deliberate vertical slices from Architecture Zero (in
> `cus-concordance`) and the signed rulings:
> - **[Vertical Slice 1](slice-1/README.md)** — the smallest closed loop: one figure acts, two oppose, a melee exchange with a Counter; the four primitives, the **object model** (Object · three axes), the PACKET grammar, the Body channel.
> - **[Vertical Slice 2](slice-2/README.md)** — a group acts and can break: the **Mind channel** (Morale · Nerve · Shaken/Broken), the **Circle**, the **Formation**, **Rout & Rally**, and the foundation **activation scheduler**.
> - **[Vertical Slice 3](slice-3/README.md)** — a battle makes history: **Persistence** as temporal *scope* on State, the **Aftermath** (Wounds → Injury → Scar, the Morale check → Mind Scar, death), the **Caravan**, and the **campaign loop**.
> - **[Composition layer](composition/README.md)** — how you *author* a figure: the four axes' values, and the **Archetype constructor** `Tempo(Signature(Role × Tool))`. **The Figure is authored; the Archetype is rendered.** (Definition-layer, not a gameplay slice.)
> - **[Interface layer](interface/README.md)** — the *physical* face: FrameSpec ⁄ physical Frame, two-sided Packet cards (both faces Presentation), the **Book** (personal) ⁄ **Caravan** (shared). Physical is Presentation + Position + containment — not a new layer.
> - **Slice 4** (next) — history deepens: recruitment, the map & travel, the Story module's Bonds accruing like Scars.
>
> The First Corpus's v0.6 files (A–N and the old HTML/Lua) are **not** carried in this tree — they
> live, frozen and authoritative, in
> [`cus-kernel-rebuild`](https://github.com/whbreifcase-arch/cus-kernel-rebuild) and in this repo's
> git history. The Second Corpus is rebuilt in dependency order from the master inventories, not by
> copying the First Corpus forward.

## Where things stand

| Repo | Role | This repo's relation |
|---|---|---|
| [`cus-kernel-rebuild`](https://github.com/whbreifcase-arch/cus-kernel-rebuild) | **First Corpus** — frozen source (archived, read-only) | fork parent (lineage) |
| [`cus-concordance`](https://github.com/whbreifcase-arch/cus-concordance) | **Concordance** — provenance, migration, protected-material custody | governs *why/how* things arrive here |
| **`cus-second-corpus`** (this repo) | **Second Corpus** — rebuilt canon | the destination |

## Authority
> Second Corpus governs present behavior. Concordance governs the explanation of migration.
> First Corpus governs claims about its own historical text. **No summary outranks its cited source.**

The rebuild has not started. When it does, it proceeds through the Concordance's charter, status
codes, and review gates — nothing enters this canon merely because it existed in the First Corpus.
