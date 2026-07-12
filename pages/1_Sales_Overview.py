import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Overview Dashboard")

# Load Dataset
sales = pd.read_csv("train.csv")

# Convert Date
sales["Order Date"] = pd.to_datetime(
    sales["Order Date"],
    dayfirst=True
)

sales["Year"] = sales["Order Date"].dt.year
sales["Month"] = sales["Order Date"].dt.month

# -----------------------------
# Total Sales by Year
# -----------------------------

st.header("Total Sales by Year")

year_sales = sales.groupby("Year")["Sales"].sum()

fig, ax = plt.subplots(figsize=(8,5))

year_sales.plot(
    kind="bar",
    ax=ax
)

ax.set_ylabel("Sales")
ax.set_xlabel("Year")

st.pyplot(fig)

# -----------------------------
# Monthly Sales Trend
# -----------------------------

st.header("Monthly Sales Trend")

monthly = sales.groupby(
    pd.Grouper(
        key="Order Date",
        freq="ME"
    )
)["Sales"].sum()

fig2, ax2 = plt.subplots(figsize=(10,5))

monthly.plot(ax=ax2)

ax2.set_ylabel("Sales")

st.pyplot(fig2)

# -----------------------------
# Interactive Filters
# -----------------------------

st.header("Sales by Region and Category")

region = st.selectbox(
    "Select Region",
    sorted(sales["Region"].unique())
)

category = st.selectbox(
    "Select Category",
    sorted(sales["Category"].unique())
)

filtered = sales[
    (sales["Region"] == region)
    &
    (sales["Category"] == category)
]

st.subheader("Filtered Sales")

fig3, ax3 = plt.subplots(figsize=(8,4))

filtered.groupby("Order Date")["Sales"].sum().plot(
    ax=ax3,
    marker="o"
)

ax3.set_xlabel("Order Date")
ax3.set_ylabel("Sales")

st.pyplot(fig3)

st.subheader("Filtered Data")
st.dataframe(filtered)