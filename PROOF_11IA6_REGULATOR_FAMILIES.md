# Proof 11I-A.6 — Regulator-family test of N_2/Δm_2

**Date:** 2026-09-23. Mode-label R. Continuum subtraction = ∫ d^3n (because V d^3q/(2π)^3 = d^3n).

Cubic: N_2 = (1/3) ∑ R n^2.  Δm_2 = ∑ R n^2 - ∫ d^3n n^2 R.

## Gaussian R=exp(-n^2/Λ^2)

Poisson: Δm_2 is the winding remainder, exponentially small in Λ^2. N_2 ~ Λ^5.

Direct sum vs exact ∫ n^2 e^{-n^2/Λ^2} = (3/2)Λ^2 (π Λ^2)^{3/2}:

    Λ=2  N_2~8.9e1   Δm_2 ~ 10^{-13} (noise)
    Λ=4  N_2~2.9e3   Δm_2 ~ 10^{-12}
    Λ=8  N_2~9.1e4   Δm_2 ~ 10^{-10}

N_2/Δm_2 is unbounded (numerically 10^{14} and growing in the noise of an exponentially small denominator). Outcome **C** for Gaussian Λ→∞.

## Sharp ball |n|≤Λ

Bulk ~ Λ^5, surface discrepancy Δm_2 ~ Λ^4 ⇒ ratio ~ Λ.

    Λ=3   N_2/Δm_2 ≈ +2.43
    Λ=5   ≈ -12.5
    Λ=8   ≈ -11.6
    Λ=12  ≈ -16.6
    Λ=16  ≈ -42
    Λ=20  ≈ -61

Sign flips, then |ratio| grows. Outcome **C** (no finite limit). Finite-Λ values are family-dependent (**B** at fixed Λ).

## Conclusion

Small-χ candidate C_0 = N_2/Δm_2 does **not** produce a regulator-independent finite constant in the two admissible families tested. It cannot be identified with 0.08 or 1/(4π).

The scalar↔tensor bridge at W→0 is not a universal number; it is either cutoff-scale-dependent (sharp) or ill-defined (Gaussian, Δm_2→0 faster than any power).

Finite-χ (not small-W) remains open: there the full Ω=m sqrt(1-χ^2 n^2) weights modes near the spectral wall and Δm_2-style cancellation need not hold. That is a different proof (11I-A.7 finite-χ), not a repair of C_0.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
