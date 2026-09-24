#!/usr/bin/env python3
from __future__ import annotations
import numpy as np
import sympy as sp

def main() -> None:
    x, q, w2 = sp.symbols("x q omega2", positive=True)
    p2 = -q
    Dlt = w2 - x * (1 - x) * q
    P = sp.expand(
        12 * Dlt**2 - 24 * Dlt * p2 * x**2 + 24 * Dlt * p2 * x - 10 * Dlt * p2
        + 4 * p2**2 * x**4 - 8 * p2**2 * x**3 + 8 * p2**2 * x**2 - 4 * p2**2 * x + p2**2
    )
    xi = sp.sqrt(1 - 4 * w2 / q)
    xL, xR = (1 - xi) / 2, (1 + xi) / 2
    integ = sp.simplify(sp.integrate(P, (x, xL, xR)))
    assert sp.simplify(integ - 4 * w2**2 * sp.sqrt(1 - 4 * w2 / q)) == 0
    def Pnum(xx, qq=8.0, ww=1.0):
        return (12*ww**2 + 48*ww*qq*xx**2 - 48*ww*qq*xx + 10*ww*qq
                + 40*qq**2*xx**4 - 80*qq**2*xx**3 + 54*qq**2*xx**2 - 14*qq**2*xx + qq**2)
    qq, ww = 8.0, 1.0
    xxi = np.sqrt(1 - 4*ww/qq)
    xs = np.linspace((1-xxi)/2, (1+xxi)/2, 8000)
    intP = float(np.trapezoid(Pnum(xs), xs))
    Im_num = intP / (64*np.pi)
    Im_an = (ww**2)*np.sqrt(1-4*ww/qq)/(16*np.pi)
    assert abs(Im_num-Im_an)/Im_an < 1e-5
    print("PASS")

if __name__ == "__main__":
    main()
