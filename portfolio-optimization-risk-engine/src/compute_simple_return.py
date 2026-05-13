# =========================================================
# DAILY RETURNS
# =========================================================

def simple_daily_return(portfolio_A, portfolio_B):
    
    simple_stock_returns_A = portfolio_A.dropna().pct_change()[1:]
    simple_stock_returns_B = portfolio_B.dropna().pct_change()[1:]

    return simple_stock_returns_A, simple_stock_returns_B

