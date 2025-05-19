# Gold Price Forecasting & Investment Strategy

This project focuses on building a **Gold Price Forecasting Model** using daily historical gold prices from **2018 to 2022**. The goal is to leverage machine learning and time series techniques to predict future gold prices and develop a simulated investment strategy based on these predictions to evaluate profitability and risk.

---

## Project Overview

This project consists of the following main components:

1. **Data Exploration & Cleaning**  
   - Load, clean, and preprocess gold price data to prepare it for analysis and modeling.  
   - Perform exploratory data analysis (EDA) including trend visualization and stationarity tests (e.g., Augmented Dickey-Fuller test).

2. **Baseline Time Series Modeling**  
   - Build a baseline forecasting model using classical methods such as **ARIMA** or **Prophet**.  
   - Evaluate model performance and generate initial forecasts.

3. **Advanced Machine Learning Modeling**  
   - Implement advanced forecasting models such as **LSTM** or **Transformer-based architectures** to capture complex temporal dependencies and improve prediction accuracy.

4. **Investment Strategy Simulation**  
   - Design a trading strategy based on model predictions.  
   - Backtest the strategy and compare its performance against a buy-and-hold benchmark.

5. **Interactive Dashboard**  
   - Develop a **Streamlit dashboard** for real-time visualization of price forecasts, trading signals, and investment performance.

---

## Data Source

The dataset used in this project contains daily historical prices of gold from **2018 to 2022**.  
**Note:** This dataset is **not for public use** and is provided solely for the purpose of this project.

- **Date:** The date of the gold price.  
- **Price:** The closing price of gold in USD.

---

## Usage

1. **Data Preprocessing and EDA**  
   Run `01_EDA_and_Cleaning.ipynb` to explore and clean the data, visualize trends, and perform statistical tests for stationarity.

2. **Model Training**  
   - Train the baseline forecasting model with `baseline_model.py` (using ARIMA or Prophet).  
   - Train the advanced forecasting model with `advanced_model.py` (using LSTM or Transformer architectures).

3. **Investment Strategy Simulation**  
   Use the model’s predictions to develop and backtest the trading strategy.

4. **Interactive Dashboard**  
   Launch the Streamlit app with `dashboard.py` to visualize predictions, simulated trades, and model performance interactively.

---

## Requirements

- Python 3.7+  
- Key libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `statsmodels`, `fbprophet`, `tensorflow` or `pytorch` (for LSTM/Transformer), `streamlit`

---

## License

This project and dataset are for educational purposes only and are **not intended for commercial use**.

---

## Contact

For any questions or feedback, please reach out at nehamathew001@gmail.com


