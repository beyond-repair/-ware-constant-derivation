# Proof 14J / 14J.1 — Collective / Hubbard–Stratonovich W

**Date:** 2026-09-23. No fundamental W. No 0.08. kappa FREE.

## Microscopic auxiliary (14J.1)

    S_Φ = (1/2) Φ D_Φ Φ + h Φ O_L ,    O_L = φ L φ .

No W in the UV. Integrating a local mass D_Φ=M^2 (zero mode):

    S_eff = - (h^2 / (2 M^2)) O_L^2 .

That is a quartic (φ L φ)^2 theory, not a free K=m^2-W L. Mean field:

    Φ_0 = - (h/M^2) <O_L> ,    W_eff := h Φ_0 = - (h^2/M^2) <φ L φ> .

On the Gaussian vacuum of K=m^2-W_eff L,

    <φ L φ> = Tr(L K^{-1}) .

Gap equation:

    W = κ Tr(L K(W)^{-1}) ,    κ := -h^2/M^2   or the sign convention that yields W>0.

At T=0 on retained modes, Tr(L K^{-1}) ∝ ∑ λ_n/Ω_n = S(W).

    W = κ S(W) .

This is **not** ∂F/∂W=0. That demanded S=0, which fails. The gap demands W proportional to S, which can have a root for some κ.

## Existence, not selection

On the unit torus (m=a=1 toy), S(W)=∑ n^2/sqrt(1-W n^2) over the wall:

    W=0.04 ⇒ κ~2.7e-6
    W=0.10 ⇒ κ~6.4e-5
    W=0.20 ⇒ κ~1.5e-3

Every W in (0,W_wall) is a root for some κ. κ is a microscopic coupling. Unless κ is derived (it is not), W_eff is not selected. 0.08 is one point on that curve, not distinguished.

## Π_W matching

Φ fluctuations: inverse propagator D_Φ + h^2 Π_{OO}. Π_{OO} is the O_L bubble = L K^{-1} L K^{-1}, i.e. the same skeleton as 14D Π_W. Mean-field HS is compatible with Π_W at quadratic level if D_Φ is chosen to match the local part of 12B (Z, V''). That local part remains FREE. Beyond mean field, S_eff is (O_L)^2: extra scattering not present in free K.

## Six-point test

| # | Requirement | HS class |
|---|---|---|
| 1 | IR K → m^2-W q^2 | YES at mean field |
| 2 | W=h<Φ> | YES by definition |
| 3 | <Φ> determined dynamically | YES, but by FREE κ |
| 4 | Π_W reproduced | YES at one loop / bubble |
| 5 | Ω^2>0 | only inside the wall; UV same as 5R |
| 6 | no extra ghost | Φ auxiliary: healthy if M^2>0; not a graviton |

Mean-field HS is a legitimate *language* for emergent W. It does not compute W. It replaces the missing 14A arrow with a gap whose kernel is already Tr(L K^{-1}).

## What this is not

Not V(W) fitted to 0.08. Not an entropy force. Not Poisson for W (spatial Φ dynamics need D_Φ(q), FREE). Not a UV completion of the wall (14G/14H still required for Ω^2 at large q).

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
