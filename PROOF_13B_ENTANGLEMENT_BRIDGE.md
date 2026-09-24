# Proof 13B — Entanglement / spectral response bridge

**Date:** 2026-09-23. Same K, same T^3. Cut A is extra structure. No S→g. No 0.08.

## Setup

Gaussian vacuum of K. Region A ⊂ T^3 with smooth cut ∂A. Covariance C_A = (K^{-1}, conjugate) restricted to A.

    S_ent(A) = ∑_k s(ν_k),   s(ν) = ((ν+1)/2)ln((ν+1)/2) - ((ν-1)/2)ln|(ν-1)/2|

with ν_k the symplectic eigenvalues of C_A (Srednicki / Casini). This is DERIVED given (K,A).

Independently, ℓ_Cas=ΔF_Cas[K] gives (ΔJ_W, Π_i) with no cut.

Dimensions: S_ent is dimensionless. ΔJ_W has dimension energy. A raw proportionality needs an extra scale. That scale is not supplied by W ([W]=0).

## UV structure (structural, not numerical)

For a free scalar in 3 spatial dimensions the replica / heat-kernel expansion on a region with boundary gives

    S_ent(A) = c_2(W,ξ) Area(∂A)/\epsilon^2 + c_0(W,ξ) ln(μ ε) + S_fin(A; W, L_i) + o(1).

The leading term is an area law. c_2 depends on the short-distance metric of the spatial operator in K (the W-weighted Laplacian) and on the cutoff ε that defines the cut.

Therefore

    ∂_W S_ent = (∂_W c_2) Area(∂A)/\epsilon^2 + ∂_W S_fin + cut-scheme terms.

ΔJ_W is a bulk T^3−R^3 difference after the Casimir subtraction of 11G. It has no ∂A and no ε_cut.

**Classification: regulator/cut dependent.** The dominant piece of ∂_W S_ent scales with Area(∂A)/\epsilon^2. ΔJ_W does not. They cannot be proportional as unsubtracted quantities.

Changing the cut (half-torus vs slab vs wiggly surface) changes Area(∂A) at fixed K. ΔJ_W is unchanged. Any map that ignored this would be manufactured by the surface.

## Isotropic half-torus (13B.3)

L_i=L, A = [0,L/2]×T^2. Then Π_i=0 by cubic symmetry. ∂_{x_i} S_ent is not tested. Only the scalar channel remains, and it is dominated by Area=2 L^2 (two T^2 faces) times ∂_W c_2.

The finite remainder S_fin for a massive free field on a torus slab is a function of χ and mL. It is a different spectral sum from ΔF_Cas (replica eigenvalues of C_A, not ∑ Ω_n). Shared origin in K does not give

    ∂_W S_fin = C(L) ΔJ_W

without an extra identity that is not in the Gaussian algebra.

## Tensor channel

L_i = L e^{x_i}, ∑ x_i=0, A held fixed in coordinate charts.

    ∂_{x_i} S_ent = (∂_{x_i} Area(∂A)) c_2/ε^2 + Area ∂_{x_i}(c_2/ε^2) + ∂_{x_i} S_fin.

The first term is the variation of the cut geometry. Π_i is the traceless variation of F_Cas with ∂_{x_i} R_Λ=0 and no cut. Again different tensors unless a Wald-type identification is *postulated* (that is the S→g ansatz, forbidden here).

## Covariance variation (13B.4)

    ∂K/∂W = -H_0    (5R, constant W),
    ∂C/∂W = - K^{-1} (∂K/∂W) K^{-1}   in the bulk resolvent sense,
    plus restriction-to-A errors supported near ∂A.

    ∂_W S_ent = Tr_A[ (δs/δC) ∂_W C_A ].

    ΔJ_W ∝ ∑ λ_n / Ω_n    (global modes).

One is a trace over A of a nonlinear function of C_A. The other is a global spectral moment of Ω_n. No algebraic identity equates them.

## Breakthrough criteria — verdict

| Test | Result |
|---|---|
| Derived common identity | NO |
| Derived proportionality with geometric C | NO (would require subtracting Area/ε^2 and then fitting C) |
| Regulator/cut dependent | YES — leading ∂_W S_ent |
| Different observables of K | YES |
| Singular/undefined | only if ε→0 is taken before subtraction |

S_ent and ℓ_Cas are different observables of the same K. The old g=η+ε∇∇S route is not supported by this comparison.

A finite comparison object that *cancels* area laws is mutual information of two disjoint regions separated by a gap. That is a new cut pair, not A vs A^c on a pure state (I(A:A^c)=2 S_A still divergent). It is 13B.2+ if pursued; it still will not select W.

13B does not produce W=0.08 and does not add a stationarity condition.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
