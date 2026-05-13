import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from compute_simple_return import simple_daily_return
from train_test_split import train_test_split
from portfolio_growth import calculate_portfolio_growth
from display_portfolio import display_portfolios


import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

end = datetime.date.today()
start = "2024-01-01"

ticker_A = ['AAPL','MSFT','JPM','XOM','UNH','PG','HD','CAT']
ticker_B = ['AAPL','MSFT','JNJ','JPM','XOM','PG','KO','PEP']

portfolio_A = download_data(start, end, ticker_A)
portfolio_B = download_data(start, end, ticker_B)

from_ = "2024-01-01"
to_ = "2026-05-01"

display_price_history(portfolio_A, ticker_A, from_, to_, "Portfolio A")
display_price_history(portfolio_B, ticker_B, from_, to_, "Portfolio B")


simple_stock_returns_A = simple_daily_return(portfolio_A, portfolio_B)
simple_stock_returns_B = simple_daily_return(portfolio_A, portfolio_B)

train_returns_A, test_returns_A, train_returns_B, test_returns_B = train_test_split(
                    simple_stock_returns_A,
                    simple_stock_returns_B
)

mean_returns_A = simple_stock_returns_A.mean() * 252
cov_matrix_A = simple_stock_returns_A.cov() * 252
mean_returns_B = simple_stock_returns_B.mean() * 252
cov_matrix_B = simple_stock_returns_B.cov() * 252


optimal_weights_A = optimize_portfolio_weights(
    mean_returns_A,
    cov_matrix_A
)

optimal_weights_B = optimize_portfolio_weights(
    mean_returns_B,
    cov_matrix_B
)

portfolio_returns_A = calculate_portfolio_returns(
    test_returns_A,
    optimal_weights_A
)

portfolio_returns_B = calculate_portfolio_returns(
    test_returns_B,
    optimal_weights_B
)

portfolio_growth_A = calculate_portfolio_growth(
    portfolio_returns_A
)

portfolio_growth_B = calculate_portfolio_growth(
    portfolio_returns_B
)

display_portfolios(
    portfolio_growth_A,
    portfolio_growth_B
)
