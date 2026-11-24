# Options market-making simulator

A learning project built one small milestone at a time. The aim is to understand and defend each pricing, risk and simulation choice.

## Current state

Milestone 1: implement a European call price and delta under Black-Scholes with no dividends. The calculation functions deliberately raise `NotImplementedError` until Yann implements them. There is no simulator or trading performance yet.

Local project: `P:\options-market-making-simulator`.
GitHub: [Yannrvt29/options-market-making-simulator](https://github.com/Yannrvt29/options-market-making-simulator), owned by `Yannrvt29` (`yannravot@gmail.com`). The local `origin` remote points there. Git transfers changes through commits and pushes; it does not sync edits automatically. The `.venv` folder stays local.

## Setup (PowerShell)

The initial environment was found at `C:\ProgramData\anaconda3\python.exe`: Python 3.12.7, NumPy 1.26.4 and SciPy 1.13.1. The dependency pins match these available versions; they are not a claim about the latest releases.

```powershell
Set-Location P:\options-market-making-simulator
& 'C:\ProgramData\anaconda3\python.exe' -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

On another machine, use a Python 3.12 interpreter in the first setup command. Call the environment's Python directly so PowerShell activation policy does not get in the way. Setup is needed once; rerun the test command after editing.

Only NumPy and SciPy are needed. Tests use Python's built-in `unittest`. A small package and pure scalar functions keep the first step easy to inspect. No event framework, notebooks or C++ yet.

Read [MILESTONE_01.md](MILESTONE_01.md) for your first task. Tests will report errors at the intentional stubs until the calculations exist.

## Roadmap

1. European option pricing and Greeks.
2. Positions, cash accounting and delta hedging.
3. Event-driven simulation and two-sided quoting.
4. Inventory-aware quoting, fees, latency and adverse selection.
5. Real options data, SVI smiles, then constrained SSVI.
6. Profile the working implementation before considering C++.

When data arrives, label its source and timestamp. Historical quotes and trades are observations. A fill produced by our model is simulated, even if it uses historical prices. Record seeds, configuration, assumptions and limitations for simulation runs.

## Interview connection

Optiver's [Graduate Quantitative Researcher role (2027 start)](https://www.optiver.com/join-us/jobs/quantitative-research-and-machine-learning/amsterdam/graduate-quantitative-researcher-2027-start/) describes pricing models, empirical testing and collaboration across research, trading and engineering (checked 24 November 2026).

This project is a way to practise explaining assumptions, testing models and measuring risk. That is our interpretation of its relevance, not an Optiver assessment requirement or a model of their proprietary systems. Later work should connect each added complexity to a clear research question.
