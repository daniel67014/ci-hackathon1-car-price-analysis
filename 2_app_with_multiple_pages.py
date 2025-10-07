import streamlit as st
import app_pages.multi_page as mp


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