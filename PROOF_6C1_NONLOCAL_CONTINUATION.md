# Proof 6C.1 — Exact nonlocal Lorentzian kernel

**Date:** 2026-09-23. Claim level ≤ 2. No 0.08, no unique healthy mode.

Same Feynman integrand as 6A–6B. After d=4-2ε, coeff of log Δ is -P/(64π²), with P the degree-2 polynomial in (Δ, p_E², x) recorded in the verification script.

Continuation p_E² → -q-i0 gives Δ=ω²-x(1-x)(q+i0). When Re Δ<0, log Δ → log|Δ|-iπ.

## Regions

0<q<4ω²: Im I_R = 0. Isolated real zeros of Gamma_{R,M} are possible only here.

q=4ω²: Δ=4ω²(x-1/2)² near x=1/2. log is integrable. I_R finite. Nonanalyticity is the sqrt opening, not the p^4 jet.

q>4ω²: Δ<0 on x in ((1-ξ)/2,(1+ξ)/2), ξ=sqrt(1-4ω²/q).

    int P dx = 4 ω^4 sqrt(1-4ω²/q)

    Im I_R(-q-i0) = [ω^4 / (16π)] sqrt(1-4ω²/q)  θ(q-4ω²)

Near threshold: Im I_R ~ (ω³ / 32π) sqrt(q-4ω²). Two-particle square-root opening.

Check: verify_proof_6C1_im.py PASS.

## Spectral density of the loop kernel

    σ_I(q) = Im I_R / π = [ω^4 / (16π²)] sqrt(1-4ω²/q) θ(q-4ω²)

Gamma_loop = -I/2 ⇒ Im Gamma_loop = -[ω^4 / (32π)] sqrt(...) θ(...).

Propagator Im G = -Im Gamma / |Gamma|^2 is not locked as a KL theorem.

## Lee-Wick (investigation, not identification)

The local p^4 jet has LW algebra (opposite residues) when Delta_R>0. The nonlocal kernel is not a local LW Lagrangian; it has this two-particle cut. Do not name the theory Lee-Wick.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
