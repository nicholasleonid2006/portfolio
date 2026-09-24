import streamlit as st
import streamlit.components.v1 as components

# Configure page layout
st.set_page_config(
    page_title="Nicholas Leonid | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit UI elements, body scrollbars, and expand the iframe container
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Remove default Streamlit padding and prevent double scrollbars */
        .block-container {
            padding: 0rem !important;
            max-width: 100% !important;
        }
        
        div[data-testid="stAppViewContainer"] {
            overflow: hidden !important;
        }

        /* Force iframe to take up the full viewport height */
        iframe {
            display: block;
            border: none;
            width: 100vw !important;
            height: 100vh !important;
            position: fixed;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Read HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render component with dynamic height
components.html(html_content, height=2500, scrolling=True)
