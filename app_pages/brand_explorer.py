import streamlit as st
import plotly.express as px
import pandas as pd
import os

def brand_explorer():
    # Load dataset from session state
    df_CarPriceCSV = st.session_state.df
    df_CarPriceCSV['count'] = 1

    st.title("🚗 Car Brand Explorer")

    # Aggregate brand-model counts
    brand_model_data = df_CarPriceCSV.groupby(['carBrand', 'carModel'], as_index=False)['count'].sum()

    # Aggregate brand-only counts
    brand_data = brand_model_data.groupby('carBrand', as_index=False)['count'].sum().sort_values('carBrand')

    # Unified dropdown: "All Brands" + specific brands
    brand_options = ["All Brands"] + brand_data['carBrand'].tolist()
    selected_brand = st.selectbox("🔍 Choose a brand to explore:", brand_options)

    # Display chart based on selection
    if selected_brand == "All Brands":
        st.subheader("Car Brands Overview")
        brand_fig = px.pie(brand_data, names='carBrand', values='count', title="Car Brands")
        st.plotly_chart(brand_fig, use_container_width=True)
    else:
        st.subheader(f"{selected_brand} Models Breakdown")
        model_data = (
            df_CarPriceCSV[df_CarPriceCSV['carBrand'] == selected_brand]
            .groupby('carModel', as_index=False)['count'].sum()
        )
        if model_data.empty:
            st.warning(f"No models found for brand: {selected_brand}")
        else:
            model_fig = px.pie(model_data, names='carModel', values='count', title=f"{selected_brand} Models")
            st.plotly_chart(model_fig, use_container_width=True)

    # Display brand distribution image
    st.image("images/panda_pie.jpg", caption="Brand distribution", use_container_width=True)