# Proof 11I-A — Epstein / winding representation

**Date:** 2026-09-23. 5R–11I frozen. Do not replace m^2-Wλ by m^2+Wλ. No 0.08. No V(W).

## Domain

T=0 source before subtraction:

    J_W = (1/4) ∑_n λ_n / sqrt(m^2 - W λ_n) .

W>0 and unbounded λ cannot keep Ω^2>0 on the whole lattice. Representation is at fixed spectral cutoff Λ, as in 11G. Schwinger

    1/sqrt(m^2-Wλ) = π^{-1/2} ∫_0^∞ ds s^{-1/2} e^{-s(m^2-Wλ)}

gives e^{+s W λ}, not the standard massive heat kernel e^{-t λ}. Ordinary Epstein–Bessel formulas for Ω^2=m^2+Wλ do **not** apply to the locked operator. Domain restriction, not a silent sign flip.

## Poisson (DERIVED)

    ∑_n e^{-t λ_n} = V (4π t)^{-3/2} ∑_r e^{-ℓ_r^2/(4t)},
    ℓ_r^2 = r1^2 L1^2 + r2^2 L2^2 + r3^2 L3^2 .

    ∑_n e^{-t λ_n} - V ∫ d^3k/(2π)^3 e^{-t k^2} = V (4π t)^{-3/2} ∑_{r≠0} e^{-ℓ_r^2/(4t)} .

r=0 is exactly R^3. The finite source is a winding sum:

    ΔJ_W^{Cas}(Λ) = ∑_{r≠0} J_r(W; Λ, L_i) = E_winding(L_i; W, m, Λ) .

Geometry enters only through the image lengths ℓ_r. Local a_n volume terms cancel in the subtraction.

## Epstein generating functional

    Z_{T^3}(s) = ∑_{r≠0} (r1^2 L1^2 + r2^2 L2^2 + r3^2 L3^2)^{-s}

is the anisotropic Epstein zeta (Eisenstein series of the rectangular lattice). After a continuation compatible with m^2-Wλ and R_Λ,

    ΔF_Cas = F_Epstein(W, m; L1,L2,L3) ,
    ΔJ_W^{Cas} = - ∂_W ΔF_Cas ,
    Δp_i^{Cas} = - V^{-1} ∂_{ln L_i} ΔF_Cas ,
    ΔΠ_i^{Cas} = - V^{-1} (∂_{ln L_i} - (1/3) ∑_j ∂_{ln L_j}) ΔF_Cas .

One scalar generates both the W-source and the shear source.

## Maxwell identity (DERIVED)

Mixed partials of ΔF_Cas commute. Safest form:

    ∂_W (V Δp_i^{Cas}) = ∂_{ln L_i} ΔJ_W^{Cas} .

Any later ΔΠ_ij = C_ij ΔJ_W must come from this geometry, not a fit.

## Signs after subtraction: OPEN

Raw J_W > 0 on retained modes. Raw F_1 decreases in W. After T^3-R^3, sign(ΔJ) and ∂_W ΔJ are not claimed. No zero of ΔJ is claimed.

## Einstein representation

On the orthogonal slice, the gravitational equation with this vacuum is

    G_00 = 8πG (T_00^m + ρ_Cas + ρ_W + ρ_local) ,
    σ̇_i + 3H σ_i = 8πG Π_i^{Cas} + …

with ρ_Cas = V^{-1} (ΔF_Cas - ∑_i ∂_{ln L_i} ΔF_Cas)/appropriate static reduction, i.e. ρ and Π are the Hilbert variations of the **same** ΔF_Cas. That is the Einstein-side representation of 11I-A: G_μν sees derivatives of F_Epstein, not an independent fluid.

## Spectral geometry link (10A)

The Laplacian here is the flat torus Laplacian (5R continuum on T^3). Image lengths ℓ_r are the dual lattice of that torus. This is **not** the Kigami gasket spectrum. W<1/6 and λ_max=6 do not enter ΔF_Cas. Do not identify Epstein data with gasket 3/5 or design 0.45.

## Next evaluation order

1. Isotropic slice L1=L2=L3=L: ΔΠ=0, isolate ΔJ_W^{Cas}(W,m,Λ;L).
2. Perturb L_i = L(1+ε_i), ∑ ε_i=0, read linear ΔΠ_i from ∂_{ln L} of F_Epstein.
3. Only then ask whether a derived R_W can intersect ΔJ (11I-B existence). Still no invented potential.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
