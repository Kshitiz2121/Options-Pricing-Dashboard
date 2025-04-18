import streamlit as st
from pricing_models import black_scholes, binomial_tree
from greeks_calculator import calculate_greeks
from implied_volatility import implied_volatility

st.title("📈 Options Pricing Dashboard")

option_type = st.selectbox("Option Type", ['call', 'put'])
model = st.radio("Pricing Model", ['Black-Scholes', 'Binomial Tree'])

S = st.number_input("Current Stock Price (S)", value=100.0)
K = st.number_input("Strike Price (K)", value=100.0)
T = st.number_input("Time to Maturity (T in years)", value=1.0)
r = st.number_input("Risk-Free Rate (r)", value=0.05)
sigma = st.number_input("Volatility (σ)", value=0.2)
steps = st.slider("Binomial Tree Steps", 10, 500, 100)

if st.button("Calculate Price"):
    if model == 'Black-Scholes':
        price = black_scholes(S, K, T, r, sigma, option_type)
    else:
        price = binomial_tree(S, K, T, r, sigma, steps, option_type)
    
    st.success(f"Option Price: {price:.2f}")
    
    greeks = calculate_greeks(S, K, T, r, sigma, option_type)
    st.subheader("Greeks")
    st.write(greeks)

if st.button("Calculate Implied Volatility"):
    option_market_price = st.number_input("Market Option Price", value=10.0)
    iv = implied_volatility(option_market_price, S, K, T, r, option_type)
    st.info(f"Implied Volatility: {iv:.2%}")
