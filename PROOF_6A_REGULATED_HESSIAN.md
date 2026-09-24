# Proof 6A — Regulated Hessian: dim-reg pole, cutoff comparison, counterterm boundary

**Date:** 2026-09-23
**Claim level:** ≤ 2
Does not unfreeze Stage 1. Does not derive 0.08, 0.23, Z_ren, or a healthy W(x).

## Conventions

I(p) and I2(k) as in the 5R ledger. Integrated coefficient

    I2_bar := ∫ d^d k/(2π)^d I2(k),    I(p)=I(0)+I2_bar p^2+O(p^4).

Quadratic determinant piece:

    Gamma_loop^(2) = -1/4 ∫ d^d p/(2π)^d W(p)W(-p) I(p).

Kinetic convention (1/2)∫ Z (∂W)^2 implies

    Z_loop = - (1/2) I2_bar.

## Theorem 6A.1 — DR of I2_bar

At d=4-2ε the Beta-function continuation (verify_proof_6A_dimreg.py) gives

    I2_bar^DR = -ω^{2}/(32 π^{2} ε) + ω^{2}/(32 π^{2}) [γ_E - log(4π) - 4/3 + log(ω^{2})] + O(ε).

    Z_loop^DR = +ω^{2}/(64 π^{2} ε) - ω^{2}/(64 π^{2}) [γ_E - log(4π) - 4/3 + log(ω^{2})] + O(ε).

STATUS: DERIVED for this kernel, d=4-2ε, and the stated Z convention.

## Theorem 6A.2 — Hard cutoff

I2(k) ~ 1/(d k^{2}). In d=4,

    ∫_{|k|≤Λ} d^4k/(2π)^4 I2(k) = Λ^{2}/(64 π^{2}) + O(log(Λ/ω)).

Z_loop^cut = -Λ^{2}/(128 π^{2})+⋯ < 0 at leading power.

Dim-reg discards that quadratic power and keeps a 1/ε pole of opposite sign. Not a contradiction: different local divergences.

LOCK: I2(k)>0 does not imply a universal negative physical Z_ren. Unrenormalized Z_loop is regulator-dependent.

## Theorem 6A.3 — Counterterm that cancels the DR pole

If S_W contains (1/2) Z_W ∫(∂W)^2 and S_ct=(1/2) δZ_W ∫(∂W)^2, the DR pole is cancelled by

    δZ_W = -ω^{2}/(64 π^{2} ε) + finite scheme term.

The determinant fixes the pole. It does not fix finite Z_ren = Z_W + Z_loop^finite + Z_ct^finite.

STATUS: counterterm structure DERIVED. Finite Z_ren OPEN. Existence of independent Z_W still a model assumption.

## Not derived

Unique finite Z_ren from the determinant; preferred renormalization condition; full I(p); Lorentzian pole/residue; 0.08; 0.23; W(n); healthy W(x).

Next package (6B): full regulated I(p), one explicit renormalization condition that does not use 0.08 or thrust, then residue analysis or a stop.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
