# Proof 12B-NL — Nonlocal W dynamics

**Date:** 2026-09-23. 12B local obstruction frozen. No 0.08. No fitted kernel.

## Why nonlocal is on the table

12B: a local L-independent V(W) cannot equal ΔJ_W(W; L_i, m, Λ) for all tori. The source is a spectral functional of the whole manifold. Any S_W that hits it on all backgrounds is nonlocal in g (and generally in W).

## Class I — Tautological antiderivative (vacuous W-equation)

Demand δS_W/δW = ΔJ_W^{Cas}[W,g] as an identity on field space. Then, along constant-W slices,

    S_W[W,g] = \int^{W} dw \, \Delta J_W^{Cas}[w,g] + F[g] .

The integral is a spectral/nonlocal functional of g (it knows every L_i and the wall). Adding Γ_Cas,

    δ(S_W + Γ_Cas)/δW = ΔJ_W - ΔJ_W = 0

for every W. The W-equation is an identity. W is not selected. Dynamics, if any, live only in δ/δg, i.e. W is a redundant label or must be composite (B2).

**Derived:** exact nonlocal matching ⇒ W drops out of its own equation. This is not a completion; it is double-counting Γ_Cas under another name.

## Class II — Wilsonian split (only non-vacuous split of the same loop)

Write Γ_Cas = Γ_UV(Λ) + Γ_IR(Λ). Absorb Γ_UV into a nonlocal (or local-EFT) S_W[Λ] and keep Γ_IR as the source:

    δS_W[Λ]/δW = ΔJ_UV ,    δΓ_IR/δW = - ΔJ_IR ,
    stationarity: ΔJ_UV + ΔJ_IR = 0 .

If UV+IR reconstruct the full Casimir, this is again Class I. It becomes non-vacuous only if S_W[Λ] is *restricted* (local operators, fixed derivative order, Λ-independent couplings). Then ΔJ_IR = - δS_W^{local}/δW is an approximation and W_* can exist as a root of a truncated equation — coefficient-dependent, 12B-FREE.

The heat kernel of K supplies the only kernel we already have:

    Tr f(K) = \int_0^\infty (dt/t) \tilde f(t) Tr e^{-t K} .

Nonlocal in x if W=W(x): e^{-t K[W]} is the heat kernel of the 5R operator. That is Γ_1 itself, not a new object.

## Class III — Independent nonlocal kernel (new physics)

    S_W = (1/2) \int d^4x d^4y \sqrt g_x √g_y W(x) G(x,y;g) W(y) + \int \sqrt g \, μ^4 V(W)

G must be a diffs bitensor. Candidates from existing structure: Green function of −□_g + m^2, or the heat kernel of H_0=−∇^2. None of these is derived as *the* W-propagator. G is FREE unless a microscopic X (7B) produces it.

Fractional (-□)^s W: s FREE. Not selected by 11I-A.7.

## Class IV — Composite / no independent W (B2)

W=W[A,ω,P] as in 11D. No S_W. Chain rule only. Nonlocality, if any, is in how A, ω are defined (integrals over closed cycles). 11F on-shell cancellation does not apply. This remains a definition, not a derivation of W_*.

## Stress-energy of a nonlocal S_W

T^W_\mu\nu from a bitensor G is well-defined as δS_W/δg^{\mu\nu} but need not be a perfect fluid and need not be locally conserved if G is specified on a background lattice. Covariant G ⇒ conservation on shell together with the W equation, same as 12B.

## Verdict

| Class | Selects W? | Status |
|---|---|---|
| I exact antiderivative | no (identity) | DERIVED tautology |
| II truncated Wilsonian | only with FREE local couplings | EFT, not derived |
| III independent G or (-□)^s | only if G or s derived | G,s FREE |
| IV composite W[g] | only if A,ω dynamics derived | OPEN definition |

Nonlocality does not by itself create a preferred 0.08 or χ_⋆. The only structurally forced nonlocal object is Γ_Cas / I_Cas, already used.

Next non-vacuous steps remain 12C (existence with FREE local S_W on one geometry) or 13B (recursive W_∞), not another kernel ansatz.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
