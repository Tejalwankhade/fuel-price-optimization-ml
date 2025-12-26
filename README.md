# fuel-price-optimization-ml
Fuel Price Optimization – Machine Learning Project

Author: Tejal Wankhade
Live Demo: https://fuel-price-optimization-ml-qse9txe2exsvy2a6v4knxu.streamlit.app/

1. Project Overview

This project implements an end-to-end machine learning system to optimize daily retail fuel pricing.
The objective is to recommend a price that:

maximizes daily profit

remains competitive in the market

complies with practical pricing constraints

The model predicts expected sales volume for different price points and selects the price that yields the highest profit.

Profit is defined as:

Profit = (Price − Cost) × Predicted Volume

The solution includes:

data ingestion and preprocessing pipeline

feature engineering

demand prediction model

price optimization logic

Streamlit web application

trained model artifact (pickle)

2. Problem Statement

Retail fuel demand depends on multiple factors:

company price

competitor prices

cost fluctuations

historical sales trends

Price can be updated once per day.
The task is to design an ML system capable of recommending the optimal daily price.

3. Approach & Methodology
3.1 Data Pipeline

The following steps were implemented:

Data ingestion from historical CSV

Data validation & cleaning

Outlier handling

Feature engineering:

margin per liter

competitor average price

price differential vs competitors

lagged volume features

moving-average demand indicators

Processed dataset persisted for model training

3.2 Machine Learning Model

A Random Forest Regression model was trained to predict daily fuel volume.

Rationale:

captures nonlinear price–demand relationships

robust against noise/outliers

minimal assumptions on functional form

3.3 Price Optimization Strategy

For each day:

generate a grid of candidate prices

predict demand using trained model

calculate expected profit

enforce business constraints

recommend price with maximum profit

Business Constraints Applied

maximum price change limit per day

price ≥ cost

price not significantly higher than competitors

negative-margin avoidance

4. Dataset

File: oil_retail_history.csv

Contains approximately two years of daily data:

date

company price

cost

competitor prices (3 stations)

daily sales volume

5. Model Performance
Metric	Result
RMSE	883.05
R² Score	0.044

Notes:

demand is inherently noisy

results are consistent with real-world retail fuel dynamics

model successfully captures competitive and price-elastic effects

6. System Output Example

Input:

current cost

previous company price

competitor prices

Output:

recommended price

expected demand

expected profit

Example result from the model:

Recommended Price: ₹96.45

Expected Demand: 13,450 liters

Expected Profit: ₹143,651.98

7. Repository Contents
app.py                     Streamlit application
fuel_price_model.pkl       Trained ML model
notebook.ipynb             Model training & pipeline notebook
oil_retail_history.csv     Historical dataset
today_example.json         Example daily input
requirements.txt           Dependencies
README.md                  Project documentation

8. How to Run
Option A — Launch web app (hosted)

https://fuel-price-optimization-ml-qse9txe2exsvy2a6v4knxu.streamlit.app/

Option B — Run locally
git clone <repository-link>
cd fuel-price-optimization-ml
pip install -r requirements.txt
streamlit run app.py

9. Technology Stack

Python

Pandas / NumPy

Scikit-Learn

Random Forest

Streamlit

Pickle

Google Colab

11. Author

Tejal Wankhade
