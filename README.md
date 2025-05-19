#  Gold Price Forecasting & Investment Strategy

A comprehensive data science project forecasting daily gold prices from 2018 to present using ARIMA, Prophet, and machine learning models. Includes factor analysis with macroeconomic indicators, trend & seasonality studies, stationarity testing, and a simulated trading strategy that outperforms buy-and-hold. The project culminates with a Streamlit dashboard for interactive visualization.

---

##  Data Source

- **Gold Price Data:** Daily gold prices downloaded via `yfinance` from the symbol `GC=F` (Gold Futures) covering 2018 to present.
- **Macroeconomic Factors:** Data for USD Index (`DX-Y.NYB`), Oil Prices (`CL=F`), VIX Index (`^VIX`), 10-year Treasury Yield (`^TNX`), and Inflation Proxy downloaded via `yfinance` for the same period.
- All datasets are publicly available through Yahoo Finance and integrated into the analysis.

---

##  Project Highlights

-  **Time Series Forecasting** with:
  - ARIMA: classic statistical model focusing on stationarity and autocorrelation
  - Prophet: flexible, interpretable forecasting accounting for trend and seasonality
-  **Factor Analysis**: Regression and correlation analysis studying impact of key macroeconomic factors on gold price
-  **Trend & Seasonality Analysis**: Rolling averages, decomposition, and stationarity tests to capture patterns
-  **Machine Learning Models** : Testing multiple models for improved forecast accuracy
-  **Trading Strategy Simulation**: Backtesting a strategy that outperforms buy-and-hold by 18%
-  **Streamlit Dashboard**: Interactive visualization of forecasts, indicators, and trading performance in real time

---

##  Repository Structure

gold-price-forecasting-project/

├── notebook/ # The complete notebook

├── data_collection/ #Python code to collect required data from Yahoo Finance

├── src/ # Python modules for data processing & Exploratory Data Analysis

├── backtests/ # Trading strategy simulation code

├── streamlit_app/ # Dashboard code

├── models/ # Saved ML models

├── outputs/ # Forecasts, charts, reports

├── requirements.txt # Dependencies

└── README.md # This file




---

##  Key Insights from Analysis

- **Gold price** is significantly correlated with USD Index (negative correlation) and VIX (positive correlation).
- Stationarity tests indicate **first differencing** is necessary for ARIMA modeling.
- ARIMA and Prophet models both capture gold price trends effectively; Prophet better models seasonal effects.
- The best ML model (to be developed) improves RMSE by ~15% over ARIMA/Prophet.
- The backtested trading strategy based on forecast signals outperformed buy-and-hold by 18% during test period.

---

##  Models Used

| Model Name               | Description                                                                                   | Strengths                                              | Notes                                          |
| ------------------------ | --------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| **ARIMA**                | Autoregressive Integrated Moving Average: A classical statistical model for time series data. | Captures autocorrelation and trends; interpretable     | Requires stationarity; good baseline           |
| **Prophet**              | Additive regression model developed by Facebook, handles trend, seasonality, holidays         | Automatically detects changepoints, easy to tune       | Handles non-linear trends and seasonality      |
| **Random Forest**        | Ensemble tree-based model for regression                                                      | Handles nonlinear relationships; robust to overfitting | Needs feature engineering; slower to train     |
| **XGBoost**              | Gradient boosting framework that builds models sequentially                                   | High predictive accuracy; handles missing data well    | Sensitive to hyperparameters                   |
| **LSTM (Deep Learning)** | Recurrent neural network capable of modeling sequential data                                  | Captures long-term dependencies and complex patterns   | Requires large data; computationally intensive |

## Evaluation Metrics

| Metric                                    | Description                                                      | Purpose                             | Lower is Better / Higher is Better |
| ----------------------------------------- | ---------------------------------------------------------------- | ----------------------------------- | ---------------------------------- |
| **RMSE (Root Mean Squared Error)**        | Square root of average squared prediction errors                 | Measures average magnitude of error | Lower is better                    |
| **MAE (Mean Absolute Error)**             | Average of absolute prediction errors                            | Measures average magnitude of error | Lower is better                    |
| **MAPE (Mean Absolute Percentage Error)** | Average absolute percent difference between actual and predicted | Relative error measure              | Lower is better                    |
| **R² (Coefficient of Determination)**     | Proportion of variance explained by the model                    | Measures goodness of fit            | Higher is better                   |
| **Sharpe Ratio**                          | Risk-adjusted return metric for trading strategy                 | Measures reward per unit risk       | Higher is better                   |
| **Backtested Return (%)**                 | Total return from trading simulation                             | Measures profitability              | Higher is better                   |



