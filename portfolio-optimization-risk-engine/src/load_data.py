import yfinance as yfin

# =========================================================
# DOWNLOAD DATA
# =========================================================

def download_data(start, end, tickers):
    
    df = yfin.download(
        tickers,
        start,
        end,
        auto_adjust=False
    )["Adj Close"]

    # convert index to timezone-aware
    df.index = df.index.tz_localize('UTC')

    return df

#portfolio_A = pd.read_csv("/data/portfolio_A.csv", index=True)
#portfolio_B = pd.read_csv("/data/portfolio_A.csv", index=True)