import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import os

current_file_path = os.path.abspath(__file__)
df_CarPriceCSV = pd.read_csv('Data/KaggleCarArchive/CarPrice_Working.csv')

df_byBrand = df_CarPriceCSV[['carBrand', 'price']].groupby('carBrand').mean().astype(int).reset_index()
df_byBrand = df_byBrand.sort_values(by='price', ascending=False)

fig, ax = plt.subplots()
ax.barh(df_byBrand['carBrand'], df_byBrand['price'])
ax.set_xlabel('Average Price')
ax.set_ylabel('Car Brand')
ax.set_title('Average Car Price by Brand')


def PriceVsBrand():
    st.title("Price vs Brand Analysis")
    st.write("Here we will analyze how car prices vary across different brands.")
    st.pyplot(fig)


