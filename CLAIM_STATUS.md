# Claim status

**Master index:** [coherence-drive](https://github.com/beyond-repair/coherence-drive)  
**Governance:** [CLAIM_VALIDATION](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)  
**Status lock:** [STATUS_LOCK_2026-10-01.md](STATUS_LOCK_2026-10-01.md)  
**Addendum:** 2026-10-01 pinch-family falsification  
**Addendum:** 2026-10-02 scale functional has no stationary point  
**Claim-0:** 2026-10-02 offline verify runnable sketch (does not raise claim level)

| Field | Value |
|--------|--------|
| Classification | RESEARCH |
| Default claim level | **≤2** (math / symbolic identities) |
| Product status | **RUNNABLE SKETCH — NOT A COMPLETE PRODUCT (Claim-0)** |
| Experimental validation | **false** |
| Energy extraction validated | **false** |
| Thrust validated | **false** |
| Constant-W action / source / concavity | **DERIVED** (checkable via `verify_constant_W_action.py`) |
| K_sym / finite-graph / I2 positivity (model-specific) | **DERIVED** (checkable via `verify_proofs_5R_7.py` and 6A–7B verifies) |
| Local dynamical W(x) | **OPEN** |
| Numerical W=0.08 from this action | **NOT DERIVED** |
| Pinch-family heat trace selects 0.08 | **REJECTED** on tested families (`FALSIFICATION_2026-10-01_PINCH.md`) |
| beta=-0.005888 independent of 0.08 | **CIRCULAR** (`verify_pinch_cubic.py`) |

Scripts in this tree are **attackable symbolic / numeric checks**, not experimental confirmation and not a derivation of W≈0.08 from the Coherence Drive thrust target.

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
