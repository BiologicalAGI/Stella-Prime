# V2-00R — Acceptance Contract

Status: **PREPARED / READ-ONLY GATE**

PASS only if fresh local observation establishes all required currentness facts without mutation:

- expected host/session identified;
- V0.1 playground resolved;
- visible launcher resolved or discrepancy explained;
- Luanti executable/version resolved;
- relevant executable hash captured;
- no unexplained relevant Luanti/server process remains active;
- evidence/receipt/checkpoint candidates enumerated and hashed where available;
- isolated V0.2 target path is free or an alternate is explicitly selected later;
- no download/install/network/file mutation/process mutation/Git mutation/SCOS mutation occurs.

HOLD if any required fact cannot be established or a target/path/version discrepancy exists.

FAIL if the card itself causes mutation or observed state contradicts a required safety invariant.

A PASS authorizes nothing by itself. It only makes V2-01 eligible to be separately scoped.