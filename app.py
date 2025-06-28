import streamlit as st
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# 🎉 App config
st.set_page_config(page_title="Energy Consumption Forecast", layout="centered")
st.title("⚡ Energy Consumption Forecast")
st.markdown("Upload your energy consumption data (CSV with **Date** and **Consumption** columns).")

# 📥 File uploader
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file:
    try:
        # ✅ Load CSV
        df = pd.read_csv(uploaded_file)

        # ✅ Ensure Date is datetime
        df['Date'] = pd.to_datetime(df['Date'])

        st.write("✅ Uploaded Data Preview:")
        st.dataframe(df.head())

        # ✅ Prepare for Prophet
        df.rename(columns={"Date": "ds", "Consumption": "y"}, inplace=True)

        # ✅ Train Prophet model
        m = Prophet()
        m.fit(df)

        # ✅ Forecast future
        future = m.make_future_dataframe(periods=30)
        forecast = m.predict(future)

        # ✅ Show Forecast Table
        st.subheader("🔮 Forecast Data")
        st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

        # ✅ Plot forecast
        fig1 = m.plot(forecast)
        plt.xlabel("Date")
        plt.ylabel("Energy Consumption")
        plt.title("Energy Consumption Forecast")
        plt.xticks(rotation=45)
        st.pyplot(fig1)

        # ✅ Plot forecast components
        st.subheader("📈 Trend & Seasonality")
        fig2 = m.plot_components(forecast)
        st.pyplot(fig2)

    except Exception as e:
        st.error(f"❌ Error: {e}")

else:
    st.info("📂 Please upload a CSV file to start.")
