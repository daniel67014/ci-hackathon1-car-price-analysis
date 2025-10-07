import streamlit as st
import app_pages.multi_page as mp

from app_pages.page1 import page1
from app_pages.page2 import page2
from app_pages.amu_page import amu_page
from app_pages.dan_page import dan_page

app = mp.Multipage("MAD Ken Dash - Car Price Analysis")

app.add_page("Page 1", page1)
app.add_page("Page 2", page2)
app.add_page("amu", amu_page)
app.add_page("dan", dan_page)

app.run()