# Stella World — Luanti V0.2 Build Contract V0.1

Status: **DRAFT / RESEARCH-ONLY / NON-CANONICAL**

## 1. Contract purpose

This contract defines ownership and proof boundaries for an isolated Stella Luanti V0.2 experiment. It does not authorize canonical promotion, SCOS integration, network use, dependency installation, or unrestricted model control.

## 2. Ownership boundaries

### `stella_state`
Owns:
- schema version
- migration/normalization
- causal event ledger
- actor-scoped epistemic state
- persistence

Must not own:
- HUD presentation
- dialogue wording
- arbitrary renderer state
- model-generated claims

### `stella_experience`
Owns:
- objective projection
- `What do I do next?`
- guidance level
- waypoint projection
- re-entry recap
- plain-language recovery

Authority: projection-only. It may expose valid state; it does not create truth.

### `stella_dialogue`
Owns:
- visible dialogue choices
- display text
- selection callbacks
- valid action proposal construction

Authority: interaction/proposal-only. A visible button is not evidence that the proposition represented by the button is true.

### `stella_inhabitants`
Owns:
- stable inhabitant IDs
- Mara embodiment
- nametag/interaction target
- animation state
- facing/locomotion presentation
- mapping from causal knowledge to inhabitant behavior

Mara remains distinct from the companion.

### `stella_navigation`
Owns:
- stable place IDs
- place graph
- route records
- actor-scoped route knowledge
- journey plans
- path-execution requests

Invariant: engine pathfinding is an executor, not epistemic authority.

### `stella_atmosphere`
Owns:
- ambience
- music
- particles
- lighting
- non-authoritative environmental reactions

Invariant: sound/light/particles do not silently create events, intent, knowledge, or permission.

### `stella_companion_port`
Owns:
- governed observation packets
- selected continuity packets
- typed action proposals
- deterministic follow/wait/point/lead executor boundary
- optional model adapter

Default network mode: `OFF`.

### `stella_devtools`
Owns:
- observer views
- diagnostics
- slash commands
- test fixtures
- proof receipts

Invariant: developer affordances are not required for normal play.

### Future `stella_sanctuary_port`
Owns:
- explicit entry/exit threshold
- separate memory namespace
- separate privacy/authority contract
- mode-specific presentation

No Sanctuary state may become public-world history merely because the same renderer executes both contexts.

## 3. Core invariants

```text
I-001 DIRECT_OBSERVATION requires actor-local legitimate sensory/world basis.
I-002 REPORT_RECEIVED never upgrades recipient knowledge to DIRECT_OBSERVATION.
I-003 UI visibility is a projection of valid affordance; it is not causal truth.
I-004 Pathfinding output cannot manufacture route knowledge.
I-005 A language model may propose; deterministic policy decides/executes.
I-006 Presentation effects are non-authoritative unless a separately authorized causal event is emitted.
I-007 Normal play cannot require exact commands, coordinates, spelling, or color-only cues.
I-008 Critical feedback cannot exist only in chat.
I-009 Imported code/media must be traceable through a license/evidence ledger.
I-010 V0.2 experimental state cannot silently promote into canonical Stella/A19/SCOS state.
I-011 Renderer-specific identifiers cannot become the sole identity of canonical actors/places/events.
I-012 Every mutating external/model action must have actor, intent, target, basis, authority class, decision, execution result, and receipt.
```

## 4. Minimum actor/place vocabulary

Actors:
- `actor.primary`
- `actor.mara`
- `actor.companion.0001` (future C0+)

Places:
- `place.meadow`
- `place.meadow.cottage`
- `place.meadow.rose_garden`
- `place.meadow.old_willow`
- `place.stream`
- `place.stream.crossing`
- `place.coast`
- `place.coast.overlook`
- `place.tide_gate`

These IDs are semantic identities. Luanti coordinates are adapter-local projections.

## 5. Event vocabulary V0

Required:
- `WORLD_ENTERED`
- `ACTOR_ENCOUNTERED`
- `DIRECT_OBSERVATION`
- `REPORT_OFFERED`
- `REPORT_RECEIVED`
- `DIALOGUE_CHOICE_SELECTED`
- `OBJECTIVE_PROJECTED`
- `GUIDANCE_REQUESTED`
- `ROUTE_LEARNED`
- `JOURNEY_PLANNED`
- `NAVIGATION_EXECUTION_REQUESTED`
- `NAVIGATION_EXECUTION_RESULT`
- `PRESENTATION_REACTION`

Future/gated:
- `COMPANION_PROPOSAL`
- `COMPANION_POLICY_DECISION`
- `COMPANION_ACTION_EXECUTED`
- `SANCTUARY_ENTERED`
- `SANCTUARY_EXITED`

`PRESENTATION_REACTION` must never be used as a substitute for a causal event.

## 6. Knowledge record shape

Conceptual minimum:

```json
{
  "actor_ref": "actor.mara",
  "subject_ref": "place.tide_gate",
  "knowledge_type": "REPORTED",
  "source_actor_ref": "actor.primary",
  "basis_event_ref": "event.report_received.0001",
  "confidence_class": "ACTOR_INTERPRETATION",
  "directly_observed": false
}
```

The schema must permit multiple evidence bases and conflicting reports later; V0.2 does not need to solve belief revision fully.

## 7. Route knowledge contract

A route record is not merely a coordinate list.

```json
{
  "route_ref": "route.meadow_to_stream.v0",
  "from_place_ref": "place.meadow",
  "to_place_ref": "place.stream",
  "semantic_steps": [
    "place.meadow.old_willow",
    "place.stream.crossing"
  ],
  "known_by": ["actor.primary"],
  "evidence_refs": ["event.route_learned.0001"]
}
```

Execution pipeline:

```text
actor intends destination
→ policy checks actor possesses legitimate route/journey basis
→ journey plan emitted
→ renderer adapter resolves current coordinates
→ `core.find_path()` or equivalent computes physical walk path
→ executor walks
→ execution receipt emitted
```

The pathfinder may fail or produce a different geometric path without altering the semantic fact of what route the actor knows.

## 8. Player-facing state machine

### P0 — Enter meadow
Visible objective: `Meet Mara near the stream.`
Recovery: `What do I do next?` returns the same objective plus optional stronger guidance.

### P1 — Mara encountered
Dialogue establishes Mara as a person before the Gate discovery.

### P2 — Explore
Objective: explore toward coast / follow environmental cues.

### P3 — Gate observed
Emit `DIRECT_OBSERVATION(actor.primary, place.tide_gate)`.
Objective changes to tell Mara.

### P4 — Return to Mara
Guidance is recoverable and adjustable.

### P5 — Report Gate
Visible choice appears because Primary possesses the observation and Mara has not yet received that report.
Click emits report events; it does not retroactively give Mara direct observation.

### P6 — Epistemic acknowledgement
Mara can state that the player told her about the Gate while explicitly distinguishing that from seeing it herself.

### P7 — Route frontier
Mara may express intent to investigate, but route knowledge/journey planning remains a separate proof.

## 9. Guidance state machine

Levels:
- `OFF`
- `SUBTLE`
- `STANDARD`
- `FULL`

Independent recovery operation:
- `WHAT_DO_I_DO_NEXT`

Recovery may temporarily provide stronger orientation than the selected ambient guidance level, but must not change world truth.

Required cue redundancy where critical:
- text
- icon/shape
- spatial placement
- optional distance/direction
- sound where useful

Never rely on color alone.

## 10. Mara dialogue state contract

Before Gate observation:
- ask what Mara is doing
- say not yet / continue exploring
- goodbye

After Primary direct Gate observation, before report:
- `Tell Mara what I saw.`
- optional questions
- leave

After report:
- Mara acknowledges report provenance
- Mara does not claim direct observation
- optional intent to investigate

Dialogue text may vary; event semantics may not.

## 11. Companion protocol V0

The model-facing surface is typed proposals only.

```json
{
  "proposal_id": "proposal.0001",
  "actor_ref": "actor.companion.0001",
  "intent": "lead_player",
  "target_place_ref": "place.stream",
  "basis_refs": ["route.meadow_to_stream.v0"],
  "authority": "PROPOSAL_ONLY",
  "requested_executor": "navigate"
}
```

Policy result:

```json
{
  "proposal_id": "proposal.0001",
  "decision": "ALLOW",
  "reason_code": "ROUTE_KNOWN_AND_ACTION_WITHIN_CAPABILITY",
  "executor_contract": "navigate.v0"
}
```

Forbidden model capabilities:
- arbitrary Lua execution
- arbitrary Python execution
- raw Miney object access
- arbitrary HTTP
- filesystem access outside an explicit adapter contract
- direct state-ledger writes
- direct authority-policy writes
- silent network provider selection

## 12. Companion development ladder

- C0 Observer: visible, receives governed observations, no world mutation.
- C1 Deterministic: follow/wait/come/point/lead to legitimately known targets.
- C2 Conversational: generated language over selected legitimate context; actions remain typed.
- C3 Model adapter: local or explicitly authorized provider; explicit network/context boundary.
- C4 Selected continuity/preferences: opt-in scoped memory only.
- C5 Sanctuary-capable: only after privacy/entry/authority contracts survive separate proof.

## 13. Surprise classes

- `PRESENTATION_ONLY`
- `PREAUTHORED_DISCOVERY`
- `SOCIAL_EXPRESSION`
- `WORLD_EVENT`
- `PRIVATE_SANCTUARY`

Rule: surprise may conceal content; it may not conceal the authority class or the fact that the player is making a consequential choice.

## 14. Dependency decision contract

Default: build a small native Stella component.

Adopt a dependency only if:
- it solves substantial complexity
- current maintenance is credible
- its license is understood
- its transitive dependencies are known
- its API surface is narrow enough to isolate
- failure is recoverable
- Stella can survive removal
- imported assets/code can be traced

Current research candidates:
- **Flow**: candidate for dialogue/UI A/B prototype.
- **formspec_ast**: possible Flow dependency; evaluate transitive cost.
- **Miney**: prior art / bridge laboratory, not direct model tool surface.
- **LLM Connect**: feasibility evidence, not architectural authority.
- **Yourland Speak Up / Simple Dialogs**: dialogue-pattern references.
- **Piranesi / The Library**: authored-experience and UX references.

## 15. License ledger format

```text
ITEM_ID
TYPE = CODE | TEXTURE | MODEL | SOUND | MUSIC | FONT | OTHER
SOURCE_URL
SOURCE_PACKAGE
AUTHOR
LICENSE
ORIGINAL_OR_MODIFIED
LOCAL_FILENAME
HASH_SHA256
PURPOSE
ATTRIBUTION_REQUIRED
AI_DISCLOSURE_REQUIRED
REVIEW_STATUS
NOTES
```

No external asset may be promoted from `CANDIDATE` to `APPROVED_FOR_BUILD` without ledger completion.

## 16. Proof ladder

### V2-00 — V0.1 closure evidence
Preserve receipts/hashes/playtest conclusions; no V0.1 feature patching.

### V2-01 — isolated V0.2 shell
New experimental copy. No canonical Stella changes.

### V2-02 — interaction vertical slice
Mara identity, visible prompt, forgiving target, dialogue UI.

### V2-03 — causal dialogue slice
Gate direct observation → valid choice → report → Mara reported knowledge only → restart persistence.

### V2-04 — orientation layer
Objectives, guidance levels, waypoint, recovery, re-entry recap.

### V2-05 — Mara embodiment
glTF mesh and independent animation tracks while epistemic tests remain unchanged.

### V2-06 — atmosphere pass
Landmarks, environmental cues, sound zones, Gate presentation. Presentation remains non-authoritative.

### V2-07 — route-knowledge laboratory
Place graph, actor-scoped route knowledge, journey plans, pathfinder executor proof.

### V2-08 — Companion C0/C1
No LLM. Typed deterministic embodiment only.

### V2-09 — Companion C2/C3 gate
Compare local/remote model adapters after C0/C1 proof. Default network OFF.

### V2-10 — governed surprise system
Presentation-only first; causal surprises separately gated.

### Future — Sanctuary contract
Prove namespace, privacy, explicit entry, permissions, and non-leakage before richer content.

## 17. V0.2 acceptance criteria

Fresh-player experience:
- launches without developer preparation
- player understands where they are
- Mara can be found without coordinates
- Mara is recognizable
- interaction requires no slash command
- dialogue is visible and recoverable
- Gate can be discovered through world cues
- Gate direct observation persists across restart
- player can find Mara again
- report is sent via visible choice
- Mara stores report, not direct observation
- `What do I do next?` works at every normal state
- exact typing is unnecessary

Technical:
- zero fatal runtime errors in acceptance run
- zero unintended canonical Stella changes
- zero SCOS changes
- zero hidden network use
- zero untracked third-party assets
- zero model-driven direct world authority
- zero state migration failures
- zero critical chat-only feedback

## 18. Pre-mutation reverification gate

Before V2-01 machine mutation, collect fresh local evidence for:
- actual Luanti executable/version
- exact playground/world/mod paths
- current V0.1 state/receipt hashes
- protected file hashes
- whether the V0.1 process/server is fully stopped
- free target path for isolated V0.2 shell
- current dependency/install state
- current Git/worktree state if a local repo will be involved

The research branch cannot satisfy these machine-state checks.

## 19. Promotion rule

No V0.2 experiment becomes canonical because it works. Promotion requires a separate review that maps experimental semantics to canonical Stella ownership, migration implications, evidence, and explicit authorization.