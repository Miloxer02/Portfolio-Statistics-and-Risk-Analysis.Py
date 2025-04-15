import pandas as pd
import os

def export_statistics_to_excel(stats_dict, mvp_weights=None, export_path="Excels", file_name="portfolio_statistics.xlsx"):
    """
    Export descriptive statistics and optional Minimum Variance Portfolio (MVP) weights to an Excel file.

    Parameters:
    - stats_dict (dict): Dictionary containing statistics for each asset
    - mvp_weights (pd.Series, optional): Series with MVP weights
    - export_path (str): Folder where the Excel file will be saved
    - file_name (str): Name of the output Excel file
    """
    os.makedirs(export_path, exist_ok=True)

    # Prepare statistics DataFrame
    stats_df = pd.DataFrame(stats_dict)
    stats_df.index.name = "Statistic"

    # Create Excel writer
    output_file = os.path.join(export_path, file_name)
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        # Write statistics to one sheet
        stats_df.to_excel(writer, sheet_name="Statistics")

        # Write MVP weights if provided
        if mvp_weights is not None:
            weights_df = mvp_weights.to_frame(name="Weight")
            weights_df.index.name = "Asset"
            weights_df.to_excel(writer, sheet_name="MinVarPortfolio")

    print(f"\n[4]✅ Statistics and MVP weights exported to Excel: {output_file}")
