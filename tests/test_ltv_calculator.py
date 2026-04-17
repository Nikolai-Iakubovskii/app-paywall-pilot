from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from tools.ltv_calculator import Plan, calculate


class CalculatorTests(unittest.TestCase):
    def test_cli_wrapper_outputs_json(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(REPO / "tools/ltv-calculator.py"),
                "--plan",
                "annual:59.99:0.7",
                "--plan",
                "monthly:9.99:0.3",
                "--installs",
                "20000",
                "--trial-start",
                "0.11",
                "--trial-paid",
                "0.30",
                "--json",
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        payload = json.loads(result.stdout)
        self.assertIn("roas", payload)
        self.assertEqual(payload["inputs"]["apple_fee"], "15%")

    def test_invalid_plan_type_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "Unknown plan_type"):
            calculate(
                plans=[Plan("invalid", 10, 1.0)],
                monthly_installs=1000,
                cr_to_purchase=0.1,
            )

    def test_negative_inputs_rejected(self) -> None:
        with self.assertRaisesRegex(ValueError, "cpi must be >= 0"):
            calculate(
                plans=[Plan("annual", 10, 1.0)],
                monthly_installs=1000,
                cr_to_purchase=0.1,
                cpi=-1,
            )

    def test_retention_curve_must_be_monotonic(self) -> None:
        bad_retention = {
            "weekly": {"7d": 0.0, "1mo": 1.0, "3mo": 0.5, "6mo": 1.0, "1yr": 1.0, "2yr": 1.0, "3yr": 1.0, "4yr": 1.0},
            "monthly": {"7d": 0.0, "1mo": 0.4, "3mo": 0.7, "6mo": 1.0, "1yr": 1.6, "2yr": 2.0, "3yr": 2.2, "4yr": 2.3},
            "quarterly": {"7d": 0.0, "1mo": 0.0, "3mo": 0.15, "6mo": 0.2, "1yr": 0.35, "2yr": 0.4, "3yr": 0.45, "4yr": 0.45},
            "annual": {"7d": 0.0, "1mo": 0.0, "3mo": 0.0, "6mo": 0.0, "1yr": 0.1, "2yr": 0.13, "3yr": 0.15, "4yr": 0.16},
            "lifetime": {"7d": 0.0, "1mo": 0.0, "3mo": 0.0, "6mo": 0.0, "1yr": 0.0, "2yr": 0.0, "3yr": 0.0, "4yr": 0.0},
        }
        with self.assertRaisesRegex(ValueError, "non-decreasing"):
            calculate(
                plans=[Plan("annual", 20, 1.0)],
                monthly_installs=1000,
                cr_to_purchase=0.1,
                custom_retention=bad_retention,
            )

    def test_zero_cpi_returns_infinite_roas(self) -> None:
        result = calculate(
            plans=[Plan("annual", 59.99, 1.0)],
            monthly_installs=1000,
            cr_to_purchase=0.1,
            cpi=0,
        )
        self.assertEqual(result.cac, 0.0)
        self.assertEqual(result.roas["7d"], float("inf"))
        self.assertEqual(result.ltv_to_cac_4yr, float("inf"))
        payload = result.to_json_dict()
        self.assertEqual(payload["roas"]["7d"], "inf")
        self.assertEqual(payload["ltv_to_cac_4yr"], "inf")


if __name__ == "__main__":
    unittest.main()
