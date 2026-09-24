# Proof 11I-A.5 — Dimensionless ratio / finite-χ audit

**Date:** 2026-09-23. ∂_x R=∂_W R=0. No 0.08. No imposed ΔM_2=0.

## Dimensionless series

χ = sqrt(W) a / m = 2π sqrt(W)/(m L),  Δm_{2r}=ΔM_{2r}/a^{2r}.

    ΔF_Cas / m = (1/2)Δm_0 - (χ^2/4)Δm_2 - (χ^4/16)Δm_4 - (χ^6/32)Δm_6 + O(χ^8)

    J-hat = 4m/a^2 ΔJ_W^{Cas} = Δm_2 + (χ^2/2)Δm_4 + (3 χ^4/8)Δm_6 + O(χ^6)

    K_log = (m/V) [ χ^2 N_2 + (χ^4/2) N_4 + O(χ^6) ]

N_2=∑ R n_1^2,  N_4=∑ R (2 n_1^4 + n_1^2 n_3^2).

Raw K/ΔJ has dimensions. Dimensionless candidate:

    R(χ, Λ L) := (V/(4W)) K_log / ΔJ_W^{Cas}
        = (N_2 / Δm_2) [ 1 + (χ^2/2)(N_4/N_2 - Δm_4/Δm_2) + O(χ^4) ]

if Δm_2 ≠ 0. Leading raw ratio ∝ W. C_0 = N_2/Δm_2 is the only small-χ candidate constant. It is regulator-sensitive until proven otherwise.

W=0 does not kill ΔJ. K_log(W=0)=0. No 0.08 or 1/(4π) in the series.

## Outcomes for C_0=N_2/Δm_2

A finite Λ-independent C.  B finite but R-dependent.  C no finite limit.

11I-A.6 tests A vs B vs C on explicit families.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
