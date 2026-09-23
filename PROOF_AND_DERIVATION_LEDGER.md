# Action Principle for W — Proof and Derivation Ledger

**Review version:** 2026-09-23

**Rule:** Do not promote a model assumption, regulator-dependent result, phenomenological parameter, or unresolved extension into a derived theorem.

Only constant-W steps 1–5 are fully locked as theorems. Local K_sym is a model definition plus Proof 5R. Hessian and I2 are exact / model-specific. Z_ren and W(n) remain open.

## Locked constant-W theorems

**P1.** Model: S_E = S_W + (1/2)<phi, K(W) phi>, K(W)=omega^2 I - W L, L=L^dagger succeq 0. Form of K is a model assumption.

**P2.** Gamma_E = S_W + (1/2) Tr ln K(W) for K succ 0. Euclidean Gaussian identity.

**P3–P4.** delta S_W / delta W = (1/2) Tr[(omega^2 I - W L)^{-1} L] = (1/2) sum_k lambda_k / (omega^2 - W lambda_k). Does not select a number for W.

**P5.** V''_1-loop(W) = -(1/2) sum_k lambda_k^2 / (omega^2 - W lambda_k)^2 < 0 on K succ 0. No convex determinant barrier.

**P6.** K succ 0 iff W < omega^2 / lambda_max. Normalized finite Sierpinski: lambda_max=6, omega=1 => W < 1/6. Not a continuum bound.

**P7.** W -> (omega^2/lambda_max)^- implies V_1-loop -> -infinity. First instability is the largest eigenvalue.

**P8.** Inside the disk |W lambda_k / omega^2|<1: V_1-loop = -(1/2) sum_n W^n / (n omega^{2n}) Tr(L^n) up to a constant.

**P9.** If lambda_k -> infinity, no W>0 keeps K globally positive without a UV restriction.

## Proof 5R — local operator

Canonical candidate (recovers P1):

    K_sym[W] = omega^2 I - (1/2)(W H_0 + H_0 W),   H_0 = -nabla^2

Rejected silent substitution: omega^2 I - (1-W) H_0.

Constant limit DERIVED: K_sym[W_0] = omega^2 I - W_0 H_0.

Finite graph: K_sym automatically Hermitian. DERIVED.

Continuum form DERIVED on C_c^infty:

    Q_W[f] = int omega^2 f^2 - int W |grad f|^2 + (1/4) int (nabla^2 W) f^2.

Kato-Rellich for the whole insertion REJECTED (second-order, not bounded).

Local slogans W>=1 or nabla^2 W > 2 omega^2 as positivity: UNPROVED / REMOVED.

Friedrichs extension: CONDITIONAL / DERIVED for W<=0, W in C_b^2, omega^2 large enough.

General sign-changing positivity: OPEN. Unique ordering: NOT DERIVED.

Full write-up: PROOF_5R_KSYM.md.

## Hessian and I2

For linear insertion V[W]=(1/2)(W H_0 + H_0 W), G=K^{-1}:

    delta Gamma_loop = -(1/2) Tr(G delta V)
    delta^2 Gamma_loop = -(1/2) Tr(G delta V G delta V)
    Gamma_loop^(2)[W1,W2] = -(1/2) Tr(G V[W1] G V[W2])

DERIVED for a linear insertion, conditional on consistent K_0.

About W=0 one has K_0 = omega^2 I. About nonzero constant W_0 one has K_0 = omega^2 I - W_0 H_0. Same Hessian algebra; different propagator.

Momentum kernel on R^d with A(k,p)=[k^2+(k+p)^2]/2:

    I(p) = int d^d k/(2pi)^d  A(k,p)^2 / [(omega^2+k^2)(omega^2+(k+p)^2)]

Angular-averaged p^2 density:

    I2(k) = k^2 [(d+1) omega^4 + (d-2) omega^2 k^2 + k^4] / [d (omega^2+k^2)^4]

Verified symbolically. For d>=2, I2(k)>0 for k!=0. Therefore unrenormalized Z_loop < 0 for this Euclidean convention and insertion. NOT a ghost theorem.

UV: I2(k) ~ 1/(d k^2); measure gives int dk k^{d-3}. d=2 log, d=3 ~ Lambda, d=4 ~ Lambda^2.

Z_ren OPEN.

## Quarantine

NOT DERIVED: 0.08, 0.23, W(n), S_W, propulsion, unique local theory, Lorentzian healthy mode.

Sierpinski map R(z)=z(5-z) does not imply W(n)=0.08 exp[0.23(n-3)].

## Canonical boundary

Constant-W action principle: DERIVED.
Local K_sym consistency + finite-graph Hermitianity: DERIVED.
Unrenormalized Z_loop<0 for the stated kernel: DERIVED (model-specific).
Renormalized propagating W(x): OPEN.
W=0.08, 0.23, W(n), propulsion: NOT DERIVED.

Next isolated package: regulator -> Gamma^(2)(p) -> counterterms -> Z_ren -> Lorentzian pole.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
