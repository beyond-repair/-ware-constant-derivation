# Proof 14E — Finite-χ subtracted ∂²ΔF/∂W²

**Date:** 2026-09-23. Same wall and T^3-R^3 as 11I-A.7. Homogeneous W only.

## Identities

ω=sqrt(1-χ^2 n^2), ΔF/m = (1/2)[∑ω-∫ω],
Δμ_2=∑ n²/ω-∫ n²/ω,  Δμ_4=∑ n^4/ω^3-∫ n^4/ω^3.

    d(ΔF/m)/dχ = -(χ/2) Δμ_2
    d²(ΔF/m)/dχ² = - (1/2) Δμ_2 - (χ²/2) Δμ_4 .

Raw lattice ∑ n^4/ω^3 is finite (ε_min = 1-χ^2 n_max^2 > 0). Continuum ∫ dn/ω^3 ∼ ∫ ε^{-3/2} dε diverges at the wall. Subtracted Δμ_4 is therefore dominated by how close the continuum cutoff sits to n=1/χ, not by the torus winding.

## Scan (sharp wall; continuum endpoint 1-10^{-8})

    χ=0.15  Δμ_2~-1.6e5   Δμ_4~-3.3e14   d²(ΔF/m)/dχ² ~ +3.7e12
    χ=0.25  Δμ_2~-1.4e4   Δμ_4~-9.1e12   d² ~ +2.8e11
    χ=0.40  Δμ_2~-6.9e2   Δμ_4~-3.4e11   d² ~ +2.7e10
    χ=0.80  Δμ_2~-4.6e1   Δμ_4~-2.6e9    d² ~ +8.5e8

Lattice S_4 ≪ continuum I_4. Subtracted second derivative is large and **positive**, opposite to the raw concave ∑ (-Ω^{-3}).

## Classification

| Test | Result |
|---|---|
| Raw ∂²F/∂W² < 0 | YES |
| Wall Ω^{-3} on retained modes | YES |
| Subtracted Π finite and Λ-stable | NO — continuum ω^{-3} endpoint dominates |
| Collective zero of D_W^{-1} | NOT ESTABLISHED |
| Stable ω^2>0 pole | NOT ESTABLISHED |
| Soft mode at the wall | NOT distinguished from operator breakdown |

The four-clue hope that Π_W supplies derived Z_eff, M_eff does **not** survive this subtraction. What is large is the mismatch between a discrete wall and a continuum integral that is allowed closer to Ω=0.

Interpretation: the Ω^{-3} spike is breakdown of K=m^2-Wλ (or of the T^3-R^3 difference for this kernel), not a demonstrated collective W pole.

Z,V remain FREE. No 0.08.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
