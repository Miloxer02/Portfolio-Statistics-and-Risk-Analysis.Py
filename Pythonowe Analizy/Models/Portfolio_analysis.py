import numpy as np

def analyze_log_return_statistics(asset_data):
    print("\n[2]✅ Descriptive Statistics – Logarithmic Returns:")

    stats_dict = {}

    for name, df in asset_data.items():
        # Calculate daily logarithmic returns
        df['Log_Return'] = np.log(df['Zamkniecie'] / df['Zamkniecie'].shift(1))
        df.dropna(inplace=True)

        # Calculate statistical measures
        price = df['Zamkniecie'].iloc[-1]
        mean = df['Log_Return'].mean()
        std = df['Log_Return'].std()
        var = df['Log_Return'].var()
        skew = df['Log_Return'].skew()
        kurt = df['Log_Return'].kurt()
        var_95 = np.percentile(df['Log_Return'], 5)
        es_95 = df[df['Log_Return'] <= var_95]['Log_Return'].mean()
        var_99 = np.percentile(df['Log_Return'], 1)
        es_99 = df[df['Log_Return'] <= var_99]['Log_Return'].mean()

        # Save all statistics for this asset
        stats_dict[name] = {
            'Latest Closing Price': price,
            'Mean Return': mean,
            'Standard Deviation': std,
            'Variance': var,
            'Skewness': skew,
            'Kurtosis': kurt,
            'Empirical VaR 95%': var_95,
            'Expected Shortfall 95%': es_95,
            'Empirical VaR 99%': var_99,
            'Expected Shortfall 99%': es_99
        }

    return stats_dict