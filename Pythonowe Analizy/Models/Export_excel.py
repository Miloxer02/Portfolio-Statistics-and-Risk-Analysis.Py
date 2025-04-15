import os
import pandas as pd

def export_statistics_to_excel(stats_dict_daily, stats_dict_annual,
                               mvp_weights=None, portfolio_stats=None,
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

        # 3. MVP Weights
        if mvp_weights is not None:
            mvp_df = pd.DataFrame(mvp_weights, columns=["Weight"])
            mvp_df.index.name = "Asset"
            mvp_df.to_excel(writer, sheet_name="MVP_Weights")

        # 4. Portfolio Stats
        if portfolio_stats is not None:
            port_df = pd.DataFrame(portfolio_stats, index=["Portfolio"])
            port_df.to_excel(writer, sheet_name="MVP_Stats")

    print(f"\n[4]✅ Exported full analysis to Excel: {output_file}")
