"""
Thank you to Tobias Rodriguez del Pozo for his assistance in writing this code.
"""

from matplotlib import dates
import numpy as np
import pandas as pd

from pathlib import Path
import misc_tools
import pull_CRSP_stock
from settings import config

OUTPUT_DIR = config("OUTPUT_DIR")
DATA_DIR = config("DATA_DIR")



def load_CRSP_mothly_stock_data(data_dir=DATA_DIR):
    path = Path(data_dir) / "CRSP_monthly_stock.parquet"
    df = pd.read_parquet(path)
    return df

    

if __name__ == "__main__":
    # Load CRSP monthly stock data
    df = load_CRSP_mothly_stock_data()

    print(df.head())