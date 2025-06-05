import streamlit as st
import pandas as pd
import pickle
import joblib
import matplotlib.pyplot as plt
from io import BytesIO

# Title
st.title("Gold Price Forecast Dashboard")

# --- Load Model ---
@st.cache_resource
def load_model():
    model = joblib.load("models/prophet_model.pkl")
    return model

model = load_model()

# --- Upload Data or Load Default ---
uploaded_file = st.file_uploader("Upload your gold price data CSV (with 'ds' and 'y' columns)", type=["csv"])

@st.cache_data
def load_default_data():
    return pd.read_csv("Preprocessed_Data_with_only price.csv")

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("Uploaded data loaded successfully!")
    except Exception as e:
        st.error(f"Error loading uploaded file: {e}")
        df = load_default_data()
else:
    df = load_default_data()
    
    
# Normalize column names for Prophet
if 'Date' in df.columns:
    df.rename(columns={'Date': 'ds'}, inplace=True)
elif 'date' in df.columns:
    df.rename(columns={'date': 'ds'}, inplace=True)

if 'Price' in df.columns:
    df.rename(columns={'Price': 'y'}, inplace=True)
elif 'price' in df.columns:
    df.rename(columns={'price': 'y'}, inplace=True)

# Check if 'ds' and 'y' exist now
if 'ds' not in df.columns or 'y' not in df.columns:
    st.error("Uploaded data must contain 'ds' (date) and 'y' (value) columns.")
    st.stop()


st.subheader("Historical Gold Prices")
st.line_chart(df.set_index('ds')['y'])

# --- User Input: Forecast Horizon ---
forecast_days = st.slider("Select forecast horizon (days ahead):", min_value=7, max_value=90, value=30)

# --- Forecast ---
future = model.make_future_dataframe(periods=forecast_days)
forecast = model.predict(future)

st.subheader("Forecasted Gold Prices")
fig1 = model.plot(forecast)
st.pyplot(fig1)

# Forecast Data Download
csv = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv(index=False).encode()
st.download_button(
    label="Download Forecast Data as CSV",
    data=csv,
    file_name='gold_forecast.csv',
    mime='text/csv',
)

# --- Forecast Components ---
st.subheader("Forecast Components")
fig2 = model.plot_components(forecast)
st.pyplot(fig2)

# --- Display Model Metrics (Optional) ---
st.subheader("Model Performance Metrics")
# You can hardcode or compute these if you have the data
# Example hardcoded metrics from your data:
mse = 0.0000055
sharpe_ratio = 1.7496
max_drawdown = -0.001132  # expressed as decimal

st.markdown(f"""
- **Test MSE:** {mse:.8f}  
- **Sharpe Ratio:** {sharpe_ratio:.4f}  
- **Max Drawdown:** {max_drawdown * 100:.4f}%
""")

# --- Footer ---
st.markdown("---")
st.markdown("Dashboard built with [Streamlit](https://streamlit.io/) and Facebook's [Prophet](https://facebook.github.io/prophet/) model.")
