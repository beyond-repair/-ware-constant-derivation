#!/usr/bin/env python3
from __future__ import annotations
import sympy as sp

def main() -> None:
    W, g, om2, lam = sp.symbols("W g omega2 lambda", positive=True)
    eq = sp.Eq(W / g, lam / (2 * (om2 - W * lam)))
    sols = sp.solve(eq, W)
    assert sp.simplify(sols[0] + sols[1] - om2 / lam) == 0
    Vpp = 1 / g - lam**2 / (2 * (om2 - W * lam) ** 2)
    Vpp_on = sp.simplify(Vpp.subs(om2 - W * lam, g * lam / (2 * W)))
    assert sp.simplify(Vpp_on - (g - 2 * W**2) / g**2) == 0
    print("PASS")

if __name__ == "__main__":
    main()
