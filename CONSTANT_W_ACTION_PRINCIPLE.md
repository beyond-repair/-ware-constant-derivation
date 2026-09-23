# Constant-W Action Principle — Canonical Lock

**Project / Version:** Action Principle for Scale Field \(W\) · Canonical Lock (Freeze Point)  
**Date:** 2026-09-23  
**Claim level:** ≤ 2  
**experimental_validation / thrust_validated / energy_extraction_validated:** false

This file is the filled derivation of the freeze text. It isolates identities that follow from a constant coupling \(W\) and a Euclidean Gaussian integral. It does **not** derive \(W=0.08\), \(W_\star=1/(4\pi)\), \(\xi=0.23\), or a healthy local field \(W(x)\).

---

## STATE

- **Objective:** Establish the mathematically verified boundary of the constant-\(W\) action principle.
- **Accepted facts:**
  - Euclidean Gaussian \(\Gamma_E = S_W + \tfrac12\operatorname{Tr}\ln K[W]\).
  - One-loop determinant contribution is strictly concave: \(V''_{\mathrm{1-loop}}(W)<0\).
  - Spectral pole: \(W\to W_{\mathrm{crit}}^-=(\omega^2/\lambda_{\max})^- \implies V_{\mathrm{1-loop}}\to-\infty\).
  - Finite normalized graph bound: \(W<1/6\) for \(\lambda_{\max}=6\), \(\omega=1\).
- **Rejected hypotheses:**
  - Determinant convex barrier / positive stabilizing wall.
  - Automatic healthy propagation (\(Z_{\mathrm{eff}}\neq 0\) is not a Lorentzian existence theorem).
  - Derived numerical values \(W=0.08\), \(W(n)=0.08\,e^{0.23(n-3)}\), or a continuum bound \(1/6\) without a UV cutoff.
- **Open questions:** Hermitian ordering \(K[W(x)]\), regularized \(\Gamma^{(2)}(p)\), renormalized \(Z_{\mathrm{ren}}\), coarse-graining \(W(x)\to W(n)\).
- **Locked invariants:** Constant-\(W\) spectral source identity derived; local dynamical \(W(x)\) open.

**Assumptions**

| ID | Class | Statement |
|----|-------|-----------|
| A1 | User | Matter sector is a real scalar with quadratic Euclidean action \(\tfrac12\phi\cdot K[W]\phi\). |
| A2 | Model | Spectral operator \(K(W)=\omega^2 I-WL\) with \(L=L^\dagger\succeq 0\) and constant \(W\). |
| A3 | Model | Work in the positive-definite domain \(K(W)\succ 0\). |
| A4 | User | \(S_W\) depends on \(W\) only; it is not derived here. |
| A5 | Model | Discrete spectrum \(\{\lambda_k\}\) of \(L\) (finite graph, or any compact realization). |

---

## 1. Microscopic Euclidean action and Gaussian integration

Let \(\phi\) be a real scalar on a finite Hilbert space (graph, lattice, or compact mode basis). The Euclidean action at **constant** \(W\) is

\[
S_E[\phi;W]
=
\frac12\,\phi^{\mathsf T}K(W)\,\phi
+
S_W[W],
\qquad
K(W)=\omega^2 I-WL.
\]

The Gaussian integral is exact:

\[
Z[W]
=
\int\mathcal D\phi\,e^{-S_E[\phi;W]}
=
e^{-S_W[W]}\,(\det K(W))^{-1/2}
\times\text{(W-independent measure factor)}.
\]

The Euclidean effective action is therefore

\[
\boxed{
\Gamma_E[W]
=
S_W[W]
+
\frac12\operatorname{Tr}\ln K(W)
+
\text{const}.
}
\]

**Convention note.** Some earlier corpus lines write \(\Gamma=-\tfrac12\operatorname{Tr}\ln K\). That is a different generating-functional convention. The identities below use the Euclidean Gaussian convention \(\Gamma_E=S_W+\tfrac12\operatorname{Tr}\ln K\).

---

## 2. Stationarity and the spectral source equation

For constant \(W\), \(\delta K=-L\,\delta W\). The first variation of the determinant term is

\[
\delta\Bigl(\tfrac12\operatorname{Tr}\ln K\Bigr)
=
\frac12\operatorname{Tr}\bigl(K^{-1}\delta K\bigr)
=
-\frac12\operatorname{Tr}\bigl(K^{-1}L\bigr)\,\delta W.
\]

Hence

\[
\frac{\delta\Gamma_E}{\delta W}
=
\frac{\delta S_W}{\delta W}
-
\frac12\operatorname{Tr}\bigl[(\omega^2 I-WL)^{-1}L\bigr].
\]

Stationarity \(\delta\Gamma_E/\delta W=0\) is the exact source equation

\[
\boxed{
\frac{\delta S_W}{\delta W}
=
\frac12\operatorname{Tr}\bigl[(\omega^2 I-WL)^{-1}L\bigr]
=
\frac12\sum_k\frac{\lambda_k}{\omega^2-W\lambda_k}.
}
\]

Geometry enters the equation of motion only through \(\{\lambda_k\}\). No value of \(W\) is selected until \(S_W\) is specified.

**Identity check.** On any finite Hermitian \(L\succeq 0\), the trace form and the spectral sum agree to machine precision (`verify_constant_W_action.py`).

---

## 3. Determinant concavity and spectral boundary

Define the matter one-loop potential (additive constant dropped)

\[
V_{\mathrm{1-loop}}(W)
=
\frac12\sum_k\ln(\omega^2-W\lambda_k),
\qquad
K(W)\succ 0.
\]

First and second derivatives:

\[
V'_{\mathrm{1-loop}}(W)
=
-\frac12\sum_k\frac{\lambda_k}{\omega^2-W\lambda_k},
\]

\[
\boxed{
V''_{\mathrm{1-loop}}(W)
=
-\frac12\sum_k\frac{\lambda_k^2}{(\omega^2-W\lambda_k)^2}
<0
}
\]

whenever at least one \(\lambda_k\neq 0\) (true for any nontrivial \(L\succeq 0\)).

Consequences:

1. **Concavity.** The determinant contribution is strictly concave on \(K\succ 0\). It does not generate a positive stabilizing wall.
2. **Pole.** If \(\lambda_{\max}>0\) has nonzero multiplicity, then as \(W\to(\omega^2/\lambda_{\max})^-\) one has \(V_{\mathrm{1-loop}}\to-\infty\).
3. **Finite graph domain.** Operator positivity requires \(W<\omega^2/\lambda_{\max}\) (and \(W\) such that every mode stays positive). On the finite normalized Sierpiński graph with the locked combinatorial value \(\lambda_{\max}=6\) and \(\omega=1\),

\[
\boxed{0\le W<\frac16.}
\]

4. **Continuum.** If the spectrum of \(L\) is unbounded, no \(W>0\) keeps \(K(W)\) globally positive without an explicit UV cutoff or regulator. The number \(1/6\) is **not** a continuum theorem.

Finite-difference checks of \(V'\) and \(V''\) against the closed formulae pass (`verify_constant_W_action.py`).

---

## 4. Boundary of promotion to \(W(x)\)

If \(W\) is promoted to a multiplication operator \(W(x)\), then \([W,L]\neq 0\) in general. A Hermitian ordering must be chosen. One admissible choice is

\[
K_{\mathrm{sym}}[W]
=
\omega^2 I
-
\frac12\bigl(WL+LW\bigr).
\]

Other orderings (left, right, Weyl with extra commutator counterterms) are different models.

The second functional derivative defines a two-point kernel

\[
\Gamma^{(2)}(x,y)
=
\frac{\delta^2\Gamma_E}{\delta W(x)\,\delta W(y)}.
\]

In a translation-invariant background its Fourier transform admits the small-\(p\) expansion

\[
\Gamma^{(2)}(p)
=
M_{\mathrm{eff}}^2
+
Z_{\mathrm{eff}}\,p^2
+
O(p^4),
\]

once a regulator is fixed. Neither \(M_{\mathrm{eff}}\) nor \(Z_{\mathrm{eff}}\) is computed in this freeze.

### Interpretation of \(Z_{\mathrm{eff}}\)

- If \(Z_{\mathrm{eff}}=0\) at the order examined, the determinant does not supply a two-derivative kinetic term.
- If \(Z_{\mathrm{eff}}\neq 0\), a derivative term exists. Health of a Lorentzian mode still requires the renormalized sign, the residue, and the rest of the quadratic action.

**Model-specific sign statement (not a universal theorem).** For the stated \(K_{\mathrm{sym}}\) under standard Euclidean heat-kernel / gradient expansions, the unrenormalized determinant contribution to the \(p^2\) term is negative (\(Z_{\mathrm{induced}}<0\)). If that sign survives renormalization, a stable propagating \(W\) needs a sufficiently positive contribution from \(S_W\) or another sector. That positive term is not derived here. A propagating \(W(x)\) therefore remains phenomenological until ordering, UV prescription, counterterms, and \(Z_{\mathrm{ren}}\) are fixed.

---

## 5. Status ledger

| Theory component | Status |
|---|---|
| Constant-\(W\) action principle | **DERIVED** \(\delta S_W/\delta W=\tfrac12\operatorname{Tr}[(\omega^2 I-WL)^{-1}L]\) |
| 1-loop potential concavity | **DERIVED** \(V''_{\mathrm{1-loop}}<0\); barrier hypothesis refuted |
| Finite-graph positivity bound | **DERIVED** \(W<1/6\) for \(\lambda_{\max}=6\), \(\omega=1\) |
| Local dynamical \(W(x)\) | **OPEN** (ordering, UV, counterterms) |
| Renormalized \(Z_{\mathrm{ren}}\) and sign | **OPEN** (unrenormalized \(Z_{\mathrm{induced}}<0\) for \(K_{\mathrm{sym}}\)) |
| Trajectory \(W(n)\) | **OPEN** (needs an independent coarse-graining map) |
| Parameters \(0.08\) and \(0.23\) | **NOT DERIVED** (external phenomenological inputs) |
| \(W_\star=1/(4\pi)\) | **NOT DERIVED** by this spectral source (separate matching / E1–E4 track) |

\[
\boxed{\text{Constant-}W\text{ action principle: DERIVED.}}
\]

\[
\boxed{\text{Local dynamical }W(x)\text{: NOT YET DERIVED.}}
\]

---

## Canonical summary

This is the action principle presently derived for constant \(W\): a spectral source for \(\delta S_W/\delta W\), a concave one-loop determinant potential, and a finite-graph positive-definiteness boundary. Promotion to a propagating \(W(x)\) remains open because the Hermitian local operator, UV prescription, counterterms, and renormalized two-point function have not been fixed. For the stated symmetrized operator and Euclidean convention, the unrenormalized determinant contribution to the \(p^2\) term is negative; that is a model-specific statement, not a universal theorem about \(W\). No action-derived value of \(0.08\) or \(0.23\) has been obtained.

Deterministic check: `verify_constant_W_action.py`.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
