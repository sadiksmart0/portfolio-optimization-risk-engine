# =========================================================
# PORTFOLIO VOLATILITY
# =========================================================

def calculate_portfolio_volatility(weights, cov_matrix):

    return np.sqrt(
        np.dot(
            weights.T,
            np.dot(cov_matrix, weights)
        )
    )