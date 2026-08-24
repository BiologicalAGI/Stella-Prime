# Stella Luanti V0.2 — Dependency Decision Register V0.1

Status: **RESEARCH / NO INSTALL AUTHORITY IMPLIED**

| Candidate | Role | Current disposition | Required proof before adoption |
|---|---|---|---|
| Native Luanti formspecs | Mara/dialogue/recovery UI | BASELINE PROTOTYPE | readability, focus/escape behavior, resizing, input accessibility, maintenance |
| Flow | higher-level UI layout | A/B CANDIDATE | compare against native; confirm maintenance/license/transitive dependency cost |
| formspec_ast | Flow dependency | TRANSITIVE CANDIDATE | only if Flow wins; inspect license/API/removal path |
| Miney | Python/Luanti bridge prior art | STUDY / LAB ONLY | do not expose raw API to model; compare against narrower custom bridge for C0/C1 |
| LLM Connect | OpenAI-compatible integration prior art | FEASIBILITY REFERENCE | never architectural authority; model integration waits for C0/C1 proof |
| Yourland Speak Up / Simple Dialogs | NPC/dialogue patterns | STUDY PATTERNS | no wholesale adoption without API/license fit |
| Ambient/atmosphere components | environmental sound | FUTURE CANDIDATE | licensing, layering behavior, removal path, no causal ownership |
| glTF Mara model/assets | inhabitant embodiment | UNSELECTED | source, author, license, animation-track suitability, attribution, provenance hash |
| Godot | future renderer/body | FUTURE ADAPTER | only reconsider when Luanti presentation becomes proven constraint |

## Decision rule

Default = small native Stella component.

Dependency adoption requires all of:

1. substantial complexity saved;
2. credible maintenance/current compatibility;
3. understood license;
4. known transitive dependencies;
5. narrow/isolate-able API surface;
6. graceful failure/removal path;
7. provenance/attribution ledger completion;
8. no transfer of causal/world authority to the dependency.

## Explicit non-decisions

- Flow is **not installed or selected**.
- Miney is **not the companion architecture**.
- LLM Connect is **not the model gateway**.
- No Mara asset is approved.
- Godot migration is **not scheduled**.