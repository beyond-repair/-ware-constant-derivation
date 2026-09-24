# Proof 14C — Casimir energy derivation details

**Date:** 2026-09-23. Consolidates 11G–11I-A. Locked operator: Ω_n^2 = m^2 - W λ_n, λ_n = ∑_i (2π n_i/L_i)^2. No 0.08. No sign flip of K.

## 1. From the Gaussian determinant

Euclidean one-loop generator (constant W, real scalar):

    Γ_1 = (1/2) Tr ln K,    K_n(ω_E) = ω_E^2 + Ω_n^2

on modes with Ω_n^2 > 0.

    Γ_1 = (1/2) ∑_n ∫ dω_E/(2π) ln(ω_E^2 + Ω_n^2) .

After a standard frequency integral (or ζ-regularized ∫ ln(ω^2+Ω^2) = Ω plus local counterterms),

    E_0 = (1/2) ∑_n R_Λ(λ_n) Ω_n

is the zero-point energy on T^3. F(T=0)=E_0. This is DERIVED given the regulator R_Λ and the Euclidean continuation.

Finite T (11H):

    F = (1/2)∑ Ω + β^{-1} ∑ ln(1-e^{-βΩ}) .

The first term is the Casimir starting point.

## 2. Domain

    Ω_n = sqrt(m^2 - W λ_n)    requires    W λ_n < m^2 .

On T^3, λ_n is unbounded, so a continuum of modes eventually violates this for any W>0. The theory used here keeps only the real spectrum

    N_χ = { n : χ^2 |n|^2 < 1 },    χ = 2π sqrt(W)/(m L)

and a mode-label regulator ∂_x R=∂_W R=0 (11I-A.4). Analytic continuation of Ω^2<0 is a different theory and is not used.

## 3. Casimir subtraction

Raw E_0 diverges as the cutoff is removed (bulk ∝ V Λ^4, …). Define

    ΔF_Cas,Λ = (1/2) [ ∑_n R_Λ Ω_n - V ∫ d^3q/(2π)^3 R_Λ Ω(q) ]

with the same R_Λ. On the n-chart, V d^3q/(2π)^3 = d^3n, so

    ΔF_Cas,Λ / (m/2) = ∑ R ω_n - ∫ d^3n R ω ,    ω=sqrt(1-χ^2 n^2) .

This difference is the Casimir energy of the compactification relative to R^3, at fixed regulator. Local Seeley–DeWitt pieces that are the same on T^3 and R^3 cancel. What remains is the winding / Poisson remainder plus finite-spectrum wall effects.

## 4. Poisson / winding

    ∑_n e^{-t λ_n} = V/(4π t)^{3/2} ∑_r e^{-ℓ_r^2/(4t)} ,
    ℓ_r^2 = ∑_i r_i^2 L_i^2 .

    ∑_n e^{-t λ_n} - V ∫ d^3q/(2π)^3 e^{-t q^2} = V/(4π t)^{3/2} ∑_{r≠0} e^{-ℓ_r^2/(4t)} .

This identity is exact for the Laplacian. It does **not** by itself convert sqrt(m^2-W λ) into a convergent Epstein–Bessel sum: the Schwinger representation of sqrt(m^2-Wλ) needs m^2-Wλ>0 on the support of the integral. Hence 11I-A: keep R_Λ and the wall explicit; do not claim an unregulated Bessel formula for the literal operator.

## 5. Heat kernel (flat T^3)

For H_0=-∇^2 on flat T^3 the Seeley coefficients of the *bulk* coincide with R^3 (a_0=1, a_1=0, a_2=0 on flat empty torus). Casimir is not those local a_n; it is the nonlocal winding sum. Curvature terms ξ R in K were suppressed on this slice (11G).

## 6. Derivatives from one generating functional

    ΔJ_W^{Cas} = - ∂_W ΔF_Cas
    V ΔΠ_i^{Cas} = - ∂_{ln L_i} ΔF_Cas

Maxwell: ∂_W (V Δp_i) = ∂_{ln L_i} ΔJ_W. At T=0,

    ∂F/∂W = - (1/4) ∑ R λ_n / Ω_n    (raw, before subtraction).

After T^3-R^3, the subtracted source is Δμ_2 (11I-A.7). Sign of ΔJ after subtraction is not a theorem of the raw positive sum; the continuum piece can dominate (scans: Δμ_2 typically negative).

Small-W series at fixed Λ (11I-A.4):

    ΔF/m = (1/2)Δm_0 - (χ^2/4)Δm_2 - (χ^4/16)Δm_4 - ⋆

Leading ΔJ is O(W^0) if Δm_2 ≠0.

## 7. What Casimir energy is not

- Not a derivation of W=0.08
- Not an H-theorem or J^μ
- Not S_ent(A) (13B)
- Not T^{info} with fitted ζ
- Not a solution of ∇^2 W = -j_W/(Z m^2) on T^3 when ∫ j ≠0 (14B)

## 8. Ledger

| Step | Status |
|---|---|
| Γ_1 → ∑ Ω/2 | DERIVED, regulator-dependent local terms |
| T^3-R^3 definition of ΔF | DEFINITION of Casimir |
| Poisson identity for e^{-tλ} | DERIVED |
| Unregulated Epstein for sqrt(m^2-Wλ) | NOT VALID without wall/cutoff |
| ΔJ = -∂_W ΔF, Π = -∂_{ln L} ΔF | DERIVED |
| Sign(ΔJ) after subtraction | OPEN in general; typically Δμ_2<0 in scans |
| Selects W | NO |

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
