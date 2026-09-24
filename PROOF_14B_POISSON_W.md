# Proof 14B — Poisson equation for W

**Date:** 2026-09-23. Status: EFT variation of 12B, not a theorem of K alone. 14A stands: D is a postulate. No 0.08.

## Postulate (12B, lowest-order elliptic)

On a Riemannian slice, take the unique two-derivative diffs-invariant kinetic term for a dimensionless scalar, with scale m already in K:

    S_W = \int d^4x √-g [ (Z(W)/2) m^2 g^{μν} ∂_μ W ∂_ν W + m^4 V(W) + ξ(W) M_Pl^2 R ] .

Z, V, ξ remain FREE (12B). Set ξ=0 and Z=const for the Poisson reduction (further ASSUMPTION, not derived).

## Variation

    δS_W/δW = √-g [ - Z m^2 □_g W + m^4 V'(W) ]

with □_g W = g^{μν} ∇_μ ∇_ν W.

Source constraint 12B / 11I:

    δS_W/δW = ΔJ_W^{Cas} .

ΔJ_W as used on T^3 is extensive (energy). The local density is

    j_W := (1/√-g) δΓ_Cas/δW   with the 11I sign  j_W = - (energy-density version of ∂F/∂W).

Matching conventions so that constant-W, unit lapse, volume V_3 gives ∫ j_W = ΔJ_W^{Cas} / (time convention):

    - Z m^2 □ W + m^4 V'(W) = j_W[W,g] .

## Poisson form

If V'=0 on the slice of interest (flat potential; ASSUMED),

    □_g W = - j_W / (Z m^2) .

Euclidean / static spatial reduction □ → ∇^2:

    ∇^2 W = - j_W / (Z m^2) .

This is the Poisson equation for W. Z is an undetermined stiffness. j_W[W,g] is the nonlocal Casimir source of the same K, so the PDE is

    ∇^2 W(x) = - (1/(Z m^2)) j_W[ W(·), g ](x) .

Nonlinear and nonlocal: the right-hand side depends on the whole field W, not on W(x) only.

## Constant-W reduction (check)

∇^2 W=0 ⇒ m^4 V'(W) = j_W. On a flat torus j_W is the 11I density, generally nonzero, so a constant solution needs a potential slope. That is 12B/11I-A.8 again: no constant W_* from the loop alone if V=0.

## What is derived vs assumed

| Piece | Status |
|---|---|
| Kinetic operator □ from 2-derivative scalar EFT | SYMMETRY-FIXED given S_W |
| Scale m^2 in the coefficient | ASSUMED (μ=m) |
| Z | FREE |
| V=0 | ASSUMED for pure Poisson |
| j_W from K | DERIVED |
| Equation holding in nature | NOT DERIVED from K |
| Selects W_* or 0.08 | NO |

## Green function on T^3

If one linearizes j_W ≈ j_0 + χ δW + … about a background W_0 (j_0 may be nonzero),

    ∇^2 δW - κ^2 δW = - j_0/(Z m^2) + …

with κ^2 depending on δj/δW and V''. Zero-mode solvability on T^3:

    ∫ j_W = 0

unless V' supplies the integral. The torus has no ∇^2-inverse on constants. A net Casimir source cannot be balanced by ∇^2 W alone. That is the electrostatic Gauss-law obstruction on a closed manifold.

**Derived obstruction:** closed T^3 + V=0 + ∫ j_W ≠0 ⇒ no solution of Poisson. Either open the manifold, add V', or drop the equation.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
