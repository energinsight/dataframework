import streamlit as st
import pandas as pd
from UI.pirce import price_page
from UI.demand import demand_page
from UI.production import Production_page

start = pd.Timestamp('2024-05-01 00:00:00', tz='Europe/Brussels')
end = pd.Timestamp('2024-06-09 23:00:00', tz='Europe/Brussels')

PAGES = {
    "Spot Price": price_page,
    "Demand": demand_page,
    "Production": Production_page
}

def main():
    
    st.sidebar.title('Fundamentals')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page(start, end)

if __name__ == "__main__":
    main()