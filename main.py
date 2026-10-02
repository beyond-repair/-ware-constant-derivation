#!/usr/bin/env python3
"""Claim-0 demo. Runs the in-tree verifiers. Does not derive W=0.08."""
from __future__ import annotations

import sys

from run_derivation_checks import main as run_checks


def main() -> int:
    return run_checks()


if __name__ == "__main__":
    sys.exit(main())
