# Stella Luanti V0.2 — Decision Record

Date: 2026-08-23
Status: **RESEARCH DECISIONS — NOT CANONICAL PROMOTION**

## D-001 — Engine

Decision: **Use Luanti for the V0.2 experimental body.**

Reason:
- V0.1 already demonstrated persistence/causal-state viability.
- 5.17 materially improves the exact embodiment area that was weak in V0.1: multi-track glTF animation and UI/HUD behavior.
- switching to Godot now would reset renderer work before the route/knowledge/interaction contracts are proven.

Exit condition:
Reconsider Godot when renderer-specific constraints become dominant: advanced facial/character animation, custom camera/cutscene needs, complex spatial UI, VR/haptics, or Sanctuary presentation that Luanti cannot support cleanly.

## D-002 — V0.1

Decision: **Close V0.1 as evidence; do not keep feature-patching it.**

Preserve:
- Gate direct observation proof
- persistence/event-ledger proof
- Mara report-vs-direct-knowledge distinction
- Luanti adapter feasibility
- repair/playtest receipts and hashes

Carry forward as negative requirements:
- no required slash commands
- no coordinates for normal navigation
- no hidden/pixel-hunt Mara interaction
- no critical chat-only feedback
- no monolithic ownership of state/UI/debugging

## D-003 — Mara

Decision: **Mara is not the companion and is not converted into an LLM.**

Reason:
The strongest Stella property is actor-specific causal/epistemic history. A generic model persona would erase the experiment rather than deepen it.

## D-004 — Companion

Decision: **Embodiment before language model.**

Order:
1. C0 observer
2. C1 deterministic follow/wait/point/lead
3. C2 conversational projection
4. C3 bounded model adapter
5. C4 selected continuity
6. C5 Sanctuary-capable context

Reason:
This lets us prove world-action semantics without attributing failures to stochastic language generation.

## D-005 — Tool authority

Decision: **No raw Miney/Lua/Python/HTTP surface for a language model.**

Model output is a proposal. Policy and deterministic executors own action authority. Every result is receipted.

## D-006 — Navigation

Decision: **Separate semantic route knowledge from geometric pathfinding.**

`core.find_path()` may compute a walkable physical path only after the actor possesses a legitimate route/journey basis. Renderer computation cannot silently manufacture character knowledge.

## D-007 — UI

Decision: **A/B native formspec vs Flow.**

Do not select Flow merely because it is attractive. Prototype the exact Mara/recovery UI in both approaches and compare readability, resizing, state handling, accessibility, dependency cost, maintenance, and testability.

## D-008 — Accessibility

Decision: **Recognition/recovery is a core system boundary.**

Required:
- persistent recovery operation (`What do I do next?`)
- adjustable guidance
- re-entry recap
- visible interaction target and prompt
- no exact spelling for normal play
- no color-only critical meaning
- no chat-only critical information
- minimal first layer with optional detail

## D-009 — World scale

Decision: **Keep V0.2 small and authored.**

Target topology:
- meadow
- cottage / rose garden / old willow
- stream / Mara / crossing
- coast / overlook / Tide Gate

Reason:
A compact topology is better for polish, accessibility, route semantics, and causal testability than procedurally infinite content at this phase.

## D-010 — Atmosphere

Decision: **Atmosphere is stateful presentation, not causal authority.**

Sound, light, particles, vegetation, music, and Gate reactions may respond to state without becoming evidence of world facts, intent, knowledge, or permission.

## D-011 — Surprise

Decision: **Govern surprises by authority class.**

Allowed first:
- presentation-only
- preauthored discoveries
- social expression

Separately gated:
- causal world events
- private Sanctuary changes

Rule: conceal content if desired; never conceal consequential authority or user choice.

## D-012 — Network/privacy

Decision: **Default network OFF.**

Later modes may include `LOCAL_ONLY` or an explicitly selected remote provider. Any model call receives a deliberately constructed context packet rather than the whole conversation/world/database by default.

## D-013 — Licensing/provenance

Decision: **No mystery assets.**

Every incorporated external/AI-generated item must be ledgered before build promotion.

## D-014 — GitHub continuity

Decision: **Preserve research on a non-main branch.**

Branch:
`research/luanti-v0.2-build-contract-2026-08-23`

Reason:
The available GitHub connector can create branches and files but does not expose repository creation. Branch isolation preserves research immediately without mixing the draft contract into `main`.

## Holds / unresolved questions

1. Reverify exact installed Luanti version on the iBUYPOWER before V2-01.
2. Reverify V0.1 receipt/hashes and protected files before any machine mutation.
3. Determine actual V0.2 target directory only from fresh machine evidence.
4. Run native formspec vs Flow A/B before dependency decision.
5. Select/validate a Mara glTF asset and its license/provenance.
6. Test keyboard/mouse/gamepad/accessibility behavior; 5.17 gamepad support does not cover formspecs.
7. Define the precise renderer-neutral serialization schema before any Godot adapter work.
8. Test pathfinding quality separately from route semantics.
9. Review Miney source/security/licensing before any local bridge experiment.
10. Do not begin remote-model networking until C0/C1 pass.

## Recommended next gate

**V2-00R — Fresh local V0.1 closure/reverification card**

Read-only goals:
- identify executable/version
- locate current playground/world/mod
- hash protected V0.1 evidence
- confirm no Luanti/server process relevant to the playground is left running
- identify a free isolated target for V0.2
- capture current dependency/install state

If PASS, request/consume a narrowly described machine mutation gate for **V2-01 isolated V0.2 shell**.

No canonical promotion should be bundled with V2-01.