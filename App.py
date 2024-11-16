import streamlit as st
import os
from pydeck.bindings.map_styles import styles
from Pages import Home,Project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar
from PIL import Image
import pandas as pd


image = Image.open('./src/jinmark.png')
st.set_page_config(initial_sidebar_state='collapsed', page_icon=image)
pages = ["Home","Project1","Project2","Project3"]
styles = {
    "nav": {
        "background-color": "red",
        "font-size": "1.5rem",
        "font-family": "Georgia, bold",
        "display": "flex",
        "justify-content": "center"
        
    },
    "img": {
        "position": "absolute",
        "left": "0px",
        "font-size": "15px",
        "top": "5px",
        "width": "200px",
        "height": "40px",
    },
    "div": {
        "max-width": "32rem"
    },
    "span": {
        "border-radius": "0.2rem",
        "color": "rgb(49,51,63)",
        "margin": "0 0.125rem",
        "padding": "0.6275rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(105, 114, 255, 0.4)",
        "color": "rgba(255, 255, 255)"
    
    },
    "hover": {
        "background-color": "rgba(0, 0, 0, 0.7)",
        "color": "rgba(255, 255, 255)",
    
    },
}
logo_path = os.path.join(os.path.dirname(__file__), "src", "tekkenlogo.svg")
page = navbar(pages, styles= styles, logo_path=logo_path,)
if page == 'Home':
    Home.Home().app()
elif page == 'Project1':
    Project1.Project1().app()
elif page == 'Project2':
    Project2.Project2().app()
elif page == 'Project3':
    Project3.Project3().app()
else:
    Home.Home().app()
st.title('hi')