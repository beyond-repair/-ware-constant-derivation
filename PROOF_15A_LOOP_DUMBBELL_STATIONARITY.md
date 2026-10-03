# Proof 15A — loop-dumbbell secular stationarity

Date: 2026-10-03
Classification: RESEARCH
Does not modify STATUS_LOCK_2026-10-01.md.
Does not raise the claim level.
experimental_validation = false
thrust_validated = false
energy_extraction_validated = false

## Object

Symmetric Kirchhoff quantum graph G_ell:

- two loops, each of length L > 0, based at vertices v_L and v_R;
- one bridge edge of length ell > 0 joining v_L to v_R;
- standard (Kirchhoff) vertex conditions: continuity of the function, sum of outward derivatives zero.

The Laplacian is -d^2/dx^2 on edges. Positive eigenvalues are written lambda = k^2, k > 0.

This object is defined before any comparison with 0.08.

## Assumption registry

- A4 (model): the graph, the edge lengths, and Kirchhoff conditions. Not a vacuum, thrust, or continuum-domain claim.
- Established: on each edge the positive solutions of -u'' = k^2 u are linear combinations of sin(kx) and cos(kx).
- No assumption that a stationary value equals 0.08, 1/6, or 1/12.

## Secular equation (derived)

Parametrize a loop of length a based at a vertex with value psi.
The unique solution with u(0) = u(a) = psi, away from the Dirichlet poles sin(ka) = 0, has outward-derivative sum

```text
-2 k tan(k a / 2) psi
```

Parametrize the bridge by u(0) = psi_L, u(ell) = psi_R. Kirchhoff at the two vertices is equivalent to the 2x2 condition

```text
alpha_L * psi_L - psi_R = 0
-psi_L + alpha_R * psi_R = 0
```

with

```text
alpha_side(k) = cos(k ell) - 2 sin(k ell) tan(k * side / 2)
```

Nontrivial kernel iff

```text
alpha_L * alpha_R - 1 = 0
```

excluding poles of tan and the zeros of sin(k ell), which are checked as a separate Dirichlet sector and do not contain the ground positive modes used below.

Symmetric case side = L for both loops:

```text
alpha(k, ell) = ±1
```

Branch -1 is antisymmetric (psi_L = -psi_R). Branch +1 is symmetric (psi_L = psi_R).
The constant function is the simple kernel k = 0 and is excluded from lambda_1.

## Theorem (closed form at ell = L/2)

Set L = 1 without loss of generality (the ratio ell/L is scale invariant; eigenvalues scale as L^{-2}).
At ell = 1/2 write theta = k/2. Then

```text
alpha = [1 - 3 sin^2(theta)] / cos(theta)
```

Branch -1, alpha = -1, gives the quadratic

```text
3 cos^2(theta) + cos(theta) - 2 = 0
(3 cos(theta) - 2)(cos(theta) + 1) = 0
```

cos(theta) = -1 is the excluded pole k = 2 pi. The admissible root is

```text
cos(k_1 / 2) = 2/3
k_1 = 2 arccos(2/3)
```

Branch +1, alpha = +1, gives

```text
3 cos^2(theta) - cos(theta) - 2 = 0
(3 cos(theta) + 2)(cos(theta) - 1) = 0
```

cos(theta) = 1 is the excluded kernel k = 0. The admissible root is

```text
cos(k_2 / 2) = -2/3
k_2 = 2 arccos(-2/3) = 2 (pi - arccos(2/3))
```

Therefore the first two positive eigenvalues satisfy

```text
I_* = lambda_2 / lambda_1 = (k_2 / k_1)^2
    = (pi / arccos(2/3) - 1)^2
```

Numerically I_* = 7.481533386207024. This is not a fit. It is the closed form evaluated in float64.

## Theorem (stationarity)

Differentiate the secular function

```text
F(k, ell; b) = cos(k ell) - 2 sin(k ell) tan(k/2) - b,   b in {+1, -1}
```

at ell = 1/2:

```text
F_ell = -3 k sin(k/2)
F_k   = -sin(k/2) [3/2 + sec^2(k/2)]
(1/k) dk/dell = -3 / (3/2 + sec^2(k/2))
```

Both admissible roots have sec^2(k/2) = 9/4. Therefore

```text
(1/k_1) dk_1/dell = (1/k_2) dk_2/dell
```

at ell = 1/2, which is exactly

```text
beta_I = ell * dI/dell = 0,   I = lambda_2 / lambda_1
```

The sign of beta_I changes from positive to negative across ell = L/2, so the stationary point is a local maximum of I.

Scale check: (L, ell) = (2, 1) reproduces the same I_* and halves both wave numbers.

## Comparison step (status-lock order)

The functional was fixed before the comparison.

```text
I_* - 0.08 = 7.401533386207024
```

0.08 is not selected. 1/6 and 1/12 are not selected. I_* - 15/2 = -0.0184666, so 15/2 is not the value either.

## Falsification

1. Pole collision at ell = L. The symmetric-sector root enters a secular pole. A naive ratio near 16.84 at ell = L is a missed root, not an eigenvalue ratio. Rejected.
2. Unequal loops. For loop lengths 1 and 1.5 the gap ratio still has a local maximum, but near ell ≈ 0.75 with I ≈ 6.99, not at ell = 1/2 and not at I_*. The stationary value is not universal in the loop-length ratio.
3. This graph is not a planar dumbbell, not a thrust functional, and not a heat-trace coefficient. It does not reopen the rejected pinch-family claim.

## Classification

- THEOREM: secular reduction, closed form I_* = (pi/arccos(2/3) - 1)^2, and beta_I(L/2) = 0, under A4.
- DERIVED RESULT: I_* ≈ 7.481533386207024; local maximum.
- FAILED: selection of 0.08 by this functional.
- FAILED: universality under unequal loop lengths.
- REJECTED: the ell = L ratio spike as a spectral ratio.
- OPEN: whether any other independently defined I on a continuum domain has a universal beta zero. Not claimed here.

Verifier: verify_proof_15A_secular.py
