"""Attackable check for Proof 15A.

Confirms the closed form and the stationarity identity at ell = L/2.
Does not claim W = 0.08. Exits nonzero on failure.
"""

from __future__ import annotations

import math
import sys


def secular(k: float, ell: float, branch: float, length: float = 1.0) -> float:
    return (
        math.cos(k * ell)
        - 2.0 * math.sin(k * ell) * math.tan(0.5 * k * length)
        - branch
    )


def main() -> int:
    theta = math.acos(2.0 / 3.0)
    k1 = 2.0 * theta
    k2 = 2.0 * (math.pi - theta)
    i_star = (k2 / k1) ** 2
    closed = (math.pi / theta - 1.0) ** 2

    r1 = abs(secular(k1, 0.5, -1.0))
    r2 = abs(secular(k2, 0.5, +1.0))
    if r1 > 1e-12 or r2 > 1e-12:
        print("FAIL secular residual", r1, r2)
        return 1
    if abs(i_star - closed) > 1e-12:
        print("FAIL closed form mismatch", i_star, closed)
        return 1

    # stationarity identity: both sectors share sec^2 = 9/4
    if abs(math.cos(k1 / 2.0) - 2.0 / 3.0) > 1e-12:
        print("FAIL cos k1/2")
        return 1
    if abs(math.cos(k2 / 2.0) + 2.0 / 3.0) > 1e-12:
        print("FAIL cos k2/2")
        return 1

    # comparison step: must not be reported as 0.08
    if abs(i_star - 0.08) < 0.1:
        print("FAIL unexpected proximity to 0.08", i_star)
        return 1

    print(f"I_star = {i_star:.16f}")
    print(f"closed = {closed:.16f}")
    print(f"residual -1 branch = {r1:.3e}")
    print(f"residual +1 branch = {r2:.3e}")
    print(f"I_star - 0.08 = {i_star - 0.08:.16f}")
    print("PASS proof 15A closed form and secular residual")
    print("experimental_validation = false")
    print("thrust_validated = false")
    print("energy_extraction_validated = false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
