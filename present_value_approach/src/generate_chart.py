"""
Thank you to Tobias Rodriguez del Pozo for his assistance in writing this code.
"""

from matplotlib import dates
import numpy as np
import pandas as pd

from pathlib import Path
from settings import config
import matplotlib.pyplot as plt


OUTPUT_DIR = config("OUTPUT_DIR")
DATA_DIR = config("DATA_DIR")



def load_CRSP_monthly_stock_data(data_dir=DATA_DIR):
    path = Path(data_dir) / "CRSP_monthly_stock.parquet"
    df = pd.read_parquet(path)
    return df


def load_r30_day_T_bill(data_dir=DATA_DIR):
    path = Path(data_dir) / "CRSP_30_day_T_bill.parquet"
    df = pd.read_parquet(path)
    return df


def generate_chart(stock_market_return, T_bill):
    # --------------------
    # Sanity checks
    # --------------------
    required_cols = {'date', 'vwretd', 'vwretx'}
    assert required_cols.issubset(stock_market_return.columns), f"Missing columns: {required_cols - set(stock_market_return.columns)}"

    # --------------------
    # Collapse stock-level data to market-level
    # --------------------
    market = (
        stock_market_return[['date', 'vwretd', 'vwretx']]
        .drop_duplicates(subset=['date'])
        .sort_values('date')
    )

    # --------------------
    # Merge risk-free rate
    # --------------------
    market = market.merge(T_bill[['date', 't30ret']], on='date', how='left')

    # --------------------
    # Plot 1: Market returns
    # --------------------
    plt.figure()
    plt.plot(market['date'], market['vwretd'], label='VW Market Return (with distributions)')
    plt.plot(market['date'], market['vwretx'], label='VW Market Return (ex distributions)')
    plt.xlabel('Date')
    plt.ylabel('Monthly Return')
    plt.title('CRSP Value-Weighted Market Returns')
    plt.legend()
    plt.tight_layout()
    # Ensure output directory exists
    Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

    plt.savefig(Path(OUTPUT_DIR) / "crsp_market_returns.png")
    plt.close()

    # --------------------
    # Plot 2: Risk-free rate
    # --------------------
    plt.figure()
    plt.plot(market['date'], market['t30ret'])
    plt.xlabel('Date')
    plt.ylabel('Monthly Risk-Free Rate')
    plt.title('30-Day Treasury Bill Rate')
    plt.tight_layout()

    plt.savefig(Path(OUTPUT_DIR) / "crsp_30day_tbill.png")
    plt.close()

     # --------------------
    # Plot 3: Excess market returns
    # --------------------

    market['excess_mkt'] = market['vwretd'] - market['t30ret']

    plt.figure()
    plt.plot(market['date'], market['excess_mkt'])
    plt.xlabel('Date')
    plt.ylabel('Excess Return')
    plt.title('Excess Market Return')
    plt.tight_layout()

    plt.savefig(Path(OUTPUT_DIR) / "excess_market_return.png")
    plt.close()

    

if __name__ == "__main__":
    # Load CRSP monthly stock data
    stock_market_return = load_CRSP_monthly_stock_data(DATA_DIR)
    T_bill = load_r30_day_T_bill(DATA_DIR)
    generate_chart(stock_market_return, T_bill)
