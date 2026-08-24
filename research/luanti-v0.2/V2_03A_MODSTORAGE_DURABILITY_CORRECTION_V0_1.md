# Stella Luanti V0.2 — V2-03A ModStorage Durability Correction V0.1

Status: **CORRECTION / RESEARCH-ONLY / NON-AUTHORITY / NON-CANONICAL**

## 1. Why this correction exists

During read-only pressure testing of `V2_03A_STATE_FOUNDATION_DESIGN_V0_1.md`, current Luanti persistence documentation exposed an overstatement in the draft design.

The draft said, in effect, that a Stella semantic transition should be considered committed only after the persistence adapter accepts a durable write.

That wording is too strong for Luanti `ModStorage`.

Current Luanti documentation describes `ModStorage` as per-world/per-mod persistent storage whose persisted snapshot granularity is controlled by the engine save interval. Therefore successful `ModStorage` mutation is not sufficient evidence that the change is already crash-durable on disk.

This correction narrows the claim before implementation.

## 2. Correct distinction

Use three distinct states:

```text
SEMANTIC_ACCEPTED_RUNTIME
  event passed Stella validation and was accepted into current runtime state

PERSISTENCE_SUBMITTED_TO_ADAPTER
  adapter accepted the corresponding ModStorage update

PERSISTENCE_REHYDRATED_PROVEN
  later controlled reload demonstrates that the semantic event survived persistence
```

Do not collapse them into one word such as `COMMITTED` without an explicit durability class.

## 3. Engine-managed persistence class

For the initial Luanti V0.2 adapter:

```text
PERSISTENCE_CLASS=ENGINE_MANAGED_INTERVAL
```

Meaning:

- Stella can submit updates through `ModStorage`;
- Luanti controls persistence snapshot timing;
- `set_string()` success does not independently prove immediate physical durability;
- a controlled restart can prove rehydration for the tested path;
- crash/power-loss durability remains a separate later experiment.

## 4. Revised V2-03A rule

Replace the overly strong design sentence with:

```text
A semantic event may become accepted runtime history only after
Stella validation succeeds and the persistence adapter accepts the
corresponding state update.

The receipt must record the durability class honestly.

For Luanti ModStorage V0.2, adapter acceptance is not equivalent to
immediate crash-durable persistence.

Persistence becomes PROVEN for the V2-03 slice only when the controlled
rehydration test observes the same semantic history after restart.
```

## 5. Receipt fields

Future receipts should distinguish:

```text
semantic_validation=PASS|FAIL
runtime_acceptance=YES|NO
persistence_adapter_update=ACCEPTED|REJECTED
persistence_class=ENGINE_MANAGED_INTERVAL
rehydration_proven=YES|NO
crash_durability_proven=YES|NO
```

For early V2-03 work, expected values before V2-03D are:

```text
rehydration_proven=NO
crash_durability_proven=NO
```

No earlier gate may silently relabel those fields as proven.

## 6. V2-03D scope clarification

V2-03D is the first gate intended to demonstrate ordinary restart/rehydration persistence for the causal distinction:

```text
Primary DIRECT=yes
Mara REPORTED=yes
Mara DIRECT=no
```

A successful graceful restart proves that tested rehydration path.

It does **not** automatically prove:

```text
power-loss durability
process-crash durability
filesystem corruption resistance
transactional atomicity under arbitrary failure
```

Those require separate fault-injection/durability work if Stella later needs that assurance.

## 7. Historical pressure-test consequence

This correction strengthens rather than weakens the retro/modern synthesis.

Older-console discipline asks:

```text
WHAT STATE EXISTS?
WHAT TRANSITION OCCURRED?
```

Modern engineering additionally asks:

```text
WHAT WAS ACCEPTED?
WHAT WAS SUBMITTED FOR PERSISTENCE?
WHAT WAS ACTUALLY REHYDRATED?
WHAT DURABILITY CLASS WAS PROVEN?
```

The event semantics remain engine-neutral even though the durability mechanism is adapter-specific.

## 8. Current effect on implementation plan

```text
V2_03A_FOUNDATION_DESIGN=STILL_PREPARED
MODSTORAGE_ADAPTER=STILL_PREFERRED_FOR_INITIAL_LUANTI_PROOF
IMMEDIATE_DURABILITY_CLAIM=REMOVED
V2_03D_REHYDRATION_PROOF=REQUIRED
CRASH_DURABILITY=FUTURE_GATED
LOCAL_MACHINE_MUTATION=NONE
CANONICAL_PROMOTION=NONE
```

## 9. Authority boundary

This correction is research evidence only. It does not authorize local mutation, runtime execution, GitHub promotion, dependency installation, network model use, SCOS integration, or canonical Stella promotion.
