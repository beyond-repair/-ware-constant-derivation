<div align="center">

# Ware Constant Derivation

### Constant-W action: derived. Local W(x) renormalized propagator: open. 0.08: not derived.

[![RESEARCH](https://img.shields.io/badge/claim_≤2-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)

</div>

---

Proof home for the scale field W. A GitHub description that derives W from the Coherence Drive thrust target is not a proof.

## Locked vs open

| Layer | Status |
|-------|--------|
| Constant-W action, source, concavity, finite-graph W<1/6 | DERIVED |
| K_sym recovers K(W0); finite-graph Hermitian; quadratic form | DERIVED |
| Exact determinant Hessian for linear insertion | DERIVED |
| I2>0 and unrenormalized Z_loop<0 for stated kernel, d≥2 | DERIVED (model-specific) |
| Kato-Rellich for the full insertion; local positivity W≥1 | REJECTED / REMOVED |
| Z_ren, Lorentzian pole, S_W, W(n), 0.08, 0.23 | OPEN / NOT DERIVED |
| Pinch-family heat trace selects Q≈0.08 | REJECTED on tested families (2026-10-01) |
| beta=-0.005888 as an independent input | CIRCULAR |

## In-tree

| File | Role |
|------|------|
| [PROOF_AND_DERIVATION_LEDGER.md](PROOF_AND_DERIVATION_LEDGER.md) | Master ledger |
| [FALSIFICATION_2026-10-01_PINCH.md](FALSIFICATION_2026-10-01_PINCH.md) | Pinch-family falsification |
| [verify_pinch_cubic.py](verify_pinch_cubic.py) | Cubic circularity check |
| [PROOF_5R_KSYM.md](PROOF_5R_KSYM.md) | Operator form / self-adjointness |
| [CONSTANT_W_ACTION_PRINCIPLE.md](CONSTANT_W_ACTION_PRINCIPLE.md) | Constant-W freeze |
| [verify_constant_W_action.py](verify_constant_W_action.py) | D11–D13 check |
| [verify_proofs_5R_7.py](verify_proofs_5R_7.py) | Form + I2 checks |

Inventory: [ware-constant-phenomenology/DERIVATION_INVENTORY.md](https://github.com/beyond-repair/ware-constant-phenomenology/blob/main/DERIVATION_INVENTORY.md)

2026-10-01: admissible pinch families produce spectral collapse under Neumann conditions and no universal fixed point at 0.08. The cubic coefficient -0.005888 is (2/25)^3-(2/25)^2.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
