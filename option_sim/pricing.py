"""European call pricing, no dividends; contract multiplier 1.

Scalar inputs only. Time is in years; rate and volatility are annual decimals.
Initial domain: finite inputs, spot/strike/maturity/volatility strictly positive.
The continuously compounded rate may be negative.
"""

import numpy as np
from scipy.special import ndtr


def call_price(
    spot: float,
    strike: float,
    maturity: float,
    rate: float,
    volatility: float,
) -> float:
    """Return the Black-Scholes call value for one unit of underlying."""
    # TODO (Yann): calculate d1, d2, then the discounted call value.
    raise NotImplementedError("Your first task: implement the European call price.")


def call_delta(
    spot: float,
    strike: float,
    maturity: float,
    rate: float,
    volatility: float,
) -> float:
    """Return d(call value)/d(spot), holding all other inputs fixed."""
    # TODO (Yann): calculate the analytic no-dividend call delta.
    raise NotImplementedError("Your first task: implement the European call delta.")
