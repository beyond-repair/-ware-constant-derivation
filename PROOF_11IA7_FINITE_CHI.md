# Proof 11I-A.7 — Finite-χ audit of scripted R

**Date:** 2026-09-23. Literal Ω=m sqrt(1-χ^2 n^2). Modes with χ|n|≥1 excluded (real spectrum). No 0.08 hunt.

## Exact scripted ratio

ω_n=sqrt(1-χ^2 n^2),  Δμ_2(χ)=∑ R n^2/ω - ∫ d^3n R n^2/ω,

N2_ω=∑ R n_1^2/ω,  N4_ω=∑ R (n_1^4-n_1^2 n_2^2)/ω^3.

From K_log and ΔJ at finite χ (mode-label R, ∂_x R=0):

    R(χ,Λ) = [ N2_ω + (χ^2/2) N4_ω ] / Δμ_2(χ) .

Small-χ reduces to N_2/Δm_2 (11I-A.5), already shown non-universal.

## Numerical survey

Admissible χ∈{0.15,0.25,0.40}. Wall n_max=floor(1/χ)- = 6, 3, 2. Families: Gaussian e^{-n^2/Λ^2}, sharp |n|≤Λ.

Gaussian, increasing Λ:

    χ=0.15:  R = -25.3, -1.00, -0.592, -0.539, -0.524, -0.517   (Λ=2..20)
    χ=0.25:  R = -0.339, -0.158, -0.115, -0.105, -0.101, -0.099
    χ=0.40:  R = -0.793, -0.721, -0.690, -0.680, -0.677, -0.675

Sharp: once Λ ≥ 1/χ every retained mode is on; R freezes

    χ=0.15:  -0.513   (Λ≥8)
    χ=0.25:  -0.098    (Λ≥5)
    χ=0.40:  -0.674    (Λ≥3)

Large-Λ Gaussian vs frozen sharp agree at the 1% level (continuum quadrature near ω=0 is the residual).

## Classification

1. **Convergence in Λ at fixed χ:** YES, provided Λ ≳ 1/χ. The spectral wall is the effective cutoff. Soft vs sharp become equivalent once all real-Ω modes are kept.

2. **Single universal number:** NO. R=R(χ). Three sample values ≈ -0.52, -0.10, -0.67.

3. **Ill-defined before invariant:** the small-χ (W→0, wall→∞) limit is the ill-defined C_0 of 11I-A.6. Finite χ is better-posed because the wall truncates the UV.

## What this means

The scalar and tensor channels still share F_Cas. At finite χ their scripted ratio appears to have a regulator-stable *function* R(χ), not a constant. Nothing in the sample selects 0.08 or 1/(4π).

Caveats: (i) continuum ∫ n^4/ω has an integrable square-root endpoint; quadrature error is visible at the 10^{-3} level; (ii) analytic continuation of Ω^2<0 modes is not included; (iii) R(χ) is a property of this torus+operator+subtraction, not a phenomenological W.

Missing ingredient for a Coherence Drive is unchanged: an independent S_W / restoring response, or a principle that *selects* χ. Finite-χ R does not select χ.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
