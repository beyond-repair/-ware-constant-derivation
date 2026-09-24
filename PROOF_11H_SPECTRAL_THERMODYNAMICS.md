# Proof 11H — Finite-temperature spectral thermodynamics

**Date:** 2026-09-23. 11G frozen. No 0.08, no ΔG/G, no H-theorem, no imposed J_I.

## Partition function

Retained modes: Ω_n^2 = m^2 - W λ_n > 0, λ_n = ∑_i (2π n_i/L_i)^2, common regulator R_Λ(λ).

Bosonic product:

    Z_{T^3} = ∏_n [ 2 sinh(β Ω_n / 2) ]^{-1},
    F = β^{-1} ∑_n ln[ 2 sinh(β Ω_n / 2) ].

Identity 2 sinh(x/2) = e^{x/2}(1-e^{-x}) ⇒

    F = (1/2) ∑_n Ω_n + β^{-1} ∑_n ln(1-e^{-\u03b2 Ω_n}) = E_0 + F_T.

T→0 ⇒ F → E_0 = (1/2)∑ Ω_n  (11G zero-point).

## Entropy and energy

    S_n = βΩ_n/(e^{\u03b2Ω_n}-1) - ln(1-e^{-\u03b2Ω_n}),
    S_spec = ∑_n S_n .

    S_spec(T→0) → 0   for every retained Ω_n > 0.

This is thermal occupancy entropy, not an arrow.

    U = ∑_n Ω_n ( 1/2 + 1/(e^{\u03b2Ω_n}-1) ) = E_0 + U_T .

## Pressure from F

    p_i = -(1/V) ∂F/∂ ln L_i ,
    ∂Ω_n/∂ ln L_i = W k_i^2 / Ω_n ,
    ∂F/∂Ω_n = (1/2) coth(β Ω_n / 2) .

    p_i = - (W/(2V)) ∑_n (k_i^2/Ω_n) coth(β Ω_n / 2) + p_i^{local} .

T→0: coth → 1, recovers 11G.

    p_i - p_j = - (W/(2V)) ∑_n [(k_i^2-k_j^2)/Ω_n] coth(β Ω_n / 2) .

Same spectrum → (S, U, p_i, Π_ij). No extra anisotropic stress inserted.

## Casimir subtraction + heat kernel

    ΔF_Cas = F_{T^3} - F_{R^3} ,   same R_Λ,
    ΔS_Cas = S_{T^3} - S_{R^3} ,
    Δp_i^{Cas} = p_i^{T^3} - p^{R^3} .

R^3 is isotropic ⇒ ΔΠ_ij^{Cas} = Π_ij^{T^3}.

Heat-kernel side (11B): on a flat torus the coincidence expansion of Tr e^{-t D} is

    (4π t)^{-2} V [ a_0 + t a_1 + t^2 a_2 + … ] + Poisson-dual winding sum.

Local polynomials a_0=1, a_1=R/6-E, a_2=C^2/120 - E_4/360 + … renormalize Λ, G^{-1}, α_{R^2}. The winding / image sum IS the Casimir piece:

    ρ_Cas(T=0) = (1/(2V)) ( ∑_n^{reg} Ω_n - ∫ d^3k/(2π)^3 √(m^2-W k^2) )

after analytic continuation of the Epstein-like zeta associated with the lattice {2π n_i/L_i}. That density is finite once local terms are stripped. Anisotropic L_i make the Epstein lattice rectangular; that is the source of ΔΠ.

Do not treat the local (volume) piece as physical vacuum pressure.

## Dimensionless outputs (not W)

    D_S(W,β,L_i) = (S_{R^3} - S_{T^3}) / S_ref ,
    D_Π = √(ΔΠ_ij ΔΠ^{ij}) / p_ref .

S_ref and p_ref are not chosen here (would be POST-HOC if set to force 0.08). These are comparison functionals for 11I+.

## W-derivative identity (DERIVED)

    ∂Ω_n/∂W = - λ_n / (2 Ω_n) ,
    ∂F/∂W = - (1/4) ∑_n (λ_n / Ω_n) coth(β Ω_n / 2) .

T→0: ∂F/∂W → - (1/4) ∑_n λ_n/Ω_n .

This is the explicit thermal spectral contribution that 11I will insert into δΓ/δW = 0 together with δS_W/δW. It is not an “information force” slogan.

## Status

| Object | Status |
|---|---|
| F,S,U,p_i from Z | DERIVED |
| T→0 → 11G | DERIVED |
| ΔΠ^{Cas} = Π(T^3) | DERIVED (structure) |
| Numerical ΔΠ, D_S, W_* | OPEN (11I) |
| H-theorem / J_I | NOT CLAIMED |

Next: 11I — δΓ/δW=0 with this ∂F/∂W, ask whether a W_*(β,L_i) exists.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
