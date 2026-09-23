# Proof 5R — Quadratic form and self-adjointness of K_sym

**Date:** 2026-09-23
**Claim level:** ≤ 2
Does not unfreeze Stage 1. Does not derive 0.08, 0.23, or a healthy W(x).

## Operator lock (no silent model change)

Frozen constant-W operator: K(W)=omega^2 I - W L, L=L^dagger succeq 0.

Continuum realization: L = H_0 = -nabla^2. Local candidate that recovers the freeze:

    K_sym[W] = omega^2 I - (1/2)(W H_0 + H_0 W)

This is a model definition, not a uniqueness theorem.

Forbidden substitution (removed from lock): K =? omega^2 I - (1-W) H_0.

For constant W=W_0 one has W H_0 = H_0 W = W_0 H_0, hence

    K_sym[W_0] = omega^2 I - W_0 H_0.

## A. Finite graph

L finite Hermitian, W=diag(W_i) real => (W L + L W)/2 Hermitian => K_sym Hermitian on C^N. Self-adjointness automatic. Positivity is a matrix eigenvalue question. No local scalar inequality on the vertex values W_i is equivalent to K_sym succ 0 in general.

STATUS: self-adjointness DERIVED on every finite Hermitian graph realization.

## B. Continuum differential expression

For W in C^2(R^d; R) and f in C_c^infty(R^d):

    H_0(W f) = W H_0 f - 2 nabla W · nabla f - (nabla^2 W) f

    (1/2)(W H_0 + H_0 W) f = W H_0 f - nabla W · nabla f - (1/2)(nabla^2 W) f

    K_sym f = omega^2 f - W H_0 f + nabla W · nabla f + (1/2)(nabla^2 W) f

With H_0 = -nabla^2 this is omega^2 f + W nabla^2 f + nabla W · nabla f + (1/2)(nabla^2 W) f.

The insertion is second-order. It is not a bounded perturbation of H_0 on L^2(R^d). Kato-Rellich does not apply to the whole insertion.

## C. Quadratic form

    Q_W[f] := <f, K_sym f> = int omega^2 f^2 - int W |grad f|^2 + (1/4) int (nabla^2 W) f^2.

Constant check: W ≡ W_0 recovers Q = omega^2 ||f||_2^2 - W_0 ||grad f||_2^2.
The form is symmetric for real W in C^2. Hence K_sym is symmetric on C_c^infty.

## D. Semiboundedness / self-adjointness (conditional)

Not claimed: unique physical domain; essential self-adjointness for arbitrary sign-changing W; any local positivity criterion.

Sufficient Friedrichs condition: W in C_b^2(R^d) and W(x) ≤ 0 everywhere. Then -int W |grad f|^2 ≥ 0. The term (1/4) nabla^2 W is bounded, so Q_W ≥ (omega^2 - C_W) ||f||_2^2 with C_W = (1/4)||nabla^2 W||_infty. If omega^2 > C_W the form is closed and bounded below on a weighted H^1 space. The Friedrichs extension exists and is self-adjoint.

If W ≥ δ > 0 on an open set and the Laplacian spectrum is unbounded, high-momentum test functions make Q_W → -∞. Same continuum obstruction already locked for constant W>0.

REMOVED FROM LOCK (unproved):
- W(x) ≥ 1 => K_sym succ 0
- nabla^2 W > 2 omega^2 => K_sym succ 0

Positivity of a variable-coefficient second-order operator is a global quadratic-form question.

## E. Status table

K_sym chosen to recover K(W0): MODEL DEFINITION + consistency DERIVED
Finite-graph Hermitianity: DERIVED
Pointwise expression: DERIVED for W in C^2, f in C_c^infty
Quadratic form Q_W: DERIVED
Kato-Rellich as bounded perturbation: REJECTED
Local inequalities as positivity: UNPROVED / REMOVED
Friedrichs for W≤0, W in C_b^2, omega^2 large: CONDITIONAL, DERIVED
General sign-changing W on R^d: OPEN
Unique physically correct ordering: NOT DERIVED

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
