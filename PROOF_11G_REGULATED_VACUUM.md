# Proof 11G — Regulated spectral vacuum response

**Date:** 2026-09-23. 11F frozen. No 0.08. No invented entropy current. Frequency dummy ≠ freeze mass: freeze mass is m (was ω in 5R).

## Determinant and positivity

On T^3, λ_n = ∑_i k_i^2, k_i = 2π n_i / L_i. Flat slice:

    Ω_n^2 = m^2 - W λ_n .

Euclidean frequency integral (dummy ν):

    Γ_1 = (1/2) ∑_n ∫ dν/(2π) ln(ν^2 + Ω_n^2)  + counterterms.

For Ω_n > 0 this equals (1/2) ∑_n Ω_n plus local UV pieces. Hence the extensive zero-point energy before subtraction is

    E_tot = (1/2) ∑_n Ω_n ,    ρ_vac = E_tot / V .

**Condition:** Ω_n^2 > 0 on every retained mode. Literal K = ν^2 - W L eventually fails for large λ unless a UV cutoff / continuation is specified (P9). 11G keeps a cutoff Λ_UV or a heat-kernel regulator; it does not change the frozen operator.

## Pressure from Γ_1

Static torus, V = L1 L2 L3:

    p_i^{vac} = - (1/V) ∂Γ_1 / ∂ ln L_i  |_W,m .

    ∂λ_n / ∂ ln L_i = -2 k_i^2 ,
    ∂Ω_n / ∂ ln L_i = (W k_i^2) / Ω_n .

With Γ_1 = (1/2) ∑ Ω_n + Γ_local,

    p_i^{vac} = - (W /(2V)) ∑_n k_i^2 / Ω_n   + p_i^{local} .

Directional structure (regulator-common):

    p_i^{vac} - p_j^{vac} = - (W /(2V)) ∑_n (k_i^2 - k_j^2) / Ω_n .

Overall sign tracks the continuation of K and the sign of W; anisotropy tracks (k_i^2-k_j^2).

L1=L2=L3 ⇒ lattice permutation symmetry ⇒ p1=p2=p3. Decomposition

    T_{ij}^{vac} = p_iso γ_{ij} + Π_{ij}^{vac} ,   γ^{ij} Π_{ij}=0 ,
    Π_i^{vac} = p_i^{vac} - (1/3) ∑_j p_j^{vac} .

Shear (Bianchi I, standard σ_i = H_i - θ/3):

    σ̇_i + 3 H σ_i = 8π G Π_i^{eff} .

Mechanism: anisotropic spectrum → Π^{vac} → shear. Sign of Π_i σ_i after subtraction is 11H, not assumed.

## Casimir subtraction

    Γ_vac = Γ_local + Γ_Casimir ,
    Γ_Casimir = Γ_{T^3} - Γ_{R^3}   (same regulator).

Local poles renormalize Λ, G^{-1}, α_{R^2}, α_{C^2} (11B). Physical anisotropic response:

    Δp_{ij}^{Casimir} = p_{ij}(T^3) - p_{ij}(R^3) .

R^3 is isotropic, so ΔΠ_{ij} = Π_{ij}(T^3) after subtraction. Carry ΔΠ into 11H, not the raw divergent p.

## Information: no unique current from K

I_f = Tr f(K/μ^2) defines a density i_f via the heat kernel, not a unique J_I^μ. Balance ∇_μ J^μ = σ_I is a schema. Sign of σ_I is not fixed by K.

Equilibrium spectral state (K Euclidean-positive after regulator):

    Z(β) = Tr e^{-β K} ,    ρ_β = e^{-β K}/Z ,
    S_spec = ln Z - β ∂_β ln Z .

This uses the same heat kernel as 11B. It is global/equilibrium, not a spacetime current.

Arrow: needs a generator L_K[ρ] with dS/dt = -Tr[ρ̇(ln ρ+1)]. Euclidean Γ_1 does not supply L_K. Reduced to 11H+ dynamics, not assumed ≥0.

## Bridge

    K(W,g) → Γ_1 → T^{vac} → Π_{ij}^{vac}
    K(W,g) → Z(β) → S_spec

W as spectral displacement is a later comparison, not G_eff.

# 11H seed — oscillator thermodynamics of the same spectrum

If each mode is a harmonic oscillator of frequency Ω_n (Lorentzian reading of Ω_n>0),

    Z = ∏_n [ 2 sinh(β Ω_n / 2) ]^{-1} ,
    F = β^{-1} ∑_n ln( 2 sinh(β Ω_n / 2) ) ,
    S = -∂F/∂T ,    p_i = - (1/V) ∂F/∂ ln L_i .

T	o0 recovers E_tot = (1/2)∑ Ω_n and the 11G pressure formula. Finite T is the first extension. Compute ΔS_spec and ΔΠ^{Casimir} as functions of (W,L_i) before any 0.08 comparison.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
