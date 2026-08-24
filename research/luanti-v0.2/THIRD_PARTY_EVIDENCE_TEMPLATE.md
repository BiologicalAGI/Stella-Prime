# Stella V0.2 — Third-Party Evidence Entry Template

Status: **TEMPLATE / NON-APPROVAL**

Use one completed entry per external code/media dependency or asset before it is eligible for build approval.

```text
ITEM_ID=
TYPE=CODE|TEXTURE|MODEL|SOUND|MUSIC|FONT|OTHER
NAME=
SOURCE_URL=
SOURCE_PACKAGE=
AUTHOR=
LICENSE=
LICENSE_EVIDENCE=
VERSION_OR_COMMIT=
RETRIEVED_DATE=
ORIGINAL_OR_MODIFIED=
LOCAL_FILENAME=
HASH_SHA256=
PURPOSE=
TRANSITIVE_DEPENDENCIES=
ATTRIBUTION_REQUIRED=
AI_DISCLOSURE_REQUIRED=
REMOVAL_PATH=
FAILURE_ISOLATION=
REVIEW_STATUS=CANDIDATE|REVIEWED|APPROVED_FOR_BUILD|REJECTED|RETIRED
REVIEWER_NOTES=
```

Rules:

- `CANDIDATE` never implies install/use permission.
- Unknown license => HOLD.
- Unknown author/source provenance => HOLD.
- Asset aesthetics do not override provenance requirements.
- Dependency availability does not transfer causal/world authority.
- If an asset or dependency is modified, preserve upstream identity and modification notes.