# 🎈 Blank app template

A simple Streamlit app template for you to modify!

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://blank-app-template.streamlit.app/)

### How to run it on your own machine
import streamlit as st
import pandas as pd
import numpy as np

st.title("Using Chat on Streamlit")
st.write("I am using Streamlit to show a chart")

df_sales = pd.read_csv("./sample-sales-data/sales_data_sample.csv", encoding="iso-8859-1")
st.write(df_sales)

# Get unique product lines
product_lines = df_sales["PRODUCTLINE"].unique()

# Create a DataFrame with ORDERDATE as index and product lines as columns
df_productline_sales = df_sales.pivot_table(values='QUANTITYORDERED', index='ORDERDATE', columns='PRODUCTLINE', fill_value=0)

# Print the DataFrame
print(df_productline_sales)

# Print the DataFrame
st.write(df_productline_sales)

#
# Area Chart
#
st.title("Area Chart")
st.area_chart(df_productline_sales)
st.markdown("---")

# z
1. Install the requirements

   ```
   $ pip install -r requirements.txt
   ```

2. Run the app

   ```
   $ streamlit run streamlit_app.py
   ```
