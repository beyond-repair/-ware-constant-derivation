#!/usr/bin/env python3
"""Checks for Proof 5R form identity (1D grid) and Proof 7 I2 integrand sign."""
from __future__ import annotations
import math
import numpy as np

def grid_laplacian_neumann(n, dx):
    L = np.zeros((n, n))
    for i in range(n):
        L[i, i] = 2.0
        if i > 0:
            L[i, i - 1] = -1.0
        else:
            L[i, i] -= 1.0
        if i < n - 1:
            L[i, i + 1] = -1.0
        else:
            L[i, i] -= 1.0
    return L / dx**2

def i2_density(k, omega, d):
    num = k**2 * ((d + 1) * omega**4 + (d - 2) * omega**2 * k**2 + k**4)
    den = d * (omega**2 + k**2) ** 4
    return num / den

def main() -> dict:
    rng = np.random.default_rng(1)
    n, dx = 64, 1.0
    H0 = grid_laplacian_neumann(n, dx)
    x = np.arange(n) * dx
    W = 0.2 * np.sin(2 * np.pi * x / n)
    Wop = np.diag(W)
    V = 0.5 * (Wop @ H0 + H0 @ Wop)
    f = rng.normal(size=n)
    q_mat = float(f @ V @ f)
    q_grad = 0.0
    for i in range(n - 1):
        q_grad += 0.5 * (W[i] + W[i + 1]) * (f[i] - f[i + 1]) ** 2 / dx**2
    d2W = np.zeros(n)
    d2W[1:-1] = (W[2:] - 2 * W[1:-1] + W[:-2]) / dx**2
    d2W[0] = (W[1] - W[0]) / dx**2
    d2W[-1] = (W[-2] - W[-1]) / dx**2
    # Operator-consistent coefficient 1/2 (corrected 2026-10-28)
    q_form = q_grad - 0.5 * float(np.dot(d2W, f**2))
    rel = abs(q_mat - q_form) / (abs(q_mat) + 1e-12)
    assert rel < 1e-8, rel
    # Deliberate wrong-coefficient check (must fail if reintroduced)
    q_wrong = q_grad - 0.25 * float(np.dot(d2W, f**2))
    rel_wrong = abs(q_mat - q_wrong) / (abs(q_mat) + 1e-12)
    assert rel_wrong > 1e-4, "wrong coefficient unexpectedly passed"
    W0 = 0.07
    V0 = 0.5 * (W0 * H0 + H0 * W0)
    assert np.allclose(V0, W0 * H0)
    omega = 1.0
    for d in (2, 3, 4):
        ks = np.linspace(0.05, 20.0, 200)
        vals = np.array([i2_density(k, omega, d) for k in ks])
        assert np.all(vals > 0), d
    k = 1e6
    for d in (2, 3, 4):
        ratio = i2_density(k, omega, d) * d * k**2
        assert math.isclose(ratio, 1.0, rel_tol=1e-6)
    print("PASS")
    print(f"  form rel. mismatch (1/2)={rel:.2e}")
    print(f"  wrong-coeff residual (1/4)={rel_wrong:.4f} (expected fail)")
    print("  constant-W recovery: exact")
    print("  I2 density > 0 for d=2,3,4")
    print("  I2 ~ 1/(d k^2) at large k")
    return {"rel": rel, "rel_wrong": rel_wrong}

if __name__ == "__main__":
    main()
