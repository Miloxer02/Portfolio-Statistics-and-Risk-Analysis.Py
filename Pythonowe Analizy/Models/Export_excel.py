import pandas as pd
import os

def export_statistics_to_excel(stats_dict, export_path="Excels", file_name="portfolio_statistics.xlsx"):
    # Ensure the export directory exists
    os.makedirs(export_path, exist_ok=True)

    # Create DataFrame where each row is an asset, each column is a statistic
    stats_df = pd.DataFrame(stats_dict)
    stats_df.index.name = "Statistic"

    # Export to Excel
    output_file = os.path.join(export_path, file_name)
    stats_df.to_excel(output_file, sheet_name="Statistics")

    print(f"\n[3]✅ Statistics exported to Excel: {output_file}")
