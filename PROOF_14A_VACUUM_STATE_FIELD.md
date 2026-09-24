# Proof 14A — Vacuum-state field equation from four clues

**Date:** 2026-09-23. Intersection of entropy / electrostatics / statics / vacuum — only what the locked chain supplies. No 0.08. No χ_vac. No propulsion.

## Objects already possessed

    K(W,g),   F[K],   J_W = -∂F/∂W,   T_μν = -2/√-g δF/δg^{μν},
    S_vN(global,T=0)=0,   S_spec(β),   S_ent(A) ≠ I_Cas.

Chain that exists:

    (g,W) → K → (F, J_W, T, S_spec).

Arrow that does not exist:

    J_W → W.

## Clue 1 — Entropy: state vs flow

S[ρ] and Ṗ are different. Global vacuum is pure, so vacuum information is not S_vN.

Accessible mode count on the real spectrum:

    N_eff(χ) = # { n ∈ Z^3 : χ^2 |n|^2 < 1 }.

This is DERIVED from K and the wall. dN_eff/dt ≠ 0 only if χ(t) or L_i(t) changes, i.e. if geometry or W already evolves. N_eff does not generate that evolution. It records it.

S_spec(β) likewise records occupancy. Ṗ_spec ≠ 0 requires β(t) or Ω_n(t).

**Clue, not equation:** distinguish static K from redistribution of N_eff. No new current is derived.

## Clue 2 — Electrostatic pattern

Poisson: ∇²φ = -ρ/ε_0. Pattern: source → potential → field → stress.

In the spectral theory:

    source  = J_W     (conjugate to W)
    potential = W     only if we declare W to be a potential
    field   = ∇W    only if W=W(x) and a kinetic term exists
    response = T^{Cas}  already derived from δF/δg, not from ∇W

J_W is a source *in the variational sense*. It is not the right-hand side of a PDE for W unless an operator D is supplied.

    D W = J_W

is **not** among the existing equations. D would be a new kinetic/Poisson operator (12B: Z, μ, λ FREE). Electrostatics is an analogy, not a derivation of D.

## Clue 3 — Static ≠ empty

Ḕ=0 can coexist with E≠0. So ∂F/∂W=0 was the wrong reduced test if the true static law is D W = J with J≠0 (11I-A.8: J_W generally nonzero). That statement is logically correct and still does not produce D.

A static law with J≠0 is precisely 12B: δS_W/δW = J_W, coefficients FREE, local V cannot match all L.

## Clue 4 — Vacuum already dynamical in g

    g → K → (F, T, J_W) → g   via Einstein if we couple T^{Cas}.

That loop is closed **for the metric** (up to covariant regulators, 12D). It is not closed for W.

Feedback

    W = W[ vacuum state of K(W,g) ]

requires a map Φ: (K,g,ρ) → W. No such Φ is in 5R–13B.

Candidates one might *postulate*:

    W = f(N_eff),   W = f(I_Cas / (m V)),   W = f(S_spec),
    W = χ^2 m^2 L^2 / (4π^2)   (identity, not a fix),
    W_* = Φ(K(W_*,g)).

The last is a fixed-point schema. It becomes an equation only after Φ is given independently of the W that sits inside K. Using Φ = “read W off K” is tautological.

Thermodynamic balance δS_vac/δW vs δF/δW: at T=0, S_vN=0 and S_spec=0, so δS/δW=0. The balance reduces to J_W=0, already false in the bulk of χ (11I-A.8). Finite-T balance is S_spec(β) vs F and still needs an independent S_W or a maxent principle — extra postulate.

## Intersection

Shared pattern that *is* derived:

    variational generator I_Cas → (J_W, T^{Cas}).

Shared pattern that is *not* derived:

    Poisson / wave operator for W,
    W = W[Q],
    Ṗ as a force.

## Classification of the proposed loop

    matter/geometry → K → vacuum → W → K

| Arrow | Status |
|---|---|
| geometry,W → K | MODEL (5R) |
| K → F,J_W,T | DERIVED |
| K → N_eff, S_spec | DERIVED |
| J_W → W or D W = J | NOT IN THEORY |
| W = Φ(K,g) independent Φ | POSTULATE |
| W_* from ∂F/∂W=0 | NO (11I-A.8) |
| W_* from entropy balance T=0 | reduces to J=0, NO |

## What additional postulate is actually required

Exactly one of:

1. An independent S_W (local EFT, 12B FREE coefficients), or
2. An independent map Φ: state → W not equal to “the W already in K”, or
3. Composite B2: W=W[A,ω] with A,ω given their own equations, or
4. Accept W as an external parameter of K.

The four clues motivate (1) or (2). They do not construct D or Φ from K alone.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
