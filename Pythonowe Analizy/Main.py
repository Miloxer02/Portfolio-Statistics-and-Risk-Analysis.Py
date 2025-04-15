
from Models.Download_Stooq import download_stooq
# from Models.Download_Yahoo import download_yahoo
from Models.Config import Config

import pandas as pd
import datetime
import matplotlib.pyplot as plt

def main():
    print("Starting procedure")

    print("\n[1] Downloading data...")
    asset_data = {}

    for asset in Config["assets"]:
        print(f"Downloading data for: {asset['name']}")

        if asset["source"] == "yfinance":
            df = download_yahoo(
                ticker=asset["ticker"],
                start_date=Config["start_date"],
                end_date=Config["end_date"],
                interval=asset["interval"]
            )
        elif asset["source"] == "stooq":
            df = download_stooq(
                ticker=asset["ticker"],
                start_date=Config["start_date"],
                end_date=Config["end_date"],
                interval=asset["interval"]
            )
        
        asset_data[asset["name"]] = df 
       

# Odpalanie funkcji
print(main())

