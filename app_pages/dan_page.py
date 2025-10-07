import streamlit as st
import plotly.express as px
import pandas as pd
import os

def dan_page():
    # Load dataset with validation
    csv_path = 'Data/KaggleCarArchive/CarPrice_Working.csv'
    if not os.path.exists(csv_path):
        st.error(f"CSV file not found at: {csv_path}")
        return

    df_CarPriceCSV = pd.read_csv(csv_path)

    # Inject count column for aggregation
    df_CarPriceCSV['count'] = 1

    # Title
    st.title("🚗 Car Brand Explorer")

    # Sidebar: brand selection
    st.sidebar.header("🔍 Select a Car Brand")

    # Aggregate brand-model counts
    brand_model_data = df_CarPriceCSV.groupby(['carBrand', 'carModel'], as_index=False)['count'].sum()

    # Aggregate brand-only counts
    brand_data = brand_model_data.groupby('carBrand', as_index=False)['count'].sum().sort_values('carBrand')

    # Brand selector
    selected_brand = st.sidebar.selectbox("Choose a brand:", brand_data['carBrand'])

    # Main: Brand pie chart
    st.subheader("Car Brands Overview")
    brand_fig = px.pie(brand_data, names='carBrand', values='count', title="Car Brands")
    st.plotly_chart(brand_fig, use_container_width=True)

    # Main: Model pie chart
    st.subheader(f"{selected_brand} Models Breakdown")

    # Filter and aggregate model data
    model_data = (
        df_CarPriceCSV[df_CarPriceCSV['carBrand'] == selected_brand]
        .groupby('carModel', as_index=False)['count'].sum()
    )

    if model_data.empty:
        st.warning(f"No models found for brand: {selected_brand}")
    else:
        model_fig = px.pie(model_data, names='carModel', values='count', title=f"{selected_brand} Models")
        st.plotly_chart(model_fig, use_container_width=True)