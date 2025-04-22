import os
import pandas as pd

def export_statistics_to_excel(stats_dict_daily, stats_dict_annual,
                               export_path="Excels", file_name="portfolio_statistics.xlsx"):

    os.makedirs(export_path, exist_ok=True)
    output_file = os.path.join(export_path, file_name)

    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        # 1. Daily Statistics
        df_daily = pd.DataFrame.from_dict(stats_dict_daily, orient="index").T
        df_daily.index.name = "Statistic"
        df_daily.to_excel(writer, sheet_name="Daily_Statistics")

        # 2. Annual Statistics
        df_annual = pd.DataFrame.from_dict(stats_dict_annual, orient="index").T
        df_annual.index.name = "Statistic"
        df_annual.to_excel(writer, sheet_name="Annual_Statistics")

        # 3. 10-Day Statistics (approximate: daily * 10)
        df_10day = df_daily * 10
        df_10day.index.name = "Statistic"
        df_10day.to_excel(writer, sheet_name="10Day_Statistics")

    print(f"\n[3]✅ Exported full analysis to Excel: {output_file}")
