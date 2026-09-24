# Proof 11I-A.3 — Exact log-volume-preserving Hessian

**Date:** 2026-09-23. Replaces the heuristic K_Ω^{-3}+K_geom split as the primary coefficient. 11I-A.2 remains valid as an expansion check.

## Coordinates

    x_i = ln L_i - (1/3) ∑_j ln L_j ,   ∑_i x_i = 0 .

Volume is fixed exactly. On the isotropic background a=2π/L,

    q_n^2 = a^2 ∑_i n_i^2 e^{-2 x_i} .

    ∂_{x_i} q^2 = -2 a^2 n_i^2 e^{-2 x_i} ,
    ∂_{x_i} ∂_{x_j} q^2 = 4 a^2 n_i^2 δ_{ij} e^{-2 x_i} .

At x=0:

    ∂_{x_i} Ω = W a^2 n_i^2 / Ω ,
    ∂_{x_i} ∂_{x_j} Ω = - (2 W a^2 n_i^2 / Ω) δ_{ij} - W^2 a^4 n_i^2 n_j^2 / Ω^3 .

First derivatives of F vanish by cubic symmetry (11I-A.2). Linear Π is the Hessian.

## Moments

    A = ∑_n R_Λ n_1^2 / Ω_n ,
    B = ∑_n R_Λ n_1^4 / Ω_n^3 ,
    C = ∑_n R_Λ n_1^2 n_2^2 / Ω_n^3 .

Convention ΔΠ_i = - V^{-1} ∂_{x_i} F,  ∂_{x_i} F = ∑_j (∂_i ∂_j F) x_j at the isotropic point.

Then ΔΠ_i = K_log x_i + O(x^2) with

    K_log = (1/V) [ W a^2 A + (W^2 a^4 / 2) (B - C) ] .

Sign: stretching x_1>0 gives Π_1 with this K_log (A term positive). Continuum subtraction does not contribute a traceless Hessian at this order.

This is the complete spectral Hessian of ΔF_{T^3} at fixed R_Λ. No split into “geom vs Ω^{-3}” is required for bookkeeping; those pieces are the two summands above.

K_log stiffens as Ω→0. Sign of K_log after the full definition (including how local counterterms are stripped) remains OPEN if those counterterms have anisotropic finite pieces — on the torus subtraction used here they do not at linear x.

## 11I-A.4 seed — small W at fixed Λ

Ω = m - (W a^2 n^2)/(2m) + O(W^2),

    A = m^{-1} A^{(0)} + (W a^2 /(2 m^3)) A^{(1)} + O(W^2) ,
    A^{(0)} = ∑ R n_1^2 ,   A^{(1)} = ∑ R n_1^2 n^2 .

    K_log = (W a^2 /(V m)) A^{(0)} + O(W^2) .

    ΔJ_W^{Cas} = (1/4)[ a^2 m^{-1} ∑ R n^2 - (continuum) ] + O(W) .

Leading K_log is O(W). Leading ΔJ is O(W^0) plus subtraction. Ratio K_log / ΔJ_W is O(W) at small W unless the subtracted ΔJ itself starts at O(W). That ratio test is 11I-A.5, after the O(W) coefficients are written with the same R_Λ.

No 0.08. No 1/(4π).

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
