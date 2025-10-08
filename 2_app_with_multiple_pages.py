import streamlit as st
import app_pages.multi_page as mp
import pandas as pd
#import os

if "df" not in st.session_state:
#    current_file_path = os.path.abspath(__file__)
    st.session_state.df = pd.read_csv('Data/KaggleCarArchive/CarPrice_Working.csv')

from app_pages.PriceVsBrand import PriceVsBrand
from app_pages.PricevsEnginesize import Price_vs_Enginesize
from app_pages.amu_page import amu_page
from app_pages.brand_explorer import brand_explorer

app = mp.Multipage("MAD Ken Dash - Car Price Analysis")

app.add_page("Price vs Brand", PriceVsBrand)
<<<<<<< HEAD
app.add_page("PricevsEnginesize", PricevsEnginesize)
app.add_page("amu", amu_page)
app.add_page("dan", dan_page)
=======
app.add_page("Price vs. Enginesize", Price_vs_Enginesize)
app.add_page("Horsepower Distribution", amu_page)
app.add_page("Brand Explorer", brand_explorer)
>>>>>>> a80da571561fb82a54a19d1a057e2de2200794be

app.run()