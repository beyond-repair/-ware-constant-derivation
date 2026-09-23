#!/usr/bin/env python3
"""Deterministic verification of the constant-W action identities."""
from __future__ import annotations

import math

import numpy as np


def spectral_source(omega2: float, W: float, evals: np.ndarray) -> float:
    return 0.5 * float(np.sum(evals / (omega2 - W * evals)))


def v_1loop(omega2: float, W: float, evals: np.ndarray) -> float:
    return 0.5 * float(np.sum(np.log(omega2 - W * evals)))


def v2_1loop(omega2: float, W: float, evals: np.ndarray) -> float:
    return -0.5 * float(np.sum(evals**2 / (omega2 - W * evals) ** 2))


def main() -> None:
    rng = np.random.default_rng(0)
    A = rng.normal(size=(12, 8))
    L = A @ A.T
    evals = np.linalg.eigvalsh(L)
    omega2 = 1.0
    lam_max = float(evals.max())
    W_crit = omega2 / lam_max
    W = 0.4 * W_crit

    K = omega2 * np.eye(L.shape[0]) - W * L
    Kinv = np.linalg.inv(K)

    source_tr = 0.5 * float(np.trace(Kinv @ L))
    source_spec = spectral_source(omega2, W, evals)
    assert math.isclose(source_tr, source_spec, rel_tol=1e-12, abs_tol=1e-12)

    h = 1e-6
    dV = (v_1loop(omega2, W + h, evals) - v_1loop(omega2, W - h, evals)) / (2 * h)
    d2V = (
        v_1loop(omega2, W + h, evals)
        - 2 * v_1loop(omega2, W, evals)
        + v_1loop(omega2, W - h, evals)
    ) / h**2
    dV_exact = -source_spec
    d2V_exact = v2_1loop(omega2, W, evals)
    assert math.isclose(dV, dV_exact, rel_tol=1e-6, abs_tol=1e-8)
    assert math.isclose(d2V, d2V_exact, rel_tol=1e-5, abs_tol=1e-6)
    assert d2V_exact < 0

    W_near = W_crit * (1 - 1e-8)
    assert v_1loop(omega2, W_near, evals) < -5.0
    assert (1.0 / 6.0) == omega2 / 6.0

    print("PASS")
    print(f"  λ_max={lam_max:.6f}  W_crit={W_crit:.6f}  W={W:.6f}")
    print(f"  Tr source={source_tr:.12f}")
    print(f"  spec source={source_spec:.12f}")
    print(f"  V''={d2V_exact:.12f}")
    print(f"  V(W_near)={v_1loop(omega2, W_near, evals):.6f}")


if __name__ == "__main__":
    main()
