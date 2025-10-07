import streamlit as st
import plotly.express as px
import pandas as pd

def amu_page():
    df = st.session_state.df

    st.title("This is Amu's page")
    st.write("This is Amu's page of the MAD Ken Dash app!")

    fig = px.box(df, x="drivewheel", y="horsepower", color="drivewheel",
                title="Horsepower Distribution by Drivewheel Type")
    st.plotly_chart(fig)