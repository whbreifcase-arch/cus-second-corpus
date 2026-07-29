# Slice 2 · The Circle

Slice 1 used one Entity kind — the **Square**, the rank-and-file figure with a facing and 2 AP. The
**Circle** is the other kind: the exceptional figure — a hero, champion, or leader. It is a new
**Entity** in the object model ([Slice 1 · 02_WORLD](../slice-1/02_WORLD.md)), and it plays by three
rules the Square does not.

```
SQUARE   2 AP   has a facing   may be flanked   tests Nerve, breaks by the Mind track   moves in formation
CIRCLE   3 AP   faceless        never flanked    never tests Nerve, breaks by a trigger   never in formation
```

## Three AP

A Circle has **3 AP** to a Square's 2. *[Ruling 2 — the base shape is the tell; no extra component.]*
More agency is the whole mechanical meaning of "exceptional": a Circle does more per activation.
Exceptions to 2/3 exist only as a named field, never prose (Slice 1 · Law 15).

## Faceless

A Circle has **no facing**. It answers threats from **every** direction and **cannot be flanked**.
Concretely, against the Counter rules from [Slice 1 · 04_COMBAT](../slice-1/04_COMBAT.md):

- a Square concedes its flanks — strike it from the side and it cannot Counter;
- a **Circle has no flanks** — struck from any side, it may still Counter (contact and authoring
  permitting).

Facing is Position, and the Circle simply has a different Position relationship: it is omnidirectional.
Nothing else in the Counter procedure changes — the Circle is just an Entity whose facing field is
"none."

## It breaks by a trigger, never by dice

This is the load-bearing rule. **A Circle never takes shock, never rolls Nerve, and never touches the
Steady→Shaken→Broken track.** It has **its own break meter**, and that meter is a **Written Trigger**,
not a save. *[Ruling 10 / CON-0010: Circles break on their own meter, by a prewritten trigger, not
by dice.]*

- A Circle carries a **break clause** on its **Definition** — an authored condition that, when it
  fires, breaks the Circle: *"breaks if its Banner is destroyed," "breaks if its sworn rival falls,"
  "breaks when the last of its Retinue is slain."* The content is per-character; the *mechanism* is
  the same Written Trigger invocation that powers the Counter and Shock ([Slice 1 · 03_GRAMMAR](../slice-1/03_GRAMMAR.md)).
- Until its clause fires, a Circle is **immune to Morale entirely** — a hero does not waver because
  the line around it wavers. When the clause fires, the Circle breaks outright (it Routs, or does
  whatever its clause states).

Object-model note: the Circle's break condition is owned at *(the Circle Entity, Definition)* — it is
authored once, per hero, and read by the engine. It is not a hidden special case; it is a field, and
a determined reader can see exactly what breaks this Circle.

> Why this shape? A dice-driven morale track models a *crowd* — many small wills averaging out. A
> hero is not a crowd; a hero breaks for a *reason*, at a *moment*, authored in advance. Modelling
> that as a trigger rather than a roll is the difference between a statistic and a story beat.

## It does not move in formation

A Circle is **never carried by formation movement**. *[Ruling 13.]* When a unit of Squares performs a
group MOVE ([03_THE_GROUP.md](03_THE_GROUP.md)), any attached Circle is left to move on **its own
Agency** — it is not swept along. A hero chooses its ground; it is not dressed into a rank.

## The Circle usually leads

Mechanically a Circle is defined by the three rules above. In play it is also, usually, the **leader**
— the Entity that can **Rally** a wavering unit. That is a Procedure, not a property of the shape, so
it lives with the group rules.

*Next: [03_THE_GROUP.md](03_THE_GROUP.md) — the formation, the leader, Rout and Rally.*
