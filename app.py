import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

# -----------------------------
# Load trained ML model
# -----------------------------
with open("fuel_price_model.pkl", "rb") as f:
    model = pickle.load(f)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("⛽ Fuel Price Optimization App")
st.write("Recommend optimal retail fuel price to maximize profit")

# User inputs
date = st.date_input("Date")

price = st.number_input("Yesterday's company price", value=95.0)
cost = st.number_input("Today's cost per liter", value=85.0)

comp1 = st.number_input("Competitor 1 price", value=95.0)
comp2 = st.number_input("Competitor 2 price", value=95.5)
comp3 = st.number_input("Competitor 3 price", value=96.0)

# -----------------------------
# Helper function: Recommend price
# -----------------------------
def recommend_price():

    avg_comp = np.mean([comp1, comp2, comp3])

    candidate_prices = np.arange(price-3, price+3, 0.1)

    best_price = None
    best_profit = -1
    best_volume = None

    for p in candidate_prices:

        # business rules
        if p < cost:
            continue
        if abs(p - price) > 2:
            continue
        if p > avg_comp + 2:
            continue

        # feature vector same as training
        row = pd.DataFrame([{
            "price": p,
            "cost": cost,
            "avg_comp_price": avg_comp,
            "price_comp_diff": p - avg_comp,
            "margin": p - cost,
            "lag_volume": 14000,     # fallback value if not stored
            "lag_price": price,
            "ma7_volume": 14000
        }])

        vol = model.predict(row)[0]
        profit = (p - cost) * vol

        if profit > best_profit:
            best_profit = profit
            best_price = p
            best_volume = vol

    return best_price, best_volume, best_profit


# -----------------------------
# Button action
# -----------------------------
if st.button("Recommend Price"):
    price_out, volume_out, profit_out = recommend_price()

    st.success(f"Recommended Retail Price: ₹{round(price_out,2)}")
    st.info(f"Expected Demand Volume: {int(volume_out)} liters")
    st.warning(f"Expected Profit: ₹{round(profit_out,2)}")
