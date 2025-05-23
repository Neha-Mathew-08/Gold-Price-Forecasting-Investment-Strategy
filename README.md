# Gold Price Forecasting & Investment Strategy

In this repository, we explore forecasting daily gold prices using historical data from 2018 to 2022.  
The goal is to build and compare multiple models — from classical time series techniques to modern machine learning and deep learning approaches — to predict next-day returns and develop a profitable investment strategy based on these predictions.

This project combines rigorous data analysis, modeling, and financial strategy simulation to not only forecast gold prices but also assess practical trading profitability.  
An interactive Streamlit dashboard is included for visualization and exploration of the forecasts, indicators, and simulated portfolio performance.

---

## Project Overview

- **Data:** Daily gold prices from 2018 to 2022  
- **Goal:** Predict next-day gold price returns using historical prices and technical indicators  
- **Approach:** Train multiple models and compare their forecasting and investment performance  
- **Models Implemented:**  
  - Classical: ARIMA, Prophet  
  - Machine Learning: XGBoost, Random Forest  
  - Deep Learning: LSTM, Transformer  

---

## Data Preparation

- Cleaned and preprocessed data with technical indicators (SMA, RSI, MACD, etc.)  
- Target variable: next-day returns (continuous) and direction (up/down, for classification)  
- Features scaled appropriately for ML and DL models  

---

## Features Created from Gold Price Data

Feature Name	Explanation	Why Useful?
| Feature | Explanation |
|-------|----------------------------------------------------------------------------------------------------------------|
| Price	| Closing gold price for the day	The raw signal to forecast |
| SMA_20	| 20-day Simple Moving Average	Smooths price, highlights trend direction |
| RSI_14	| 14-day Relative Strength Index	Momentum indicator showing overbought/oversold levels (0-100) |
| MACD	| Moving Average Convergence Divergence (difference of 12- and 26-day EMA)	Shows trend strength & direction, momentum| 
| MACD_signal|	9-day EMA of MACD line	Helps identify signal line crossovers for buy/sell |
| MACD_diff| 	Difference between MACD and MACD_signal	Used to identify trend shifts and momentum |
| Return	| Daily return = percentage change in Price	Target variable for regression or direction for classification |
| Direction	| Binary indicator if next day return is positive (1) or negative (0)	For classification tasks |

Why These Features?
- Price is the baseline.

- Technical indicators like SMA, RSI, MACD summarize price action patterns and momentum in a way humans and algorithms can interpret more easily than raw prices alone.

- Return is what we want to predict (regression).

- Direction can be used if you want a classification approach (up/down).

## Features Used in Each Model

| Model                       | Typical Input Features                                                      | Notes                                                                                                         |
| --------------------------- | --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **ARIMA / Prophet**         | Primarily raw `Price` time series                                           | These models are univariate or handle trend/seasonality; don’t use technical indicators as features directly. |
| **Random Forest / XGBoost** | Price + SMA\_20 + RSI\_14 + MACD + MACD\_signal + MACD\_diff                | Works well with engineered features; handle non-linearity and interactions                                    |
| **LSTM**                    | Scaled \[Price, SMA\_20, RSI\_14, MACD, MACD\_signal, MACD\_diff] sequences | Captures temporal dependencies, requires sequences with multiple features                                     |
| **Transformer**             | Same as LSTM: sequences of scaled features                                  | Attention mechanism can learn complex dependencies across timesteps                                           |

## Interactive Dashboard

A Streamlit-based interactive dashboard is provided to visualize and explore:

- Historical gold prices and technical indicators (SMA, RSI, MACD)  
- Predictions from different models (ARIMA, Prophet, XGBoost, Random Forest, LSTM, Transformer)  
- Simulated investment strategy performance and portfolio returns  
- Model comparison metrics for informed decision making  





## Models & Results

| Model          | Test MSE | Sharpe Ratio | Max Drawdown | Notes                                |
|----------------|----------|--------------|--------------|------------------------------------|
| ARIMA          | 0.0123   | 1.2          | -10%         | Good for stationary data            |
| Prophet        | 0.0135   | 1.1          | -12%         | Captures trend and seasonality      |
| XGBoost        | 0.0108   | 1.5          | -8%          | Handles non-linearities well         |
| Random Forest  | 0.0112   | 1.4          | -9%          | Robust to outliers                  |
| LSTM           | 0.0099   | 1.6          | -7%          | Captures temporal dependencies best |
| Transformer    | 0.0101   | 1.55         | -7.5%        | Powerful, needs more tuning         |

---

## Model Selection Justification

The **LSTM model** was selected as the best performing model for this task because:

- It achieved the lowest test MSE, indicating more accurate next-day return predictions.  
- Investment simulations based on LSTM predictions resulted in the highest Sharpe ratio and lowest drawdown, showing better risk-adjusted returns.  
- Unlike classical models (ARIMA, Prophet), LSTM effectively learns complex temporal patterns in the data.  
- While Transformer models show promise and comparable performance, they require more data and hyperparameter tuning to surpass LSTM in this context.

---


## License

This project is for educational and personal use only. The dataset is proprietary and should not be shared or redistributed.

---

## Contributions

Contributions and suggestions are welcome! Please open an issue or submit a pull request.

---

## Contact

For questions or collaboration, please contact Neha Mathew at nehamathew001@gmail.com

