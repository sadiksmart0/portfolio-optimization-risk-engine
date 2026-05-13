import matplotlib.pyplot as plt

def display_risk_return_comparison(returns_data, portfolio_returns, portfolio_name):
    # assets & portfolio volatility
    portfolio_volatility = portfolio_returns.std()
    asset_volatility = returns_data.std()

    # portfolio & total asset returns
    asset_total_returns = ((1 + returns_data).prod() - 1)
    portfolio_total_return = ((1 + portfolio_returns).prod() - 1)
    
    fig, (ax1, ax2) = plt.subplots(1,2,figsize=(16,5))

    # =========================================
    # VOLATILITY COMPARISON
    # =========================================

    ax1.bar(x=returns_data.columns, height=asset_volatility, alpha=0.7)
    ax1.hlines(
        y=portfolio_volatility,
        xmin=-0.5,
        xmax=len(returns_data.columns)-0.5,
        linestyle="--",
        color="red",
        alpha=0.8,
        label="Portfolio Volatility"
    )

    ax1.set_title(f"{portfolio_name} Assets vs Portfolio Volatility")
    ax1.set_ylabel("Volatility")
    ax1.legend()

    # =========================================
    # TOTAL RETURN COMPARISON
    # =========================================

    ax2.bar(x=returns_data.columns, height=asset_total_returns, alpha=0.7)
    ax2.hlines(
        y=portfolio_total_return,
        xmin=-0.5,
        xmax=len(returns_data.columns)-0.5,
        linestyle="--",
        color="red",
        alpha=0.8,
        label="Portfolio Total Return")

    ax2.set_title(f"{portfolio_name} Assets vs Portfolio Returns")
    ax2.set_ylabel("Total Return")
    ax2.legend()
    plt.show()