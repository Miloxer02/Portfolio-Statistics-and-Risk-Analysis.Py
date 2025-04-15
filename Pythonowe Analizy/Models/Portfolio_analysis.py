import numpy as np

def analyze_log_return_statistics(asset_data):
    print("\n[2] Descriptive Statistics – Logarithmic Returns:")

    for name, df in asset_data.items():
        print(f"\n📈 {name} – latest closing price:")
        print(df[['Date', 'Zamkniecie']].tail(1))

        # Calculate daily logarithmic returns
        df['Log_Return'] = np.log(df['Zamkniecie'] / df['Zamkniecie'].shift(1))
        df.dropna(inplace=True)

        # Calculate statistical measures
        mean = df['Log_Return'].mean()
        std = df['Log_Return'].std()
        var = df['Log_Return'].var()
        skew = df['Log_Return'].skew()
        kurt = df['Log_Return'].kurt()
        rolling_mean = df['Log_Return'].rolling(5).mean().iloc[-1]
        var_95 = np.percentile(df['Log_Return'], 5)
        es_95 = df[df['Log_Return'] <= var_95]['Log_Return'].mean()
        var_99 = np.percentile(df['Log_Return'], 1)
        es_99 = df[df['Log_Return'] <= var_99]['Log_Return'].mean()
        

        # Display results
        print(f"Mean Return: {mean:.4f}")
        print(f"Standard Deviation: {std:.4f}")
        print(f"Variance: {var:.4f}")
        print(f"Skewness: {skew:.4f}")
        print(f"Kurtosis: {kurt:.4f}")
        print(f"Rolling Mean (5 days): {rolling_mean:.4f}")
        print(f"Empirical VaR 95%: {var_95:.4f}")
        print(f"Expected Shortfall 95%: {es_95:.4f}")
        print(f"Empirical VaR 99%: {var_99:.4f}")
        print(f"Expected Shortfall 99%: {es_99:.4f}")

