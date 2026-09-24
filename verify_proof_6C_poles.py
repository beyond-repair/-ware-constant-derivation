#!/usr/bin/env python3
"""Algebraic checks for Proof 6C pole/residue/threshold identities."""
from __future__ import annotations
import sympy as sp

def main() -> None:
    m2, Z, lam, q = sp.symbols("m_R2 Z_R lambda_R q")
    qA = sp.solve(m2 - Z * q, q)[0]
    assert sp.simplify(qA - m2 / Z) == 0
    assert sp.simplify(sp.diff(m2 - Z * q, q) + Z) == 0
    Gamma = lam * q**2 - Z * q + m2
    roots = sp.solve(Gamma, q)
    Disc = Z**2 - 4 * lam * m2
    dG = sp.diff(Gamma, q)
    for r in roots:
        assert sp.simplify(dG.subs(q, r) ** 2 - Disc) == 0
    prod = sp.simplify(dG.subs(q, roots[0]) * dG.subs(q, roots[1]))
    assert sp.simplify(prod + Disc) == 0
    x = sp.symbols("x")
    assert sp.diff(x * (1 - x), x).subs(x, sp.Rational(1, 2)) == 0
    assert (x * (1 - x)).subs(x, sp.Rational(1, 2)) == sp.Rational(1, 4)
    print("PASS")
    print("  Case A: q=m_R2/Z_R, dGamma/dq=-Z_R")
    print("  Case B: residues opposite when Delta>0")
    print("  Cut threshold: max x(1-x)=1/4 => q_th=4 omega^2")

if __name__ == "__main__":
    main()
