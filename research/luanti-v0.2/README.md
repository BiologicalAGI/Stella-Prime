# Stella World — Luanti V0.2 Research Index

Status: **RESEARCH / DESIGN — NON-CANONICAL**  
Branch: `research/luanti-v0.2-build-contract-2026-08-23`  
Research date: 2026-08-23  
Machine mutation represented by this branch: **none**  
SCOS mutation represented by this branch: **none**

## Purpose

This branch preserves the research and design synthesis for a possible Stella Playground V0.2 without promoting it into canonical Stella state or treating renderer capability as world authority.

The central design question is not whether Luanti can hold persistent state. V0.1 already supplied evidence that the experimental body can carry the causal/epistemic proof. The V0.2 question is whether that proof can become a coherent, accessible authored experience while preserving the distinctions between observation, report, knowledge, route knowledge, physical path execution, presentation, companion proposals, and world authority.

## Governing design law

> If normal play requires the player to know an implementation detail, the interface is wrong.

Normal play must therefore avoid exact slash commands, coordinates, hidden interaction conventions, required command spelling, color-only cues, and critical chat-only feedback.

## Current decisions

1. **Keep Luanti for V0.2.** Godot remains a future renderer/adapter candidate rather than a replacement for the causal core.
2. **Target Luanti 5.17.0+ for the V0.2 experiment.** The August 20, 2026 release adds independently controllable multi-track glTF animations and named animation tracks, alongside formspec and HUD improvements and security fixes.
3. **Preserve renderer independence.** The world kernel and its state/event semantics must remain engine-neutral enough to support a later Godot adapter.
4. **Do not make Mara an LLM.** Mara remains an inhabitant with bounded causal history and knowledge.
5. **Do not give a language model raw Luanti/Miney/Lua authority.** A companion language layer may only produce typed proposals through a policy/authority gateway.
6. **Default network mode OFF.** Any local or remote model bridge must receive an explicit, bounded context packet and explicit HTTP/network configuration.
7. **Surprise may conceal content, never authority.** Presentation-only surprises and authored discoveries are separate from causal world events.
8. **Dependency adoption is conservative.** Prefer small native Stella components; use external dependencies only when their maintenance, license, API surface, isolation, and removal path are understood.
9. **Licensing is first-class.** Every imported media/code asset must have source, author, license, modification status, purpose, hash where practical, and review status.
10. **Accessibility/recovery is architectural.** `What do I do next?`, re-entry recap, visible interaction affordances, adjustable guidance, and redundant cues are part of the experience layer, not optional polish.

## Research artifacts

- `V0_2_BUILD_CONTRACT_V0_1.md` — ownership boundaries, invariants, state/event vocabulary, player-facing states, companion contract, proof ladder, acceptance criteria.
- `EVIDENCE_LEDGER_2026-08-23.md` — current external evidence and confidence notes.
- `DECISION_RECORD_2026-08-23.md` — what changed, what survived pressure testing, what remains unresolved.

## Hard separation rules

```text
RENDERER CAPABILITY != CHARACTER KNOWLEDGE
PATH EXISTS != ROUTE KNOWN
BUTTON EXISTS != FACT TRUE
REPORT RECEIVED != DIRECT OBSERVATION
MODEL TEXT != WORLD AUTHORITY
PRESENTATION REACTION != CAUSAL EVENT
PRIVATE CONTEXT != PUBLIC WORLD HISTORY
EXTERNAL DEPENDENCY != ARCHITECTURAL OWNER
```

## Next implementation gate

The first machine-side V0.2 mutation should remain an isolated shell/prototype, not a canonical Stella promotion. Before that mutation, reverify the local Luanti version, V0.1 evidence/receipts/hashes, playground paths, protected files, and current machine state. This branch is research evidence, not machine-state evidence.