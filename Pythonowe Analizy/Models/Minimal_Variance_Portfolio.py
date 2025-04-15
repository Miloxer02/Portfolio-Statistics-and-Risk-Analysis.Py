import numpy as np
import pandas as pd
from scipy.optimize import minimize

def calculate_min_variance_portfolio(asset_data):
    """
    Calculate Minimum Variance Portfolio using the variance-covariance method.

    Parameters:
    - asset_data (dict): Dictionary of DataFrames, each containing 'Log_Return'

    Returns:
    - pd.Series: Optimal weights per asset
    """
    print("\n[3]✅ Calculating Minimum Variance Portfolio (Var-Cov method)")

    # Create aligned DataFrame of log returns
    log_returns = pd.DataFrame({name: df['Log_Return'] for name, df in asset_data.items()})
    log_returns.dropna(inplace=True)

    # Covariance matrix of log returns
    cov_matrix = log_returns.cov()

    # Objective function: portfolio variance
    def portfolio_variance(weights):
        return np.dot(weights.T, np.dot(cov_matrix, weights))

    num_assets = len(log_returns.columns)
    init_weights = np.ones(num_assets) / num_assets
    bounds = [(0, 1) for _ in range(num_assets)]  # No short-selling
    constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}

    result = minimize(portfolio_variance, init_weights, bounds=bounds, constraints=constraints)

    if not result.success:
        raise ValueError("❌ Optimization failed: " + result.message)

    weights = pd.Series(result.x, index=log_returns.columns)

    return weights
