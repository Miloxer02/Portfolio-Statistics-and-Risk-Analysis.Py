import numpy as np

def analyze_log_return_statistics(asset_data):
    stats_dict = {}

    print("\n[2]✅ Calculating descriptive statistics with Log Returns")

    for name, df in asset_data.items():
        df = df.copy()
        df['Log_Return'] = np.log(df['Zamkniecie'] / df['Zamkniecie'].shift(1))
        df.dropna(inplace=True)
        asset_data[name] = df
        
        var_95 = np.percentile(df['Log_Return'], 5)
        es_95 = df[df['Log_Return'] <= var_95]['Log_Return'].mean()
        var_99 = np.percentile(df['Log_Return'], 1)
        es_99 = df[df['Log_Return'] <= var_99]['Log_Return'].mean()

        stats = {
            "Last Close Price": df['Zamkniecie'].iloc[-1],
            "Mean Return": df['Log_Return'].mean(),
            "Standard Deviation": df['Log_Return'].std(),
            "Variance": df['Log_Return'].var(),
            "Skewness": df['Log_Return'].skew(),
            "Kurtosis": df['Log_Return'].kurt(),
            "Empirical VaR 95%": var_95,
            "Expected Shortfall 95%": es_95,
            "Empirical VaR 99%": var_99,
            "Expected Shortfall 99%": es_99
        }

        stats_dict[name] = stats

    return stats_dict
        
