# Proof 11I-A.2 — Regulated isotropic source + linear shear susceptibility

**Date:** 2026-09-23. Literal m^2-Wλ. R_Λ fixed. No R_W. No 0.08.

## Scalar source (isotropic)

a=2π/L, Ω_n^{(0)}=sqrt(m^2-W a^2 n^2), χ=2π sqrt(W)/(m L), χ^2 n^2<1.

    ΔJ_{W,Λ}^{Cas} = (1/4)[ ∑_n R_Λ a^2 n^2 / Ω_n^{(0)} - V ∫ d^3q/(2π)^3 R_Λ q^2/sqrt(m^2-W q^2) ].

Sign after subtraction OPEN.

## First variation vanishes

L_i=L(1+ε_i), ∑ε_i=0 ⇒ δΩ_n = (W a^2 / Ω^{(0)}) ∑_i ε_i n_i^2 .

    δF = (W a^2 / 2) ∑_n (R_Λ/Ω^{(0)}) ∑_i ε_i n_i^2 .

Cubic symmetry equalizes ∑ R n_i^2/Ω for i=1,2,3. Hence δF ∝ ∑ ε_i = 0.

    δF_Cas^{(1)} = 0 .

Linear shear is **not** this first variation. It comes from the second variation of F (and from how p_i = -V^{-1} ∂_{ln L_i} F hits the quadratic form).

## Quadratic expansion

E_n=∑_i ε_i n_i^2, Q_n=∑_i ε_i^2 n_i^2,

    q_n^2 = a^2 (n^2 - 2 E_n + 3 Q_n) + O(ε^3),

    Ω_n = Ω^{(0)} + (W a^2/Ω^{(0)}) E_n - (3 W a^2 /(2 Ω^{(0)})) Q_n - (W^2 a^4 /(2 (Ω^{(0)})^3)) E_n^2 + O(ε^3).

Continuum subtraction is rotationally invariant ⇒ no traceless O(ε) piece.

## Susceptibility split

    ΔΠ_i^{Cas} = K(W, mL, Λ) ε_i + O(ε^2),
    K = K_{Ω^{-3}} + K_geometric .

Spectral Hessian (E_n^2/Ω^3), after cubic projection ∑ R (n_i^2-n^2/3) n_i^2 = ∑ R (n_i^2-n^2/3)^2:

    K_{Ω^{-3}} = (W^2 a^4 /(2V)) ∑_n R_Λ (n_i^2 - n^2/3)^2 / (Ω_n^{(0)})^3 .

The 3Q_n/Ω term is a geometric pressure derivative. It is **not** absorbed into K_{Ω^{-3}}. Full K is not claimed to equal K_{Ω^{-3}}.

Within a fixed retained-mode set, K_{Ω^{-3}} stiffens as W a^2 n^2 → m^2. That is a prediction of the literal operator. Sign of full K after all terms + subtraction is OPEN.

## Common spectral boundary

ΔJ ~ Ω^{-1}, K_{Ω^{-3}} ~ Ω^{-3}, ΔF ~ Ω. Same wall W → m^2/(a^2 n^2). Regulator stays on.

ΔJ_W^{Cas} = -∂_W ΔF_Cas still does not vanish by itself. Source ≠ stationary point. No W_*.

## 11I-A.3 seed — small-W at fixed Λ

At W=0, Ω=m (all modes). Expand

    Ω^{-1} = m^{-1} (1 + (W a^2 n^2)/(2 m^2) + O(W^2)),
    Ω^{-3} = m^{-3} (1 + (3 W a^2 n^2)/(2 m^2) + O(W^2)).

Then ΔJ_W^{Cas} and K_{Ω^{-3}} have Taylor series in W whose coefficients are cutoff-dependent lattice moments of n^2, (n_i^2-n^2/3)^2. That is the controlled perturbative regime **before** the Ω=0 wall. Compare those series; do not send Λ→∞ first.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
