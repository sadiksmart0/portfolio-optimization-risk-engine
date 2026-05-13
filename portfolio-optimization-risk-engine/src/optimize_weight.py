import numpy as np
from scipy.optimize import minimize

# =========================================================
# OPTIMIZE PORTFOLIO WEIGHTS
# =========================================================

def optimize_portfolio_weights(mean_returns, cov_matrix):

    num_assets = len(mean_returns)

    # equal weight initialization
    initial_weights = np.ones(num_assets) / num_assets

    # weights must sum to 1
    constraints = ({
        'type': 'eq',
        'fun': lambda w: np.sum(w) - 1
    })

    # no short selling
    bounds = tuple((0, 1) for _ in range(num_assets))

    optimization = minimize(
        calculate_portfolio_volatility,
        initial_weights,
        args=(cov_matrix,),
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )

    return optimization.x