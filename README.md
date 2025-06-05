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
| EMA_20	| 20-day Exponential Moving Average	To identify potential trend changes and entry/exit points for trades. |
| RSI_14	| 14-day Relative Strength Index	Momentum indicator showing overbought/oversold levels (0-100) |
| MACD	| Moving Average Convergence Divergence (difference of 12- and 26-day EMA)	Shows trend strength & direction, momentum| 
| MACD_signal|	9-day EMA of MACD line	Helps identify signal line crossovers for buy/sell |
| MACD_diff| 	Difference between MACD and MACD_signal	Used to identify trend shifts and momentum |
| Bollinger_High| When the daily price touches the Bollinger_High, it might be considered relatively expensive or overbought |
| Bollinger_Low | When the daily price touches the Bollinger_Low, it might be seen as relatively cheap or oversold |
| ATR_14 | 	 Average True Range (ATR) over 14 periods (typically days) is a measure of market volatility. ATR_14 quantifies the average magnitude of daily price bars, giving a more direct read on typical price movement. |
| Momentum_10 | 	Momentum_10 calculated from daily prices helps traders understand the strength and direction of price movements over the past two weeks (10 trading days), providing insights into whether a trend is accelerating, decelerating, or potentially reversing |
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
| **Random Forest / XGBoost** | Price + All other features; handle non-linearity and interactions                                    |
| **LSTM**                    | Scaled \[Price + All other features] sequences | Captures temporal dependencies, requires sequences with multiple features                                     |
| **Transformer**             | Same as LSTM: sequences of scaled features                                  | Attention mechanism can learn complex dependencies across timesteps                                           |

## Interactive Dashboard

**Gold Price Forecast Dashboard**: 

This interactive dashboard leverages a trained Prophet model to forecast gold prices, providing a user-friendly interface for exploring historical data and future predictions.

**Features**

* **View Historical Gold Prices**:
  Visualize past gold price trends through an intuitive line chart, helping you understand the market’s historical behavior.

* **Upload Your Own Data**:
  Easily upload your own CSV file containing gold prices (with required columns ds for dates and y for prices) to generate personalized forecasts.

* **Adjustable Forecast Horizon**:
  Select how many days into the future you want to forecast (from 7 up to 90 days) using a simple slider — see predictions tailored to your needs.

* **Interactive Forecast Visualization**:
  View forecasted gold prices plotted alongside historical data, including confidence intervals that indicate uncertainty ranges.

* **Download Forecast Data**:
  Export the forecasted results as a CSV file for further analysis or reporting.

* **Forecast Components Breakdown**:
  Understand the underlying factors influencing the forecast with detailed components plots, including trends and seasonality.

* **Model Performance Metrics**:
  Displays key metrics such as Test Mean Squared Error (MSE), Sharpe Ratio, and Max Drawdown to assess model accuracy and risk-adjusted returns.



## Models & Results

| Model          | Test MSE | Sharpe Ratio | Max Drawdown | Notes                                |
|----------------|----------|--------------|--------------|------------------------------------|
| ARIMA          | 42196.4554451664  | 0.75          | -20.06%         | Test MSE: 42,196. Sharpe Ratio: 0.75 indicates good risk-adjusted returns. Max Drawdown: -20.06% shows moderate price dips. Overall, the model suggests stable long-term growth of gold prices.|
| Prophet        | 0.0000055   | 1.7496         | -0.1132%         | Captures trend and seasonality      |
| XGBoost        | 	0.000058   | 0.3721          | -9.79%        | Handles non-linearities well         |
| Random Forest  | 0.000060   | 0.1877          | 0.0925         | Robust to outliers                  |
| LSTM           | 	0.000063  | -0.5490         | -0.1463          | Captures temporal dependencies best |
| Transformer    | 0.002020   | -0.5135        | -0.1463       | Powerful, needs more tuning         |

---

## Model Selection Justification

Among all models evaluated for gold price forecasting, **Prophet** outperformed with the **lowest Test MSE (0.0000055**), the **highest Sharpe Ratio (1.75)**, and the **smallest Max Drawdown (-0.11%)**, indicating both exceptional prediction accuracy and superior risk-adjusted returns. This suggests Prophet is the most reliable model for stable, long-term financial forecasting in this context.

Despite using only historical price data, the Prophet model significantly outperformed all others across key metrics. This highlights Prophet’s exceptional ability to model trend and seasonality effectively, even without engineered features — making it the most robust and reliable choice for stable, long-term gold price forecasting.

---


## License

This project is for educational and personal use only. The dataset is proprietary and should not be shared or redistributed.

---

## Contributions

Contributions and suggestions are welcome! Please open an issue or submit a pull request.

---

## Contact

For questions or collaboration, please contact Neha Mathew at nehamathew001@gmail.com

