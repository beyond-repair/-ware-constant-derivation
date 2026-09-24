#!/usr/bin/env python3
"""Dimensional-regularization Laurent series of integrated I2 at d=4-2ε."""
from __future__ import annotations
import sympy as sp

def integrated_I2():
    eps = sp.symbols("epsilon", positive=True)
    omega = sp.symbols("omega", positive=True)
    d = 4 - 2 * eps
    pref_ang = 2 ** (1 - d) * sp.pi ** (-d / 2) / sp.gamma(d / 2)
    pref = pref_ang * omega ** (d - 2) / (2 * d)

    def B_gamma(mu):
        return sp.gamma(mu) * sp.gamma(4 - mu) / sp.gamma(4)

    J = (d + 1) * B_gamma(d / 2 + 1) + (d - 2) * B_gamma(d / 2 + 2) + B_gamma(d / 2 + 3)
    return sp.simplify((pref * J).rewrite(sp.gamma)), eps, omega

def main() -> None:
    expr, eps, omega = integrated_I2()
    series = expr.series(eps, 0, 1)
    pole = series.coeff(1 / eps)
    expected_pole = -(omega**2) / (32 * sp.pi**2)
    assert sp.simplify(pole - expected_pole) == 0, pole
    finite_expected = (
        omega**2
        / (32 * sp.pi**2)
        * (sp.EulerGamma - sp.log(4 * sp.pi) - sp.Rational(4, 3) + sp.log(omega**2))
    )
    finite = (series - pole / eps).removeO()
    assert sp.simplify(finite - finite_expected) == 0, finite
    print("PASS")
    print("  I2_DR pole = -ω^2/(32 π^2 ε)")
    print("  finite = ω^2/(32 π^2) [γE - log(4π) - 4/3 + log(ω^2)]")
    print("  Z_loop_DR pole = +ω^2/(64 π^2 ε)  under Z = -I2/2")

if __name__ == "__main__":
    main()
