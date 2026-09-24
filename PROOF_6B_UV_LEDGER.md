# Proof 6B — UV ledger of I_d(p) and minimal renormalization

**Date:** 2026-09-23
**Claim level:** ≤ 2
Does not unfreeze Stage 1. Does not derive 0.08, 0.23, a unique physical Z_ren, or a healthy Lorentzian W.

Depends on Proof 5R and Proof 6A conventions Z_loop = -I2_bar/2 with I2_bar = A1.

## 6B.1 Expansion

I_d(p) as in 5R/6A. Feynman x, shift k=l-(1-x)p:

    Delta = ω^{2} + x(1-x)p^{2},   c=x^{2}+(1-x)^{2},   a=1-2x.

After odd-l drop and scaleless int 1 = 0 in dim-reg:

    I_d(p) = ∫_0^1 dx [ -2 Delta I1 + Delta^{2} I2 + (c+a^{2}/d)p^{2}(I1-Delta I2) + (c^{2}/4)p^{4} I2 ]

with I_ν = (4π)^{-d/2} Gamma(ν-d/2)/Gamma(ν) Delta^{d/2-ν}.

I_d(p) = A0 + A1 p^{2} + A2 p^{4} + O(p^6) at d=4-2ε.

Check: verify_proof_6B_uv.py (PASS).

    A0 = 3ω^{4}/(16π^{2}ε) + 3ω^{4}/(16π^{2})[-γ_E+log(4π)-log(ω^{2})+2/3] + O(ε)

    A1 = -ω^{2}/(32π^{2}ε) + ω^{2}/(32π^{2})[γ_E-log(4π)-4/3+log(ω^{2})] + O(ε)

    A2 = 1/(960π^{2}) + O(ε)

A1 equals I2_bar^DR from 6A (pole and finite). Chain 5R → I(p) → A1 → 6A closed.

The 1/ε density of A2 is a polynomial in x that integrates to 0 on [0,1]. For this kernel the (Box W)^{2} dim-reg pole cancels. A finite p^{4} remainder remains.

## 6B.2 Counterterms

Gamma^(2) = -I/2 implies

    m_loop^{2} = -A0/2,   Z_loop = -A1/2,   lambda_loop = -A2/2.

Z_loop^DR pole = +ω^{2}/(64π^{2}ε) as in 6A.

m_loop^{2} pole = -3ω^{4}/(32π^{2}ε).

lambda_loop = -1/(1920π^{2}) + O(ε)  (no 1/ε).

W^{2} must be renormalized. (∂W)^{2} must be renormalized. (Box W)^{2} has no 1/ε in this kernel but a finite remainder. A propagating mode cannot be read from A1 alone.

## 6B.3 Minimal schemes

1/ε_bar := 1/ε - γ_E + log(4π). Restore μ by log(ω^{2})→log(ω^{2}/μ^{2}).

MSbar poles:

    δm^{2} = 3ω^{4}/(32π^{2} ε_bar),
    δZ_W = -ω^{2}/(64π^{2} ε_bar),
    δlambda = 0.

If the bare kinetic coefficient is set to 0 rather than derived:

    Z_ren^{MSbar, Z_W bare=0} = ω^{2}/(64π^{2}) [ 4/3 - log(ω^{2}/μ^{2}) ].

This is a scheme remainder, not a first-principles Z. It depends on μ. It is not 0.08.

MOM definition (not a derived output):

    d Gamma_R^(2) / d p^{2}  at p_E^{2}=μ^{2}  equals 1.

That normalizes the renormalized field at μ. Independent conditions are still required for p^0 and p^4 if a fully subtracted two-point function is claimed.

## Not derived

Lorentzian pole/residue (Proof 6C, only after Gamma_R is fully specified);
unique physical Z_ren; 0.08; 0.23; W(n); thrust.
If 6C fails, stop. Do not insert phenomenology.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
