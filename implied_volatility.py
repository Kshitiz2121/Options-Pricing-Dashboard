from scipy.optimize import brentq
from pricing_models import black_scholes

def implied_volatility(option_price, S, K, T, r, option_type='call'):
    func = lambda sigma: black_scholes(S, K, T, r, sigma, option_type) - option_price
    return brentq(func, 1e-5, 5)
