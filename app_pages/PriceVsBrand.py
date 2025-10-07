import streamlit as st
import plotly.express as px

df_CarPriceCSV = st.session_state.df
df_byBrand = df_CarPriceCSV[['carBrand', 'price']].groupby('carBrand').mean().astype(int).reset_index()
df_byBrand = df_byBrand.sort_values(by='price', ascending=False)

def PriceVsBrand():
    st.title("Price vs Brand Analysis")
    st.write("Here we will analyze how car prices vary across different brands.")

    # Brand selection
    brand_list = df_byBrand['carBrand'].tolist()
    selected_brand = st.selectbox("Select a brand to view price distribution (or leave blank for main chart):", [""] + brand_list)

    if selected_brand:
        # Show histogram for selected brand
        st.subheader(f"Price Distribution for {selected_brand}")
        brand_prices = df_CarPriceCSV[df_CarPriceCSV['carBrand'] == selected_brand]['price']
        fig_hist = px.histogram(brand_prices, nbins=20, labels={'value': 'Price'}, title=f'Price Distribution for {selected_brand}')
        st.plotly_chart(fig_hist)
        if st.button("Back to main chart"):
            st.experimental_rerun()
    else:
        # Show main horizontal bar chart
        fig_bar = px.bar(
            df_byBrand,
            x='price',
            y='carBrand',
            orientation='h',
            labels={'price': 'Average Price', 'carBrand': 'Car Brand'},
            title='Average Car Price by Brand'
        )
        st.plotly_chart(fig_bar)


