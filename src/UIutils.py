
import streamlit as st
from src.utils import createDataFrame



@st.cache_data
def load_data(_Loaderobj, List):
    # Replace this with the code to load your data
    return createDataFrame(_Loaderobj, List)