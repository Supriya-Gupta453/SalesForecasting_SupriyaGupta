import streamlit as st

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Sales Forecasting Dashboard")

st.markdown("""
## Welcome

This dashboard presents the results of a complete Sales Forecasting and Business Analytics project.

### Features

- 📊 Sales Overview Dashboard
- 📈 Forecast Explorer
- 🚨 Anomaly Report
- 📦 Product Demand Segments

Use the **sidebar** on the left to navigate between pages.
""")

st.success("Project completed using Python, Streamlit, Scikit-Learn, Statsmodels, Prophet and XGBoost.")