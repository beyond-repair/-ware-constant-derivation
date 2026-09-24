# Proof 11A — Covariant completion / stress-energy audit

**Date:** 2026-09-23. 5R–10A frozen. Do not identify L_gasket with Box_g. No 0.08, r_p, Omega_c, a0, thrust. Do not set G_eff=G(1+W).

## 1. Minimal covariant matter operator

Flat 5R quadratic form (Proof 5R):

    Q_W[f] = ∫ ω² f² - ∫ W |∇f|² + (1/4)∫ (∇² W) f².

The unique minimal diffeomorphism-covariant replacement that recovers this when g_μν=η_μν is

    Q_W[f;g] = ∫ √g [ ω² f² - W g^{μν} ∇_μ f ∇_ν f + (1/4) f² Box_g W ].

Equivalently the Friedrichs operator of that form, K(W,g), reduces to K_sym when g=η.

| Term | Class |
|---|---|
| √g, Box_g, g^{μν}∇_μ∇_ν | REQUIRED FOR COVARIANCE |
| ω², W-gradient insertion as above | LOCKED flat limit |
| ξ R f² | FREE (non-minimal). ξ=1/6 is conformal for a massless scalar, not forced here (ω≠0) |
| W R, (∇W)² R, Riemann contractions | FREE / not required for the flat limit |
| Replacing Box_g by L_gasket | FORBIDDEN by 10A |

This is a covariant *matter* completion. It is not a derivation of Einstein gravity and not a derivation of S_W.

## 2. Effective action

    Γ[g,W] = S_W[g,W] + (1/2) Tr ln K(W,g)

S_W remains an independent input (6D–7B). The determinant is the one-loop effective action of φ, now on a metric background. UV: Seeley–DeWitt / heat-kernel poles in a0,a1,a2 (vacuum energy, R, R²/Weyl). Same renormalization logic as 6A–6B, plus curvature counterterms.

## 3. Stress tensor

    T_μν^eff = - (2/√-g) δΓ/δg^{μν}

Split:

    T = T^{S_W} + T^{1-loop}

T^{1-loop} is the standard <T_μν> of a free scalar with kinetic form Q_W. If Γ is a diffeomorphism scalar and W,g obey the variational equations that follow from Γ, ∇^μ T_μν = 0 on-shell. That is REQUIRED FOR COVARIANCE, not a halo theorem.

Divergent pieces: Λ_vac g_μν, c R_μν, higher derivative. Scheme-dependent finite remainders exist. This is the cosmological-constant / vacuum-energy problem of QFT, not a derivation of Ω_c.

## 4. Einstein equation

Nothing in 5R–10A produces the Einstein–Hilbert term. A field equation

    G_μν + Λ g_μν = 8π G T_μν^eff

requires EH (and Λ, G) as an **independent gravitational input**. Modified-gravity operators (f(R), R_μν R^{μν}, G_eff=G(1+W), …) are additional assumptions. Forbidden as silent insertions.

Does the spectral structure necessarily gravitate? Yes, in the universal QFT sense: a covariant matter action sources T_μν. That is true of any scalar, with or without W. It is not a distinctive Coherence Drive mechanism and it does not modify ∇²Φ=4πGρ unless W is a dynamical metric-coupled field with a derived S_W, or new gravitational operators are added.

## 5. Weak field

Only after assuming EH + this matter:

- External prescribed W(x): T_00^{1-loop}[W] is an ordinary inhomogeneous energy density. Poisson is still ∇²Φ=4πG(ρ_φ+ρ_W-loop). No new gravitational law. ρ_W-loop is not computed numerically here and is not a rotation-curve fit.
- Dynamical W: would be a scalar-tensor theory whose kinetic sign is the open 6C problem (Z_R). Not derived.

Rotation curves: not calculated. Not licensed as a test until S_W and the gravitational action are fixed.

## 6. Cosmology

FLRW + this T_μν would contribute to H²(a) like any other fluid (and like vacuum energy). Ω_c is not an output. STOP before inserting it.

## 7. Proton

No electromagnetic current. G_E(Q^2) unavailable.

## 8. One-principle test

Same microscopic parameters do **not** simultaneously control a derived T_μν law, nucleon structure, and cosmological density. Knobs: S_W, ξ, EH/Λ/G, vacuum subtraction. Fails as a one-parameter unification.

## 9. Consistency (conditional on the assumptions)

- Covariance of the *minimal* Q_W[f;g]: yes by construction.
- Conservation: on-shell if S_W is a scalar and W is varied or held as a background consistently.
- Ghosts / Z_R: still 6C, open.
- Flat-space limit: yes for the minimal operator.
- Equivalence principle: a prescribed external W(x) is a medium and can violate universality; a dynamical W coupled only through the above form is a scalar-tensor sector, untested here.

## Classification

    NEW GRAVITATIONAL INPUT REQUIRED

to have Einstein (or modified) dynamics at all;

    UNDERDETERMINED

as a completion of the freeze (S_W, ξ, vacuum subtraction free).

Not INCONSISTENT at the level of writing a minimal K(W,g).
Not a COVARIANT COMPLETION of the *program* in the sense of derived gravity + derived W dynamics.

The spectral sector can gravitate in the same way every QFT gravitates. That is not a door to halos or Ω_c.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
