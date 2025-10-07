import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("C:\\Users\\admin\\Documents\\vscode-projects\\ci-hackaton1-car-price-analysis\\ci-hackathon1-car-price-analysis\\Data\\KaggleCarArchive\\CarPrice_Working.csv")

st.title("This is Amu's page")
st.write("This is Amu's page of the multipage app!")

fig = px.box(df, x="drivewheel", y="horsepower", color="drivewheel",
             title="Horsepower Distribution by Drivewheel Type")
fig.show()