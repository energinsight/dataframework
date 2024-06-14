import streamlit as st
from UI.pirce import price_page
from UI.demand import demand_page
from UI.production import Production_page


PAGES = {
    "Spot Price": price_page,
    "Demand": demand_page,
    "Production": Production_page
}

def main():
    
    st.sidebar.title('Fundamentals')
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page()

if __name__ == "__main__":
    main()