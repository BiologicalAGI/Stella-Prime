# Stella Research-to-Implementation Crosswalk V0.1

Status: **RESEARCH INDEX / IMPLEMENTATION ORCHESTRATION / NON-AUTHORITY / NON-CANONICAL**

## 1. Purpose

This crosswalk prevents Stella research from becoming an archive of good ideas that are never connected to implementation.

It answers, for each research finding:

```text
WHAT DID WE LEARN?
WHAT HAS ALREADY BEEN USED?
WHAT IS ONLY PREPARED?
WHAT WAS DELIBERATELY DEFERRED?
WHAT WAS ACCIDENTALLY LEFT WITHOUT A GATE?
WHEN DOES IT BECOME ELIGIBLE?
WHAT WOULD PROVE IT?
```

The crosswalk does **not** turn recorded research into an implementation queue and does not grant authorization.

## 2. Status vocabulary

```text
PROVEN             directly demonstrated by existing evidence
PARTIALLY_USED     influences current architecture but lacks its full proof
PREPARED           design exists; implementation/proof not yet performed
DEFERRED           intentionally later
NOT_IMPLEMENTED    researched but no implementation exists
REJECTED           investigated and intentionally not adopted
CURRENTNESS_DRIFT  older orchestration text no longer matches newer evidence
```

## 3. Source families

Primary Stella research families currently represented:

```text
A. STELLA_HISTORICAL_PRESSURE_TEST_AND_COGNITIVE_ARCHITECTURE_V0_1
B. STELLA V0.2 EXPERIENCE BLUEPRINT / BUILD CONTRACT
C. V2 PROOF TEST MATRIX / NEXT GATE MAP
D. V2-02 END-OF-NIGHT SESSION CHECKPOINT
E. ENGINE / UX / ACCESSIBILITY RESEARCH
F. MODEL / RETRIEVAL / COMPANION RESEARCH
G. LOCAL V0.1 / V0.2 PROOF RECEIPTS
```

## 4. Core historical game-system crosswalk

### RG-001 — Circuit / irreducible state-transition test

```text
SOURCE_FAMILY=A
CORE_LESSON=INPUT -> STATE -> TRANSITION -> OUTPUT before presentation or intelligence
STATUS=PARTIALLY_USED
CURRENT_OWNER=stella_state
EARLIEST_GATE=V2-03A
PROOF_NEEDED=Gate/report semantics remain correct when reduced to minimal symbolic state
DO_NOT_CONFUSE_WITH=rich UI or model behavior proving semantic correctness
```

Implementation consequence:

- represent direct observation and report receipt as explicit transitions;
- keep presentation and interpretation outside causal truth.

### RG-002 — Atari / minimum active-state test

```text
SOURCE_FAMILY=A
CORE_LESSON=EXISTS_IN_WORLD != MUST_BE_HOT; HAS_HISTORY != FULL_HISTORY_TOUCHED_EACH_TICK
STATUS=PREPARED
CURRENT_OWNER=stella_state / future simulation scheduler
EARLIEST_GATE=V2-03A architecture constraint
FULL_EXPERIMENT=post-V2-03 causal foundation
PROOF_NEEDED=correct state with bounded active working set
```

### RG-003 — 8-bit compact-world representation

```text
SOURCE_FAMILY=A
CORE_LESSON=shared tables + stable IDs + sparse state + causes/references/deltas
STATUS=PARTIALLY_USED
CURRENT_OWNER=stella_state
EARLIEST_GATE=V2-03A
PROOF_NEEDED=actor knowledge references shared semantic IDs without duplicating canonical geography
```

### RG-004 — Text/MUD logical-world test

```text
SOURCE_FAMILY=A
CORE_LESSON=world capability must remain coherent without graphics
STATUS=PARTIALLY_USED
CURRENT_OWNER=World Kernel + all adapters
EARLIEST_GATE=V2-03
PROOF_NEEDED=causal dialogue state can be inspected/replayed without Luanti presentation
```

### RG-005 — Elite / procedural-local-bubble principle

```text
SOURCE_FAMILY=A
CORE_LESSON=PROCEDURAL_BASELINE + HISTORICAL_DELTAS = CURRENT_WORLD
STATUS=PREPARED
CURRENT_OWNER=future world simulation
EARLIEST_GATE=post-V2-03 for architecture; later world-scaling experiment for implementation
PROOF_NEEDED=deterministic reconstruction preserves causal history
```

### RG-006 — X/X3 multi-resolution simulation

```text
SOURCE_FAMILY=A
CORE_LESSON=simulation fidelity may vary; causal and epistemic law may not
STATUS=PREPARED
CURRENT_OWNER=future simulation scheduler
EARLIEST_GATE=after V2-03; before population-scaling claims
PROOF_NEEDED=lower-resolution distant simulation yields same causal/epistemic result as focused simulation for test fixture
```

### RG-007 — Modern replay/provenance/migration discipline

```text
SOURCE_FAMILY=A/B/G
CORE_LESSON=stable IDs + deterministic replay + provenance + versioned schemas + migration + renderer independence
STATUS=PARTIALLY_USED / SOME COMPONENTS PROVEN IN V0.1
CURRENT_OWNER=World Kernel / stella_state
EARLIEST_GATE=V2-03A
PROOF_NEEDED=V2-03 history survives persistence/rehydration and remains attributable
```

## 5. Historical conversation / language crosswalk

### RL-001 — ELIZA reaction boundary

```text
SOURCE_FAMILY=A
CORE_LESSON=LINGUISTIC_REACTION != WORLD_COGNITION
STATUS=PREPARED_AS_TEST_LENS
CURRENT_OWNER=stella_dialogue / future language adapter
EARLIEST_GATE=V2-03E
PROOF_NEEDED=fixed response can express legitimate state without creating new truth
```

### RL-002 — PARRY persistent character-state boundary

```text
SOURCE_FAMILY=A
CORE_LESSON=character state can alter response selection without a general language model
STATUS=NOT_IMPLEMENTED
CURRENT_OWNER=future inhabitant cognition / dialogue policy
EARLIEST_GATE=post-V2-03 deterministic dialogue work
PROOF_NEEDED=state-dependent semantic response changes while fluency layer remains replaceable
```

### RL-003 — AIML-like epistemic deterministic fallback

```text
SOURCE_FAMILY=A
CORE_LESSON=transparent rules can enforce legitimate character knowledge
STATUS=NOT_IMPLEMENTED
CURRENT_OWNER=stella_dialogue / language policy
EARLIEST_GATE=V2-03E or immediate post-V2-03
PROOF_NEEDED=reported-only Mara can state report provenance and cannot claim direct sight
```

Reference semantic condition:

```text
DIRECT_KNOWLEDGE(TIDE_GATE)=false
REPORTED_KNOWLEDGE(TIDE_GATE)=true
```

Permitted meaning:

```text
I have not seen it; I have only been told about it.
```

### RL-004 — Retrieval-based memory selection

```text
SOURCE_FAMILY=A/F
CORE_LESSON=do not put an inhabitant's entire lifetime into every context; retrieve bounded relevant memory with provenance
STATUS=NOT_IMPLEMENTED
CURRENT_OWNER=future memory/retrieval adapter
EARLIEST_GATE=pre-model V2-09 preparation
PROOF_NEEDED=relevant memory retrieval without unrelated-history leakage or provenance loss
```

### RL-005 — Statistical/small-model language realization

```text
SOURCE_FAMILY=A/F
CORE_LESSON=fluency can improve expression without owning world knowledge
STATUS=NOT_IMPLEMENTED
CURRENT_OWNER=model adapter
EARLIEST_GATE=V2-09
PROOF_NEEDED=same semantic response contract survives deterministic and small-model realizers
```

### RL-006 — Transformer / LLM realization

```text
SOURCE_FAMILY=A/F
CORE_LESSON=LLM value is phrasing, ambiguity resolution, repair, humor, explanation, negotiation, storytelling, style—not canonical truth
STATUS=NOT_IMPLEMENTED
CURRENT_OWNER=model adapter
EARLIEST_GATE=V2-09
PROOF_NEEDED=generated response remains within permitted semantic claims
```

### RL-007 — Tool/agent port boundary

```text
SOURCE_FAMILY=A/B/F
CORE_LESSON=model requests bounded observations/actions through typed Stella capabilities; model does not receive raw world authority
STATUS=PREPARED
CURRENT_OWNER=stella_companion_port
EARLIEST_GATE=V2-08 deterministic contract; V2-09 model adapter
PROOF_NEEDED=typed proposal -> policy decision -> deterministic executor -> receipt
```

### RL-008 — Graceful model degradation

```text
SOURCE_FAMILY=A/F
CORE_LESSON=MARA SHOULD SURVIVE MODEL REPLACEMENT
STATUS=PREPARED
CURRENT_OWNER=language adapter / inhabitant architecture
EARLIEST_GATE=V2-09 acceptance
PROOF_NEEDED=rich model -> small model -> retrieval+rules -> deterministic dialogue with durable Mara state intact
```

### RL-009 — Cross-model semantic equivalence

```text
SOURCE_FAMILY=A/F
CORE_LESSON=different language engines may vary wording but must preserve permitted meaning and forbidden claims
STATUS=NOT_IMPLEMENTED
CURRENT_OWNER=model-independent response contract
EARLIEST_GATE=V2-09
PROOF_NEEDED=multiple realizers produce semantically equivalent governed responses over identical Stella state
```

## 6. Conversation-as-world-event crosswalk

### RC-001 — Semantic conversation event

```text
SOURCE_FAMILY=A
CORE_LESSON=SURFACE_WORDING != CAUSAL_SEMANTICS
STATUS=PREPARED
CURRENT_OWNER=stella_state + stella_dialogue boundary
EARLIEST_GATE=V2-03C
```

Minimum future event meaning should be able to represent:

```text
speaker_ref
listener_ref
speech_act
claim_ref
basis_refs
heard_or_received_status
semantic_consequence
surface_utterance_as_presentation
```

The stored causal result must remain understandable if surface wording or language model changes.

### RC-002 — Claim identity

```text
CORE_LESSON=conversation history should reference semantic claims rather than depend on prose reconstruction
STATUS=NOT_IMPLEMENTED
EARLIEST_GATE=V2-03C schema hook
FULL_EXPANSION=later conversation system
PROOF_NEEDED=same claim can be expressed by different surface utterances without changing event meaning
```

### RC-003 — Report provenance

```text
CORE_LESSON=REPORT_RECEIVED never becomes DIRECT_OBSERVATION
STATUS=PREPARED / CENTRAL V2-03 TARGET
EARLIEST_GATE=V2-03C
PROOF_NEEDED=Primary DIRECT=yes; Mara REPORTED=yes; Mara DIRECT=no
```

## 7. Candidate inhabitant memory classes

Research currently proposes:

```text
EPISODIC
SEMANTIC
REPORTED
PROCEDURAL
RELATIONAL
CONVERSATIONAL
CULTURAL
SELF_HISTORY
```

These are not all V2-03 requirements.

### RM-001 — direct/reported foundation

```text
STATUS=PREPARED
EARLIEST_GATE=V2-03
```

### RM-002 — procedural / route memory

```text
STATUS=DEFERRED
EARLIEST_GATE=V2-07
```

### RM-003 — conversational / retrieved memory

```text
STATUS=DEFERRED
EARLIEST_GATE=V2-09
```

### RM-004 — episodic / semantic / relational / cultural / self-history expansion

```text
STATUS=DEFERRED
EARLIEST_GATE=post-V0.2 inhabitant expansion unless an earlier proof requires a minimal hook
```

Schema rule now:

```text
DO NOT MODEL KNOWLEDGE AS ONE BOOLEAN
```

V2-03 should remain small while allowing later evidence classes.

## 8. Cognitive / simulation level-of-detail crosswalk

### RS-001 — DORMANT

Minimal durable identity + scheduled causal references.

```text
STATUS=PREPARED
EARLIEST_EXPERIMENT=after V2-03
```

### RS-002 — WARM

Compact state + knowledge + relationship references + future activity.

```text
STATUS=PREPARED
EARLIEST_EXPERIMENT=after V2-03
```

### RS-003 — HOT

Near-term decision state and immediate intent.

```text
STATUS=PREPARED
EARLIEST_EXPERIMENT=after V2-03
```

### RS-004 — FOCUSED

Detailed perception / encounter / conversation / local reasoning / rich presentation.

```text
STATUS=PREPARED
EARLIEST_EXPERIMENT=after deterministic causal dialogue exists
```

### RS-005 — HISTORY

Durable archive remains retrievable without being processed every decision.

```text
STATUS=PARTIALLY_USED_AS_ARCHITECTURAL_PRINCIPLE
EARLIEST_GATE=V2-03 persistence design
```

Central scaling hypothesis remains unproven:

```text
MANY INHABITANTS MAY EXIST
!=
MANY FULL HISTORIES MUST BE HOT

MANY INHABITANTS MAY EXIST
!=
ALL INHABITANTS MUST THINK EVERY TICK
```

## 9. V0.2 gameplay / UX crosswalk

### UX-001 — recognition over recall

```text
STATUS=PARTIALLY_PROVEN_BY_V2-02
OWNER=stella_experience / stella_dialogue / stella_inhabitants
NEXT_GATE=V2-04
```

Rules:

```text
no exact spelling for normal play
no required slash commands
no critical chat-only information
no color-only critical meaning
large forgiving interaction targets
plain-language recovery
```

### UX-002 — What do I do next?

```text
STATUS=PREPARED
OWNER=stella_experience
EARLIEST_GATE=V2-04
PROOF_NEEDED=recovery works independently of ambient guidance level
```

### UX-003 — Guidance levels

```text
OFF
SUBTLE
STANDARD
FULL
```

```text
STATUS=PREPARED
EARLIEST_GATE=V2-04
```

### UX-004 — re-entry recap

```text
STATUS=PREPARED
EARLIEST_GATE=V2-04
CORE_LESSON=memory serves orientation without rewriting world truth
```

### UX-005 — Mara recognizable embodiment

```text
STATUS=V2-02 TEMPORARY RECOGNIZABILITY PROVEN; FINAL EMBODIMENT DEFERRED
EARLIEST_GATE=V2-05
```

## 10. World / navigation crosswalk

### RN-001 — semantic place graph

```text
STATUS=PREPARED
OWNER=stella_navigation
EARLIEST_GATE=V2-07
```

### RN-002 — path exists != actor knows path

```text
STATUS=PREPARED / CORE INVARIANT
EARLIEST_GATE=V2-07
PROOF_NEEDED=pathfinder output cannot grant route knowledge
```

### RN-003 — route knowledge distinctions

Future proof must preserve:

```text
KNOW_OF_PLACE != KNOW_WHERE_IT_IS
KNOW_WHERE_IT_IS != KNOW_ROUTE
PARTIAL_ROUTE != COMPLETE_ROUTE
MAP_DERIVED_ROUTE != DIRECTLY_TRAVELED_ROUTE
REPORTED_DIRECTIONS != DIRECTLY_EXPERIENCED_ROUTE
CANONICAL_WORLD_GRAPH != INHABITANT_ROUTE_KNOWLEDGE
```

```text
STATUS=PREPARED
EARLIEST_GATE=V2-07
```

### RN-004 — historical route pressure test

Apply circuit, Atari, 8-bit, MUD, Elite, multi-resolution, deterministic dialogue, LLM and modern replay tests to the same route capability.

```text
STATUS=PREPARED
EARLIEST_GATE=V2-07
```

## 11. Companion crosswalk

### CP-001 — C0 observer companion

```text
STATUS=DEFERRED
EARLIEST_GATE=V2-08
MODEL_REQUIRED=NO
```

### CP-002 — C1 deterministic companion

```text
ACTIONS=follow / wait / come / point / lead to legitimately known target
STATUS=DEFERRED
EARLIEST_GATE=V2-08
MODEL_REQUIRED=NO
```

### CP-003 — C2 conversational companion

```text
STATUS=DEFERRED
EARLIEST_GATE=V2-09
WORLD_ACTIONS=typed deterministic only
```

### CP-004 — C3 model adapter

```text
STATUS=DEFERRED
EARLIEST_GATE=V2-09
NETWORK_DEFAULT=OFF
```

### CP-005 — C4 governed selected continuity

```text
STATUS=DEFERRED
EARLIEST_GATE=after C2/C3 proof
RULE=no indiscriminate transcript dump
```

### CP-006 — C5 Sanctuary-capable companion

```text
STATUS=DEFERRED
EARLIEST_GATE=separate future Sanctuary proof
```

## 12. Presentation / atmosphere crosswalk

### PA-001 — atmosphere is presentation, not authority

```text
STATUS=PREPARED
EARLIEST_GATE=V2-06
```

Invariant:

```text
SOUND != WORLD FACT
PARTICLE != KNOWLEDGE
MUSIC != INTENT
LIGHTING != CAUSAL EVENT
```

### PA-002 — authored landmarks as spatial language

```text
STATUS=PREPARED
EARLIEST_GATE=V2-06; feeds V2-07
```

### PA-003 — recurring motifs may matter without being mechanically exhausted

```text
STATUS=DESIGN PRINCIPLE
EARLIEST_GATE=V2-06
```

## 13. Dependency / asset crosswalk

### DA-001 — native-first dependency rule

```text
DEFAULT=build small native Stella component
STATUS=ACTIVE DESIGN RULE
```

Adopt dependency only when substantial complexity is removed, maintenance/license/transitive surface are understood, failure is isolatable, and Stella can survive removal.

### DA-002 — Flow vs native formspec A/B

```text
STATUS=PREPARED / UNRESOLVED
EARLIEST_GATE=V2-04 or later dialogue UI refinement
DEPENDENCY=Flow + formspec_ast if chosen
PROOF_NEEDED=readability, sizing, accessibility, resizing, state handling, dependency cost, testability
```

### DA-003 — third-party evidence ledger

```text
STATUS=PREPARED
EARLIEST_GATE=before external art/audio/code enters build
```

No mystery assets.

## 14. Engine-independence crosswalk

### EI-001 — Luanti is experimental body

```text
STATUS=ACTIVE ARCHITECTURAL RULE
```

### EI-002 — Godot is future adapter candidate

```text
STATUS=DEFERRED
TRIGGER=presentation becomes primary constraint rather than causal architecture
```

### EI-003 — renderer-specific identifiers cannot become semantic identity

```text
STATUS=ACTIVE RULE
EARLIEST_GATE=all gates
```

## 15. Experimental program not yet represented as explicit V2 gates

These research items require future placement rather than being silently forgotten.

### EP-001 — bounded real-runtime throughput benchmark

```text
STATUS=NOT_IMPLEMENTED
PROPOSED_EARLIEST_POINT=after V2-03 causal unit is stable
```

### EP-002 — runtime memory measurement

```text
STATUS=NOT_IMPLEMENTED
PROPOSED_EARLIEST_POINT=after V2-03D persistence proof
```

### EP-003 — Stella Simulation Unit definition

```text
STATUS=NOT_IMPLEMENTED
PROPOSED_EARLIEST_POINT=after one complete V2-03 causal interaction can be measured
```

### EP-004 — retro-budget representation experiments

```text
STATUS=NOT_IMPLEMENTED
PROPOSED_EARLIEST_POINT=V2-03 foundation can host first minimal-state comparison
```

Suggested profiles for later experiment:

```text
CIRCUIT
ATARI-LIKE
8BIT-LIKE
16BIT-LIKE
32BIT-LIKE
MODERN
```

These are conceptual resource profiles, not current console ports.

### EP-005 — compact stable-ID / shared-template experiment

```text
STATUS=PARTIALLY_USED
PROPOSED_EARLIEST_POINT=V2-03A implementation measurement
```

### EP-006 — synthetic population scaling

```text
SEQUENCE=1 -> 10 -> 100 -> 1,000 -> 10,000 and beyond only when justified
STATUS=NOT_IMPLEMENTED
PROPOSED_EARLIEST_POINT=after multi-resolution inhabitant model exists
```

No population maximum is currently proven.

## 16. Current V2 gate overlay

### V2-03 — causal dialogue / epistemic persistence

Research items eligible now:

```text
RG-001 circuit transition test
RG-002 minimum active-state constraint
RG-003 compact shared-ID representation
RG-004 logical-world independence
RG-007 replay/provenance/migration
RC-001 semantic conversation event
RC-002 claim identity hook
RC-003 report provenance
RM-001 direct/reported foundation
RS-005 history != active working set
EP-004 retro-budget representation experiment foundation
EP-005 compact stable-ID measurement
```

Potential deterministic dialogue items near V2-03E:

```text
RL-001 ELIZA boundary test
RL-002 PARRY-style state response
RL-003 AIML-like epistemic fallback
```

### V2-04 — orientation / accessibility

Eligible:

```text
UX-001 through UX-004
DA-002 Flow/native UI A/B if needed
```

### V2-05 — Mara embodiment

Eligible:

```text
UX-005
EI-003 renderer identity separation
```

### V2-06 — atmosphere / authored spatial language

Eligible:

```text
PA-001 through PA-003
DA-003 third-party asset ledger before imports
```

### V2-07 — route knowledge

Eligible:

```text
RN-001 through RN-004
RM-002 procedural memory
```

### V2-08 — deterministic companion

Eligible:

```text
CP-001
CP-002
RL-007 typed tool/agent port foundation
```

### V2-09 — retrieval / language-model gate

Eligible:

```text
RL-004 retrieval
RL-005 small model
RL-006 large model
RL-007 typed model/tool boundary
RL-008 graceful degradation
RL-009 cross-model semantic equivalence
RM-003 conversational/retrieved memory
CP-003
CP-004
```

### V2-10 — governed surprise

Eligible:

```text
presentation-only surprise first
causal surprise separately classified and gated
```

### Future — Sanctuary

Eligible only after explicit private-context / memory / authority contract survives its own proof.

## 17. Current research-debt findings

### RD-001 — orchestration currentness drift

Newer end-of-night evidence records:

```text
V2-00R=PASS
V2-01=PASS
V2-02=PASS
NEXT=V2-03
```

Older test/gate orchestration documents still contain earlier PENDING / V2-00R-next language.

```text
STATUS=CURRENTNESS_DRIFT
ACTION=do not rewrite until fresh local reverify confirms the current working position
```

### RD-002 — research program not fully visible in V2 ladder

```text
STATUS=CONFIRMED
ACTION=this crosswalk supplies the missing overlay
```

### RD-003 — language-history experiments lack explicit subgates

```text
STATUS=CONFIRMED
ACTION=attach deterministic/retrieval/model experiments to V2-03E and V2-09 instead of creating unbounded parallel implementation
```

### RD-004 — simulation scaling lacks explicit future gate

```text
STATUS=CONFIRMED
ACTION=preserve as post-foundation experimental program; do not make scale claims early
```

## 18. Today's V2-03 application

Before local mutation, the current design should incorporate:

```text
1. SIMPLE TRANSITION FIRST
2. STABLE SEMANTIC IDS
3. CAUSES / REFERENCES / DELTAS
4. VERSIONED EVENT LEDGER
5. ACTOR-SCOPED KNOWLEDGE PROVENANCE
6. CONVERSATION SEMANTICS SEPARATE FROM WORDING
7. CLAIM / SPEECH-ACT HOOKS WITHOUT BUILDING FULL NLP
8. HISTORY REPLAYABLE WITHOUT ALL HISTORY HOT
9. MODEL INDEPENDENCE FROM DAY ONE
10. FAIL CLOSED ON UNKNOWN SCHEMA / INVALID LEDGER
```

Do not expand V2-03 into route knowledge, full memory taxonomy, companion, LLM, atmosphere, final Mara art, or Sanctuary.

## 19. Crosswalk update rule

When a proof closes:

```text
1. identify research items exercised;
2. attach evidence references;
3. change status only when proof supports it;
4. record newly eligible research items;
5. preserve deferred items explicitly;
6. never inherit authorization from eligibility.
```

A completed gate should therefore answer:

```text
WHAT DID THIS PROVE?
WHAT RESEARCH DID IT CASH IN?
WHAT DID IT MAKE ELIGIBLE NEXT?
WHAT REMAINS DELIBERATELY DORMANT?
```

## 20. Authority boundary

This crosswalk is orientation and research orchestration only.

It does not authorize local mutation, GitHub mutation, runtime execution, dependency installation, network model use, canonical promotion, SCOS integration, or Sanctuary context change.

Fresh currentness and appropriate explicit authorization remain required.
