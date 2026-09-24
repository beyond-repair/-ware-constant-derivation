# Proof 14G.1 — Minimal q^4 stabilization

**Date:** 2026-09-23. Completes Ω^2=m^2-W q^2 at large q. c_4, M FREE. No 0.08.

## Dispersion

    Ω^2(x) = m^2 - W x + c_4 x^2 / M^2 ,    x=q^2 .

IR: q ≪ M ⇒ Ω^2 = m^2 - W q^2 + O(q^4/M^2). Recovers the locked operator.

c_4>0 required for a high-q floor. c_4<0 makes the UV worse.

    dΩ^2/dx = -W + 2 c_4 x / M^2
    x_⋆ = W M^2 / (2 c_4)     (minimum if c_4>0, W>0)
    Ω_min^2 = m^2 - W^2 M^2 / (4 c_4)

## Regimes (DERIVED given this ansatz)

    stable:    4 c_4 m^2 > W^2 M^2    ⇒  Ω^2(q)>0 all q
    critical:  4 c_4 m^2 = W^2 M^2    ⇒  Ω(q_⋆)=0 and dΩ^2/dq=0
    unstable:  4 c_4 m^2 < W^2 M^2    ⇒  a band with Ω^2<0

Critical coupling:

    W_crit = 2 m sqrt(c_4) / M .

This is a **relation among three FREE quantities** (m, M, c_4), not a predicted number. m is already in K; M and c_4 are new UV data. No mechanism in 5R–14E fixes M/m or c_4.

## Soft mode and entropy

As W → W_crit^-, Ω(q_⋆)→0. Thermal n_B(Ω)→∞ and S_spec is dominated by that shell. Entropy *responds* to the soft mode; it does not set W_crit.

Static Green function of the *matter* dispersion (not D_W):

    G_φ(q) = 1 / (m^2 - W q^2 + c_4 q^4/M^2)

blows up at q_⋆ when critical. That is enhanced vacuum response of φ, not a derived Poisson law for W.

## Does Π_W become finite?

Raw ∂²F/∂W^2 ∝ - ∑ λ^2 / (8 Ω^3).

At large q, Ω ∼ sqrt(c_4) q^2 / M, λ=q^2 ⇒ λ^2/Ω^3 ∼ M^3 / (c_4^{3/2} q^2).

    ∫ d^3q / q^2 ∼ ∫^Λ dq    still linearly UV divergent.

The finite-q pole is gone if Ω_min>0, but Π_W is **not** UV-finite. Need a harder completion (c_6, form factor, or cutoff) or accept a subtracted Π.

## Is ΔF_{T^3-R^3} well-defined?

E_0=∑ Ω/2 with Ω∼ q^2 at large q ⇒ ∫ d^3q Ω ∼ ∫ q^4 dq, worse power than the old sqrt(m^2-Wq^2) (which was not even defined at large q). The *difference* T^3-R^3 still exists as a Poisson remainder of a smoother symbol, but local counterterms of dimension ≤5 must be specified. Not automatic.

## Checklist

| Condition | q^4 completion |
|---|---|
| Ω^2>0 possible | YES if 4 c_4 m^2 > W^2 M^2 |
| IR = m^2-Wq^2 | YES |
| Π_W finite at high q | NO (∫ dq) |
| ΔF well-defined without new ct | NO |
| Soft mode possible | YES at W=W_crit |
| Selects a number for W | NO |

## Verdict

Minimal q^4 is a *possible* IR-stable UV patch. It converts the old wall into a critical surface W_crit=2m sqrt(c_4)/M in a larger parameter space. It does not compute W, Z, or 0.08. Π_W remains UV-divergent. Next allowed test is c_6 or a form factor if one wants finite Π; that is another FREE coefficient, not a derivation.

W as a phase-control parameter is an interpretation of this ansatz, not a theorem of the 5R operator.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
