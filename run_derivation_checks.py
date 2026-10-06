#!/usr/bin/env python3
"""Run every in-tree verifier and print the numbers those checks actually produce.

Exit status 0 means every existing assertion passed. It does not mean W ≈ 0.08
was derived. The pinch cubic recovers 0.08 only because that value built beta.
"""
from __future__ import annotations

import importlib
import sys
import traceback
from typing import Any

CHECKS = (
    "verify_constant_W_action",
    "verify_pinch_cubic",
    "verify_proofs_5R_7",
    "verify_proof_6A_dimreg",
    "verify_proof_6B_uv",
    "verify_proof_6C_poles",
    "verify_proof_6C1_im",
    "verify_proof_7B_hs",
    "verify_proof_15A_secular",
)


def _summary(name: str, result: dict[str, Any]) -> str:
    if name == "verify_constant_W_action":
        return (
            "random graph seed 0: "
            f"λ_max={result['lam_max']:.6f}  "
            f"W_crit={result['W_crit']:.6f}  "
            f"W={result['W']:.6f}  "
            f"V''={result['d2V']:.6f}  "
            f"V(W_near)={result['V_near']:.6f}  "
            "(W is not 0.08 and W_crit is not 1/6 on this matrix)"
        )
    if name == "verify_pinch_cubic":
        roots = ", ".join(f"{complex(r).real:.7g}" for r in result["roots"])
        return (
            f"circular beta={result['beta']} = {float(result['beta'])} "
            f"recovers input root 0.08; roots [{roots}]"
        )
    if name == "verify_proofs_5R_7":
        return (
            f"discrete form rel. mismatch={result['rel']:.4f} "
            "(not exact; script tolerance 0.15); constant-W recovery exact; I2>0"
        )
    if name == "verify_proof_6C1_im":
        return (
            f"Im_num={result['Im_num']:.8f} Im_an={result['Im_an']:.8f} "
            f"rel={result['rel']:.3e} (tolerance 1e-5)"
        )
    return "algebraic identities held"


def main(argv: list[str] | None = None) -> int:
    del argv  # no configuration; seeds and regulators are fixed in the scripts
    failed = 0
    print("Ware Constant derivation checks")
    print("Claim-0: identities in this tree. 0.08 is not a derived output.")
    print("experimental_validation = false")
    for name in CHECKS:
        print(f"\n=== {name} ===")
        try:
            module = importlib.import_module(name)
            result = module.main()
        except Exception:
            failed += 1
            print("FAIL")
            traceback.print_exc()
            continue
        if isinstance(result, int):
            if result != 0:
                failed += 1
                print("FAIL (nonzero exit)")
                continue
            print("PASS")
            print("integer verifier exit 0; does not derive 0.08")
            continue
        if not isinstance(result, dict):
            failed += 1
            print("FAIL (verifier returned no result dict)")
            continue
        print("PASS")
        print(_summary(name, result))
    print(f"\nchecks={len(CHECKS)} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
