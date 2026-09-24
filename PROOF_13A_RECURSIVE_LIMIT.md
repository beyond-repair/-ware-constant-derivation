# Proof 13A — Recursive branch / infinite-depth limit

**Date:** 2026-09-23. Source: optimization-limit-conjecture Theorem A + CONJECTURE.md. No min_|W-0.08|.

## Theorem A (finite D) — CONFIRMED

    Φ_D(x_0) = ∑_{d=0}^D k^d (a^d x_0 - x̄)^2 ,   k∈N, k≥1, a∈(0,1).
    ∂²Φ/∂x_0^2 = 2 ∑ (k a^2)^d > 0 .
    x_0^*(D) = x̄  ∑(ka)^d / ∑(ka^2)^d .

Unique minimizer. This does **not** define W.

## Convergence domain (DERIVED)

Geometric sums ∑_{d=0}^∞ r^d converge iff |r|<1.

    |ka| < 1  ⇔  a < 1/k
    |ka^2| < 1 ⇔  a < 1/√k

For k≥2, 1/k ≤ 1/√k, so **both** converge iff a < 1/k.

Inside that domain:

    x_0^∞ = x̄ (1 - k a^2) / (1 - k a) .

**Correction:** Proofs/TheoremA.tex writes x̄(1-ka)/(1-ka^2). That swaps numerator and denominator. The finite-D ratio ∑(ka)^d/∑(ka^2)^d → [1/(1-ka)]/[1/(1-ka^2)] = (1-ka^2)/(1-ka).

Default experiment (k,a)=(3,0.8) has ka=2.4>1. The infinite optimizer **does not exist** for those parameters. x_0^*(D) grows with D.

## What R_D actually is

CONJECTURE.md:

    R_D = (1/N_D) ∑_i 1(|x_i - x̄| > ε) ,   x_d = a^d x_0^* .

This is a **counting fraction**, not x_0^*/x̄ and not a coupling in K. It depends on (k,a,ε,x̄,D).

On a k-ary tree N_D = (k^{D+1}-1)/(k-1) is leaf-dominated. If the infinite-depth values a^d x_0^∞ violate for all large d, then R_D → 1. If only a finite band of depths violates, R_D → 0. Intermediate limits in (0,1) occur only if a positive *leaf* fraction keeps violating as D→∞, i.e. the fail set includes a nonvanishing share of the last layer — typically a rational in k, not a universal irrational.

The code path `R_inf = (1/k)^{d_star+1}/(1-1/k)` is a *different* measure (reweights layers by k^{-d}). It is not the CONJECTURE.md definition. Do not mix them.

## Normalization (13A.2)

    (x, x̄, ε) → (c x, c x̄, c ε)   leaves every indicator invariant.
    (x, x̄) → (c x, c x̄) at fixed ε   changes R_D.

So R_D is dimensionless but **not** invariant under rescaling the state unless ε/|x̄| is held fixed. The invariant is ε/|x̄|, together with (k,a).

    a → c a  is not a symmetry of x_d = a^d x_0.
    k is a discrete graph datum.

There is no unique R_∞(k,a) independent of ε/|x̄|.

## Dimensionless recursive candidates that *are* invariant

Inside a<1/k:

    ρ(k,a) := x_0^∞ / x̄ = (1 - k a^2)/(1 - k a)

is invariant under (x,x̄)→c(x,x̄) and independent of ε. It is a function of two FREE parameters (k,a). It is not selected by the optimizer; the optimizer *assumes* (k,a).

No principle in Theorem A picks (k,a). The repo objective min_Θ |W(Θ)-0.08| is QUARANTINED (matching, not derivation).

## Bridge test — not an identification

W_rec or χ_rec would require a map (k,a,ε) → spectral (W,m,L) that is not supplied. ρ(k,a) is not χ and not W in K=m^2-Wλ.

    R_∞  ≫  W_spectral .
    ρ(k,a) ≫ χ .

The recursive branch is an independent optimizer. It does not presently supply the missing S_W or a unique dimensionless coupling.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
