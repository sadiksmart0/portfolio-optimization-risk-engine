import matplotlib.pyplot as plt

# =========================================================
# ASSET PRICE HISTORY VISUALIZATION
# =========================================================

def display_price_history(df, assets, from_, to_, name):

    fig = plt.figure(figsize=(14,7))
    ax = fig.add_subplot(111)

    df.loc[from_:to_, assets].plot(ax=ax)

    ax.set_title(f"{name} Historical Asset Price Performance")
    ax.set_ylabel("Adjusted Closing Price")
    ax.set_xlabel("Date")

    ax.legend(
        title="Assets",
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.show()