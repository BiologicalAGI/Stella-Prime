# Stella Workbench Envelope V0.1

Status: **RESEARCH / MODEL-EXTERNAL OPERATING ENVELOPE / NON-AUTHORITY / NON-CANONICAL**

## 1. Purpose

This document defines a model-external working envelope for reasoning about and operating on Stella without treating any language model, renderer, connector, recovery packet, or tool as the owner of Stella truth.

It does **not** modify a language model's weights, system runtime, platform security boundaries, or canonical Stella state.

The envelope exists to make project state, evidence, research, tool capability, currentness, authorization, execution, and promotion explicit before action.

Core distinction:

```text
REASONING / LANGUAGE MODEL
!=
OPERATING ENVELOPE
!=
PROJECT TRUTH
!=
TOOL EXECUTION
```

The intended result is a durable workspace that can survive model replacement in the same way Stella world semantics are intended to survive renderer replacement.

## 2. Architectural analogy

```text
STELLA WORLD
  semantic kernel
      -> renderer adapter
      -> Luanti / future engine

MARA
  durable identity / knowledge / history
      -> language adapter
      -> deterministic rules / retrieval / model

STELLA WORKBENCH
  project state / evidence / memory / authority
      -> reasoning + tool gateway
      -> current language model / future model
```

Shared invariant:

```text
IDENTITY / TRUTH / HISTORY
!=
EXECUTION ENGINE
!=
PRESENTATION
```

## 3. Envelope layers

The working envelope contains nine conceptual layers.

### 3.1 Project identity

Required minimum:

```text
project_id
subproject_id
active proof frontier
semantic owner
renderer / adapter role
separate-project exclusions
```

For current Stella Luanti V0.2 work:

```text
PROJECT=STELLA
SUBPROJECT=LUANTI_V0_2
WORLD_AUTHORITY=STELLA_WORLD_KERNEL
ENGINE_ROLE=EXPERIMENTAL_BODY
MARA_ID=actor.mara
SCOS=SEPARATE
CANONICAL_PROMOTION=NONE
```

### 3.2 Current-state packet

Keep the active working state compact.

Minimum fields:

```text
last_proven
current_proof_frontier
next_safe
next_prepared
active_card
currentness_status
open_holds
current_authority
```

Historical state and present currentness are separate.

### 3.3 Research overlay

Research is retrieved by relevance to the active gate rather than loaded indiscriminately.

Examples of selectable overlays:

```text
historical game pressure tests
historical conversation pressure tests
engine documentation
UX / accessibility research
model / retrieval research
licensing / dependency research
route knowledge research
companion / tool-port research
```

Research may influence design. It does not grant execution authority.

### 3.4 Working-memory profile

The workbench uses explicit context-resolution profiles.

#### MICRO

For one exact card or bounded verification:

```text
project
gate
authority
target
expected result
critical identities
holds
```

#### WARM

For normal development:

```text
current checkpoint
current gate contract
relevant research
open observations
tool boundaries
recent evidence
```

#### HOT

For debugging or implementation reasoning:

```text
current implementation
exact code / artifact identity
recent failures
historical pressure test
alternative hypotheses
validator state
```

#### FOCUSED

For temporary deep research:

```text
multiple research sources
current artifacts
engine documentation
comparative architectures
cross-model / cross-engine evidence
```

#### ARCHIVE

Durable but not continuously active:

```text
old conversations
historical checkpoints
proof receipts
old versions
unused ideas
large event histories
```

Core rule:

```text
HAS HISTORY
!=
FULL HISTORY MUST BE HOT
```

### 3.5 Authority / currentness firewall

The workbench must preserve these planes independently:

```text
EVIDENCE
CAPABILITY
CURRENTNESS
AUTHORIZATION
EXECUTION
PROMOTION
```

Non-equivalence rules:

```text
CAN_DO != MAY_DO
WAS_TRUE != IS_TRUE_NOW
TEST_PASSED != CANONICAL
GITHUB_ARTIFACT != LOCAL_MACHINE_STATE
MODEL_PROPOSAL != AUTHORIZATION
DEPENDENCY_AVAILABLE != DEPENDENCY_APPROVED
PLAYER_CHOICE != HIDDEN CONSENT
PRIVATE_CONTEXT != PUBLIC_WORLD_HISTORY
```

### 3.6 Tool capability registry

Each tool or connector is treated as a port.

Conceptual record:

```text
tool_id
capabilities
read_scope
write_scope
network_class
mutation_class
authority_requirement
truth_domain
input_contract
output_contract
failure_modes
receipt_type
```

Example principle:

```text
GITHUB CAN REPORT GITHUB STATE
GITHUB CANNOT PROVE CURRENT IBUYPOWER STATE
```

A tool capability never grants its own permission to execute.

### 3.7 Event / receipt history

Development work should be representable as semantic events rather than only conversational prose.

Candidate envelope:

```text
event_ref
event_type
actor_ref
target_ref
basis_refs
authority_class
started_at
completed_at
result
evidence_refs
notes
```

Candidate development event classes:

```text
RESEARCH_RETRIEVED
DESIGN_DECISION_PREPARED
AUTHORIZATION_GRANTED
VALIDATION_STARTED
VALIDATION_FAILED
VALIDATOR_REPAIRED
VALIDATION_PASSED
ARTIFACT_CREATED
ARTIFACT_UPDATED
REVIEW_RECEIVED
REVIEW_REPLIED
REREVIEW_REQUESTED
LOCAL_REVERIFY_COMPLETED
GATE_OPENED
GATE_CLOSED
```

These are workbench events, not Stella world events. Shared envelope concepts do not imply shared authority namespaces.

### 3.8 Validation / historical pressure tests

Each major capability should be interrogated from the simplest representation upward.

Game-system ladder:

```text
CIRCUIT / STATE TRANSITION
ATARI / MINIMUM ACTIVE STATE
8-BIT / SHARED TABLES + SPARSE REFERENCES
TEXT / MUD / LOGICAL WORLD
ELITE / PROCEDURAL + LOCAL BUBBLE
X / MULTI-RESOLUTION SIMULATION
MODERN / REPLAY + PROVENANCE + MIGRATION
```

Conversation ladder:

```text
ELIZA / REACTION
PARRY / PERSISTENT CHARACTER STATE
ALICE-AIML / TRANSPARENT DETERMINISTIC RESPONSE
RETRIEVAL / BOUNDED MEMORY SELECTION
STATISTICAL / SMALL MODEL
TRANSFORMER / LLM
TOOL / AGENT PORT
```

Interpretation:

```text
If a capability fails the simplest representation,
its semantic model may be confused.

If it only works with a rich renderer or large model,
world logic may be hidden in presentation.

If it passes simple logic but fails systemic interaction,
it may lack useful emergence.

If it passes interaction but fails replay/provenance/migration,
it is not durable enough for Stella.
```

### 3.9 Output / next-action contract

Before proposing action, produce:

```text
WHERE_ARE_WE
WHAT_WAS_LAST_PROVEN
WHAT_CHANGED
WHAT_IS_SAFE_NEXT
WHAT_IS_PREPARED_NEXT
CURRENT_AUTHORITY
WHAT_REQUIRES_REVERIFY
WHAT_WILL_CHANGE
EXPECTED_OUTPUT
HARD_STOP
```

Normal work should prefer one bounded active card at a time.

## 4. Model-independent reasoning contract

The envelope may prepare a semantic response contract for any reasoning or language engine.

Conceptual example:

```json
{
  "intent": "explain_current_gate",
  "known_facts": [
    "V2-02 passed at the last proven checkpoint",
    "V2-03A is prepared"
  ],
  "forbidden_claims": [
    "V2-03 already passed",
    "local state is current without reverify"
  ],
  "required_distinctions": [
    "evidence_vs_authority",
    "prepared_vs_authorized"
  ]
}
```

Different models may phrase the answer differently. They must not change the semantic constraints.

## 5. Retrieval discipline

Context compilation should follow:

```text
QUESTION / ACTIVE GATE
        -> identify relevant domain
        -> retrieve bounded evidence
        -> mark source/currentness/truth domain
        -> construct working context
        -> reason
        -> validate against invariants
        -> emit answer / proposal / receipt
```

Do not treat retrieval volume as a proxy for reasoning quality.

Preferred principle:

```text
CORRECT CONTEXT
+
CORRECT RESOLUTION
+
PROVENANCE
+
BOUNDARIES
>
UNBOUNDED CONTEXT
```

## 6. Graceful model replacement

The workbench should preserve project continuity when the reasoning/language engine changes.

Desired property:

```text
WORKBENCH REMAINS
PROJECT HISTORY REMAINS
EVIDENCE REMAINS
AUTHORITY RULES REMAIN
TOOL CONTRACTS REMAIN

MODEL MAY CHANGE
```

This enables later cross-model semantic-equivalence experiments without making any one model the canonical project memory.

## 7. Current Stella use — V2-03

For the current causal-dialogue frontier, the WARM envelope should load:

```text
latest V2-02 checkpoint
V2-03 causal contract
historical game pressure-test lessons
historical conversation pressure-test lessons
current build contract
open observations
research-to-implementation crosswalk
PR #3 validation status
```

Keep dormant unless specifically needed:

```text
SCOS
Sanctuary implementation
full companion model integration
final Mara embodiment
atmosphere implementation
large-population scaling
unrelated hardware work
```

## 8. Immediate V2-03 design consequences

The envelope currently yields four research-derived rules for V2-03A:

```text
1. REDUCE TO SIMPLE STATE TRANSITIONS
   before adding intelligence.

2. STORE CAUSES / REFERENCES / DELTAS
   rather than duplicated world copies.

3. CONVERSATION SEMANTICS ARE WORLD EVENTS;
   SURFACE WORDING IS PRESENTATION.

4. DESIGN FOR MODEL AND SIMULATION DEGRADATION
   from the beginning.
```

This implies that `stella_state` should favor:

```text
stable semantic IDs
versioned schema
causal event ledger
compact projections
replayable actor-scoped knowledge
explicit provenance
persistence adapter separation
future memory-class compatibility
```

and should avoid:

```text
renderer-local IDs as sole identity
giant duplicated actor copies
raw generated prose as sole conversation history
model-owned canonical memory
shutdown-only semantic persistence
silent reset on unknown schema
```

## 9. Fail-closed state handling

Unknown or invalid persisted semantic state should not silently become a fresh world.

```text
UNKNOWN_SCHEMA
or
INVALID_LEDGER
        -> STATE_LOAD_HOLD
        -> NO SEMANTIC WRITES
        -> PRESERVE EVIDENCE
```

Migration is explicit and versioned.

## 10. Workbench self-tests

The envelope should be considered useful only if it passes practical tests.

### Test A — currentness

Question: "What is safe next?"

Expected: old PASS evidence does not become fresh machine currentness.

### Test B — research relevance

Question: "What belongs in V2-03A?"

Expected: relevant historical game/language research is retrieved while unrelated project material remains dormant.

### Test C — semantic boundary

Question: "Can a model decide Mara directly saw the Gate?"

Expected: no; model inference cannot create DIRECT_OBSERVATION.

### Test D — context budget

Question: "Should all project history be active?"

Expected: no; archive remains retrievable without becoming the active working set.

### Test E — model replacement

Question: "Can another model express the same governed state?"

Expected: yes, if the semantic response contract and evidence are preserved.

## 11. Known gaps

Current gaps to investigate before claiming the workbench is mature:

```text
GAP-01 durable research-to-implementation crosswalk
GAP-02 document-currentness tracking
GAP-03 formal tool capability registry
GAP-04 shared work-event envelope
GAP-05 context compiler / retrieval policy implementation
GAP-06 cross-model semantic-equivalence harness
GAP-07 explicit project DORMANT/WARM/HOT/FOCUSED state manager
```

## 12. Authority boundary

This document is recoverable orientation and research.

Reading it later does not authorize:

```text
local machine mutation
GitHub mutation
runtime execution
network model use
dependency installation
canonical promotion
SCOS integration
```

Fresh currentness verification and appropriate explicit authorization remain required for consequential work.

## 13. Current classification

```text
WORKBENCH_VERSION=V0_1
STATUS=RESEARCH_PROTOTYPE
MODEL_CORE_MODIFIED=NO
STELLA_CANON_MODIFIED=NO
SCOS_MODIFIED=NO
LOCAL_MACHINE_MODIFIED=NO
MODEL_INDEPENDENCE_GOAL=YES
CURRENT_PRIMARY_USE=CONTEXT_DISCIPLINE_AND_RESEARCH_TO_IMPLEMENTATION_RECONCILIATION
```
