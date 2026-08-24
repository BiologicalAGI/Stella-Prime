# Stella Luanti V0.2 — Proof Test Matrix V0.1

Status: **RESEARCH / NON-CANONICAL**

This matrix turns the build ladder into independently falsifiable proofs. A later stage cannot retroactively pass an earlier stage.

| Gate | Proof target | Must prove | Must not infer | Result |
|---|---|---|---|---|
| V2-00R | Fresh local reverify | current executable/version, paths, receipts/hashes, process state, target isolation | old packet = current machine | PENDING |
| V2-01 | Isolated shell | V0.2 launches separately and cannot overwrite V0.1/canonical Stella | launch = feature correctness | PENDING |
| V2-02 | Interaction slice | Mara identifiable; prompt/target/dialogue usable without command knowledge | visible choice = causal truth | PENDING |
| V2-03 | Causal dialogue | Primary direct observation persists; Mara receives REPORT only; restart preserves distinction | report = direct observation | PENDING |
| V2-04 | Orientation | objectives, guidance, recovery and re-entry work without exact typing/color-only/chat-only dependence | formspec alone = accessibility | PENDING |
| V2-05 | Embodiment | mesh/nametag/animation improve character presentation without changing epistemic state | animation = intent/fact | PENDING |
| V2-06 | Atmosphere | cues/sound/particles improve legibility while remaining presentation-only | presentation = event | PENDING |
| V2-07 | Route knowledge | actor-scoped route evidence precedes journey/path execution | pathfinder output = route knowledge | PENDING |
| V2-08 | Companion C0/C1 | observation/follow/wait/point/lead through typed deterministic contracts | companion expression = authority | PENDING |
| V2-09 | Companion C2/C3 | bounded context/model adapter; default network OFF; proposal-only actions | provider connectivity = permission | PENDING |
| V2-10 | Surprise | presentation-only surprises do not mutate truth; causal surprises separately gated | hidden content = hidden authority | PENDING |

## Cross-cutting invariants

Every gate checks where relevant:

- zero unintended canonical Stella mutation;
- zero SCOS mutation unless separately authorized;
- zero hidden network use;
- zero untracked external assets;
- zero critical chat-only feedback;
- no exact typing required for normal play;
- no color-only critical meaning;
- restart/persistence semantics remain explicit;
- event provenance remains attributable;
- renderer-local coordinates/IDs do not become sole canonical identity.

## Input/accessibility proof for V2-02 / V2-04

Because Luanti 5.17 gamepad support does not make formspec interaction itself a gamepad-complete accessibility solution, test interaction as a system rather than as one widget:

1. mouse/keyboard normal interaction;
2. large forgiving world-space target;
3. clear focus/escape behavior;
4. visible recovery outside critical chat text;
5. Guidance OFF/SUBTLE/STANDARD/FULL;
6. `WHAT_DO_I_DO_NEXT` independent of guidance level;
7. critical cues use text plus at least one additional non-color channel;
8. failure or cancellation returns to a comprehensible state.

## Result vocabulary

- `PASS` — required observations directly demonstrated.
- `HOLD` — insufficient/currentness evidence or a prerequisite unresolved.
- `FAIL` — observed behavior violates the gate.
- `REPAIR_FIRST` — failure is understood and bounded enough to repair before continuing.
- `FUTURE_GATED` — intentionally outside the active proof.

No `PASS` may be inherited solely from design intent.