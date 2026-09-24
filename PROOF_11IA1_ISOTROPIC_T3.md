# Proof 11I-A.1 — Isotropic T^3 evaluation

**Date:** 2026-09-23. Keep m^2-Wλ. Cutoff explicit. No R_W, no 0.08. Poisson does not license an unregulated Schwinger/Bessel sum for this operator.

## Regulated generating functional

    ΔF_{Cas,Λ} = (1/2) [ ∑_n R_Λ(q_n^2) sqrt(m^2-W q_n^2) - V ∫ d^3q/(2π)^3 R_Λ(q^2) sqrt(m^2-W q^2) ].

Differentiate at fixed R_Λ:

    ΔJ_{W,Λ}^{Cas} = (1/4) [ ∑_n R_Λ q_n^2/Ω_n - V ∫ d^3q/(2π)^3 R_Λ q^2/Ω_q ].

This is the object that may be differentiated. Sign after subtraction remains OPEN.

## Isotropic slice

L1=L2=L3=L,  q_n^2 = (2π/L)^2 |n|^2,

    χ := 2π sqrt(W) / (m L)   (W>0),
    χ^2 |n|^2 < 1

on retained modes. Compactification enters the isotropic spectrum only through mL/sqrt(W).

Cubic permutation symmetry ⇒ p1=p2=p3 ⇒ ΔΠ_i^{Cas}=0. Scalar source ΔJ_W may be nonzero; shear is off.

Continuum piece scales as V m^4 / W^{5/2} times a regulated ∫ dx x^4/sqrt(1-x^2). Sensitivity grows toward the spectral boundary. Subtraction can still flip the sign of ΔJ.

## First anisotropic deformation

L_i = L(1+ε_i), ∑ ε_i=0, |ε|≪1.

    q_n^2 = (2π/L)^2 [ n^2 - 2 ∑_i ε_i n_i^2 ] + O(ε^2),
    δΩ_n = [ W (2π/L)^2 / Ω_n^{(0)} ] ∑_i ε_i n_i^2 + O(ε^2).

    δF_{T^3} = (1/2) ∑_n R_Λ δΩ_n = ∑_i ε_i Q_i + O(ε^2),
    Q_i = (1/2) W (2π/L)^2 ∑_n R_Λ(q_n^2) n_i^2 / Ω_n^{(0)} .

Cubic symmetry + ∑ε=0 ⇒ ∑ Q_i is projected out of the first-order traceless sector.

Define the susceptibility by ΔΠ_i^{Cas} = K(W, mL, Λ) ε_i + O(ε^2).

Explicit kernel (same R_Λ, V=L^3 + O(ε^2)):

    K = - (W / V) (2π/L)^2 ∑_n R_Λ (n_i^2 - n^2/3) n_i^2 / Ω_n^{(0)}   / ε-normalization

more cleanly: because Π_i = p_i - (1/3)∑ p and p_i = -V^{-1} ∂_{ln L_i} F,

    K = - V^{-1} ( ∂Q_i/∂ε_i |_{cubic} converted to Π )
      = - (W /(2 V)) (2π/L)^2 ∑_n R_Λ [ n_i^2 - n^2/3 ] (2 n_i^2) / Ω_n^{(0)}
        after using one ε-derivative on q^2 and the definition of Π.

The exact algebraic prefactor is 11I-A.2 bookkeeping; the structure is

    K = K[ ∑_n R_Λ (n_i^2 - n^2/3)^2 / Ω_n^{(0)} ]

by cubic reduction (n_i^2-n^2/3 is the unique traceless quadratic). No extra anisotropic coupling.

## Linearized Maxwell

    ∂_W ΔΠ_i^{Cas} = V^{-1} P_i ΔJ_W^{Cas}

with P_i = ∂_{ln L_i}-(1/3)∑_j ∂_{ln L_j}, extensive bookkeeping as in 11I-A.
Schematically ΔΠ_i ∼ ε_i ∂_{ln L} ΔJ_W at linear order.

Two-step experiment inside the theory:
compactification → ΔJ_W ;  anisotropic compactification → ΔΠ.
No W_*, no operator flip.

## Ledger

| Item | Status |
|---|---|
| m^2-Wλ, cutoff | RETAINED |
| ΔF, ΔJ isotropic formulas | DERIVED |
| χ = 2π sqrt(W)/(m L) | DERIVED |
| isotropic ΔΠ | 0 |
| linear ΔΠ_i = K ε_i | STRUCTURE DERIVED |
| numerical K, sgn ΔJ | OPEN (11I-A.2) |
| W_* | NOT CLAIMED |

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
