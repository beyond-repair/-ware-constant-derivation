# Proof 7B — Microscopic completion / emergence of W

**Date:** 2026-09-23. 5R–7A frozen. No 0.08.

Within the locked model W is an external dimensionless coefficient. 7B tests reinterpretation without inventing X to hit a target.

## Vertex

(1/2) phi K(W) phi = (ω²/2)||phi||² - (W/2)(phi, L phi).
W–phi vertex is linear in W, bilinear in phi. No latent X in the three-repo corpus.

## Composite

Rayleigh (φ,Lφ)/(φ,φ) is a functional of φ, not an independent W with kernel K(W). Composite route not constructed.

## Hubbard–Stratonovich (vertex-motivated)

UV candidate, not the freeze:

    S[phi] = (ω²/2)||phi||² + (g/2)(phi, L phi)²   (g>0)

HS rewrite reproduces K(W)=ω² I - W L and

    S_W^HS = W²/(2g)    (constant mode; tree Z_W=0)

g is FREE. W0 is an output given (g,ω,spectrum):

    W0/g = (1/2) Σ_k λ_k / (ω² - W0 λ_k)

One-mode: W++W- = W_crit; V''(on-shell)=(g-2W²)/g²; disc=ω^4-2g λ².
Check: verify_proof_7B_hs.py PASS.

(φ,Lφ)² in d=4 has dimension 6 (irrelevant). Continuum RG drives g→0; on a graph g stays a free number.

Branch: completion with a free parameter. 6D stays closed as a unique prediction.

## RG

Blocking Gaussian φ at fixed W does not generate S_W. Wetterich flow of v_k(W) needs a UV function v_Λ. No RG-fixed W0 without that data.

## No-go

Inside the freeze: integrating φ cannot generate S_W. The freeze cannot complete itself.
Not claimed: no completion in any larger theory can stabilize W.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
