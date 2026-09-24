#!/usr/bin/env python3
"""Verify A0, A1, A2 poles of I_d(p) and A1 vs Proof 6A."""
from __future__ import annotations
import sympy as sp

def coefficients():
    eps, x, p2, w2 = sp.symbols("epsilon x p2 omega2", positive=True)
    c = x**2 + (1 - x) ** 2
    a = 1 - 2 * x
    d = 4 - 2 * eps
    C = (4 * sp.pi) ** (-d / 2)
    Delta = w2 + x * (1 - x) * p2
    I1 = C * sp.gamma(eps - 1) * Delta ** (1 - eps)
    I2 = C * sp.gamma(eps) * Delta ** (-eps)
    coeff = c + a**2 / d
    piece = (
        -2 * Delta * I1 + Delta**2 * I2
        + coeff * p2 * I1 - coeff * p2 * Delta * I2
        + (c**2 / 4) * p2**2 * I2
    )
    s = piece.series(p2, 0, 3).removeO()
    out = {}
    for n, name in enumerate(("A0", "A1", "A2")):
        expr = s.coeff(p2, n)
        ser = sp.expand(expr).series(eps, 0, 1)
        pole = ser.coeff(1 / eps)
        fin = ser.removeO() - pole / eps
        out[name] = (
            sp.simplify(sp.integrate(pole, (x, 0, 1))),
            sp.simplify(sp.integrate(fin, (x, 0, 1))),
        )
    return out, w2

def main() -> None:
    coeffs, w2 = coefficients()
    A0p, A0f = coeffs["A0"]
    A1p, A1f = coeffs["A1"]
    A2p, A2f = coeffs["A2"]
    assert sp.simplify(A0p - 3 * w2**2 / (16 * sp.pi**2)) == 0
    assert sp.simplify(A1p + w2 / (32 * sp.pi**2)) == 0
    assert sp.simplify(A2p) == 0
    assert sp.simplify(A2f - 1 / (960 * sp.pi**2)) == 0
    expected_A1f = w2 / (32 * sp.pi**2) * (
        sp.EulerGamma - sp.log(4 * sp.pi) - sp.Rational(4, 3) + sp.log(w2)
    )
    assert sp.simplify(A1f - expected_A1f) == 0
    print("PASS")
    print("  A0 pole = 3 ω^4 / (16 π^2 ε)")
    print("  A1 pole = -ω^2 / (32 π^2 ε)  [matches 6A]")
    print("  A2 pole = 0 after x-integration")
    print("  A2 finite = 1/(960 π^2)")
    print("  A1 finite matches 6A I2 finite piece")

if __name__ == "__main__":
    main()
