import streamlit as st
import pandas as pd

st.set_page_config(page_title="Anomaly Report", page_icon="🚨")

st.title("🚨 Anomaly Report")

st.write("This page displays the anomalies detected using Isolation Forest.")

anomalies = pd.DataFrame({
    "Order Date": [
        "2015-01-04",
        "2015-02-08",
        "2015-02-22",
        "2015-03-22",
        "2015-07-19",
        "2015-09-13",
        "2016-01-24",
        "2017-12-17",
        "2018-11-04",
        "2018-11-18",
        "2018-12-02"
    ],
    "Sales": [
        304.508,
        968.534,
        224.912,
        37703.665,
        1387.686,
        29959.137,
        358.522,
        25449.800,
        29017.467,
        30572.447,
        35998.900
    ]
})

st.dataframe(anomalies, use_container_width=True)

st.markdown("""
### Business Interpretation

- Very low sales weeks may indicate holidays or reduced demand.
- Very high sales weeks may correspond to promotions or festive seasons.
- Isolation Forest detected **11 anomalous weeks**.
""")