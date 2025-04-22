import os
import pandas as pd

def export_statistics_to_excel(stats_dicts,
                               export_path="Excels",
                               file_name="portfolio_statistics.xlsx"):
    # Create export directory if it doesn't exist
    os.makedirs(export_path, exist_ok=True)
    output_file = os.path.join(export_path, file_name)

    with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
        for interval, stats in stats_dicts.items():
            # Convert nested dictionary to DataFrame
            df = pd.DataFrame.from_dict(stats, orient="index").T
            df.index.name = "Statistic"

            # Use interval directly (e.g. "1D", "3D", "Annual")
            sheet_name = f"{interval}_Statistics"
            df.to_excel(writer, sheet_name=sheet_name)

    print(f"\n[3]✅ Exported full analysis to Excel: {output_file}")
