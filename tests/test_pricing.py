"""Acceptance checks for milestone 1. Stubs intentionally do not pass."""

import unittest

from option_sim.pricing import call_delta, call_price


class CallPricingTests(unittest.TestCase):
    def test_reference_price(self):
        actual = call_price(100.0, 100.0, 1.0, 0.0, 0.20)
        self.assertAlmostEqual(actual, 7.965567455405804, delta=1e-8)

    def test_reference_delta(self):
        actual = call_delta(100.0, 100.0, 1.0, 0.0, 0.20)
        self.assertAlmostEqual(actual, 0.539827837277029, delta=1e-8)

    def test_positive_rate_reference(self):
        # Standard S=K=100, T=1, r=5%, sigma=20% Black-Scholes example.
        actual_price = call_price(100.0, 100.0, 1.0, 0.05, 0.20)
        actual_delta = call_delta(100.0, 100.0, 1.0, 0.05, 0.20)
        self.assertAlmostEqual(actual_price, 10.450583572185565, delta=1e-8)
        self.assertAlmostEqual(actual_delta, 0.6368306511756191, delta=1e-8)

    def test_delta_matches_central_finite_difference(self):
        h = 1e-3
        for spot in (80.0, 100.0, 120.0):
            with self.subTest(spot=spot):
                price_up = call_price(spot + h, 100.0, 0.7, 0.03, 0.25)
                price_down = call_price(spot - h, 100.0, 0.7, 0.03, 0.25)
                numerical_delta = (price_up - price_down) / (2.0 * h)
                analytic_delta = call_delta(spot, 100.0, 0.7, 0.03, 0.25)
                self.assertAlmostEqual(analytic_delta, numerical_delta, delta=1e-7)


if __name__ == '__main__':
    unittest.main()
