# =========================================================
# PORTFOLIO GROWTH
# =========================================================

def calculate_portfolio_growth(portfolio_returns):

    return (1 + portfolio_returns).cumprod()