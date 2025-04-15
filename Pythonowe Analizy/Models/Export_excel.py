import pandas as pd
import numpy as np
import os

def export_statistics_to_excel(asset_data, export_path="Excels", file_name="statistics_summary.xlsx"):
    os.makedirs(export_path, exist_ok=True)
    output_file = os.path.join(export_path, file_name)

    stats_dict = {}

    for name, df in asset_data.items():
        df = df.copy()
        df['Log_Return'] = np.log(df['Zamkniecie'] / df['Zamkniecie'].shift(1))
        df.dropna(inplace=True)

        var_95 = np.percentile(df['Log_Return'], 5)
        var_99 = np.percentile(df['Log_Return'], 1)
        es_95 = df[df['Log_Return'] <= var_95]['Log_Return'].mean()
        es_99 = df[df['Log_Return'] <= var_99]['Log_Return'].mean()

        stats = {
            "Mean Return": df['Log_Return'].mean(),
            "Standard Deviation": df['Log_Return'].std(),
            "Variance": df['Log_Return'].var(),
            "Skewness": df['Log_Return'].skew(),
            "Kurtosis": df['Log_Return'].kurt(),
            "Rolling Mean (5d)": df['Log_Return'].rolling(5).mean().iloc[-1],
            "Empirical VaR 95%": var_95,
            "Empirical VaR 99%": var_99,
            "Expected Shortfall 95%": es_95,
            "Expected Shortfall 99%": es_99
        }

        stats_dict[name] = stats

    # Zamiana do DataFrame
    stats_df = pd.DataFrame(stats_dict)
    
    # Zapis do Excela
    with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
        stats_df.to_excel(writer, sheet_name="Summary_Stats")

    print(f"\n✅ Statistical summary saved to: {output_file}")
