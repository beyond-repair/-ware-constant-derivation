# Proof 10A — Spectral geometry / continuum-limit audit

**Date:** 2026-09-23. 5R–9A frozen. No 0.08, r_p, Ω_c, a0, thrust.

## 1. Origin of L

The freeze uses **two different operators** under the same letter.

| Use | What L is | Class |
|---|---|---|
| P1–P9 finite-graph bound W<1/6 | Combinatorial Laplacian on a normalized Sierpiński graph, λ_max=6 | Graph Laplacian / discretization |
| 5R local K_sym | H_0=-∇² on R^d | Continuum model **definition**, not a derived limit of that graph |
| ω²I-WL in general text | Placeholder with L=L†≿0 | Unresolved until one of the above is chosen |

L is not derived from a metric variational principle. It is inserted so that W multiplies a positive operator. PHYSICAL OPERATOR: not established. PHENOMENOLOGICAL CONSTRUCTION: accurate for the coupling pattern. DISCRETIZATION: accurate for the gasket identities.

## 2. Continuum limits (do not fuse them)

**Gasket.** PCF / Kigami theory supplies a controlled limit of the discrete Sierpiński Dirichlet form to a continuum fractal Laplacian L_∞ on the gasket. That limit is mathematics of *that* set. Spectral dimension d_s=2 log 3 / log 5, energy scaling 3/5, resistance 5/3 are TOPOLOGICALLY FIXED for the gasket. They are DISCRETIZATION-DEPENDENT if exported to R^3 or to a galaxy.

**5R.** H_0=-∇² is the ordinary flat Laplacian. It is not the Kigami limit of the graph used for W<1/6. P9 already: unbounded spectrum ⇒ no W>0 keeps K≻0 without a UV cutoff. The number 1/6 does **not** survive this limit (P6).

There is no in-corpus theorem

    L_graph,N → -∇²_physical.

Assuming a graph Laplacian “is” space is POST-HOC.

## 3. Geometry produced

| Question | Gasket L_∞ | 5R -∇² |
|---|---|---|
| Metric / distance | Resistance metric on the gasket | Euclidean |
| Dimension | Fractal (d_s ≠ d_spectral walk) | d |
| Curvature | Not a Riemannian Einstein space | Flat |
| Volume | Bernoulli / self-similar measure | Lebesgue |
| Causal structure | None (Dirichlet form) | None in Euclidean 5R |

Neither object is a spacetime metric g_μν. Geometry appearing does not authorize inserting Einstein equations.

## 4. Spectral invariants that survive *their* limit

- Tr f(L) on a finite graph: DERIVED, DISCRETIZATION-DEPENDENT.
- ζ_L(s), heat-kernel coefficients of -∇²: standard analysis, not computed as a W-theory output in this corpus.
- Spectral dimension of the gasket: TOPOLOGICALLY FIXED for the gasket; UNDEFINED as a claim about QCD or halos.
- Seeley–DeWitt a_2 (trace anomaly density) for a scalar with operator K(W,g): not derived here.

## 5. Coupling to gravity / W

S[W,g] and K(W,g) are not in the freeze. Writing them is a new axiom. 9A already: Maxwell + Ware-weight hooks ≠ Δ_μν.

## 6. Anomaly and trace RG (requested audit)

**Weyl / trace anomaly.** For a free scalar, ∫ Tr ln(-∇²+m²) on a curved background produces T^μ_μ ∝ a E_4 + c W_4 +… after heat-kernel expansion. That is textbook QFT on a *given* g_μν. It is not derived from L_graph, and it does not identify W with a conformal factor unless that identification is ASSUMED.

**Trace / Wetterich RG.** No exact RG equation for Γ_k[W] exists in-corpus. The 6B log is still not β_W (9A.B).

Neither anomaly nor ERG supplies L_graph → L_physical.

## 7. Cross-scale and no-go

Without L → L_physical that is independent of r_p and Ω_c, the spectral sector cannot be used as a fundamental explanation of protons or galaxies.

**Scoped no-go.** As a *cross-scale physical geometry*, the current L is not established. Graph quantities (λ_max=6, W<1/6, 3/5, 0.45 design scale) are not continuum spacetime invariants.

**Not a no-go** against using -∇² as an ordinary QFT kinetic operator in 5R–6C (that use is internal and already frozen).

## Classification

    EFFECTIVE / DISCRETIZED

as a candidate fundamental geometry connecting microphysics to gravity.

The 5R operator is a separate flat-space MODEL DEFINITION. The gasket limit is a separate fractal analysis. They must not be silently identified.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
