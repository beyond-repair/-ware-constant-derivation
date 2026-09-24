# Proof 11I-A.8 — Spectral wall and χ-selection

**Date:** 2026-09-23. Fixed m,L so W ∝ χ^2 and dF/dW=0 ⇔ dF/dχ=0 for χ≠0. No S_W. No 0.08.

## Domain

N_χ = {n ∈ Z^3 : χ^2 |n|^2 < 1}. Cardinality jumps at χ = 1/|n|.

Near a threshold ε_n = 1-χ^2 n^2 →0^+:

    Ω = m ε^{1/2}     → 0     (mode contribution to F vanishes)
    1/Ω ~ ε^{-1/2}    integrable in ε as a 1D endpoint
    1/Ω^3 ~ ε^{-3/2}  NOT integrable; Hessian/K_log stiffens (11I-A.3)

The wall is an integrable zero of that mode's energy and a non-integrable stiffening of the shear kernel. F is continuous across dropout (Ω→0). Derivatives of F need not be.

## Stationarity identity (DERIVED)

ω=sqrt(1-χ^2 n^2),  ΔF/m = (1/2)[∑ ω - ∫ d^3n ω] on the real-mode ball (sharp / wall-as-cutoff).

    ∂ω/∂χ = - χ n^2 / ω
    d(ΔF/m)/dχ = -(χ/2) Δμ_2 ,   Δμ_2 = ∑ n^2/ω - ∫ n^2/ω d^3n .

Hence, at fixed m,L and χ≠0:

    dF/dχ = 0  ⟷  Δμ_2 = 0  ⟷  ΔJ_W^{Cas} = 0 .

The χ-stationarity condition is exactly the vanishing of the Casimir W-source. Not a new equation.

## Scan

Δμ_2(χ) for Gaussian Λ=20 and sharp (wall cutoff), χ∈[0.08,0.95]:

Almost everywhere Δμ_2 < 0 and |Δμ_2| decreases as χ grows (fewer modes).

One thin sign flip: both families cross + near χ≈0.70 and back - near χ≈0.71, i.e. the |n|^2=2 wall (1/√2≈0.707). That is a threshold spike, not a broad well.

ΔF/m itself changes sign repeatedly as shells drop (0.10: -2.9, 0.15: +0.78, 0.40: +1.37, 0.50: -0.53, …). Discrete-mode Casimir wiggles, not a single interior minimum.

## Classification

**A interior χ⋆:** not found as a robust, regulator-stable root of Δμ_2=0.

**B boundary:** no evidence the functional drives χ→0 (source stays large) or cleanly to χ→1 (only 7 modes left, F still wiggles).

**C no stationary point:** YES for the smooth bulk of (0,1).

**D singular wall:** YES locally. Hessian ~ ε^{-3/2}. Do not promote the 0.707 spike to a physical selected state without a regularization theorem.

## Consequence

The spectral determinant alone does not select W or χ. That is the 11I / 6D conclusion at finite χ.

Allowed next moves, not both at once as a fit:

1. Specify derived S_W and require δS_W/δW = ΔJ_W^{Cas}.
2. Ask whether another corpus branch supplies a selection principle:
   - recursive W_∞ = lim R_D (optimization-limit-conjecture; Theorem A ≠ W_∞)
   - S_ent → I → W (entanglement repo; g=η+ε∇∇S is not derived)

Do not import quarantined CFT v3.1 v^4=ζ^2 G^2 M^2, W(n)=0.08 e^{0.23(n-1)}, Origin Point λ(ρ,n), or IFP T_info with W≈0.08.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
