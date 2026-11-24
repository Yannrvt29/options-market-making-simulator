# Milestone 1: a European call price and delta

## Your task

Implement only `call_price` and `call_delta` in `option_sim/pricing.py`. Keep the function signatures unchanged. Use NumPy for basic maths and `scipy.special.ndtr` for the standard normal CDF. Imports are already provided.

Start with a single scalar contract. Inputs must be finite, with `spot > 0`, `strike > 0`, `maturity > 0`, `volatility > 0`; the continuously compounded rate may be negative. For this first exercise these are documented preconditions. Input validation, expiry and zero-volatility limits are a later small task.

| Input | Meaning | Reference |
| --- | --- | --- |
| spot | Underlying price now | 100 |
| strike | Exercise price | 100 |
| maturity | Time to expiry in years | 1 |
| rate | Continuously compounded annual rate | 0 |
| volatility | Annualised volatility as a decimal | 0.20 |

No dividends. Contract multiplier is 1, so the option price is also its cash value per contract.

Expected price: `7.965567455405804` (about 7.9656).
Expected delta: `0.539827837277029` (about 0.5398).
These are theoretical reference values, not performance results.

## First hints

- Use the Black-Scholes European call formula. Form the dimensionless variables `d1` and `d2` from log-moneyness, carry, variance and `volatility * sqrt(maturity)`.
- A call is a discounted risk-neutral expected payoff under the model assumptions. Its formula combines an underlying term and a discounted strike term.
- Delta is the derivative of price with respect to spot, holding the other inputs fixed. Without dividends it equals the normal CDF evaluated at `d1`.
- `ndtr(x)` is a CDF, not a normal density. Volatility 20% is `0.20`, not `20`.

Black-Scholes assumes constant volatility and rate, a lognormal underlying, continuous trading, and no transaction costs. These assumptions give us a clear starting model. Later milestones will expose the costs and risks of discrete hedging and imperfect execution.

## Check your work

Run the README test command. The checks cover the reference call price and delta, a positive-rate reference case to catch missing discounting, and a central finite-difference delta at several spots. The finite-difference check compares your analytic delta to `(C(S+h) - C(S-h)) / (2h)` with `h = 1e-3`. The tolerance allows numerical round-off without accepting a materially wrong hedge ratio.

After your first attempt, we will review it before expanding scope. Once a put price exists, add the independent no-dividend identity `C - P = S - K * exp(-r*T)`. Do not implement the put using parity and then claim parity is an independent validation. Expiry and zero-volatility cases follow after the positive-time calculation works.

## Explain it aloud

1. Why can an at-the-money call have positive value at a zero interest rate?
2. What does delta about 0.54 tell you about the shares needed to hedge one short call with multiplier 1?
3. Why is delta not generally the risk-neutral probability of exercise?

Stop here. Send your implementation for review; ask for a hint if stuck.
