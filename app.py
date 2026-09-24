import streamlit as st
import streamlit.components.v1 as components

# Configure page layout
st.set_page_config(
    page_title="Nicholas Leonid | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit header/footer margins
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        .block-container {
            padding: 0rem !important;
            margin: 0rem !important;
            max-width: 100% !important;
        }
        
        iframe {
            width: 100% !important;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Read HTML content
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render full page height directly inside Streamlit
components.html(html_content, height=3200, scrolling=True)
