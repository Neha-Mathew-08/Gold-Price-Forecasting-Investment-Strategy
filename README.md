Gold Price Forecasting & Investment Strategy
This project focuses on building a Gold Price Forecasting Model using daily historical gold prices from 2018 to 2022. The model will leverage machine learning and time series techniques to predict future gold prices. Additionally, we will develop a simulated investment strategy based on these price predictions to evaluate profitability and risk.

Project Overview
This project consists of the following main components:
1. Data Exploration & Cleaning: We first clean and preprocess the data, ensuring it’s ready for modeling and analysis.
2. Baseline Time Series Model: Using ARIMA or Prophet to establish a baseline for predicting future gold prices.
3. Advanced Machine Learning Model: Implementing an advanced model (LSTM or Transformer) for gold price forecasting.
4. Investment Strategy Simulation: Building a trading strategy based on predicted prices and backtesting it for profitability.
5. Interactive Dashboard: Developing a dashboard to visualize the predictions, trading strategy, and model performance.

Data Source
The dataset used in this project contains daily historical prices of gold from 2018 to 2022. Please note that this dataset is not for public use and is provided solely for the purposes of this project.
The data consists of:
Date: The date of the gold price.
Price: The closing price of gold (USD).

Usage
Data Preprocessing and EDA:
Run 01_EDA_and_Cleaning.ipynb to explore and clean the data. This step includes loading the dataset, visualizing the trends, and performing statistical tests (e.g., ADF test for stationarity).

Model Training:
Train the baseline model (baseline_model.py) using ARIMA or Prophet to predict future gold prices.
Implement the advanced model (advanced_model.py) using LSTM or Transformer-based architectures for a more sophisticated approach.
Simulate Investment Strategy:
Use the model’s predictions to develop and backtest a trading strategy.

Interactive Dashboard:
Run the Streamlit app (dashboard.py) to create an interactive interface for visualizing predictions, simulated trades, and model performance.

License
This project is for educational and personal use only. The dataset used in this project is not publicly available and should not be redistributed or shared without appropriate permissions.

Contributing
Contributions to improve the project are welcome. If you have suggestions or improvements, feel free to open an issue or submit a pull request.

Contact
If you have any questions, please contact Neha Mathew at nehamathew001@gmail.com 
