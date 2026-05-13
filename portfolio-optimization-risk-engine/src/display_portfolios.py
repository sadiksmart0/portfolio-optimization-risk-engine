import matplotlib.pyplot as plt

# =========================================================
# DISPLAY PORTFOLIOS
# =========================================================

def display_portfolios(
    portfolio_growth_A,
    portfolio_growth_B
):

    fig, ax = plt.subplots(figsize=(14,7))

    portfolio_growth_A.plot(
        ax=ax,
        linewidth=3,
        label="Portfolio A"
    )

    portfolio_growth_B.plot(
        ax=ax,
        linewidth=3,
        label="Portfolio B"
    )

    ax.set_title(
        "Out-of-Sample Portfolio Performance (2026)"
    )
    ax.legend()
    plt.show()

    return