import numpy as np

def analyze_log_return_statistics(asset_data):
    # Dictionary to store statistics for different holding periods
    stats_dicts = {
        "1D": {},
        "3D": {},
        "5D": {},
        "10D": {},
        "Annual": {}
    }

    print("\n[2]✅ Calculating Statistics using Log Returns for multiple intervals")

    for name, df in asset_data.items():
        df = df.copy()

        # Calculate log returns
        df['Log_Return'] = np.log(df['Close'] / df['Close'].shift(1))
        df.dropna(inplace=True)

        # Compute daily statistical measures
        mean = df['Log_Return'].mean()
        std = df['Log_Return'].std()
        var = df['Log_Return'].var()
        skew = df['Log_Return'].skew()
        kurt = df['Log_Return'].kurt()

        # Value at Risk and Expected Shortfall
        var_95 = np.percentile(df['Log_Return'], 5)
        es_95 = df[df['Log_Return'] <= var_95]['Log_Return'].mean()
        var_99 = np.percentile(df['Log_Return'], 1)
        es_99 = df[df['Log_Return'] <= var_99]['Log_Return'].mean()

        # Helper function to scale daily stats to other intervals
        def scale_stats(factor):
            return {
                "Last Close Price": df['Close'].iloc[-1].item(),
                "Mean Return": mean * factor,
                "Standard Deviation": std * np.sqrt(factor),
                "Variance": var * factor,
                "Skewness": skew,
                "Kurtosis": kurt,
                "VaR 95%": var_95 * np.sqrt(factor),
                "ES 95%": es_95 * np.sqrt(factor),
                "VaR 99%": var_99 * np.sqrt(factor),
                "ES 99%": es_99 * np.sqrt(factor)
            }

        # Store statistics for all selected intervals
        stats_dicts["1D"][name] = scale_stats(1)
        stats_dicts["3D"][name] = scale_stats(3)
        stats_dicts["5D"][name] = scale_stats(5)
        stats_dicts["10D"][name] = scale_stats(10)
        stats_dicts["Annual"][name] = scale_stats(250)

    return stats_dicts
