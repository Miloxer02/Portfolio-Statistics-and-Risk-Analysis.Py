import pandas as pd
import os

def export_statistics_to_excel(stats_dict, mvp_weights=None, portfolio_stats=None, export_path="Excels", file_name="portfolio_statistics.xlsx"):
    # Ensure the export directory exists
    os.makedirs(export_path, exist_ok=True)

    output_file = os.path.join(export_path, file_name)

    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        # 1. Statistics
        stats_df = pd.DataFrame.from_dict(stats_dict, orient="index").T
        stats_df.index.name = "Statistic"
        stats_df.to_excel(writer, sheet_name="Statistics")

        # 2. MVP weights
        if mvp_weights is not None:
            mvp_df = pd.DataFrame(mvp_weights, columns=["Weight"])
            mvp_df.index.name = "Asset"
            mvp_df.to_excel(writer, sheet_name="MVP_Weights")

        # 3. Portfolio-level stats
        if portfolio_stats is not None:
            port_df = pd.DataFrame(portfolio_stats, index=["Portfolio"])
            port_df.to_excel(writer, sheet_name="MVP_Stats")

    print(f"\n[4]✅ Exported full analysis to Excel: {output_file}")
