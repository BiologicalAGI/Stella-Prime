# V2-00R — Acceptance Contract

Status: **PREPARED / READ-ONLY GATE**

## Two-step proof rule

V2-00R is intentionally split into:

1. **fresh local evidence collection**; and
2. **reconciliation/classification** against prior receipts/baselines plus the live authority context.

The PowerShell card may report that evidence collection completed cleanly, but it must **not self-award the final V2-00R PASS**.

## Evidence collection is complete only if

- host/session identified;
- visible Desktop resolved from current system sources rather than assumed from an old packet;
- V0.1 playground resolved or a discrepancy explicitly surfaced;
- visible launcher resolved or discrepancy surfaced;
- Luanti executable resolved with version and SHA256;
- active executable is not ambiguous;
- Luanti version is compatible with the current V0.2 research target (5.17.0+), or discrepancy is surfaced;
- no unexplained relevant Luanti/server process remains active;
- evidence/receipt/checkpoint candidates are enumerated and hashed;
- isolated V0.2 target path is free or collision is surfaced;
- no download/install/network/file mutation/process mutation/Git mutation/SCOS mutation occurs.

## Final V2-00R PASS requires subsequent reconciliation

PASS only if the fresh output is reviewed and the required currentness facts are consistent with the relevant prior receipts/baselines, with discrepancies explained rather than silently ignored.

A clean evidence-collection run is therefore **necessary but not sufficient** for final V2-00R PASS.

## HOLD

HOLD if:

- any required current fact cannot be established;
- multiple candidates make active state ambiguous;
- expected path/version/currentness differs without explanation;
- receipt/baseline reconciliation is unavailable or unresolved;
- a relevant process is active and unexplained;
- the V0.2 isolation target collides with existing material.

## FAIL

FAIL if the card itself causes prohibited mutation or observed state directly contradicts a required safety invariant.

## Authority rule

A final V2-00R PASS authorizes nothing by itself. It only makes V2-01 eligible to be separately scoped and explicitly authorized.
