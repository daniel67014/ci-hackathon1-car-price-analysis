import streamlit as st
import plotly.express as px
import pandas as pd

def amu_page():
    """Render Amu's analysis page:
    - reads dataframe from Streamlit session_state
    - provides sidebar filters for drivewheel type
    - shows a box plot of horsepower distribution by drivewheel
    - shows filtered raw data in an expander
    """

    # Retrieve shared dataframe stored in Streamlit session state
    df = st.session_state.df

    # Page title and short description
    st.title("🚘 Amu's Car Analysis Page")
    st.markdown("""
    Welcome to **Amu's interactive analysis page**!  
    Use the filters below to explore **horsepower distribution** by different drivewheel types.
    """)

    # Sidebar filter controls
    st.sidebar.header("🔧 Filter Options")

    # Get unique drivewheel types from the dataframe for selection options
    drive_options = df["drivewheel"].unique()
    selected_drive = st.sidebar.multiselect(
        "Select Drivewheel Type(s):", 
        options=drive_options, 
        default=drive_options
    )

    # Filter dataframe according to the user's selection
    filtered_df = df[df["drivewheel"].isin(selected_drive)]

    # Section header for the plot
    st.subheader("📊 Horsepower Distribution by Drivewheel Type")

    # Create a box plot with Plotly Express showing horsepower distribution per drivewheel type
    fig = px.box(filtered_df, x="drivewheel", y="horsepower", color="drivewheel",
                title="Horsepower Distribution by Drivewheel Type")
    # Render the plot in Streamlit; use_container_width makes it responsive
    st.plotly_chart(fig, use_container_width=True)

    # Provide raw filtered data inside an expander so users can inspect underlying rows
    with st.expander("🔍 View Raw Data"):
        st.dataframe(filtered_df)

    st.image("images/horse_and_panda.jpg", caption="Horsepower distribution", use_container_width=True)
