import numpy as np
from scipy.stats import norm

def calculate_greeks(S, K, T, r, sigma, option_type='call'):
    """
    Calculates the Greeks (Delta, Gamma, Vega, Theta, Rho) for European options
    using the Black-Scholes model.
    
    Parameters:
        S: float - Current stock price
        K: float - Strike price
        T: float - Time to maturity (in years)
        r: float - Risk-free interest rate
        sigma: float - Volatility (standard deviation)
        option_type: str - 'call' or 'put'
        
    Returns:
        dict - Greek values
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == 'call':
        delta = norm.cdf(d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                 - r * K * np.exp(-r * T) * norm.cdf(d2))
        rho = K * T * np.exp(-r * T) * norm.cdf(d2)
    else:
        delta = -norm.cdf(-d1)
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                 + r * K * np.exp(-r * T) * norm.cdf(-d2))
        rho = -K * T * np.exp(-r * T) * norm.cdf(-d2)

    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    vega = S * norm.pdf(d1) * np.sqrt(T)

    return {
        'Delta': round(delta, 4),
        'Gamma': round(gamma, 4),
        'Vega': round(vega / 100, 4),   # per 1% change
        'Theta': round(theta / 365, 4), # per day
        'Rho': round(rho / 100, 4)      # per 1% change
    }
