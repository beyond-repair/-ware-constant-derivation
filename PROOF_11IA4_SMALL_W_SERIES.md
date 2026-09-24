# Proof 11I-A.4 — Fixed-Λ small-W series

**Date:** 2026-09-23. Expand the Casimir *difference*, not the lattice term alone. No 0.08.

## Regulator lock

    ∂_{x_i} R_Λ = 0 ,    ∂_W R_Λ = 0 .

R_Λ is a mode-label cutoff R_Λ(n) on this slice, not a physical-q^2 cutoff that moves with L_i. A q^2-regulator is a different Hessian and is not used here.

## Moments

    M_{2r}^{T^3}(Λ) = ∑_n R_Λ q_n^{2r} ,    q_n^2 = a^2 n^2 ,
    M_{2r}^{R^3}(Λ) = V ∫ d^3q/(2π)^3 R_Λ(n-map) q^{2r} ,
    ΔM_{2r} = M_{2r}^{T^3} - M_{2r}^{R^3} .

(The continuum R must be the same prescription after the Poisson dual is taken; at this order we only need that it is W-independent and rotation-invariant.)

## ΔF and ΔJ

    Ω = m sqrt(1 - W q^2/m^2)
      = m - W q^2/(2m) - W^2 q^4/(8 m^3) - W^3 q^6/(16 m^5) + O(W^4) .

    ΔF_{Cas,Λ} = (m/2) ΔM_0 - (W/(4m)) ΔM_2 - (W^2/(16 m^3)) ΔM_4 - (W^3/(32 m^5)) ΔM_6 + O(W^4) .

    ΔJ_{W,Λ}^{Cas} = -∂_W ΔF
      = (1/(4m)) ΔM_2 + (W/(8 m^3)) ΔM_4 + (3 W^2/(32 m^5)) ΔM_6 + O(W^3) .

Generic leading term: (1/(4m)) ΔM_2. W→0 is not a stationary point unless ΔM_2=0, which is a condition to test, not to impose.

## K_log series

    1/Ω = 1/m + W q^2/(2 m^3) + 3 W^2 q^4/(8 m^5) + O(W^3) ,
    1/Ω^3 = 1/m^3 + 3 W q^2/(2 m^5) + O(W^2) .

    K_log = (W a^2 /(V m)) ∑ R n_1^2
          + (W^2 a^4 /(2 V m^3)) ∑ R (n_1^2 n^2 + n_1^4 - n_1^2 n_2^2)
          + O(W^3) .

Bracket = 2 n_1^4 + n_1^2 n_3^2. The O(W^2) piece mixes the expansion of A (the 1/Ω term) with (B-C). Confirms 11I-A.2: O(W^2) is not Ω^{-3} alone.

Leading K_log is O(W). Leading ΔJ is O(W^0) if ΔM_2 ≠ 0.

## Ratio (if ΔM_2 ≠ 0)

    K_log / ΔJ_W^{Cas} = [4 W a^2 / V] (∑ R n_1^2) / ΔM_2 + O(W^2) .

    K_log / ΔJ_W ∼ W    near W=0 .

No universal W-independent constant relating shear to scalar source at leading order. A scalar↔tensor relation must come from geometry at finite χ, or from a cancellation ΔM_2=0, neither assumed.

## 11I-A.5 seed

Form the dimensionless ratio in χ = 2π sqrt(W)/(m L) and dimensionless moments Δm_{2r} = ΔM_{2r} / a^{2r} . Ask: (1) Λ-independent limit? (2) dependence only on mL? (3) any unfitted special number? If none, that is the result.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
