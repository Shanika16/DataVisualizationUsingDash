# import streamlit as st
# import plotly.express as px
# import pandas as pd

# # Read in the data
# data = pd.read_csv("precious_metals_prices_2018_2021.csv")

# # Create a plotly figure for use by st.plotly_chart()
# fig = px.line(
#     data,
#     title="Precious Metal Prices 2018-2021",
#     x="DateTime",
#     y=["Gold"],
#     color_discrete_map={"Gold": "gold"}
# )

# # Streamlit part
# st.title("Precious Metal Prices")

# # Header area
# #st.header("Gold Prices")
# st.write("The cost of precious metals between 2018 and 2021")

# # Menu area
# metal_filter = st.selectbox("Select Metal", data.columns[1:], index=0)

# # Filter data for the selected metal
# selected_data = data[["DateTime", metal_filter]]

# # Create a plotly figure for the selected metal
# selected_fig = px.line(selected_data, x="DateTime", y=metal_filter, title=f"{metal_filter} Prices 2018-2021")

# # Display the updated chart
# st.plotly_chart(selected_fig)



import streamlit as st
import plotly.express as px
import pandas as pd

# Read in the data
data = pd.read_csv("precious_metals_prices_2018_2021.csv")

# Let Pandas infer the datetime format
data["DateTime"] = pd.to_datetime(data["DateTime"], infer_datetime_format=True)

# Streamlit part
st.title("Precious Metal Prices 2018-2021")

# Header area
st.header("Precious Metal Prices")
st.write("The cost of precious metals between 2018 and 2021")

# Menu area
metal_filter = st.selectbox("Select Metal", data.columns[1:], index=0)
date_range = st.date_input("Select Date Range", [data["DateTime"].min(), data["DateTime"].max()])

# Convert the selected date range to pandas Timestamp
start_date = pd.Timestamp(date_range[0])
end_date = pd.Timestamp(date_range[1])

# Filter data based on selected metal and date range
filtered_data = data.loc[(data["DateTime"] >= start_date) & (data["DateTime"] <= end_date)]

# Create a plotly figure for the selected metal and date range
fig = px.line(
    filtered_data,
    title="Precious Metal Prices 2018-2021",
    x="DateTime",
    y=[metal_filter],
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

# Display the updated chart
st.plotly_chart(fig)
