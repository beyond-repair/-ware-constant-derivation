<div align="center">

# Ware Constant Derivation

### Constant-W action: derived. Local W(x) renormalized propagator: open. 0.08: not derived.

[![RESEARCH](https://img.shields.io/badge/claim_≤2-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)

</div>

---

**Status:** RUNNABLE SKETCH — NOT A COMPLETE PRODUCT (Claim-0 identity checks).

This tree does not derive \(W \approx 0.08\). The GitHub description that ties W to a Coherence Drive thrust target is not a proof. The scripts below check identities already written in the ledgers and print the numbers they compute, including misses.

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```

## Quick start (stranger path)

No configuration file. Seeds, regulators, and the pinch input \(\delta = 2/25\) are fixed in the scripts. Nothing is downloaded at runtime.

```bash
git clone https://github.com/beyond-repair/-ware-constant-derivation.git
cd -- -ware-constant-derivation
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pip install -e .
ware-constant-checks
pytest -q
```

`ware-constant-checks` (or `python run_derivation_checks.py`) exits 0 when every in-tree assertion passes. Exit 0 is not a measurement of 0.08.

What a passing run reports, and does not claim:

| Check | What passes | What it does not say |
|-------|-------------|----------------------|
| `verify_constant_W_action.py` | Trace source matches the spectral sum; \(V''<0\) on a seed-0 random positive matrix | That matrix is not \(\lambda_{\max}=6\). Printed \(W_{\mathrm{crit}}\) is not \(1/6\) and printed \(W\) is not 0.08 |
| `verify_pinch_cubic.py` | \(\beta=(2/25)^3-(2/25)^2=-92/15625=-0.005888\), and the cubic recovers root 0.08 | Circular. 0.08 is the input \(\delta\), not an output |
| `verify_proofs_5R_7.py` | Constant-\(W\) recovery is exact; \(I_2>0\) for \(d=2,3,4\); large-\(k\) tail \(\sim 1/(d k^2)\) | Discrete Neumann form vs matrix insertion is **not** exact (relative mismatch printed; tolerance 0.15) |
| `verify_proof_6A_dimreg.py`, `verify_proof_6B_uv.py`, `verify_proof_6C_poles.py`, `verify_proof_6C1_im.py`, `verify_proof_7B_hs.py` | Stated Laurent / pole / cut / Hubbard–Stratonovich identities | \(Z_{\mathrm{ren}}\), a Lorentzian healthy mode, and \(S_W\) stay open |

Optional direct calls: `python verify_constant_W_action.py` and the other `verify_*.py` scripts.

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
| [verify_constant_W_action.py](verify_constant_W_action.py) | D11–D13 check (random graph; not 0.08) |
| [verify_proofs_5R_7.py](verify_proofs_5R_7.py) | Form + I2 checks (form mismatch is not zero) |
| [verify_proof_6A_dimreg.py](verify_proof_6A_dimreg.py) | Dim-reg Laurent series of integrated I2 |
| [verify_proof_6B_uv.py](verify_proof_6B_uv.py) | A0, A1, A2 poles |
| [verify_proof_6C_poles.py](verify_proof_6C_poles.py) | Pole / residue / threshold algebra |
| [verify_proof_6C1_im.py](verify_proof_6C1_im.py) | Cut imaginary part vs quadrature |
| [verify_proof_7B_hs.py](verify_proof_7B_hs.py) | Hubbard–Stratonovich stationarity algebra |
| [run_derivation_checks.py](run_derivation_checks.py) | Runs every verifier and prints the numbers |
| [tests/](tests/) | pytest for the same checks |

Inventory: [ware-constant-phenomenology/DERIVATION_INVENTORY.md](https://github.com/beyond-repair/ware-constant-phenomenology/blob/main/DERIVATION_INVENTORY.md)

2026-10-01: admissible pinch families produce spectral collapse under Neumann conditions and no universal fixed point at 0.08. The cubic coefficient -0.005888 is (2/25)^3-(2/25)^2.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
