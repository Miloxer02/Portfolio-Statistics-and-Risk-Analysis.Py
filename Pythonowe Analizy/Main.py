
from Models.Config import Config
from Models.Download_Stooq import download_stooq
# from Models.Download_Yahoo import download_yahoo
from Models.Portfolio_analysis import analyze_log_return_statistics
from Models.Export_excel import export_statistics_to_excel
from Models.Minimal_Variance_Portfolio import calculate_min_variance_portfolio

import pandas as pd
import datetime

# Function for downloading data from Download_Stooq, Download_Yahoo and Condig
def main():
    print("Starting procedure")

    print("\n[1]✅ Downloading data...")
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

    # Run Statistics from Portfolio_Analysis
    stats_dict = analyze_log_return_statistics(asset_data)

    # Calculate Minimal Variance Portfolio
    mvp_weights = calculate_min_variance_portfolio(asset_data)

    # Export results to Excel from Export_excel
    export_statistics_to_excel(stats_dict, mvp_weights)

# Function Run
print(main())

