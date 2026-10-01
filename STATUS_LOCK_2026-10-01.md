# Status lock — 2026-10-01

**Classification:** RESEARCH  
**experimental_validation:** false

## Locked statement

0.08 is falsified as a universal consequence of the tested (X, L, R) sequences.

That does not establish Q ≠ 0.08 for every conceivable construction. It establishes that the proposed universality does not survive the admissible families already tested.

Honest status: 0.08 is a phenomenological candidate, not a derived invariant.

## What the cubic is

```text
delta = 2/25
beta  = delta^3 - delta^2 = -92/15625 = -0.005888
```

The cubic route is closed unless an independent derivation of beta is produced. Recovering 0.08 from this beta is circular.

## Level set is not a fixed point

On the Neumann dumbbell the gap ratio is monotone on the tested widths and passes through 0.08 near w ≈ 2.4. That is

```text
R(w_*) = 0.08
R'(w_*) ≠ 0
```

A fixed point would require R'(w_*) = 0, equivalently beta_R(w_*) = dR/d ln w = 0. That condition failed. Writing R'(w_*) = 0 for this crossing is incorrect.

Dirichlet dumbbell, metric-graph bridge, conductance pinch, and Dirichlet interval do not share a nonzero scale-beta zero. Boundary conditions change the ratios. A claim that a topological mouth universally generates a particular counter-pressure is unsupported.

Neumann near-zero mode splitting with bulk scale O(1) is a spectral fact. It is not an informational 8% law.

## Ordering still required

Forbidden:

```text
choose functional -> observe 0.08 -> declare invariant
```

Required:

```text
derive I[L_ell] = F(a0, a_{1/2}, a1, ...)
derive beta_I = dI / d ln ell
find ell_* with beta_I(ell_*) = 0
test neck length, chamber size, boundary condition, mesh -> 0, pinch family
only then compare the dimensionless value at ell_* with 0.08
```

1/6 and 1/12 stay comparison values. Proximity to 0.08 is not a reason to adopt them.

Spectral route remains open only as: does some independently defined I have a universal fixed point? No such I is defined yet.

```text
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
