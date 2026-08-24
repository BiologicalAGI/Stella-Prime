# Stella Luanti V0.2 — External Evidence Ledger

Date: 2026-08-23
Status: **CURRENT RESEARCH SNAPSHOT — NOT TIMELESS TRUTH**

This ledger records external evidence used to pressure-test the Stella Luanti V0.2 blueprint. Reverify time-sensitive claims before implementation.

## E-001 — Luanti 5.17.0 release

Source: Luanti changelog / GitHub release / Luanti release blog  
Observed: 5.17.0 released 2026-08-20; release warns of security vulnerabilities affecting client and server and recommends upgrade.  
Confidence: HIGH.

Relevant changes:
- multi-track glTF animations
- several independently controllable animation tracks
- named animation track support through the new animation interface
- basic gamepad support for in-game actions (not formspecs)
- formspec interaction fixes
- HUD `hideable` field
- `hypertip` rich tooltips

Implication: V0.2 can target 5.17+ for Mara embodiment, but formspec interaction still needs keyboard/gamepad/accessibility testing because gamepad support explicitly does not cover formspecs.

Sources:
- https://docs.luanti.org/about/changelog/
- https://blog.luanti.org/2026/08/21/5.17.0-released/
- https://github.com/luanti-org/luanti/releases

## E-002 — glTF animation interface

Source: Luanti API class reference  
Observed: new interface is intended for glTF, supports mixing/matching separate named tracks, and is properly supported by 5.17+ clients.  
Confidence: HIGH.

Implication: Mara can have independent idle/walk/gesture/talk tracks without baking every combination into one timeline. This strengthens Luanti as the V0.2 embodiment target.

Source:
- https://api.luanti.org/class-reference/

## E-003 — Luanti glTF model support

Source: Luanti creator model documentation  
Observed: glTF/GLB is the recommended modern animated model path; clients 5.10+ support glTF; documentation notes limitations and recommends validation.  
Confidence: HIGH.

Implication: asset pipeline should preserve source model plus validator receipt; test exact skinning/animation compatibility before approving a Mara asset.

Source:
- https://docs.luanti.org/for-creators/models/

## E-004 — Forms/UI

Source: Luanti NodeMetaData/formspec docs + Flow ContentDB listing  
Observed:
- Luanti supports formspecs and dynamic server-driven forms through `core.show_formspec()`.
- Flow is a formspec layout/API replacement that automatically positions/sizes elements.
- Flow has a relationship/dependency with `formspec_ast` that must be included in dependency review.
Confidence: HIGH for capability; MEDIUM for dependency decision until exact current release/license/transitive behavior is inspected at implementation gate.

Implication: execute a native-formspec vs Flow A/B prototype rather than selecting Flow by assumption.

Sources:
- https://docs.luanti.org/for-creators/api/classes/nodemetadata/
- https://content.luanti.org/packages/luk3yx/flow/

## E-005 — Critical information should not be chat-only

Source: Luanti controls documentation  
Observed: player can hide/show chat with F2.  
Confidence: HIGH.

Implication: objective/recovery/critical causal feedback cannot exist solely in chat.

Source:
- https://docs.luanti.org/for-players/controls/

## E-006 — Native HTTP boundary

Source: Luanti HTTP API documentation  
Observed: HTTP use requires a mod to be listed in `secure.trusted_mods` or `secure.http_mods`.  
Confidence: HIGH.

Implication: network access can remain explicit and default-off. A future companion model adapter should be a narrow named gateway and should not expose the HTTP API table broadly.

Source:
- https://docs.luanti.org/for-creators/api/http-api/

## E-007 — Mod security

Source: Luanti installing-mods security guidance  
Observed: mods normally execute in a restricted environment; trusted mods or disabled mod security run with broader privileges; official guidance recommends caution.  
Confidence: HIGH.

Implication: no casual `secure.trusted_mods`, no blanket security disable, and no assumption that a popular mod is safe enough for a privileged bridge.

Source:
- https://docs.luanti.org/for-players/installing-mods/

## E-008 — Miney

Source: ContentDB listing  
Observed: Miney connects Python to Luanti using the Luanti protocol and exposes a Pythonic interface to server/player/block concepts. Current listing/release activity demonstrates an actively usable bridge pattern.  
Confidence: HIGH for feasibility; implementation/security details require direct source review before any adoption.

Implication: strong prior art for a Python-side embodiment/observer bridge, but raw Miney should not be the language model tool surface.

Source:
- https://content.luanti.org/packages/Miney/miney/

## E-009 — LLM Connect

Source: ContentDB listing/releases  
Observed: LLM Connect connects Luanti with OpenAI-compatible model endpoints and has evolved into a broader AI-assisted development/agent environment.  
Confidence: HIGH for feasibility evidence.

Implication: model integration inside/alongside Luanti is feasible. Stella should still implement a narrower proposal gateway rather than adopt a broad agent surface as authority.

Source:
- https://content.luanti.org/packages/H5N3RG/llm_connect/

## E-010 — Existing dialogue/NPC patterns

Sources: Yourland Speak Up; Simple Dialogs  
Observed: mature Luanti ecosystem examples exist for NPC speech and conversation trees.  
Confidence: HIGH as prior art.

Implication: study data-model/editor patterns and failure modes; do not transplant wholesale before checking ownership and license fit.

Sources:
- https://content.luanti.org/packages/Sokomine/yl_speak_up/
- https://content.luanti.org/packages/Kilarin/simple_dialogs/

## E-011 — Authored adventure references

Sources: The Library; Piranesi Restoration Project  
Observed: Luanti can support authored exploration/puzzle/story experiences distinct from survival sandbox conventions.  
Confidence: HIGH.

Implication: the V0.2 goal of a compact memorable meadow/stream/coast authored loop is engine-compatible. Use these as UX/structural references, not asset sources by default.

Sources:
- https://content.luanti.org/packages/regulus/regulus_mtgj2024/
- https://content.luanti.org/packages/Warr1024/piranesi_redo/

## E-012 — ContentDB AI/license disclosure

Source: ContentDB package inclusion policy/copyright guidance  
Observed: AI-generated content is allowed but must be disclosed when significant; package/media licensing and attribution matter for publication.  
Confidence: HIGH.

Implication: maintain third-party/AI provenance from the beginning instead of reconstructing it later.

Sources:
- https://content.luanti.org/policy_and_guidance/
- https://content.luanti.org/help/copyright/

## E-013 — Luanti hardcoded UI constraints

Source: Luanti hardcoded-features documentation  
Observed: some chat/status/form styling/control behavior remains engine-hardcoded or incompletely customizable.  
Confidence: HIGH.

Implication: accessibility targets must be tested against actual engine limitations. Do not promise fully custom spatial UI or input behavior before proving it.

Source:
- https://docs.luanti.org/for-creators/list-of-hardcoded-features/

## E-014 — Godot current state

Source: Godot official release pages  
Observed: Godot 4.7.2 stable released 2026-08-18 as a maintenance release.  
Confidence: HIGH.

Implication: Godot remains a healthy later adapter candidate. Nothing in the current evidence creates a V0.2 migration requirement.

Sources:
- https://godotengine.org/article/maintenance-release-godot-4-7-2/
- https://godotengine.org/download/archive/4.7.2-stable/

## Evidence-derived architecture conclusions

### Strongly supported
- stay with Luanti for the V0.2 vertical slices
- require 5.17+ if using the new named/multi-track animation interface
- keep critical play feedback outside chat-only channels
- keep network access explicit and permission-gated
- separate model proposals from deterministic execution
- treat third-party provenance as a build gate
- prototype UI choices instead of assuming a framework

### Not yet proven
- Flow is better than native formspecs for this exact UI
- a selected Mara model will animate correctly on the target machine
- Miney is the best companion transport
- any local model meets latency/context/privacy goals
- the current iBUYPOWER Luanti install is actually 5.17.0
- V0.1 local receipts/hashes remain unchanged
- pathfinding alone will produce acceptable companion motion/game feel
- Sanctuary requirements can be met cleanly in Luanti

## Reverification triggers

Recheck this ledger when:
- more than 30 days have passed
- Luanti 5.18 releases
- a dependency is selected for actual installation
- a model bridge is authorized
- Godot migration becomes an active decision
- ContentDB publication begins
- a third-party asset is promoted into the build
