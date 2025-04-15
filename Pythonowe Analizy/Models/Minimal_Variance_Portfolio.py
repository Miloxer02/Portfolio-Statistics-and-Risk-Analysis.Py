import numpy as np
import pandas as pd
from scipy.optimize import minimize

def calculate_min_variance_portfolio(asset_data):
    """
    Calculate Minimum Variance Portfolio using variance-covariance method based on:
    - Log returns for each asset (computed if not present)
    - Covariance matrix derived from σ_i * σ_j * ρ_ij
    """

    print("\n[3]✅ Calculating Minimum Variance Portfolio (Variance-Covariance Method)")

    # Ensure each asset has 'Log_Return' computed
    for name, df in asset_data.items():
        if 'Log_Return' not in df.columns:
            df['Log_Return'] = np.log(df['Zamkniecie'] / df['Zamkniecie'].shift(1))
            df.dropna(inplace=True)
            asset_data[name] = df

    # Create aligned DataFrame of log returns
    log_returns = pd.DataFrame({
        name: df['Log_Return'] for name, df in asset_data.items()
    })
    log_returns.dropna(inplace=True)

    # Mean and std of log returns
    means = log_returns.mean()
    stds = log_returns.std()
    corr_matrix = log_returns.corr()

    # Build covariance matrix: σ_i * σ_j * ρ_ij
    cov_matrix = stds.values.reshape(-1, 1) * stds.values.reshape(1, -1) * corr_matrix.values

    # Define the objective function (minimize portfolio variance)
    def portfolio_variance(weights):
        return np.dot(weights.T, np.dot(cov_matrix, weights))

    num_assets = len(log_returns.columns)
    init_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1) for _ in range(num_assets)]
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

    result = minimize(portfolio_variance, init_weights, method='SLSQP', bounds=bounds, constraints=constraints)

    if not result.success:
        raise ValueError("❌ Optimization failed: " + result.message)

    weights = pd.Series(result.x, index=log_returns.columns)

    # Portfolio stats
    portfolio_mean = np.dot(weights, means)
    portfolio_std = np.sqrt(portfolio_variance(weights))

    return weights, portfolio_mean, portfolio_std
