import streamlit as st
import plotly.express as px
import pandas as pd

def amu_page():
    df = pd.read_csv("Data/KaggleCarArchive/CarPrice_Working.csv")

    st.title("This is Amu's page")
    st.write("This is Amu's page of the multipage app!")

    fig = px.box(df, x="drivewheel", y="horsepower", color="drivewheel",
                title="Horsepower Distribution by Drivewheel Type")
    st.plotly_chart(fig)