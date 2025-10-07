import streamlit as st
import app_pages.multi_page as mp

from app_pages.page1 import page1
from app_pages.page2 import page2
from app_pages.PriceVsBrand import PriceVsBrand

app = mp.Multipage("My First Multipage App")

app.add_page("Page 1", page1)
app.add_page("Page 2", page2)
app.add_page("Price vs Brand", PriceVsBrand)

app.run()