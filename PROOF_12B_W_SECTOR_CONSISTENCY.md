# Proof 12B — Missing W-sector from consistency (not invention)

**Date:** 2026-09-23. 12A frozen: \mathfrak{I}=\Delta F_Cas. No 0.08. No \chi_vac. Entanglement postponed.

## 1. Variational constraint (DERIVED)

If W is independently varied,

    S_tot = S_EH[g] + S_m[\varphi,g] + S_W[W,g] + Γ_Cas[W,g] + S_ct .

    \delta S_tot/\delta W = 0  \Rightarrow  \delta S_W/\delta W = - \deltaΓ_Cas/\delta W .

With 11I/12A convention \deltaΓ_Cas/\delta W = -\Delta J_W^{Cas} (after the same subtraction that defines \mathfrak{I}),

    \delta S_W / \delta W = \Delta J_W^{Cas} .

This is a *source constraint* on S_W. It does not pick a Lagrangian.

On a homogeneous static slice the left side is V R_W(W) if S_W=\int d^4x \sqrt g L_W and R_W=\partial L_W/\partial W at constant W. Then R_W = \Delta J_W / V_4-density, i.e. an energy-density-worth of source. Scales must match.

## 2. Dimensions (DERIVED)

[W]=0. In ħ=c=1 a 4d Lagrangian density has dimension 4.

A function of W alone cannot supply dimension 4. Every local potential or kinetic term needs a scale.

Scales already present: m (in K), L_i (geometry), M_Pl from S_EH, and the regulator Λ. Introducing a new μ is a new FREE parameter.

Lowest diffeomorphism-invariant local operators (scalar W):

    L_W = μ^4 V(W) + (1/2) Z(W) μ^2 (\nabla W)^2 + \xi(W) M_Pl^2 R
        + (\lambda/2) (\square W)^2 + \cdots

Classification of coefficients:

| Term | Scale | Coefficient |
|---|---|---|
| μ^4 V(W) | new or m^4 or M_Pl^2 m^2 | V FREE as a function |
| Z(W) μ^2 (\nabla W)^2 | μ or m or M_Pl | Z FREE |
| \xi(W) M_Pl^2 R | M_Pl already in EH | \xi FREE (non-minimal) |
| \lambda (\square W)^2 | none (dim 4) | \lambda FREE |

Using only m from K: replace μ\to m. That is a *choice of identification*, SYMMETRY-ALLOWED, not DERIVED. Using L^{-1} as the scale mixes geometry into S_W and double-counts T^Cas vs T^W.

Shift symmetry W\to W+const is NOT a symmetry of K (K=m^2-W\lambda). So a potential V(W) is allowed. A flat V=const is allowed but then \delta S_W/\delta W=0 at constant W and cannot cancel a nonzero ΔJ_W.

## 3. Homogeneous source test

Constant W, orthogonal T^3, ignore ∇W and σ for this slice:

    \delta S_W/\delta W = \sqrt g \, \mu^4 V'(W) + \xi'(W) M_Pl^2 R + \cdots

Flat torus: R=0, so only V'(W) survives.

    \mu^4 V'(W) = \Delta J_W^{Cas}(W; m, L, Λ) / (spatial volume \times lapse)

Right-hand side is a specific function of W computed in 11I (generally nonzero, 11I-A.8: no root). Left-hand side is whatever V we write.

**Result:** existence of a W_* is equivalent to existence of a function V such that V' hits that source. That always exists as a quadrature

    V(W) = \mu^{-4} \int^W dw \, j_Cas(w) + const

if we *define* V from j_Cas. That is matching, not derivation. It imports the entire Casimir function into S_W and does not predict W.

A polynomial V of fixed degree generally cannot hit ΔJ_W(W) for all L,m. A universal V independent of L cannot satisfy the constraint for every torus (RHS depends on L through χ). Therefore a *local potential alone* cannot be L-independent and still cancel ΔJ_W on every compactification.

**Derived obstruction:** if S_W is a strictly local function of W and g (no explicit L, no nonlocal Casimir kernel), it cannot satisfy \delta S_W/\delta W=ΔJ_W for all geometries. Either S_W is nonlocal, or the equation holds only on a submanifold of {L_i}, or we give up on-shell W for generic tori.

## 4. Stress and conservation

    T^W_\mu\nu = -2/\sqrt-g \, \delta S_W/\delta g^{\mu\nu}
    T^Cas_\mu\nu = -2/\sqrt-g \, \delta\mathfrak{I}/\delta g^{\mu\nu}

If S_EH + S_m + S_W + Γ_Cas is a diffeomorphism scalar, Bianchi + matter + the W equation imply

    \nabla^μ (T^m + T^Cas + T^W)_\mu\nu = 0

on shell. Conservation is NOT an extra coefficient constraint. It is automatic for an invariant action.

It FAILS if the regulator that defines Γ_Cas breaks diffs (mode-label R_Λ(n) on a fixed lattice is not covariant). Then T^Cas is only conserved up to regulator artifacts. That is a real 12D issue: covariantize the cutoff or accept approximate conservation.

## 5. Minimal local basis (allowed list, coefficients FREE)

    S_W[W,g] = \int d^4x √-g [
        m^4 V(W) + (Z(W)/2) m^2 (\nabla W)^2 + \xi(W) M_Pl^2 R + (\lambda/2)(\square W)^2
    ]

with {V, Z, \xi, \lambda} unmarked functions/numbers, all FREE, unless a later proof fixes them.

Identifying μ with m: ASSUMED.
Setting Z=1, ξ=0, λ=0: ASSUMED.
Choosing V so that V' = j_Cas at one L: MATCHED, not derived.

## 6. Verdict

    Spectral theory does not determine the W-dynamics.

No admissible *local L-independent* S_W satisfies the source constraint on all T^3. A local S_W can exist as an EFT with FREE coefficients; it does not output W_*. Nonlocal S_W ≡ -\Gamma_Cas would cancel the loop by definition and leave W undetermined again (double counting).

## 12C seed

Simultaneous variation: Einstein equation with T^Cas + T^W[V,Z,ξ,λ] and the W equation V',Z,\square W vs ΔJ_W. Ask whether any FREE-coefficient choice admits a constant-W solution on some (m,L) without fitting 0.08. That is existence, not uniqueness.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
