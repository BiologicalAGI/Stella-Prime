# Stella → Luanti Upstream Evidence Capture V0.1

Status: **PREPARED TEST CONTRACT / NO CLAIM OF BUG / NO UPSTREAM POSTING**

## Purpose

Define the smallest empirical record Stella should capture during V2-02 and V2-04 so any later Luanti feedback is reproducible, useful, and separable from Stella-specific design choices.

This is an evidence-capture contract, not an issue draft.

## Primary upstream questions

### Q1 — Gamepad world actions vs formspec interaction

Does the same controller that performs supported in-game actions allow the player to:
- open the Stella interaction surface;
- move focus between visible dialogue choices;
- activate a focused choice;
- cancel/close safely;
- recover after closing/cancelling;
- complete the Mara report interaction without mouse/touch fallback?

Related upstream issue: `luanti-org/luanti#4153`.

### Q2 — Can game/mod code identify the active input mechanism?

Can Stella determine, using public APIs rather than platform-specific assumptions, whether the player is currently using:
- keyboard/mouse;
- gamepad;
- touchscreen;
- a mixed/hot-switched configuration?

Can it adapt prompt text or UI sizing without guessing?

Related upstream issue: `luanti-org/luanti#12264`.

## Required environment record

Capture before each test run:

```text
TEST_ID=
TIMESTAMP_LOCAL=
OS=
OS_BUILD=
LUANTI_VERSION=
LUANTI_EXE_SHA256=
ACTIVE_RENDERER=
DISPLAY_RESOLUTION=
WINDOW_MODE=
UI_SCALE_RELEVANT_SETTINGS=
STELLA_BUILD_ID=
STELLA_STATE_SCHEMA_VERSION=
WORLD_ID_OR_FIXTURE_ID=
CONTROLLER_VENDOR=
CONTROLLER_PRODUCT=
CONTROLLER_CONNECTION=USB|BLUETOOTH|OTHER
CONTROLLER_PRESENT_AT_LAUNCH=YES|NO
CONTROLLER_HOTPLUGGED=YES|NO
INPUT_BINDING_PROFILE=
```

If a field cannot be observed, record `UNKNOWN`; never infer it.

## Baseline matrix

Run the same Stella interaction flow with:

| Input configuration | World movement/action | Open interaction | Move dialogue focus | Activate choice | Cancel/escape | Recovery usable | Result |
|---|---|---|---|---|---|---|---|
| Keyboard + mouse | | | | | | | PENDING |
| Keyboard only where possible | | | | | | | PENDING |
| Gamepad present at launch | | | | | | | PENDING |
| Gamepad hot-plugged after launch | | | | | | | PENDING |
| Gamepad disconnected/reconnected | | | | | | | PENDING |
| Mixed gamepad + mouse fallback | | | | | | | PENDING |

Do not interpret a successful world-action column as formspec success.

## Stella fixture requirements

The test fixture should be deliberately small:
- one recognizable Mara interaction target;
- one visible interaction prompt;
- one formspec/dialogue with at least three choices;
- deterministic state reset;
- one cancel/close path;
- one state-changing choice with visible non-chat confirmation;
- one `What do I do next?` recovery affordance outside critical chat-only feedback.

The fixture should not require Gate discovery or the full V0.2 authored world to reproduce input behavior.

## Focus test

For each input configuration record:
- initial focus owner, if observable;
- whether focus is visually discernible;
- traversal order;
- wrap/no-wrap behavior;
- whether disabled/non-actionable elements receive focus;
- whether focus survives formspec refresh/update;
- whether focus returns to a comprehensible state after cancel;
- whether the player can become trapped without a mouse.

Aesthetic preference is not a bug. Record only behavior.

## Prompt/adaptation test

Where possible, determine whether Stella can truthfully display an input-specific prompt such as:

```text
Press E to talk
Press controller button X to talk
Click to talk
```

Classify:
- `API_SUPPORTED` — public Luanti API gives sufficient current input information;
- `STATIC_CONFIG_ONLY` — only configuration can be observed, not active mechanism;
- `HEURISTIC_ONLY` — Stella would have to guess from events/state;
- `NOT_AVAILABLE` — no bounded public method identified;
- `UNKNOWN` — not yet researched/reproduced.

Do not invent input-method certainty for UX convenience.

## Hot-plug/re-entry test

Sequence:
1. launch without controller;
2. enter fixture;
3. attach controller;
4. test world actions;
5. test formspec interaction;
6. close/re-open formspec;
7. leave/re-enter world if needed;
8. disconnect/reconnect controller;
9. repeat.

Record which transitions require restart, menu return, or manual fallback.

## Reproduction quality levels

- `R0 OBSERVATION_ONLY` — seen once in Stella.
- `R1 REPEATED_STELLA` — repeated at least three times in the same Stella fixture.
- `R2 MINIMAL_FIXTURE` — reproduced in a stripped standalone mod/fixture.
- `R3 CROSS_SESSION` — survives process restart and repeated fresh launches.
- `R4 CROSS_DEVICE_OR_SECOND_TESTER` — reproduced with another controller/device/tester.

Only R2+ should normally be considered for upstream bug feedback unless maintainers request earlier evidence.

## Upstream-worthiness gate

Before considering public feedback, answer:

```text
CURRENT_STABLE_OR_RELEVANT_DEV_BUILD?=
REPRODUCIBLE?=
MINIMAL_FIXTURE_AVAILABLE?=
ALREADY_REPORTED?=
ENGINE_OR_STELLA_SPECIFIC?=
EXPECTED_BEHAVIOR_DOCUMENTED?=
LOGS/SCREEN_RECORDING_USEFUL?=
SECURITY_SENSITIVE?=
HUMAN_CONTRIBUTOR_UNDERSTANDS_RESULT?=
```

Classification:
- `NOT_UPSTREAM` — Stella-specific or expected behavior.
- `DUPLICATE_EVIDENCE` — useful only as additional data on an existing issue.
- `UPSTREAM_COMMENT_CANDIDATE` — adds reproducible data to an existing issue.
- `NEW_ISSUE_CANDIDATE` — genuinely distinct reproducible engine defect after search.
- `PRIVATE_SECURITY_REPORT_CANDIDATE` — potential vulnerability; do not post publicly.

## Communication boundary

This file may contain AI-assisted internal analysis. Luanti's current AI policy is stricter for communication intended for humans upstream.

Therefore:
- do not paste this file into an upstream issue;
- do not have an agent post an issue/comment/PR autonomously;
- the human contributor must review the empirical evidence and write the upstream message in their own words;
- significant AI use connected to an upstream contribution must be disclosed as required by Luanti's current policy;
- keep the upstream message minimal and focused on verified facts.

## Current status

```text
EVIDENCE_CAPTURE_CONTRACT=PREPARED
FRESH_LOCAL_DATA=NONE_YET
KNOWN_UPSTREAM_BUG=NONE_CLAIMED
PRIMARY_EXISTING_ISSUE=luanti-org/luanti#4153
SECONDARY_EXISTING_ISSUE=luanti-org/luanti#12264
PUBLIC_COMMUNICATION=NONE
```
