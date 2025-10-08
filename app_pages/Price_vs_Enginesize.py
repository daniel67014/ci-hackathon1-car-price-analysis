import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df_CarPriceCSV = st.session_state.df

def Price_vs_Enginesize():
    st.write("Welcome to the Price vs Engine Size analysis page!")
    
    col1, col2 = st.columns([3, 1])
    with col1:
        # Create a scatter plot visualization for Engine Size vs Price
        plt.figure(figsize=(10, 6))
        plt.scatter(df_CarPriceCSV['enginesize'], df_CarPriceCSV['price'], color='blue')
        plt.xlabel('Engine Size')
        plt.ylabel('Price')
        plt.title('Engine Size vs Price')
        plt.tight_layout()
        st.pyplot(plt)
    with col2:
        # Display an image related to car prices
        st.image("images/engine_price.jpg", caption="Car price analysis", use_container_width=True)
