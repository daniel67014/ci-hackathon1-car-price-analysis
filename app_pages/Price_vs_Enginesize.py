import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


df_CarPriceCSV = pd.read_csv('Data/KaggleCarArchive/CarPrice_Working.csv')

def Price_vs_Enginesize():
    st.title("Page 1")
    st.write("Welcome to Page 1 of the multipage app!")
    
    # Create a bar chart visualization for Engine Size vs Price
    plt.figure(figsize=(10, 6))
    plt.bar(df_CarPriceCSV['enginesize'], df_CarPriceCSV['price'], color='blue')
    plt.xlabel('Engine Size')
    plt.ylabel('Price')
    plt.title('Engine Size vs Price')
    plt.tight_layout()
    st.pyplot(plt)



