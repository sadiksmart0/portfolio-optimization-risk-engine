# Portfolio Optimization & Risk Modeling Engine

A quantitative finance project implementing portfolio optimization,
risk analysis, and out-of-sample portfolio evaluation using
Modern Portfolio Theory (MPT).

The project compares two diversified equity portfolios using
historical market data, covariance-based risk estimation,
and constrained optimization techniques to evaluate
risk-adjusted portfolio performance.

---

## Project Overview

This project explores portfolio construction and optimization
under the mean-variance optimization framework introduced
by Harry Markowitz.

Using historical stock market data, the system:

- Downloads and preprocesses financial time series data
- Computes simple and log returns
- Estimates annualized returns and covariance matrices
- Optimizes portfolio allocations
- Evaluates portfolio volatility and expected returns
- Performs out-of-sample backtesting
- Compares portfolio performance using Sharpe ratios
- Visualizes portfolio growth and risk-return characteristics

The project emphasizes clean quantitative research workflows,
modular financial analysis, and practical portfolio evaluation.

---

## Features

### Data Collection & Processing
- Historical equity market data retrieval using `yfinance`
- Time-series preprocessing
- Daily simple return computation
- Daily log return computation

### Portfolio Analytics
- Annualized expected returns
- Annualized covariance matrix estimation
- Portfolio return calculation
- Portfolio volatility estimation

### Portfolio Optimization
- Minimum volatility optimization
- Long-only portfolio constraints
- Weight normalization constraints
- Portfolio allocation analysis

### Risk Modeling
- Covariance heatmaps
- Volatility comparison
- Risk-return analysis
- Sharpe ratio evaluation

### Backtesting & Evaluation
- Train/test split methodology
- Out-of-sample portfolio testing
- Portfolio growth simulation
- Comparative portfolio performance analysis

---

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- SciPy
- yFinance

---

## Mathematical Concepts

The project implements several key quantitative finance concepts.

### Portfolio Expected Return

\[
E[R_p] = w^T \mu
\]

Where:

- \(w\) = portfolio weights
- \(\mu\) = expected asset returns

---

### Portfolio Volatility

\[
\sigma_p = \sqrt{w^T \Sigma w}
\]

Where:

- \(\Sigma\) = covariance matrix of asset returns

---

### Sharpe Ratio

\[
S = \frac{E[R_p] - r_f}{\sigma_p}
\]

Where:

- \(r_f\) = risk-free rate
- \(\sigma_p\) = portfolio volatility

---

## Portfolio Construction

### Portfolio A
- AAPL
- MSFT
- JPM
- XOM
- UNH
- PG
- HD
- CAT

### Portfolio B
- AAPL
- MSFT
- JNJ
- JPM
- XOM
- PG
- KO
- PEP

---

## Optimization Methodology

The optimization process minimizes portfolio volatility
subject to the following constraints:

- Portfolio weights sum to 1
- No short selling
- Long-only allocations

Optimization is performed using:

```python
scipy.optimize.minimize(method='SLSQP')
```

---

## Out-of-Sample Evaluation

The project uses a train/test split approach:

- Training Data:
  - 2024–2025

- Testing Data:
  - 2026

Optimized weights are learned from training data
and evaluated on unseen test data to assess
generalization and robustness.

---

## Example Results

### Portfolio A
- Annual Return: 8.94%
- Volatility: 11.20%
- Sharpe Ratio: 0.798

### Portfolio B
- Annual Return: 16.68%
- Volatility: 10.07%
- Sharpe Ratio: 1.656

Portfolio B achieved superior risk-adjusted performance,
delivering both higher returns and lower volatility
during the out-of-sample evaluation period.

---

## Visualizations

The project includes several visual analytics components:

- Historical asset price trends
- Covariance heatmaps
- Portfolio growth comparison
- Asset vs portfolio volatility comparison
- Asset vs portfolio return comparison

---

## Project Structure

```text
portfolio_optimization_risk_modeling/
│
├── notebooks/
│   └── portfolio_optimization.ipynb
│
├── src/
│   ├── data.py
│   ├── metrics.py
│   ├── optimization.py
│   ├── visualization.py
│   └── utils.py
│
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Key Learning Outcomes

This project demonstrates:

- Quantitative finance fundamentals
- Portfolio optimization techniques
- Financial risk modeling
- Numerical optimization using SciPy
- Financial data engineering
- Scientific Python programming
- Research-oriented software design

---

## Author

Abubakar Muktar

Master's in Data Science & Analytics  
Background in Computer Science, Quantitative Finance,
Portfolio Optimization, and Financial Engineering

---

## License

This project is licensed under the MIT License.