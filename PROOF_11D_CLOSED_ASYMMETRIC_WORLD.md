# Proof 11D/11E — Closed asymmetric world and min-action circulation

**Date:** 2026-09-23. Protocol: ASSUME → FORMALIZE → DERIVE → EXTEND. 5R–11B frozen as the flat/covariant matter sector. No 0.08.

This package **adds a geometric seed**. It does not retract 6D (S_W unconstructed) or 10A (gasket L ≠ Box). Those remain constraints on how the seed may couple.

## 11D.0 — Assumptions (explicit)

| ID | Statement | Class |
|---|---|---|
| G1 | Spatial sections are diffeomorphic to T^3 | ASSUMED |
| G2 | Three independent circumferences L1,L2,L3 > 0 | ASSUMED |
| G3 | A unit timelike u^μ exists and is C^2 | ASSUMED |
| G4 | W is a composite scalar W(A,ω,ℋ,ℙ) at this order | ASSUMED |
| G5 | S_grav is Einstein–Hilbert unless replaced later | ASSUMED (11A) |
| G6 | L in K is the 5R continuum operator, not the gasket | REQUIRED by 10A |

## 11D.1 — Geometry

Take the product background (later to be relaxed)

    ds^2 = -N^2 dt^2 + ∑_{i=1}^3 a_i(t)^2 (dθ^i)^2 ,   θ^i \sim θ^i + 1,

so L_i = a_i (period 1). Anisotropy scalar

    A = [(L1-L2)^2+(L2-L3)^2+(L3-L1)^2] / (L1^2+L2^2+L3^2).

Properties DERIVED from the definition:

- A ≥ 0, A = 0 iff L1=L2=L3.
- A is dimensionless and invariant under simultaneous rescaling L_i → λ L_i.
- A ≤ 2 (attained when one L_i → 0 with the others fixed, formally).

Handedness. Let {e_i} be the oriented co-frame dual to ∂_θ^i. Then

    ℋ = ε_μνρσ u^μ e1^ν e2^ρ e3^σ / vol

reduces to sgn(det e) = ±1 on an orientable T^3. It does not yet distinguish a *time* orientation; it only orients the spatial frame relative to u.

Kinematic vorticity (standard 3+1):

    ω^μ = (1/2) ε^{μνρσ} u_ν ∇_ρ u_σ ,   ω^μ u_μ = 0.

On the diagonal Bianchi-I torus with u = N^{-1}∂_t and vanishing shift, ω^μ = 0. Therefore a nonzero ω requires either a shift / twist identification (e.g. mapping torus), a non-comoving u, or a different topology. That is a REPAIR item, not a kill: the seed must be enlarged beyond orthogonal Bianchi I if “the world spins” is to be geometric rather than kinematic on the matter flow.

Pontryagin density ℙ = *RR is independently defined on any oriented 4-manifold. On the orthogonal torus it vanishes.

## 11D.2 — Composite W

Lowest-order scalar list with [W]=0:

    W = c1 A + c2 ℓ^2 ω_μ ω^μ + c3 ℓ^4 ℙ + c4 A^2 + ···

ℓ is a new length (ASSUMED) unless identified with a derived scale from 5R (ω^{-1} or q_th^{-1/2}). Coefficients c_i are FREE at this order. Odd powers of ℋ are pseudoscalars; they are allowed only if the matter sector admits a parity-odd coupling (not present in locked K_sym). Record: c_odd is either 0 by 5R parity or a new assumption.

This is an equation *schema*, not a determination of W.

## 11D.3 — Feedback identity (DERIVED)

If W=W[g,u] is a local scalar built from (A,ω,ℙ) and Γ=Γ[g,W(g)], then

    δΓ/δg^{μν} = (δΓ/δg^{μν})|_W + (δΓ/δW)(δW/δg^{μν}).

Stationarity of W still uses the locked source (P2),

    δS_W/δW = (1/2) Tr(K^{-1} L),

now evaluated on K(W(A,ω,ℙ),g). The chain-rule term is the geometric backreaction of the composite. That identity is DERIVED. A solution (g_*,u_*,W_*) is NOT yet constructed.

## 11E — Min-action closed circulation

On the flat metric torus (N=1, a_i constant), closed geodesics are winding classes n ∈ Z^3 \ {0}:

    γ_n(λ) = (λ n1, λ n2, λ n3),   period T_n = |n|_L := √(∑ n_i^2 L_i^2).

The action of a free particle / length functional is T_n itself.

DERIVED:

- The shortest closed geodesic has length L_* = min{ L1, L2, L3 } (classes ±e_i).
- Orientation on that cycle is the sign of n_i on the shortest axis; it does not select a time arrow.
- Angular momentum of the geodesic (as a 1-cycle) is Poincaré dual to that axis.
- If two L_i coincide and are strictly smaller than the third, the minimizer is degenerate (an S^1 family).

EXTEND (not yet derived): promote a_i(t) and allow a constant twist so that ω ≠ 0; then the minimizer among closed timelike/null congruences is a different variational problem (Gödel-like / tilted Bianchi). Do not claim entropy production from T_n alone.

Entropy target ω^μ ≠ 0 ⇒ ∇_μ s^μ ≥ 0 remains a HYPOTHESIS. It needs a defined s^μ (e.g. from the 1-loop density of states of K after coarse-graining). Not derived in this package.

## Self-consistent triple

Seek (g_*,u_*,W_*) such that

    δΓ/δg = 0,   δΓ/δW = 0,   δ S_closed[γ] = 0

with W=W[A(g),ω(u),ℙ(g)]. Status: POSED. On the orthogonal torus, ω=ℙ=0 reduces W	o c1 A + c4 A^2. Then  δΓ/δW=0 is the old spectral source at that A, and δΓ/δg=0 is Bianchi I Einstein plus the 11A T_μν and the chain-rule term ∝ ∂W/∂A · ∂A/∂g. That reduced system is the first solvable slice (11F).

## Repair list (feed the next derivation)

1. Orthogonal Bianchi I has ω=0. Add twist or tilted u if circulation is required.
2. ℓ and {c_i} are free unless fixed by a symmetry or by matching to 5R scales (ω, 4ω^2).
3. s^μ is undefined until a coarse-grained current is constructed from K.
4. Do not replace Box by L_gasket.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
