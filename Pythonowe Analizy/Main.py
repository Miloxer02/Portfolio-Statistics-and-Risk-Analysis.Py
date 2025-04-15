
from Models.Config import Config
from Models.Download_Stooq import download_stooq
# from Models.Download_Yahoo import download_yahoo
from Models.Portfolio_analysis import analyze_log_return_statistics
from Models.Export_excel import export_statistics_to_excel

import pandas as pd
import datetime
import matplotlib.pyplot as plt

# Function for downloading data
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

    # Run Statistics
    analyze_log_return_statistics(asset_data)
    print(stats_dict)

    # Export results to Excel
    #export_statistics_to_excel(asset_data)


# Function start
print(main())

