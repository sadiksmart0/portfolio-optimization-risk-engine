import numpy as np

# =========================================================
# PORTFOLIO RETURN
# =========================================================

def calculate_portfolio_return(weights, mean_returns):

    return np.dot(weights, mean_returns)