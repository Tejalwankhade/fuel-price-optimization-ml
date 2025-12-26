# fuel-price-optimization-ml
⛽ Fuel Price Optimization – Machine Learning Project

👤 Author: Tejal Wankhade
🌐 Live Demo: https://fuel-price-optimization-ml-qse9txe2exsvy2a6v4knxu.streamlit.app/

📌 1. Project Overview

This repository contains an end-to-end Machine Learning solution for optimizing daily retail fuel price.
The goal is to recommend a price that:

 maximizes daily profit
 remains competitively aligned
 respects business pricing constraints

The solution predicts expected sales volume at different price levels and selects the price that provides highest profit.

Profit Formula:
Profit = (Price − Cost) × Predicted Volume

🎯 2. Problem Statement

Retail fuel demand depends on:

✔️ company price
✔️ competitor price movements
✔️ daily cost changes
✔️ historical demand trends

Since price can only be changed once per day, a data-driven strategy is required to recommend the optimal daily price.

 3. Approach & Methodology
 3.1 Data Pipeline

The following pipeline was implemented:

 Data ingestion from historical CSV
 Data cleaning & validation
 Outlier detection

🏗 Feature engineering including:

margin per liter
competitor average price
price differential
lag features (previous volume, price)
moving-average indicators
Processed dataset was persisted for reproducible training.

🤖 3.2 Machine Learning Model

Algorithm used: Random Forest Regression
Target variable: daily fuel volume

Why Random Forest?
handles nonlinear relationships
robust to noise/outliers
performs well with tabular business data

💹 3.3 Price Optimization Strategy

Steps performed per day:

generate a grid of possible prices
predict demand for each price
compute expected profit
apply business constraints
return price with maximum profit

Business Constraints Applied:

maximum price change per day
price ≥ cost (no negative margin)
competitive alignment (price not far above competitors)
eliminate economically infeasible price points

🗂️ 4. Dataset Description

File: oil_retail_history.csv

Includes ~2 years of daily records:

date
company retail price
cost per liter
competitor 1/2/3 prices
sales volume (liters)

📊 5. Model Performance
Metric	Result
RMSE	883.05
R² Score	0.044

📌 Interpretation:

retail fuel demand is naturally noisy
despite noise, the model captures:
price sensitivity
competitor influence
seasonal demand patterns

🧮 6. Example System Output

Input includes:

today’s cost
yesterday’s price
competitor prices

Model Output:

✅ Recommended Price: ₹96.45

🛢 Expected Demand: 13,450 liters

💰 Expected Profit: ₹143,651.98

📦 7. Repository Contents
app.py                     → Streamlit web application
fuel_price_model.pkl       → Trained ML model (pickle)
notebook.ipynb             → Training & pipeline notebook
oil_retail_history.csv     → Historical dataset
today_example.json         → Sample input file
requirements.txt           → Project dependencies
README.md                  → Project documentation

🚀 8. How to Run
▶️ Option A — Hosted Web App

👉 https://fuel-price-optimization-ml-qse9txe2exsvy2a6v4knxu.streamlit.app/

💻 Option B — Run Locally
git clone <repository-link>
cd fuel-price-optimization-ml
pip install -r requirements.txt
streamlit run app.py

🛠️ 9. Technology Stack

Python
Pandas / NumPy
Scikit-Learn
Random Forest
Streamlit
Pickle
Google Colab

Author

Tejal Wankhade


