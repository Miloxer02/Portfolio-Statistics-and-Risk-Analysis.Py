import numpy as np

def analyze_log_return_statistics(asset_data):
    stats_dict_daily = {}
    stats_dict_annual = {}

    print("\n[2]✅ Calculating Statistics using Log Returns")

    for name, df in asset_data.items():
        df = df.copy()
        df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
        df.dropna(inplace=True)

        # Daily
        mean = df['Log_Return'].mean()
        std = df['Log_Return'].std()
        var = df['Log_Return'].var()
        skew = df['Log_Return'].skew()
        kurt = df['Log_Return'].kurt()

        var_95 = np.percentile(df['Log_Return'], 5)
        es_95 = df[df['Log_Return'] <= var_95]['Log_Return'].mean()
        var_99 = np.percentile(df['Log_Return'], 1)
        es_99 = df[df['Log_Return'] <= var_99]['Log_Return'].mean()

        stats_dict_daily[name] = {
            "Last Close Price": df['Close'].iloc[-1],
            "Mean Return": mean,
            "Standard Deviation": std,
            "Variance": var,
            "Skewness": skew,
            "Kurtosis": kurt,
            "VaR 95%": var_95,
            "ES 95%": es_95,
            "VaR 99%": var_99,
            "ES 99%": es_99
        }

        stats_dict_annual[name] = {
            "Last Close Price": df['Close'].iloc[-1],
            "Mean Return": mean * 250,
            "Standard Deviation": std * np.sqrt(250),
            "Variance": var * 250,
            "Skewness": skew,
            "Kurtosis": kurt,
            "VaR 95%": var_95 * np.sqrt(250),
            "ES 95%": es_95 * np.sqrt(250),
            "VaR 99%": var_99 * np.sqrt(250),
            "ES 99%": es_99 * np.sqrt(250)
        }

    return stats_dict_daily, stats_dict_annual
