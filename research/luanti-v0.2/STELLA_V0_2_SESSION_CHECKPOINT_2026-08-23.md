# Stella Luanti V0.2 — End-of-Night Session Checkpoint — 2026-08-23

Status: **ORIENTATION / EVIDENCE INDEX / NON-AUTHORITY / NON-CANONICAL**

This checkpoint records the governed working position reached during the 2026-08-23 local Stella Luanti V0.2 session. It is evidence and orientation only. Reading this file does not recover, imply, or grant authorization for any future action.

```text
CHECKPOINT_DATE=2026-08-23
CHECKPOINT_LOCAL_TIME_APPROX=21:58 America/Los_Angeles
REPOSITORY=BiologicalAGI/Stella-Prime
RESEARCH_BRANCH=research/luanti-v0.2-build-contract-2026-08-23

CURRENT_ACTIVE_CARD=NONE
STANDING_AUTHORIZATION=NONE
CANONICAL_PROMOTION=NONE
SCOS_INTEGRATION=NONE
NETWORK_MODEL_USE=NONE
```

## 1. Where are we?

The current local proof frontier is:

```text
V2-00R = PASS
V2-01  = PASS
V2-02  = PASS

CURRENT_PROOF_FRONTIER=
MARA_IDENTIFIABLE_VISIBLE_INTERACTION_SLICE_PROVEN

NEXT_GATE=V2-03
NEXT_GATE_STATUS=PREPARED_NOT_AUTHORIZED
```

Stella world semantics remain separate from Luanti. Luanti is the experimental renderer/body/interaction adapter. Mara remains the semantic inhabitant `actor.mara`; the current Luanti entity/body is presentation, not identity or epistemic authority.

## 2. What was last proven?

### V2-00R — fresh local V0.1 closure / V0.2 readiness

Fresh local evidence reconciled the prior closure position and established:

```text
WORLD_KERNEL_ROOT=C:\Users\travi\Desktop\STELLA_WORLD_KERNEL_V0_1
WORLD_KERNEL_RECURSIVE_FILE_COUNT=129

A18_PATH=C:\Users\travi\Desktop\STELLA_WORLD_KERNEL_V0_1\DEVELOPMENT_MEMORY\STELLA_A18_SEMANTIC_RESOLUTION_SYNTHESIS_CHECKPOINT_V0_1.md
A18_SHA256=45C26E2626E1950F1ACF1FFB63B6B9993FBBDEEF53A6918C145E2E6BD42CCB7F
A18_SIZE=16969

LUANTI_FILE_VERSION=5.17.0
LUANTI_EXE_SHA256=7091913D6C7D1FACCF0F1895A9C009FC51C8F409DFFD577ABF17BAFC6AA1715F

V0_1_PLAYGROUND=C:\Users\travi\Desktop\STELLA_LUANTI_PLAYGROUND_V0_1
V0_2_TARGET=C:\Users\travi\Desktop\STELLA_LUANTI_PLAYGROUND_V0_2
V0_2_TARGET_WAS_FREE_BEFORE_BUILD=YES
```

The collector's earlier `ACTIVE_LUANTI_VERSION_NOT_PARSEABLE` HOLD was reconciled as a metadata-format false HOLD: `ProductVersion=5.17`, `FileVersion=5.17.0`, and the executable hash matched the expected Luanti binary.

The earlier 513-file playground count and A18=0 observation were excluded from closure evidence because they were collected from the wrong scope/root. Corrected R3 evidence established the 129-file World Kernel count and exact A18 identity.

### V2-01 — isolated V0.2 shell

An isolated sibling was constructed and launched independently:

```text
TARGET_ROOT=C:\Users\travi\Desktop\STELLA_LUANTI_PLAYGROUND_V0_2
GAME_ID=stella_v0_2_shell
WORLD_ID=stella_v0_2_shell_world
MOD_ID=stella_shell
```

Construction evidence:

```text
V2_01A_RESULT=PASS_V2_01A_ISOLATED_SHELL_CONSTRUCTED
V2_01A_RECEIPT_SHA256=25EBA7BC0EE93A14892BE4FE01F825F6FBB76BE704D9B67AFF4215BE7420153A
SOURCE_V0_1_PROTECTED_HASHES_UNCHANGED=YES
LUANTI_LAUNCHED_DURING_V2_01A=NO
```

First controlled launch evidence:

```text
V2_01B_RESULT=PASS_V2_01B_CONTROLLED_FIRST_LAUNCH_EVIDENCE
OBSERVED_PROCESS_PATH_MATCHES_TARGET=YES
SHELL_LOAD_MARKER_COUNT=1
FATAL_ERROR_PATTERN_COUNT=0
POST_WORLD_FILE_COUNT=8
WORLD_MT_GAME_ID_IS_V0_2=YES
SOURCE_V0_1_PROTECTED_HASHES_UNCHANGED=YES
V0_2_CODE_AND_CONSTRUCTION_EVIDENCE_UNCHANGED=YES
```

V2-01 therefore proved isolated construction + isolated launch. It did not prove feature correctness or canonical promotion.

### V2-02 — Mara identifiable interaction slice

V2-02A built two new isolated V0.2 components:

```text
stella_dialogue
stella_inhabitants
SEMANTIC_MARA_ACTOR_REF=actor.mara
```

V2-02A build receipt:

```text
V2_02A_BUILD_RECEIPT_SHA256=B141B05A4FC9A40053CF354FA8FD072707AC1C8041C07D9825D98BD3654A15A0
```

Initial V2-02B playtest proved the interaction system but produced one human-facing HOLD:

```text
HUMAN_FOUND_MARA_WITHOUT_EXACT_KNOWLEDGE=YES
HUMAN_MARA_VISUALLY_DISTINGUISHABLE=NO
HUMAN_MARA_NAME_READABLE=YES
HUMAN_INTERACTION_CUE_UNDERSTANDABLE=YES
HUMAN_TARGET_FORGIVING=YES
HUMAN_DIALOGUE_OPENED=YES
HUMAN_QUESTION_RESPONSE_WORKED=YES
HUMAN_BACK_WORKED=YES
HUMAN_GOODBYE_WORKED=YES
HUMAN_DIALOGUE_REOPENED=YES
HUMAN_ESCAPE_RECOVERY_WORKED=YES

MACHINE_PROBLEM_COUNT=0
HUMAN_PROBLEM_COUNT=1
HUMAN_HOLD=HUMAN_PLAYTEST_RECOGNIZABLE
```

The observed defect was specific: the placeholder read as two pink cubes rather than as a recognizable person.

## 3. V2-02 repair lineage

The failure was preserved rather than relabeled.

### V2-02R1A — first visual repair attempt

A seven-part code-built humanoid presentation was prepared. A static checker incorrectly treated `.obj` inside ordinary Lua identifiers such as `self.object` / `parent_object` as an imported OBJ asset reference.

The transaction automatically rolled back:

```text
RESULT=HOLD_V2_02R1A_REPAIR_ROLLED_BACK
ROLLBACK_INHABITANTS_SHA256=CF863C16F97272A9D99A2030F153DD48B04CE6252ED88C6ED922B61C73BF1C3A
ROLLBACK_TO_PRE_REPAIR_STATE=YES
LUANTI_LAUNCHED=NO
```

This was a validator false positive, not a runtime or architectural failure.

### V2-02R1A-R1 — corrected visual repair

The corrected checker distinguished real asset-like extension references from Lua object identifiers.

```text
RESULT=PASS_V2_02R1A_R1_CORRECTED_MARA_VISUAL_REPAIR_BUILT
POST_REPAIR_INHABITANTS_INIT_SHA256=FB36E8B3ECE92DA6C73C23BDA88C5C53F6A3A92BA402328735800536B1725519
R1_REPAIR_RECEIPT_SHA256=76C103F80CE75915B74108D8DCF56BABD9FC79EA4679F019116BE33E58803119

VISIBLE_HUMANOID_PART_COUNT=7
EXTERNAL_ASSET_REFERENCE_COUNT=0
EXTERNAL_OBJ_ASSET_REFERENCE_COUNT=0
EXTERNAL_ASSETS=NONE
DIALOGUE_MUTATED=NO
V0_2_WORLD_MUTATED=NO
V0_1_MUTATED=NO
LUANTI_LAUNCHED=NO
```

Visible presentation parts:

```text
head
hair
torso
left_arm
right_arm
left_leg
right_leg
```

The presentation remains temporary, code-built, and presentation-only. The interaction root remains `actor.mara`.

### V2-02R1B — decisive human retest

The exact failed observation was retested without allowing the floating nameplate to serve as evidence.

```text
HUMAN_MARA_RECOGNIZABLE_WITHOUT_NAMEPLATE=YES
RECOGNIZABILITY_REPAIR_RESULT=HUMAN_PASS

HUMAN_TARGET_FORGIVING=YES
HUMAN_DIALOGUE_OPENED=YES
HUMAN_QUESTION_RESPONSE_WORKED=YES
HUMAN_BACK_WORKED=YES
HUMAN_GOODBYE_WORKED=YES
HUMAN_DIALOGUE_REOPENED=YES
HUMAN_ESCAPE_RECOVERY_WORKED=YES
```

Runtime corroboration:

```text
DIALOGUE_READY=1
MARA_READY=1
HUMANOID_PRESENTATION_READY=1
VISUAL_PART_FAILED=0
INTERACTION_STAGE_READY=1
DIALOGUE_OPEN=2
DIALOGUE_CHOICE=2
DIALOGUE_CLOSED=2
FATAL_ERROR_PATTERN_COUNT=0

SOURCE_V0_1_PROTECTED_HASHES_UNCHANGED=YES
V0_2_REPAIR_CODE_AND_RECEIPT_UNCHANGED=YES
```

Final gate classification:

```text
V2_02_FINAL_CLASSIFICATION=PASS
PASS_MARA_IDENTIFIABLE_AND_INTERACTION_SLICE_PROVEN
```

## 4. Current layer ownership

```text
WORLD KERNEL
  owns semantic truth, stable IDs, causal events, provenance,
  actor-scoped epistemic state, and persistence semantics.

LUANTI
  owns renderer/body/input/UI/execution projection only.

stella_shell
  owns experimental V0.2 shell identity and shell-load proof.

stella_dialogue
  owns visible dialogue, button interaction, and proposal/display surfaces.
  It does not create causal truth merely because a button is shown or clicked.

stella_inhabitants
  owns actor.mara -> Luanti embodiment mapping, presentation,
  selection target, and world-space interaction projection.

CURRENT MARA BODY
  is a temporary seven-part code-built humanoid presentation.
  It is not actor identity, semantic truth, final art, or epistemic authority.
```

Non-equivalence:

```text
actor.mara != current Luanti object
actor.mara != current humanoid block body
actor.mara != nametag
actor.mara != dialogue wording
```

## 5. Open observations carried forward

These observations did not block V2-02 but must not be silently normalized or forgotten.

### OPEN-01 — invalid mapgen stone alias

```text
OBSERVED=ERROR[ServerStart]: Mapgen alias 'mapgen_stone' is invalid!
STATUS=UNRESOLVED
BLOCKS_V2_02=NO
MUST_BE_REVISITED=YES
```

### OPEN-02 — invalid mapgen water alias

```text
OBSERVED=ERROR[ServerStart]: Mapgen alias 'mapgen_water_source' is invalid!
STATUS=UNRESOLVED
BLOCKS_V2_02=NO
MUST_BE_REVISITED=YES
```

### OPEN-03 — player appeared flying/floating

```text
SOURCE=HUMAN_OBSERVATION
STATUS=UNRESOLVED
BLOCKS_V2_02=NO
LIKELY_RELEVANT_TO=environment / movement / orientation
MUST_BE_REVISITED=YES
```

### OPEN-04 — Mara embodiment remains temporary

```text
CURRENT=code-built attached block humanoid
STATUS=INTENTIONAL_TEMPORARY_PRESENTATION
BLOCKS_V2_02=NO
FINAL_EMBODIMENT=NO
EXPECTED_LATER_HOME=V2-05
```

### OPEN-05 — runtime error-detector coverage

The V2-02R1B PowerShell fatal-pattern detector reported zero fatal patterns, while the visible Luanti client showed `ERROR[ServerStart]` mapgen alias messages. Future runtime harnesses must explicitly distinguish at least:

```text
FATAL
ERROR
WARNING
KNOWN_NONBLOCKING_OBSERVATION
```

No future test should equate `FATAL_ERROR_PATTERN_COUNT=0` with `NO_RUNTIME_ERRORS_OF_ANY_KIND`.

## 6. Prepared V2-03 causal contract

V2-03 is prepared conceptually but is not authorized for mutation.

Fundamental invariant:

```text
SEEING != BEING_TOLD
```

Required epistemic distinction:

```text
DIRECT_OBSERVATION(actor.primary, place.tide_gate)
!=
REPORT_RECEIVED(actor.mara, place.tide_gate)
```

Minimum intended sequence:

```text
P0 INITIAL
  Primary has not observed Gate.
  Mara has not received a report.

P1 PRIMARY_OBSERVED_GATE
  Primary DIRECT_OBSERVATION(place.tide_gate)=YES
  Mara DIRECT_OBSERVATION(place.tide_gate)=NO
  Mara REPORT_RECEIVED(place.tide_gate)=NO

P2 REPORT_AFFORDANCE_VALID
  "Tell Mara what I saw" may appear only because Primary
  possesses the causal prerequisite.

P3 REPORT_COMMITTED
  Primary observation remains.
  Mara receives REPORT.
  Mara does not receive DIRECT_OBSERVATION.

P4 MARA_ACKNOWLEDGES_PROVENANCE
  Mara may acknowledge that Primary told her.
  Mara may not claim that she saw the Gate.

P5 REHYDRATED
  After restart, the provenance distinction survives.
```

Minimum engine-neutral event vocabulary for the slice:

```text
event.world_entered.*
event.direct_observation.*
event.dialogue_choice_selected.*
event.report_offered.*
event.report_received.*
```

Critical forbidden consequence:

```text
NO event.direct_observation for actor.mara
may be synthesized merely because a report was received.
```

## 7. V2-03 falsification ladder

Each transition must be independently falsifiable.

```text
A. Before Primary observes the Gate:
   report affordance must NOT be available.

B. Legitimate Gate observation:
   Primary DIRECT_OBSERVATION becomes true from an attributable basis.

C. Projection:
   report affordance becomes available only after the prerequisite exists.

D. Report transaction:
   explicit player choice emits attributable report events.

E. Epistemic separation:
   Primary DIRECT=yes
   Mara REPORTED=yes
   Mara DIRECT=no

F. Dialogue wording:
   Mara may say "you told me" but may not claim "I saw it"
   from report-only knowledge.

G. Restart:
   the same provenance distinction survives persistence/rehydration.

H. Duplicate safety:
   reopening dialogue must not manufacture duplicate historical events.
```

## 8. Prepared V2-03 implementation split

Do not bundle the whole causal slice into one mutation.

```text
V2-03A
  stella_state foundation
  schema + ledger + persistence contract
  no Gate gameplay yet

V2-03B
  Gate observation source
  prove Primary DIRECT_OBSERVATION

V2-03C
  report affordance + causal transaction
  prove Mara REPORTED != DIRECT

V2-03D
  restart / persistence proof

V2-03E
  human-facing causal dialogue playtest
```

## 9. Intentionally out of scope

```text
Mara route knowledge=NO
Mara pathfinding=NO
Mara walking to Gate=NO
companion=NO
LLM/model=NO
network provider=NO
complex belief revision=NO
conflicting-report resolution=NO
Sanctuary=NO
final Mara model=NO
atmosphere pass=NO
canonical Stella promotion=NO
SCOS integration=NO
```

## 10. Recovery position for the next session

```text
WHERE_ARE_WE=
V2_02_MARA_IDENTIFIABLE_INTERACTION_SLICE_PROVEN

LAST_PROVEN=
PASS_V2_02R1B_MARA_RECOGNIZABILITY_AND_INTERACTION

WHY_STOPPED=
MEANINGFUL_PROOF_BOUNDARY_REACHED;
DO_NOT_BEGIN_CAUSAL_STATE_WITHOUT_FRESH_PRE-MUTATION_REVERIFY

SAFE_NEXT=
READ_ONLY_REVERIFY_OF_V2_02_CHECKPOINT_AND_OPEN_OBSERVATIONS

PREPARED_NEXT=
V2_03A_STELLA_STATE_FOUNDATION

CURRENT_AUTHORITY=
NONE_FOR_FURTHER_MACHINE_OR_GITHUB_MUTATION

REVERIFY_BEFORE_MUTATION=
V0_1 protected hashes;
V0_2 executable identity;
V2_02 active inhabitants hash;
V2_02 repair receipt hash;
stella_dialogue hash;
world identity;
Luanti process quiescence;
V2_03 target files absent/free;
open-observation standing

HOLDS=
invalid mapgen alias observations;
player flying/floating observation;
temporary Mara embodiment;
runtime error-detector coverage

CANONICAL_PROMOTION=NONE
SCOS_INTEGRATION=NONE
NETWORK_MODEL_USE=NONE
ACTIVE_CARD=NONE
```

## 11. Authority and promotion rules preserved

```text
CAN_DO != MAY_DO
WAS_TRUE != IS_TRUE_NOW
TEST_PASSED != CANONICAL
GITHUB_ARTIFACT != LOCAL_MACHINE_STATE
MODEL_PROPOSAL != AUTHORIZATION
DEPENDENCY_AVAILABLE != DEPENDENCY_APPROVED
```

This checkpoint records what was proven and prepared. It grants no standing authority, does not promote V0.2 into canonical Stella, and does not establish future machine currentness merely because the file exists.

## Recovery classification

```text
PASS_FOR_ORIENTATION
HOLD_FOR_FURTHER_MUTATION_PENDING_FRESH_REVERIFY_AND_EXPLICIT_AUTHORIZATION
```
