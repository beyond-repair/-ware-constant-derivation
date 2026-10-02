"""Exercise the in-tree verifiers. Numbers are whatever the code computes."""
from __future__ import annotations

from fractions import Fraction

import numpy as np
import pytest

import verify_constant_W_action as constant_w
import verify_pinch_cubic as pinch
import verify_proof_6A_dimreg as proof_6a
import verify_proof_6B_uv as proof_6b
import verify_proof_6C1_im as proof_6c1
import verify_proof_6C_poles as proof_6c
import verify_proof_7B_hs as proof_7b
import verify_proofs_5R_7 as proofs_5r
from run_derivation_checks import CHECKS, main as run_all


def test_constant_w_identities_do_not_select_008():
    out = constant_w.main()
    assert out["source_tr"] == pytest.approx(out["source_spec"], rel=1e-12, abs=1e-12)
    assert out["d2V"] < 0
    assert out["V_near"] < -5.0
    assert out["W"] == pytest.approx(0.4 * out["W_crit"])
    # This draw is not the normalized Sierpinski bound and not the phenomenology target.
    assert abs(out["W_crit"] - (1.0 / 6.0)) > 1e-3
    assert abs(out["W"] - 0.08) > 1e-3
    assert out["lam_max"] > 0


def test_pinch_cubic_is_circular():
    out = pinch.main()
    delta = Fraction(2, 25)
    assert out["beta"] == delta**3 - delta**2 == Fraction(-92, 15625)
    assert float(out["beta"]) == -0.005888
    assert float(delta) == pytest.approx(0.08)
    recovered = [
        complex(r)
        for r in out["roots"]
        if abs(complex(r).real - 0.08) < 1e-12 and abs(complex(r).imag) < 1e-12
    ]
    assert len(recovered) == 1
    # Other roots are not 0.08. None of them is an independent derivation.
    others = [complex(r).real for r in out["roots"] if abs(complex(r).imag) < 1e-10]
    assert any(abs(x - 0.08) > 0.5 for x in others)


def test_discrete_form_is_not_exact():
    out = proofs_5r.main()
    # Neumann grid form vs matrix insertion. The script allows 0.15; equality fails.
    assert 0.0 < out["rel"] < 0.15


def test_imaginary_part_quadrature_tracks_analytic():
    out = proof_6c1.main()
    assert out["status"] == "PASS"
    assert out["rel"] < 1e-5
    assert out["Im_num"] == pytest.approx(out["Im_an"], rel=1e-5)


@pytest.mark.parametrize(
    "module",
    (proof_6a, proof_6b, proof_6c, proof_7b),
)
def test_algebraic_checks(module):
    assert module.main()["status"] == "PASS"


def test_runner_lists_every_script_and_passes():
    assert len(CHECKS) == 8
    assert run_all() == 0


def test_i2_large_k_tail_from_exported_density():
    omega = 1.0
    k = 1e6
    for d in (2, 3, 4):
        ratio = proofs_5r.i2_density(k, omega, d) * d * k**2
        assert ratio == pytest.approx(1.0, rel=1e-6)
        assert proofs_5r.i2_density(1.0, omega, d) > 0


def test_spectral_source_matches_trace_on_seed_0():
    rng = np.random.default_rng(0)
    gram = rng.normal(size=(12, 8))
    laplacian = gram @ gram.T
    evals = np.linalg.eigvalsh(laplacian)
    omega2 = 1.0
    w_crit = omega2 / float(evals.max())
    w = 0.4 * w_crit
    kernel = omega2 * np.eye(laplacian.shape[0]) - w * laplacian
    source_tr = 0.5 * float(np.trace(np.linalg.inv(kernel) @ laplacian))
    source_spec = constant_w.spectral_source(omega2, w, evals)
    assert source_tr == pytest.approx(source_spec, rel=1e-12, abs=1e-12)
    assert constant_w.v2_1loop(omega2, w, evals) < 0


def test_main_delegates_to_runner(monkeypatch):
    import main as demo

    monkeypatch.setattr(demo, "run_checks", lambda: 0)
    assert demo.main() == 0
