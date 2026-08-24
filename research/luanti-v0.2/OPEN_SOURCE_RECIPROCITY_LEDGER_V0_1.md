# Stella Luanti V0.2 — Open Source Reciprocity Ledger V0.1

Status: **RESEARCH / RECIPROCITY PREPARATION / NO UPSTREAM POSTING AUTHORIZED BY THIS FILE**

## Purpose

Track what upstream projects make possible for Stella, what empirical value Stella may be able to return, and what boundaries must be respected before any public contribution.

This ledger is not a gratitude page and is not a queue of promised contributions. It is a reciprocity map: benefit received → evidence generated → possible return path → human review / upstream policy gate.

## Governing reciprocity rule

```text
USEFUL_DEPENDENCY_OR_PLATFORM
        ↓
UNDERSTAND WHAT IT GAVE US
        ↓
GENERATE REAL EVIDENCE WHILE USING IT
        ↓
CHECK WHETHER UPSTREAM ALREADY KNOWS
        ↓
RETURN ONLY NOVEL / REPRODUCIBLE / MAINTAINER-USEFUL VALUE
        ↓
FOLLOW UPSTREAM CONTRIBUTION AND AI POLICY
```

Do not create noise merely to demonstrate gratitude.

## Upstream: Luanti engine

What Stella receives:
- open-source voxel/world engine and modding environment;
- persistent world/runtime substrate for the V0.1 causal proof and planned V0.2 experience;
- current gamepad support for in-game actions;
- formspec/HUD APIs;
- glTF animated model support including 5.17 multi-track animation improvements;
- pathfinding and world APIs that can serve as renderer/executor capabilities without owning Stella semantics;
- a mature public issue tracker, documentation set, release process, security process, and contributor community.

Current relevant upstream evidence:
- Luanti roadmap identifies input handling/gamepad quality as a medium-term concern.
- Luanti roadmap identifies UI/formspec replacement as a medium-term concern.
- `luanti-org/luanti#4153` remains open and explicitly lists `Formspec support` as incomplete in the complete-gamepad-support effort.
- `luanti-org/luanti#12264` remains open and asks for an API exposing available/active input mechanisms so games/mods can adapt UI.
- Luanti 5.17 adds basic gamepad support for in-game actions but not formspecs.

Potential high-value return from Stella:
1. **Windows 11 + Luanti 5.17 input matrix** from an authored game rather than a synthetic menu-only test.
2. Exact controller identification, connection state, active mappings, and whether hot-plug/re-entry changes behavior.
3. Explicit separation of world-action success from formspec/dialogue navigation success.
4. Focus, cancel/escape, recovery, and re-entry observations for formspec dialogue.
5. Mouse/keyboard baseline results from the same build and state machine.
6. Evidence about whether a game can reliably infer or adapt to the player's current input mechanism using public APIs.
7. Minimal standalone repro fixture if a defect is reproducible outside Stella.
8. Before/after evidence if a future Luanti release changes the behavior.

Contribution threshold:
- `CANDIDATE` until V2-02/V2-04 produces fresh local evidence.
- `UPSTREAM_WORTHY` only if the observation is reproducible, current, not already adequately documented, and narrowed enough to help a maintainer.
- Public communication must be written/reviewed by the human contributor in compliance with Luanti's current AI policy.

## Upstream: Flow / formspec_ast

What Stella may receive:
- higher-level UI layout and less error-prone formspec construction.

Potential return:
- compatibility evidence against Luanti 5.17 on Windows;
- minimal reproductions of focus/layout/input problems discovered in the native-vs-Flow A/B test;
- documentation correction only if an actual discrepancy is verified.

Current status: `NOT_ADOPTED / A-B CANDIDATE`.

Do not file upstream feedback until Flow is actually tested.

## Upstream: Miney

What Stella receives now:
- architectural prior art demonstrating Python/Luanti bridging and external control possibilities.

Potential return:
- only actual reproducible compatibility/security/documentation findings discovered during a bounded lab test.

Current status: `PRIOR_ART / LAB_ONLY`.

Do not present Stella's policy boundary choices as Miney defects. A deliberately narrower Stella authority model is a design preference, not an upstream bug.

## Upstream: LLM Connect

What Stella receives now:
- feasibility evidence that Luanti can connect to OpenAI-compatible endpoints.

Potential return:
- actual endpoint compatibility/recovery findings only after C0/C1 and a separately authorized model/network experiment.

Current status: `FEASIBILITY_REFERENCE / NO NETWORK MODEL TEST`.

Do not confuse architectural disagreement with a defect report.

## Asset / media creators

What Stella may receive:
- Mara model, textures, music, sound, fonts, environmental media.

Mandatory return:
- license compliance;
- attribution where required;
- preservation of author/source/provenance;
- no removal of notices;
- no ambiguous ownership claims;
- no AI-generated replacement presented as the original creator's work.

A paid asset is not exempt from attribution/license obligations.

## Non-code ways to return value

Potential routes, subject to the user's choice and upstream rules:
- careful bug reproduction and regression testing;
- release-candidate testing on Windows hardware;
- translations through the project's designated translation system;
- human-written documentation corrections backed by verified behavior;
- donations/sponsorship through official project channels;
- respectful testing/review of existing concept-approved work;
- maintaining accurate attribution in Stella;
- sharing minimal reproducible test content when requested by maintainers.

## Anti-noise rules

Do not:
- open a new issue when an existing issue already owns the problem;
- post speculative design essays as bug reports;
- report Stella-specific architecture preferences as Luanti defects;
- post AI-generated prose to Luanti humans;
- automate upstream comments/issues/PRs;
- send raw research dumps when a minimal reproducer is possible;
- claim a bug until current local reproduction exists;
- claim a security vulnerability publicly before following Luanti's responsible-disclosure process.

## Current reciprocity position

```text
LUANTI_RECIPROCITY=PREPARED_NOT_YET_EARNED_BY_FRESH_TEST_DATA
PRIMARY_CANDIDATE=GAMEPAD_FORMSPEC_INPUT_ACCESSIBILITY_EVIDENCE
RELATED_UPSTREAM_ISSUES=4153,12264
PUBLIC_UPSTREAM_POSTING=NONE
UPSTREAM_AI_POLICY_REVIEWED=YES
HUMAN_AUTHORSHIP_REQUIRED_FOR_UPSTREAM_COMMUNICATION=YES
NEXT_EVIDENCE_SOURCE=V2-02_AND_V2-04_AFTER_V2-00R_AND_V2-01
```
