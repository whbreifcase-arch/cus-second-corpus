# Interface · The Frame — FrameSpec & physical housing

"Frame" names **one design at two resolutions.** They are the same architecture; they are not two
authorities. Neither is a new root Object ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md) — the roots are
Entity, Packet, Relationship); a Frame is authoring/interface tooling.

## FrameSpec — the digital resolution
The **authoring schema** for a functional cell (`Role × Tool`, [../composition/02_ARCHETYPE.md](../composition/02_ARCHETYPE.md)).
It is *non-operative tooling data* — the engine never resolves it; it only **guides and validates
construction**:

- a **socket contract** — required sockets (a primary capability, a role-appropriate capability) and optional sockets (reposition, a WAIT-response, resource, support);
- **capacity** — how many packets, of which kinds, may be fitted;
- **compatibility** — which Packet Tool/category each socket accepts;
- **Signature + Tempo** declaration slots.

Its job is to let a player **build a soldier** — insert existing Packets, or author compatible new
ones — without assembling unconstrained JSON, and to **validate** the result (references exist,
capacity legal, sockets filled, Tool compatible). It **never infers** identity ([CON-0023]).

## Physical Frame — the material resolution
The **printed housing / sleeve / tray** that receives a Figure's components and is the *material
Presentation of the FrameSpec*:

- **keyed slots** that accept Packet cards (and reject the wrong kind — see [03_GEOMETRY.md](03_GEOMETRY.md));
- **windows / masks** exposing only the fields needed in play (cost, dice, range, conditions, effect) and covering Kernel detail until wanted;
- **capacity** enforced by the number of physical slots;
- **orientation** enforced by a notch, so nothing goes in backwards;
- Role · Tool · Signature · Tempo communicated by geometry, icons, and placement;
- a completed Frame that is **readable at a glance** and **communicates the Archetype** — which it *shows*, never *stores*.

## Same design, two resolutions
```
FrameSpec (digital)        →  socket contract · capacity · compatibility · validation   (authoring/tooling)
Physical Frame (material)  →  housing · keyed slots · windows · notch                    (Presentation of the FrameSpec)
```
If the physical Frame and the FrameSpec ever disagree, the **FrameSpec is authoritative** and the
component is corrected — the plastic mirrors the schema, never the reverse.

*See also: [02_PACKET_CARDS.md](02_PACKET_CARDS.md) · [03_GEOMETRY.md](03_GEOMETRY.md).*
