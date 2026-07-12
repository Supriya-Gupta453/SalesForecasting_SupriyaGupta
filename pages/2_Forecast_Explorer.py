import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Forecast Explorer")

st.markdown("### Explore 3-Month Sales Forecast")

# ----------------------------
# Select Forecast Type
# ----------------------------

forecast_type = st.selectbox(
    "Forecast Type",
    ["Category", "Region"]
)

if forecast_type == "Category":

    option = st.selectbox(
        "Select Category",
        [
            "Furniture",
            "Technology",
            "Office Supplies"
        ]
    )

    forecasts = {
        "Furniture":[23847.38,33749.40,34796.55],
        "Technology":[23906.68,26703.65,22540.94],
        "Office Supplies":[26368.79,26271.98,26271.98]
    }

else:

    option = st.selectbox(
        "Select Region",
        [
            "West",
            "East"
        ]
    )

    forecasts = {
        "West":[17494.54,18152.15,29018.54],
        "East":[21521.73,22350.08,22623.29]
    }

# ----------------------------
# Forecast Horizon
# ----------------------------

months = st.slider(
    "Forecast Horizon (Months)",
    1,
    3,
    3
)

forecast = forecasts[option][:months]

forecast_months = [
    "Month 1",
    "Month 2",
    "Month 3"
][:months]

forecast_df = pd.DataFrame({

    "Forecast Month":forecast_months,
    "Predicted Sales":forecast

})

st.subheader("Forecast Values")

st.dataframe(forecast_df)

# ----------------------------
# Forecast Plot
# ----------------------------

fig, ax = plt.subplots(figsize=(8,5))

ax.plot(
    forecast_months,
    forecast,
    marker="o",
    linewidth=2
)

ax.set_ylabel("Predicted Sales")

ax.set_title(option + " Forecast")

st.pyplot(fig)

# ----------------------------
# Model Performance
# ----------------------------

st.subheader("Best Model Performance")

st.metric(
    "MAE",
    "14163.32"
)

st.metric(
    "RMSE",
    "19267.49"
)

st.success(
    "Recommended Model : XGBoost Regressor"
)