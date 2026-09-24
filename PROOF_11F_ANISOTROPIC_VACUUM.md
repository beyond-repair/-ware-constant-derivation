# Proof 11F — Self-consistent anisotropic vacuum (orthogonal slice)

**Date:** 2026-09-23. Protocol ASSUME→FORMALIZE→DERIVE. No 0.08 input. No G_eff=G(1+W).

## Metric and kinematics

    ds^2 = -dt^2 + a1(t)^2 dx^2 + a2(t)^2 dy^2 + a3(t)^2 dz^2,
    x^i \sim x^i + 1,    L_i(t) = L_{i0} a_i(t),    H_i = ā_i/a_i,    θ = ∑ H_i.

    A = [(L1-L2)^2+(L2-L3)^2+(L3-L1)^2] / ∑ L_k^2 = A[a].

Orthogonal slice: ω^μ = 0, *RR = 0. Hence

    W = c1 A + c4 A^2 + ··· ,    W_,A = c1 + 2 c4 A + ···

with {c_i} FREE.

Einstein tensor (vacuum Bianchi I, lapse 1):

    G_00 = H1 H2 + H2 H3 + H3 H1,
    G^i_i (no sum) = -(H_j + H_k)dot - H_j^2 - H_k^2 - H_j H_k   (i,j,k cyclic).

## Two variational regimes (do not fuse)

**B1 — Independent W.** Γ=Γ[g,W], δΓ/δW=0 is a separate equation (locked source = ½ Tr(K^{-1}L) + δS_W/δW). Then

    δΓ/δg^{μν} = (δΓ/δg^{μν})|_W + (δΓ/δW)(δW/δg^{μν})

and the second term VANISHES ON SHELL. Do not count it as an extra force.

**B2 — Composite only.** W:=W(A[g]) is not varied independently. There is no δΓ/δW=0. The chain-rule term IS the coupling of A to gravity and must be kept.

11F proceeds with B1 as the dynamical-W slice the user specified, and records B2 as the alternative if S_W stays missing (6D).

## Where the vacuum enters (B1, on-shell)

    G_μν + Λ g_μν = 8π G ( T_μν^{matter} + T_μν^{vac}[W,g] + T_μν^{W} )

    T_μν^{vac} = - (2/√-g) δ/δg^{μν} (½ Tr ln K) |_W .

T^W is the explicit S_W variation (still unconstructed). Higher-curvature from a2 stay as in 11B.

## Mode sum on T^3 (DERIVED structure)

Constant-W, continuum 5R reduction on the torus:

    λ_n = ∑_{i=1}^3 (2π n_i / L_i)^2 ,   n∈Z^3,
    K_n = ω^2 - W λ_n     (positivity: W λ_n < ω^2 for all retained modes).

Regulated one-loop:

    Γ_1-loop = (1/2) ∑_n μ^{2ε} ln(K_n/μ^2)   + counterterms from 6A/11B.

Dependence on L_i is only through λ_n. Define the Casimir derivatives at fixed W:

    V ρ_vac = (1/2) ∑_n' ln K_n ,
    V p_i^{vac} = - (L_i / V) ∂Γ_1-loop/∂L_i |_W
               = - (1/2V) ∑_n [ (-W) ∂λ_n/∂L_i ] / K_n
               = (W / V) ∑_n [ (2π n_i)^2 / L_i^3 ] / K_n .

Hence, at fixed W, if L_i ≠ L_j then the sums over n_i^2/L_i^3 generally give

    p_i^{vac} ≠ p_j^{vac} .

This is the anisotropic Casimir identity of the locked operator on T^3. It does not use the chain rule. It does not use 0.08. Sign of (p_i-p_j) tracks which L_i is smaller once the regulator is fixed; that sign is 11G work, not an input.

Isotropic point L1=L2=L3 ⇒ A=0 ⇒ p1=p2=p3 by symmetry.

## Einstein slice

    H1 H2 + H2 H3 + H3 H1 = 8π G ρ_eff ,
    (H_j + H_k)dot + H_j^2 + H_k^2 + H_j H_k = -8π G p_i^{eff} .

Shear evolution is sourced by p_i^{eff}-p_j^{eff}. If vacuum dominates that difference, the vacuum drives anisotropy. Whether it damps toward A=0 or runs away is a dynamical question for the regulated sums + S_W, not settled here.

## Spectral information (definition, not a measure yet)

    I[K] = Tr f(K/μ^2),
    ∂I/∂W = - μ^{-2} Tr[ f'(K/μ^2) L ] .

Stationarity of Γ is NOT the same as stationarity of I unless f= (1/2) ln and S_W is included. f remains OPEN. Do not set I/I_ref = 0.08.

Two distinct later tests:

    (H-info)   W_*  =?  ΔI / I_ref
    (H-G)      W_*  =?  ΔG / G

They are not identified. 8B already forbids inventing the ratio after seeing 0.08. 0.08 may be compared only after W_* is produced by the fixed-point system.

## Current (posed for 11G)

Closed T^3 ⇒ no spatial boundary flux.
If a current J_I^μ[K] exists with ∇_μ J_I^μ = σ_I, then

    d/dt ∫_{T^3} √γ J_I^0 = ∫_{T^3} √γ σ_I .

Sign of σ_I is not assumed. Construct J from the same K that yields T^{vac}.

## Status

| Item | Status |
|---|---|
| On-shell drop of chain rule in B1 | DERIVED |
| Keep chain rule in B2 | DERIVED |
| p_i^{vac}≠p_j^{vac} when L_i≠L_j at fixed W | DERIVED (structure) |
| Sign of p_i-p_j, backreaction on A(t) | OPEN (11G) |
| f, J_I, σ_I | OPEN |
| W_* numerical | NOT DERIVED |

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
