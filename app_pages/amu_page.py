import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(
    page_title="Amu's Car Analysis",
    page_icon="🚗",
    layout="wide"
)

@st.cache_data
def load_data():
    df = pd.read_csv(
        "C:\\Users\\admin\\Documents\\vscode-projects\\ci-hackaton1-car-price-analysis\\ci-hackathon1-car-price-analysis\\Data\\KaggleCarArchive\\CarPrice_Working.csv"
    )
    return df

df = load_data()

st.title("🚘 Amu's Car Analysis Page")
st.markdown("""
Welcome to **Amu's interactive analysis page**!  
Use the filters below to explore **horsepower distribution** by different drivewheel types.
""")


st.sidebar.header("🔧 Filter Options")

drive_options = df["drivewheel"].unique()
selected_drive = st.sidebar.multiselect(
    "Select Drivewheel Type(s):", 
    options=drive_options, 
    default=drive_options
)

filtered_df = df[df["drivewheel"].isin(selected_drive)]

st.subheader("📊 Horsepower Distribution by Drivewheel Type")

fig = px.box(df, x="drivewheel", y="horsepower", color="drivewheel",
             title="Horsepower Distribution by Drivewheel Type")
#fig.show()

st.plotly_chart(fig, use_container_width=True)

with st.expander("🔍 View Raw Data"):
    st.dataframe(filtered_df)