import streamlit as st
import app_pages.multi_page as mp
import pandas as pd

import os


if "df" not in st.session_state:
    current_file_path = os.path.abspath(__file__)
    st.session_state.df = pd.read_csv('Data/KaggleCarArchive/CarPrice_Working.csv')

from app_pages.PriceVsBrand import PriceVsBrand
from app_pages.aidid_page import aidid_page
from app_pages.amu_page import amu_page
from app_pages.dan_page import dan_page

app = mp.Multipage("MAD Ken Dash - Car Price Analysis")

app.add_page("Price vs Brand", PriceVsBrand)
app.add_page("aidid", aidid_page)
app.add_page("amu", amu_page)
app.add_page("dan", dan_page)

app.run()