import streamlit as st
import streamlit.components.v1 as components

# Configure page layout
st.set_page_config(
    page_title="Nicholas Leonid | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default UI padding and elements
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            border: none;
            width: 100vw;
            height: 100vh;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Read and render index.html
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=1000, scrolling=True)