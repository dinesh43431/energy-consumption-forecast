# ⚡ Energy Consumption Forecast App

This Streamlit app forecasts future energy consumption using Facebook Prophet.

## Features
- Upload your own CSV file with daily energy consumption data
- Visualize historical and forecasted consumption
- See trend and seasonality components

## Example CSV Format
```
Date,Consumption
2025-06-01,120
2025-06-02,130
...
```

## How to Run
1. Install requirements:
   ```
   pip install -r requirements.txt
   ```
2. Start the app:
   ```
   streamlit run app.py
   ```
3. Open the app in your browser and upload your data (or use `example_energy.csv`).

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Files
- `app.py` — Main Streamlit app
- `requirements.txt` — Python dependencies
- `example_energy.csv` — Example data file

---
Made with ❤️ using Streamlit and Prophet.
