import streamlit as st
import plotly.express as px
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Output, Input

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")
data["DateTime"] = pd.to_datetime(data["DateTime"], format="%Y-%m-%d")

# Sidebar
st.sidebar.title("Precious Metal Prices 2018-2021")

metal = st.sidebar.selectbox("Select Metal", data.columns[1:], index=1)

date_range = st.sidebar.date_input(
    "Select Date Range",
    [data["DateTime"].min().date(), data["DateTime"].max().date()]
)

filtered_data = data.loc[
    (data["DateTime"] >= date_range[0]) & (data["DateTime"] <= date_range[1])
]

# Plot
fig = px.line(
    filtered_data,
    title=f"Precious Metal Prices 2018-2021 ({metal})",
    x="DateTime",
    y=metal,
    color_discrete_map={
        "Platinum": "#E5E4E2",
        "Gold": "gold",
        "Silver": "silver",
        "Palladium": "#CED0DD",
        "Rhodium": "#E2E7E1",
        "Iridium": "#3D3C3A",
        "Ruthenium": "#C9CBC8"
    }
)

fig.update_layout(
    template="plotly_dark",
    xaxis_title="Date",
    yaxis_title="Price (USD/oz)",
    font=dict(
        family="Verdana, sans-serif",
        size=18,
        color="white"
    ),
)

# Display the plot
st.plotly_chart(fig)
