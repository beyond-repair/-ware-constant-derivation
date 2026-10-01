"""Circularity check. Not a derivation of 0.08.

beta = delta**3 - delta**2 at delta = 2/25 is exactly -92/15625.
Solving the cubic with that beta recovers the input root.
"""
from fractions import Fraction

import numpy as np


def main() -> None:
    delta = Fraction(2, 25)
    beta = delta**3 - delta**2
    assert beta == Fraction(-92, 15625)
    assert float(beta) == -0.005888
    roots = np.roots([1.0, -1.0, 0.0, -float(beta)])
    assert any(abs(r.real - 0.08) < 1e-12 and abs(r.imag) < 1e-12 for r in roots)
    print("circular: beta", beta, "recovers input root 0.08")
    print("other roots", roots)


if __name__ == "__main__":
    main()
