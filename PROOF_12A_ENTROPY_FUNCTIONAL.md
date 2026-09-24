# Proof 12A — Entropy functionals determined by K

**Date:** 2026-09-23. 5R–11I-A.8 frozen. No 0.08. No imposed J^\mu. No identification with G_eff.

## What K already is

A real Gaussian theory with positive (regulated) operator K[W,g] has a unique vacuum |0_K> and a unique thermal family

    \rho_\beta = e^{-\beta K} / Z(\beta),   Z = Tr e^{-\beta K}.

Every entropy we are allowed to write without extra axioms is a functional of (K, \beta, a region A, a reference K_0).

## Theorem 12A.1 — Global vacuum is pure

On a closed spatial slice (T^3) at T=0 the Gaussian vacuum is a single vector |0_K>.

    S_vN(|0_K><0_K|) = 0.

**Derived.** There is no global von Neumann “information loss” in the T=0 vacuum of this theory. Coherence-as-global-entropy of the whole torus is identically zero. Any nonzero information measure must be thermal, relative, or regional.

## Theorem 12A.2 — Thermal spectral entropy (already 11H)

    F = \beta^{-1} \sum_n ln(2 sinh(\beta \Omega_n / 2))
    S_spec = \sum_n [ \beta\Omega_n/(e^{\beta\Omega_n}-1) - ln(1-e^{-\beta\Omega_n}) ]
    S_spec(T\to0) = 0 on the retained real spectrum.

This is occupancy entropy of the same modes that produce F_Cas. It is **not** an H-theorem and does not define J^\mu.

## Theorem 12A.3 — Relative spectral entropy is the canonical comparison

Let K and K_0 be two admissible operators (e.g. W and W=0, or T^3 and R^3) on the same regulated mode space.

Gaussian relative entropy of thermal states (Araki / Umegaki, free fields) reduces to

    S(\rho_\beta[K] || \rho_\beta[K_0])
    = \beta (F[K]-F[K_0]) - \beta Tr( \rho_\beta[K] (K-K_0) ) wait

Exact free-boson form from the partition functions:

    S_rel(\beta; K, K_0)
    = \beta ( F[K] - F[K_0] ) + \beta ( U[K_0] - U_cross )

where the energy difference is the expectation of K_0 in the K-state minus U[K_0].

At T=0, for two Gaussians with frequencies \Omega and \Omega_0 on a common basis (constant-W, same L_i),

    S_rel(0; K, K_0) = 0

because both vacua are pure and the relative entropy of two pure states is 0 if they are the same ray and +\infty if they are distinct and we refuse to regularize the overlap. After UV subtraction of the common local divergence, the **finite** T=0 comparison is not S_vN but the Casimir free-energy difference already locked:

    I_Cas[K, K_ref] := \Delta F_Cas[K] = F[K]_{T^3} - F[K]_{R^3}
                      (or F[W] - F[W=0] at fixed geometry).

**Classification:** I_Cas is DERIVED as the unique finite T=0 scalar comparison available from the determinant. It is a relative free-energy, not a von Neumann entropy of the global state.

## Theorem 12A.4 — One functional already generates both channels

    I_Cas[W, g] = \Delta F_Cas
    \delta I_Cas / \delta W = - \Delta J_W^{Cas}
    (1/\sqrt g) \delta I_Cas / \delta g^{\mu\nu}  \to  T_\mu\nu^{Cas} / \Pi_{ij}^{Cas}

This is the missing “single functional” for the *spectral* program. No extra f is required if we accept free energy as the generator. Arbitrary Tr f(K/\mu^{2}) is UNDERDETERMINED (f FREE) unless f = (1/2) ln, which is Γ_1.

## Theorem 12A.5 — Regional entanglement from the covariance

If a region A ⊂ T^3 is specified, the reduced Gaussian state is fixed by the covariance

    C = K^{-1}|_A   (spatial two-point of the field and conjugate momentum).

    S_ent(A; K) = (1/2) Tr [ (C_A^{1/2} + 1) ln(C_A^{1/2}+1) - (C_A^{1/2}-1) ln |C_A^{1/2}-1| ]

(standard real-scalar formula; Peskin/Srednicki/Casini). This **is** derived once A is given. It is UV-divergent on the boundary \partial A; the finite piece after area-law subtraction is the mutual information / renormalized entanglement.

Variations:

    \delta S_ent / \delta W |_{A} \neq \delta I_Cas / \delta W
    \delta S_ent / \delta g^{\mu\nu} |_{A}  is a wall-supported Wald-like term plus bulk

**Not derived:** S_ent \to Einstein-Hilbert. The entanglement repo jump

    g_\mu\nu = \eta_\mu\nu + \epsilon \nabla_\mu \nabla_\nu S

is an ANSATZ. It does not follow from S_ent(A; K) without choosing A, a cutoff, and a map S \mapsto metric that is not supplied by K.

## Theorem 12A.6 — No unique current from K

A number S_spec or I_Cas does not determine J^\mu with \nabla_\mu J^\mu = \sigma \ge 0. Construction of J requires a local density and a coarse-graining generator L_K (11G). Still OPEN.

## What is NOT an entropy functional of this theory

- W itself
- 0.08 or ΔI/I_ref fitted to 0.08
- \chi_vac, ζ, S(ρ,L)=tanh(ρ/\rho_th)
- IFP T_info = W(\rho_coh g - \nabla\nabla\rho_coh) with W\simeq0.08 from an “entropy cubic”
- Origin Point \lambda(\rho,n)

Those remain quarantined.

## Ledger

| Functional | Status |
|---|---|
| \Gamma_1 = (1/2) Tr ln K | DERIVED; generates ΔJ and T^{Cas} |
| I_Cas = \Delta F_Cas | DERIVED; unique finite T=0 comparison |
| S_spec(\beta) | DERIVED; thermal; \to0 at T=0 |
| S_vN(global, T=0) | DERIVED; = 0 |
| S_rel regularized T=0 | = I_Cas after subtraction |
| S_ent(A) | DERIVED given A; UV on \partial A |
| S_ent \to g_\mu\nu | NOT DERIVED |
| J_I^\mu, σ_I \ge 0 | NOT DERIVED |
| f in Tr f(K) | FREE unless f=(1/2)ln |
| Selects \chi or W | NO (11I-A.8) |

## Canonical choice if we refuse extra axioms

    \mathfrak{I}[W,g] := \Delta F_{Cas}[K(W,g)]

Projections: \delta\mathfrak{I}/\delta W, \delta\mathfrak{I}/\delta g^{\mu\nu}, S_spec from the same Z(\beta). That is the entropy/information sector of the *existing* Gaussian theory. It does not replace S_W and does not output 0.08.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
