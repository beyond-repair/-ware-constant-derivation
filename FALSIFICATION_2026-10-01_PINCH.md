# Falsification — pinch family heat trace, 2026-10-01

**Status:** NOT DERIVED.  
**Lock:** STATUS_LOCK_2026-10-01.md  
**Rule:** 0.08 is forbidden upstream of the final comparison.  
**Classification:** RESEARCH.  
**experimental_validation:** false

## Locked conclusion

0.08 is falsified as a universal consequence of the tested (X, L, R) sequences.

This does not say Q ≠ 0.08 in every construction. It says the proposed universality does not survive the admissible families already tested.

Status: 0.08 is a phenomenological candidate, not a derived invariant.

## Sequence under test

```text
pinch family -> L_ell -> K(t,ell) -> {a_k} -> delta K -> I(ell) -> beta_derived -> RG fixed points -> Q
```

Low-pass / high-reflect is not assumed. lambda_min -> 0 is not taken as proof of a topological mouth.

## Cubic route is circular

With delta = 2/25,

```text
beta = delta^3 - delta^2 = -92/15625 = -0.005888
```

exactly. The polynomial delta^3 - delta^2 - beta = 0 then has roots 0.08, approximately 0.9940412, and approximately -0.0740412. The root 0.08 is recovered because it was used to build beta. The cubic route is closed unless beta is derived independently.

Reproduction: `python3 verify_pinch_cubic.py`.

## Operator families (0.08 not an input)

Assumptions are A4 model assumptions: stated lattice or graph Laplacian, stated boundary conditions, stated chamber sizes.

### Neumann grid dumbbell

Chamber 8, neck length 5. First positive eigenvalue falls as the neck narrows. Collapse is real. A fixed point is not.

| w | lambda_1 | lambda_1/lambda_2 | w^2 lambda_1 |
|---|----------|-------------------|--------------|
| 1 | 0.004212 | 0.03298 | 0.00421 |
| 2 | 0.007614 | 0.06648 | 0.03046 |
| 3 | 0.010595 | 0.10037 | 0.09536 |
| 4 | 0.013457 | 0.13311 | 0.21532 |
| 6 | 0.018491 | 0.19599 | 0.66566 |
| 8 | 0.022338 | 0.25140 | 1.42965 |

The gap ratio is monotone on this family and meets 0.08 between w=2 and w=3 (about 2.4 by linear interpolation). That is a level set:

```text
R(w_*) = 0.08
R'(w_*) ≠ 0
```

It is not a fixed point. A fixed point would require dR/d ln w = 0. That failed. Change chamber size or neck length and the crossing moves.

### Dirichlet grid dumbbell

Chamber 10, neck length 6. partial_{ln w} ln(w^2 lambda_1) stays in (1.25, 1.98). No sign change. Heat-trace variation (1/K) Delta K / Delta ln w at t=0.5 stays positive (about 0.045 to 0.23).

### Metric-graph bridge

Two loops of length 1 joined by a bridge of length ell. g = ell^2 lambda_1 is strictly increasing. Discrete beta in (0.63, 1.76). No zero. Gap-ratio minimum near ell=0.5 is about 0.134, and moves if the loop length changes.

### Exact controls

- Conductance pinch, spectrum {0, 2 eps}. partial_{ln eps} ln lambda_1 = 1 at every eps.
- Dirichlet interval of length L. Engineering fixed point L^2 lambda_1 = pi^2. Gap ratio 1/4. Heat trace K ~ L/(2 sqrt(pi t)) - 1/2. The constant term is a boundary Seeley coefficient, not a free RG root.

## Outcomes

1. Universal root near 0.08: falsified on these families.
2. Geometry-dependent level crossing: yes. Not a stationary point.
3. No nonzero anomalous fixed point of the scale beta: result for every beta computed from L_ell.

Boundary conditions matter. A topological mouth that universally generates a particular counter-pressure is unsupported.

Neumann near-zero splitting with bulk scale O(1) is a spectral phenomenon. It is not an informational 8% law.

1/6 and 1/12 remain comparison values only. Proximity to 0.08 is not candidacy.

## Missing object

No scale functional has yet been defined as I[L_ell] = F(a0, a_{1/2}, a1, ...) before any numerical target. Until that exists, another numerical hunt is circular.

Required order: derive I, derive beta_I, find a stationary point, test neck length / chamber size / boundary condition / mesh / pinch family, only then compare the value at ell_* with 0.08.

## What remains locked

Constant-W action principle, finite-graph Hermitianity, and the model-specific unrenormalized I2 sign stay as in the ledger. This note does not reopen those. It does not promote 0.08, 0.23, W(n), or propulsion.

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
