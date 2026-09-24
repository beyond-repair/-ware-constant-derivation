# Proof 6C — Lorentzian continuation and pole audit

**Date:** 2026-09-23
**Claim level:** ≤ 2
Does not unfreeze Stage 1. Does not derive 0.08, 0.23, W(n), thrust, or a unique physical Z.

Gate: use only the 6A–6B two-point structure. Keep m_R^{2}(μ), Z_R(μ), λ_R(μ) independent and symbolic. Do not set Z_R=1. Do not treat loop pieces as the full action.

## Object

    Gamma_R^(2)(p_E^{2}) = m_R^{2} + Z_R p_E^{2} + λ_R p_E^{4} + Gamma_nl,R

Mostly-minus Wick p_E^{2} → -p_M^{2} - i0, q := p_M^{2}:

    Gamma_{R,M}(q) = m_R^{2} - Z_R q + λ_R q^{2} + Gamma_nl,M(q)

G_R = 1/Gamma_{R,M} (overall i is convention, not the ghost diagnostic).

## Case A — λ_R=0, local, nl=0

    q_star = m_R^{2} / Z_R          (Z_R ≠ 0)
    Res G = -1/Z_R

Positive Minkowski mass-squared needs m_R^{2} and Z_R the same sign.
Euclidean stability of the local quadratic form needs Z_R>0 and m_R^{2}>0, which gives q_star>0.
Z_R<0 makes the Euclidean kinetic term unbounded below.

Setting λ_R=0 is an admissible finite renormalization: 6B found no 1/ε pole in A2. Case A is a scheme choice, not the unique continuation of the loop.

STATUS: second-order baseline DERIVED. Healthy-pole existence is the sign condition, not a theorem of the determinant.

## Case B — λ_R≠0, local, nl=0

    Delta_R = Z_R^{2} - 4 λ_R m_R^{2}
    q_± = [Z_R ± sqrt(Delta_R)] / (2 λ_R)

Delta_R<0: complex pair. =0: repeated root. >0: two real roots.

    (d Gamma/dq)|_{q_±} = ± sqrt(Delta_R)
    Res_± G = ± 1/sqrt(Delta_R)     (Delta_R>0)

Whenever both roots are real, residues are opposite. That is the local higher-derivative pattern. Zero UV pole for A2 does not remove it if λ_R is kept nonzero.

λ_R→0: one root → m_R^{2}/Z_R, the other → ∞.

STATUS: DERIVED for the local quartic jet.

## Case C — nonlocal remainder

    Delta(x,q) = ω^{2} - x(1-x)(q+i0),   x in [0,1]
    max x(1-x) = 1/4  ⇒  cut opens at q_th = 4 ω^{2}

Below the cut the subtracted loop stays off the branch. The local polynomial does not reproduce the cut.
A candidate pole from A/B must be checked on the physical sheet of the subtracted I_d(-q-i0). That full function-of-q search is not executed here.

STATUS: threshold DERIVED. Full nonlocal pole search OPEN.

## Scheme

MSbar vs MOM move Z_R(μ) and the 6B finite remainder. They do not cancel Case B residue opposition or move q_th=4ω^{2}.
The MSbar remainder is not a physical constant and is not 0.08.

## Not concluded

No numerical mass or Z. No healthy Coherence Drive mode. No ghost-in-nature theorem — only the local quartic dichotomy if λ_R≠0 and Delta_R>0 are kept. No Im Gamma_nl above the cut.
If a later full I_d continuation finds no isolated physical-sheet pole with Z_R>0, freeze; do not insert 0.08.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
