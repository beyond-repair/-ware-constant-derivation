# Addendum — 2026-10-03 loop-dumbbell stationarity

Does not modify STATUS_LOCK_2026-10-01.md. Does not reopen P1–P9, Proof 5R, or the pinch-family rejection.

An independent functional was fixed before comparison:

```text
I(ell) = lambda_2(ell) / lambda_1(ell)
beta_I = ell * dI / dell
```

on the symmetric two-loop Kirchhoff graph (loops of length L, bridge of length ell).

Result: beta_I(L/2) = 0, and

```text
I_* = (pi / arccos(2/3) - 1)^2 ≈ 7.481533386207024
```

This is a local maximum. It is not 0.08. Unequal loop lengths move the stationary value, so it is not universal.

Record: PROOF_15A_LOOP_DUMBBELL_STATIONARITY.md
Check: verify_proof_15A_secular.py

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
