# Proof 6D.1–6D.3 — Independent S_W audit and stationarity gate

**Date:** 2026-09-23. Claim level ≤ 2. No 0.08. Loop is not S_W.

## 6D.1 — Independent S_W audit

Locked model (P1, A4):

    S_E = S_W[W] + (1/2)<phi, K(W) phi>

S_W depends on W only and is not derived in P1–P9, 5R, or 6A–6C. The Gaussian identity Gamma_E = S_W + (1/2) Tr ln K is an identity given S_W. It does not produce S_W.

Candidate density compatible with the 6B counterterm list (not selected):

    L_W = (1/2) Z_W (∂W)² + (1/2) λ_W (□W)² + V_W(W) + higher

Z_W, λ_W, and the couplings in V_W are free. Signs undetermined by the determinant. Boundary conditions unstated. Counterterms identified in 6A–6B (poles in Z and m²; A2 pole vanishes).

Nothing in the corpus derives those coefficients from a prior symmetry or a non-fit matching.

Verdict: S_W is an independent input, not a derived object. Dynamical determination of W is frozen until L_W is independently derived.

## 6D.2 — Stationarity, then constant W0

    δ Gamma_R / δW(x) = δ S_{W,R}/δW(x) + δ Gamma_matter,R / δW(x) = 0

For the 5R linear insertion the matter piece is -(1/2) Tr(G δV/δW). At constant W0 this is the locked spectral source:

    δS_W/δW |_{W0} = (1/2) Tr(K(W0)^{-1} L) = (1/2) Σ_k λ_k / (ω² - W0 λ_k)

That fixes the slope of S_W at W0, or constrains the pair (S_W, W0). It does not output W0.

Constant background: V_W'(W0) + V_matter'(W0) = 0.
V_matter' is the spectral source. ω and {λ_k} are microscopic inputs. V_W' is assumed/free. m_R, Z_R, λ_R, μ are fluctuation-sector inputs, not a substitute for V_W.

Verdict: W0 = F(derived quantities) is not obtained. W0 = F(free V_W couplings, ω, spectrum). A coefficient fitted to a target W0 is a fit.

## 6D.3 — Scheme and uniqueness (conditional)

If some V_W(W; {g_i}) were given, F(W0; {g_i}, ω, spectrum, μ)=0 may have several roots. Selecting one near 0.08 is forbidden. A raw MSbar piece ~ log(ω²/μ²) is not an observable. Defining Z_R is not determining W.

No numerical branch is computed: that would choose {g_i}.

## Stops hit

No independent S_W in the corpus. Spectral source remains the only closed W-equation. Free coefficient to hit a target ⇒ not a prediction.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
