import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return price


def binomial_tree(S, K, T, r, sigma, steps, option_type='call'):
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    prices = np.zeros((steps + 1, steps + 1))
    for i in range(steps + 1):
        prices[steps, i] = max(0, (S * (u ** i) * (d ** (steps - i)) - K) if option_type == 'call' else (K - S * (u ** i) * (d ** (steps - i))))

    for j in range(steps - 1, -1, -1):
        for i in range(j + 1):
            prices[j, i] = np.exp(-r * dt) * (p * prices[j+1, i+1] + (1 - p) * prices[j+1, i])

    return prices[0, 0]