# Proof 11I — W-stationarity

**Date:** 2026-09-23. 5R–11H frozen. No 0.08, no ΔG/G, no fitted W_*, no imposed J_I.

## Full equation

    Γ = S_grav[g] + S_W[W,g] + Γ_1[W,g] + Γ_ct[W,g]
    δΓ/δW = δS_W/δW + δΓ_1/δW + δΓ_ct/δW = 0 .

From 11H, on retained modes λ≥0, Ω>0, coth>0:

    ∂F_1/∂W = - (1/4) ∑_n (λ_n/Ω_n) coth(β Ω_n / 2) < 0

unless only λ=0 modes survive. Therefore ∂F_1/∂W = 0 does **not** produce an interior W_*>0. A nonzero W_* requires additional W-dependent structure. That is a boundary, not a kill.

## Branches (remain separate)

**B1 dynamical.** S_W must come from a microscopic construction (6D/7B still open). Then

    δS_W/δW = - δΓ_1/δW   (after ct).

**B2 composite.** W=W(A,ω,ℙ,…) is not independently varied. Only δΓ/δg, including the chain rule.

## W-source

    J_W := -∂F_1/∂W = (1/4) ∑_n (λ_n/Ω_n) coth(β Ω_n / 2) > 0

on the retained spectrum. Raw J_W is UV-dominated. Physical object:

    ΔJ_W^{Cas} = -∂_W (F_{T^3}-F_{R^3})
    = (1/4) [ ∑_n (λ_n/Ω_n)coth - ∫ d^3k/(2π)^3 (k^2/Ω_k)coth ]_reg .

Trace vs shear of the same response:

    ∂F/∂W  ↔  trace ,     Π_ij  ↔  traceless .

Not two mechanisms.

B1 homogeneous model: R_W := V^{-1} δS_W/δW ,

    F(W; β, L_i) := R_W(W,g) - ΔJ_W^{Cas}(W,β,L_i) = 0 .

W_* = W_*(β,L_i; derived R_W) IF a root exists in 0 < W < W_UV (Ω_n^2>0). R_W is not invented here.

## Vacuum-push (defensible form only)

    geometry → K → F → (∂F/∂W, Π_ij)
    G_μν+Λ g_μν = 8πG (T^m + T^vac + T^W)
    ∇^μ(T^m+T^vac+T^W)=0

A spatially varying T^vac can exchange with T^W. This does **not** establish that gravity is a vacuum push.

## 11I-A seed — Epstein / Poisson form of ΔJ

At T=0, ΔF_Cas is the difference of Epstein zeta values for Ω=sqrt(m^2-W λ) on the rectangular lattice vs R^3. Poisson summation on the heat kernel

    ∑_n e^{-t λ_n} - V ∫ d^3k/(2π)^3 e^{-t k^2} = ∑_{n≠0} (V/(4π t)^{3/2}) e^{-|n·L|^2/(4t)}

converts the UV-common piece into a winding sum over image lengths |n·L|. Then ΔJ_W^{Cas} = -∂_W of that winding functional. Sign and W-slope of ΔJ_Cas are 11I-A outputs. Intersection with a *derived* R_W is 11I-A existence; intersection with an invented V'(W) is forbidden.

## 11I-B (after a root)

If W_* exists, compute ΔS_spec(W_*), ΔΠ^{Cas}(W_*), ΔJ_W^{Cas}(W_*), and test whether ΔΠ_ij = C_ij ΔJ_W with C_ij from geometry, not a fit.

## Classification

    Loop alone: NO interior W_*.
    ΔJ_W^{Cas}: DEFINED, not numerically evaluated.
    W_*: UNDERDETERMINED pending R_W (B1) or else B2.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
