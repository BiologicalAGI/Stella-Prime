# Stella Luanti V0.2 — V2-03A State Foundation Design V0.1

Status: **PREIMPLEMENTATION DESIGN / RESEARCH-ONLY / NON-AUTHORITY / NON-CANONICAL**

## 1. Purpose

V2-03A prepares the smallest engine-neutral causal-state foundation needed for the V2-03 proof:

```text
SEEING != BEING_TOLD
```

It does not yet implement Tide Gate gameplay, route knowledge, companion behavior, language-model use, atmosphere, final Mara embodiment, or canonical promotion.

The purpose of this design is to ensure that later dialogue and model work operate on legitimate semantic state rather than creating it.

## 2. Historical pressure-test constraints applied now

V2-03A must survive four historical pressure tests before richer systems are allowed to depend on it.

### 2.1 Circuit test

The causal rule must reduce to:

```text
INPUT
  -> STATE
  -> VALIDATED TRANSITION
  -> OUTPUT / PROJECTION
```

For the future Gate slice:

```text
INPUT: Primary legitimately observes Tide Gate
STATE: no prior Primary direct observation
TRANSITION: append attributable DIRECT_OBSERVATION event
OUTPUT: Primary projected direct knowledge becomes true
```

and later:

```text
INPUT: Primary explicitly reports Gate to Mara
STATE: Primary DIRECT=yes; Mara REPORTED=no; Mara DIRECT=no
TRANSITION: append attributable REPORT_RECEIVED event
OUTPUT: Mara REPORTED=yes; Mara DIRECT remains no
```

If those transitions cannot be represented without Luanti formspecs or language generation, the semantic design is invalid.

### 2.2 Minimum active-state test

```text
EXISTS_IN_WORLD != MUST_BE_HOT
HAS_HISTORY != FULL_HISTORY_TOUCHED_EACH_TICK
```

The ledger is durable history. Projected actor knowledge is an active view. The design must permit the view to be rebuilt from durable history without requiring all historical events to remain in a continuously processed structure.

### 2.3 Compact shared-reference test

Store semantic references rather than duplicated world descriptions.

Preferred:

```text
actor.primary
actor.mara
place.tide_gate
claim.tide_gate.exists
```

Avoid embedding duplicate canonical geography or prose descriptions inside each actor's knowledge record.

### 2.4 Modern replay/provenance test

A valid event must remain attributable and replayable after renderer or language changes.

Minimum properties:

```text
stable event identity
schema version
semantic event type
actor / participant refs
target / subject refs
basis refs
world-relative sequence / tick where available
explicit payload
validation result
```

## 3. Ownership boundary

`stella_state` owns:

```text
schema version
semantic event validation
event identity / ordering
append-only causal ledger
actor-scoped epistemic projection
persistence adapter
load / normalization / migration gate
state inspection API
```

`stella_state` must not own:

```text
Mara's visible wording
formspec layout
nametag or mesh
pathfinding
world coordinates as canonical identity
language-model prompts
model-selected world truth
atmosphere
```

## 4. Event-first design

V2-03A should not make mutable knowledge booleans the authoritative source.

Preferred architecture:

```text
VALIDATED SEMANTIC EVENTS
          |
          v
       REDUCER
          |
          v
COMPACT PROJECTED STATE
```

The ledger is factual history.

Projected state is a rebuildable view.

Example:

```text
event.direct_observation.000001
  actor_ref=actor.primary
  subject_ref=place.tide_gate
  basis=WORLD_OBSERVATION

                |
                v

projection:
  actor.primary / place.tide_gate / DIRECT = true
```

A later report:

```text
event.report_received.000002
  speaker_ref=actor.primary
  listener_ref=actor.mara
  subject_ref=place.tide_gate
  basis_event_ref=event.direct_observation.000001

                |
                v

projection:
  actor.primary / place.tide_gate / DIRECT = true
  actor.mara    / place.tide_gate / REPORTED = true
  actor.mara    / place.tide_gate / DIRECT = false
```

## 5. Initial schema version

Proposed experimental schema identifier:

```text
stella.state.v0.1
```

This is a V0.2 experimental schema, not canonical World Kernel promotion.

Suggested persisted envelope:

```json
{
  "schema_version": "stella.state.v0.1",
  "ledger_version": 1,
  "next_event_sequence": 1,
  "events": []
}
```

V2-03A may internally maintain compact projections, but the durable truth should remain derivable from accepted events.

## 6. Minimum event envelope

Proposed conceptual shape:

```json
{
  "event_ref": "event.direct_observation.000001",
  "event_type": "DIRECT_OBSERVATION",
  "schema_version": "stella.event.v0.1",
  "sequence": 1,
  "actor_ref": "actor.primary",
  "subject_ref": "place.tide_gate",
  "basis_refs": [],
  "payload": {},
  "world_tick": null
}
```

Not every event requires every role field. Event-specific validators define required fields.

## 7. Initial event vocabulary

V2-03A should define the event vocabulary without implementing all event producers.

Minimum declared types:

```text
WORLD_ENTERED
DIRECT_OBSERVATION
DIALOGUE_CHOICE_SELECTED
REPORT_OFFERED
REPORT_RECEIVED
```

V2-03A itself may only create foundation/test fixtures. Gameplay producers arrive in later V2-03 subgates.

## 8. Typed causal API

Do not expose a public unrestricted `append_event(anything)` API to other mods as the normal integration surface.

Preferred public semantic operations:

```text
record_world_entered(...)
record_direct_observation(...)
record_dialogue_choice_selected(...)
record_report_offered(...)
record_report_received(...)
```

A private/internal append primitive may exist beneath those operations.

Reason:

```text
VALID EVENT CONSTRUCTION
should be easier than
ARBITRARY EVENT INJECTION
```

## 9. DIRECT_OBSERVATION invariant

`DIRECT_OBSERVATION` requires an actor-local legitimate observation basis.

Minimum required fields:

```text
actor_ref
subject_ref
observation_basis
```

For V2-03B the accepted basis will be a bounded world-observation source tied to the Primary actor.

Forbidden V2-03 consequence:

```text
REPORT_RECEIVED
  -> synthesize DIRECT_OBSERVATION for listener
```

That transition must be structurally impossible through the typed report API.

## 10. REPORT_RECEIVED invariant

Minimum conceptual fields:

```text
speaker_ref
listener_ref
subject_ref
source_basis_refs
claim_ref (optional hook in V0.1, expected later)
```

Report receipt creates a reported evidence basis for the listener.

It does not certify the report as true and does not create direct observation.

Later belief revision can distinguish accepted, disputed, corroborated, contradicted, or uncertain reports; V2-03 does not need those classes yet.

## 11. Conversation semantic hooks

The historical language research showed that raw prose should not become the sole durable record of meaningful conversation.

V2-03A should therefore reserve compatibility for:

```text
speaker_ref
listener_ref
speech_act
claim_ref
basis_refs
heard_successfully
surface_utterance
```

But V2-03A should **not** build a full NLP or claim ontology.

Current rule:

```text
SEMANTIC CONSEQUENCE
!=
SURFACE WORDING
```

V2-03C will exercise this with explicit report semantics.

## 12. Knowledge projection

Conceptual query surface:

```text
has_direct_observation(actor_ref, subject_ref)
has_reported_knowledge(actor_ref, subject_ref)
get_evidence_bases(actor_ref, subject_ref)
```

Possible normalized record:

```json
{
  "actor_ref": "actor.mara",
  "subject_ref": "place.tide_gate",
  "knowledge_class": "REPORTED",
  "basis_event_refs": ["event.report_received.000002"],
  "source_actor_refs": ["actor.primary"],
  "directly_observed": false
}
```

Do not design knowledge as one boolean because later Stella research includes direct, reported, procedural, episodic, semantic, relational, conversational, cultural, and self-history evidence classes.

V2-03 implements only what it needs.

## 13. Duplicate / idempotency behavior

Reopening dialogue must not manufacture history.

The state layer therefore needs a way for callers to prevent or detect duplicate causal commits.

V2-03 does not require universal distributed idempotency.

Minimum slice requirement:

```text
same logical report transaction
must not silently append duplicate REPORT_RECEIVED history
```

Candidate strategies to compare during implementation:

```text
explicit transaction_ref
semantic dedupe key
caller-owned one-shot affordance state
```

Do not choose a strategy solely for convenience until the local implementation is inspected.

## 14. Persistence adapter — Luanti ModStorage

For the Luanti V0.2 adapter, current Luanti documentation describes ModStorage as a per-world, per-mod persistent string key-value store.

Important implications:

```text
LUANTI MODSTORAGE
= persistence mechanism
!= Stella semantic authority
```

The adapter should obtain ModStorage at mod load time and store namespaced Stella state.

Potential keys:

```text
stella_state:schema_version
stella_state:ledger_meta
stella_state:event:<sequence>
stella_state:projection_checkpoint
```

The exact storage layout should be chosen after fresh local currentness and implementation review.

## 15. Why not one giant serialized blob by default?

Current Luanti persistence guidance notes that storage/update cost and save granularity matter. ModStorage persistence is tied to engine save intervals, and full serialization scales with the amount of serialized data.

Stella's historical research already favors:

```text
STORE CAUSES / REFERENCES / DELTAS
```

Therefore the preferred direction is a change-oriented/event-oriented layout rather than rewriting one ever-growing world-history blob after every semantic event.

V2-03 does not need a high-scale database design; it only needs to avoid baking an obviously non-scalable authority model into the first proof.

## 16. Commit-time semantic discipline

The code should treat a semantic transition as committed only after the persistence adapter accepts the corresponding durable write operation according to the chosen adapter contract.

Do not rely solely on an `on_shutdown` save.

Crash/power-loss behavior remains a later durability test, but V2-03 should not intentionally design shutdown-only semantic persistence.

## 17. Load / rehydration path

Conceptual load flow:

```text
MOD LOAD
  -> obtain persistence adapter
  -> read schema metadata
  -> classify state
       EMPTY_VALID
       KNOWN_SCHEMA_VALID
       UNKNOWN_SCHEMA
       INVALID_LEDGER
  -> if valid: rebuild / load projection
  -> if invalid: HOLD semantic writes
```

V2-03D will prove restart persistence with known-good state.

## 18. Fail-closed state handling

Never silently translate unreadable state into a fresh empty Stella history.

```text
UNKNOWN_SCHEMA
or
INVALID_LEDGER
        -> STATE_LOAD_HOLD
        -> SEMANTIC_WRITES_ENABLED=NO
        -> PRESERVE ORIGINAL STORAGE
```

Any later migration must be explicit, versioned, bounded, and independently proven.

## 19. Retro-budget representation profile

V2-03A can later support a small historical pressure-test without porting to old consoles.

### CIRCUIT profile

Truth can be reduced conceptually to bits:

```text
PRIMARY_SAW_GATE
MARA_HEARD_REPORT
MARA_SAW_GATE
```

Required state after report:

```text
1 / 1 / 0
```

### 8-BIT-like profile

Use compact IDs:

```text
ACTOR 01 = primary
ACTOR 02 = mara
PLACE 07 = tide_gate
KNOWLEDGE 01 = direct
KNOWLEDGE 02 = reported
```

Semantic truth must remain equivalent to the modern representation.

### MODERN profile

Adds:

```text
stable string IDs
versioned events
basis refs
replay
migration hooks
inspection tools
```

Core semantics may become richer in representation but may not contradict the minimal profiles.

## 20. Model-independence consequence

No language model is required for V2-03A.

Future language systems receive bounded legitimate state.

They may produce wording or proposals.

They may not directly write the ledger or invent epistemic basis.

Desired degradation path remains:

```text
RICH MODEL
  -> SMALL LOCAL MODEL
  -> RETRIEVAL + RULES
  -> DETERMINISTIC DIALOGUE
  -> CORE MARA / WORLD STATE INTACT
```

## 21. V2-03A implementation split

### V2-03A1 — foundation build

Expected bounded work:

```text
create stella_state module
schema constants
semantic ID validation helpers
event validators
private ledger append
knowledge reducer
ModStorage adapter
load classification
inspection-only dev output
static self-tests
```

No Luanti launch required during construction.

### V2-03A2 — controlled load proof

Prove:

```text
module loads once
schema recognized
empty ledger is valid
empty projected epistemic state is valid
no spontaneous causal events
no semantic writes occur merely from load
no fatal runtime error
graceful close
post-code identity unchanged
```

### V2-03B — direct Gate observation producer

Later proof:

```text
Primary DIRECT=yes
Mara DIRECT=no
Mara REPORTED=no
```

### V2-03C — explicit report transaction

Later proof:

```text
report affordance prerequisite valid
explicit choice commits report
Primary DIRECT=yes
Mara REPORTED=yes
Mara DIRECT=no
```

### V2-03D — restart / rehydration

Later proof:

```text
same provenance distinction survives restart
```

### V2-03E — human-facing causal dialogue

Later proof:

```text
player can understand the causal distinction through normal interaction
Mara wording respects evidence basis
no exact command required
```

## 22. V2-03A negative tests

Foundation should reject at least:

```text
unknown event type
missing required actor_ref
missing required subject_ref
invalid semantic ID form where validator applies
REPORT_RECEIVED that attempts listener direct_observation=true
unknown schema during load
malformed persisted ledger
sequence collision / malformed event identity
```

Implementation may refine the exact set after code is prepared.

## 23. V2-03A positive tests

Foundation should prove at least:

```text
empty valid state loads
valid DIRECT_OBSERVATION fixture reduces to direct knowledge
valid REPORT_RECEIVED fixture reduces to reported knowledge
report fixture does not produce direct observation
replay of same accepted ledger produces equivalent projection
serialization / rehydration preserves semantic IDs and basis refs
```

Test fixtures are development evidence only and must not be confused with live gameplay history.

## 24. Current open observations from V2-02

Carry forward without forcing them into this gate:

```text
OPEN-01 invalid mapgen_stone alias
OPEN-02 invalid mapgen_water_source alias
OPEN-03 player flying/floating observation
OPEN-04 Mara body temporary
OPEN-05 runtime detector missed ERROR[ServerStart]
OPEN-06 orchestration document currentness drift
```

Expected V2-03A relevance:

```text
OPEN-01/02 likely nonblocking for state foundation, reverify first
OPEN-03 likely nonblocking for state foundation, relevant to later movement/orientation
OPEN-04 intentionally deferred to V2-05
OPEN-05 directly relevant to V2-03A2 runtime harness design
OPEN-06 documentation reconciliation after fresh local currentness
```

## 25. Explicitly dormant research during V2-03A

Do not implement now:

```text
route knowledge
pathfinding
procedural travel
population scaling
DORMANT/WARM/HOT inhabitant runtime scheduler
retrieval memory system
small/large language model adapter
companion
Flow dependency
final Mara mesh
atmosphere
Sanctuary
canonical World Kernel migration
SCOS integration
```

They remain visible in the research crosswalk.

## 26. Acceptance condition for V2-03A foundation

V2-03A is not complete because code exists.

It is complete only when a bounded foundation is constructed and independently shown to preserve:

```text
schema validity
event validity
semantic ID stability
replay equivalence
direct/report separation
persistence load discipline
fail-closed malformed-state behavior
no spontaneous history
no hidden model/network use
no V0.1 mutation
no canonical Stella mutation
no SCOS mutation
```

## 27. Authority and currentness boundary

This document prepares a design only.

Before any local V2-03A mutation:

```text
freshly reverify V0.1 protected identities
freshly reverify Luanti executable identity
freshly reverify current V2-02 inhabitants/dialogue identities
freshly reverify V2-02 repair receipt
freshly reverify world identity
freshly prove Luanti quiescent
freshly prove stella_state target absent/free
reconcile open observations
obtain exact bounded local mutation authorization
```

No authorization is inherited from this document.

## 28. Current classification

```text
DESIGN=V2_03A_STATE_FOUNDATION_V0_1
STATUS=PREPARED_RESEARCH_ONLY
LOCAL_CODE_CREATED=NO
LUANTI_RUN=NO
MODEL_USED_IN_GAME=NO
NETWORK_MODEL_USE=NO
CANONICAL_PROMOTION=NO
SCOS_INTEGRATION=NO
NEXT_SAFE_LOCAL_STEP=READ_ONLY_PREMUTATION_REVERIFY
```
