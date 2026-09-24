# Proof 14H — Nonlocal field theories as UV completions of K

**Date:** 2026-09-23. After 14G.1 (q^4 still leaves Π_W ~ ∫ dq). No 0.08. Form factor not fitted.

## Why nonlocal is the next class

Polynomial Ω^2 = m^2 - W q^2 + ∑_{n≥2} c_{2n} q^{2n}/M^{2n-2} always leaves a power-counting UV for Π_W ~ ∫ q^{4-3 deg_Ω} d^3q. Entire-function form factors can give exponential Euclidean decay and (if ghost-free) no extra poles.

Standard IDG / Efimov / Biswas–Mazumdar-type kinetic dressing:

    K(q) = (m^2 - W q^2)  F(q^2/M^2)

or, equivalently, a dressed frequency

    Ω^2(q) = (m^2 - W q^2) exp(q^2/M^2)     example, F entire, F(0)=1.

IR: F=1+O(q^2/M^2) recovers 5R up to a renormalization of W,m. UV Euclidean: loops damped if F grows fast enough on the Euclidean axis.

## Ghost constraint (known NLQFT)

If F has zeros, the propagator acquires extra poles; Weierstrass factorization implies at least one ghost if extra zeros are present. Ghost-free class: F entire and zero-free (typically F=exp(γ) with γ entire, γ(0)=0). Then the physical spectrum is the zeros of m^2-W q^2 only — which is exactly the old wall unless that factor is itself completed.

**Collision with 5R:** dressing (m^2-W q^2) by a zero-free F does **not** remove the locus m^2=W q^2. It only changes the residue/measure. To have Ω^2>0 for all q one still needs the local factor to never vanish (14G.1 q^4, or m^2+W q^2 sign flip — forbidden here).

So a ghost-free entire F multiplies the *same* IR operator. It can make Π_W UV-finite while leaving W_crit / the wall in the local factor.

Hybrid allowed by this audit:

    Ω^2(q) = ( m^2 - W q^2 + c_4 q^4/M^2 ) exp(q^2/M_*^2)

with c_4>0 so the polynomial is positive in the stable regime, and exp damping so Π_W integrals converge. Two new scales (M, M_*) and c_4: all FREE.

## Π_W with exponential damping

    ∂²F/∂W^2 ∝ - ∫ d^3q  (q^2)^2 / Ω(q)^3 .

If Ω(q) ~ q^2 exp(q^2/(2M^2)) at large Euclidean q, the integrand is ~ exp(-3 q^2/(2M^2)) / q^2 and the integral converges. That is the first completion in this program that can make Π_W finite without a hard wall cutoff.

This is existence, not uniqueness. Any entire F with sufficient Euclidean growth works. Krasnikov/Efimov: the form factor is otherwise almost arbitrary; predictions are weak until an extra principle fixes F.

## Causality / unitarity (ledger, not derived here)

NLQFT literature: tree-level unitarity if no extra poles; perturbative unitarity claimed for a class of entire F; microcausality replaced by exponential tails of width 1/M; Minkowski contour issues exist (Euclidean definition + continuation). None of that selects W.

## Relation to 12B-NL

12B-NL: exact S_W = ∫ ΔJ is tautological. Here nonlocality is in the *matter* kinetic operator K, not in an independent W-action. Different slot. It can UV-complete φ loops. It still does not give δS_W/δW unless one identifies F_Cas of the dressed K as the generator — which is 12A again, and still does not select W (14A).

## Classification

| Question | Answer |
|---|---|
| Can NL form factors exist as completions of K? | YES (standard IDQFT class) |
| Ghost-free F remove m^2-Wq^2=0? | NO |
| Hybrid q^4 × entire F make Ω^2>0 and Π_W finite? | YES, with FREE (c_4,M,M_*,F) |
| Is F derived from 5R–14E? | NO |
| Does NLQFT predict 0.08? | NO |
| Does it close J→W? | NO |

Nonlocal QFT is a legitimate UV *language* for the next completion. It is not a substitute for the missing W-equation.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
