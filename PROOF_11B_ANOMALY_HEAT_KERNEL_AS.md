# Proof 11B — Anomaly-induced stress energy, heat kernels, asymptotic safety

**Date:** 2026-09-23. 5R–11A frozen. Does not derive W, 0.08, Omega_c, or thrust.

This is textbook QFT-in-curved-space plus the Reuter program. It does not reopen 8B–10A.

## Heat kernel

For a Laplace-type operator on a closed Riemannian 4-manifold,

    D = -∇² + E ,     E = ξ R + E_W

with E_W the endomorphism from the 11A W-insertion (mass-like and first-derivative pieces after bringing Q_W to Weitzenböck form),

    Tr e^{-t D} \sim (4\pi t)^{-2} \sum_{n=0} t^n \int \sqrt{g}\, \mathrm{tr}\,a_n .

Local densities (real scalar, bundle curvature \Omega_{\mu\nu}=0):

    a_0 = 1

    a_1 = R/6 - E = (1/6 - \xi) R - E_W

    a_2 = \frac{1}{180}R_{\alpha\beta\gamma\delta}R^{\alpha\beta\gamma\delta}
         - \frac{1}{180}R_{\alpha\beta}R^{\alpha\beta}
         + \frac{1}{2}\Bigl(\xi-\frac{1}{6}\Bigr)^2 R^2
         + \frac{1-5\xi}{30}\Box R
         + \frac12 E_W^2 - \frac16 R E_W + \cdots

Equivalent 4d Weyl/Euler form (E_W=0):

    a_2 = \frac{1}{120} C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}
        - \frac{1}{360} E_4
        + \frac12(\xi-1/6)^2 R^2
        + \frac{1-5\xi}{30}\Box R

with

    C^2 = Riem^2 - 2 Ricci^2 + R^2/3 ,
    E_4 = Riem^2 - 4 Ricci^2 + R^2 .

One-loop Euclidean Γ_{\phi} = (1/2) Tr ln D. Proper-time:

    (1/2) Tr ln D = -1/2 \int_{\epsilon}^\infty dt/t Tr e^{-tD} + (\mu\text{-scheme}).

Poles in 4d:

    \sim \frac{1}{32\pi^2\epsilon^2}\int a_0 + \frac{1}{16\pi^2\epsilon}\int a_1 + \frac{\log(\mu^2\epsilon)}{32\pi^2}\int a_2 + finite .

These renormalize \Lambda, G^{-1}, and higher-derivative couplings. Same bookkeeping as 6A–6B, now with curvature.

## Anomaly-induced <T_{\mu\nu}>

For a classically Weyl-invariant theory (\xi=1/6, E_W=0, massless),

    g^{\mu\nu}\langle T_{\mu\nu}\rangle
    = \frac{c}{16\pi^2} C_{\alpha\beta\gamma\delta}C^{\alpha\beta\gamma\delta}
    - \frac{a}{16\pi^2} E_4
    + b \Box R .

One real conformal scalar: a = 1/360, c = 1/120. The \Box R coefficient is scheme-dependent (local R^2 counterterm).

The anomaly does not determine the full tensor. The conserved, symmetric completion is the variational derivative of the Riegert / Fradkin–Tseytlin nonlocal action built from those densities. In FLRW that reduces to the Starobinsky / anomaly-driven trace

    \langle T^\mu_\mu\rangle \propto \Box R + R^2 \text{ combinations},

which can source vacuum energy and an effective R^2 inflationary term. That is a property of conformal matter on a metric, not of the freeze's W, and not Ω_c.

If E_W \neq 0 or \xi \neq 1/6, the theory is not Weyl invariant. The trace then has extra non-anomalous pieces \sim E_W \langle\phi^2\rangle and improvement terms. Those are model-dependent and not a derivation of a universal χ.

## Asymptotic safety

Weinberg (1979): gravity can be UV-complete at an interacting fixed point with finitely many relevant couplings. Reuter (1998): Wetterich equation for Γ_k[g], Einstein–Hilbert truncation

    Γ_k = \frac{1}{16\pi G_k} \int \sqrt{g}\,(R-2\Lambda_k),
    g_k = G_k k^2,\quad \lambda_k = \Lambda_k/k^2 .

Evidence (truncation-dependent, mostly Euclidean): a non-Gaussian fixed point (Reuter point) with typically two relevant directions, G and Λ. Critical exponents in EH-type truncations are O(1) and often a complex pair; higher-derivative and f(R) truncations keep a small number of relevant operators. Matter can deform the point without destroying it in many SM-like counts. Lorentzian status is open. Fixed-point coordinates (g_*,\lambda_*) are truncation artifacts; IR G and Λ are fitted to observation along relevant directions.

Heat kernels enter AS as the evaluation of FRG traces Tr[(\Gamma_k^{(2)}+R_k)^{-1} \partial_t R_k] on backgrounds. That uses the same a_n technology. It does not identify W with g_* and does not compute a Ware constant.

## Ledger versus the freeze

| Claim | Status |
|---|---|
| Explicit a_0,a_1,a_2 for a Laplace-type scalar | Standard (Gilkey) |
| Anomaly <T^\mu_\mu> for a conformal scalar | Standard; a=1/360, c=1/120 |
| Full <T_{\mu\nu}> from the 11A K(W,g) | UNDERDETERMINED (E_W, ξ, S_W) |
| AS Reuter point as a UV scenario for EH | Research program; not derived from 5R |
| W or 0.08 from a_* or g_* | FORBIDDEN / NOT DERIVED |
| Ω_c from the anomaly | NOT DERIVED (CC problem) |

11A stands: the sector gravitates as QFT gravitates. 11B only names the local polynomials and the AS literature. No new door to protons or halos.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
