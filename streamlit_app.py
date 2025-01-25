#
# Streamlight App
# Authors: Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan 
#          and Aidan Murray
# Purpose: App connects to "beacons" placed at iconic landmarks
#          around the city. Using HTTPS messages, sends data
#          to the app which lets the app know which
#          landmark the user is at. App shows the user 
#          the history of the landmark, including 
#          pictures, videos, audio, etc.
#

import streamlit as st

# Add custom CSS to change the background color to Neon Pink and adjust margins
st.markdown(
    """
    <style>
    body, .block-container {
        background-color: #FF10F0 !important;  # Neon Pink color code
        margin: 0 !important;  # Remove default margin
        padding: 0 !important;  # Remove default padding
    }
    </style>
    """, unsafe_allow_html=True
)

# Add custom CSS to change background color and hide header/footer elements
st.markdown(
    """
    <style>
    body, .block-container {
        background-color: #FF10F0 !important;  # Neon Pink color code
        margin: 0 !important;  # Remove default margin
        padding: 0 !important;  # Remove default padding
    }

    /* Hide the header */
    .css-1d391kg {  
        display: none !important;  
    }

    /* Hide the footer */
    .css-1k8p3ln { 
        display: none !important;
    }

    /* Hide the GitHub button at the bottom */
    .css-1s7veaj {  
        display: none !important;
    }

    </style>
    """, unsafe_allow_html=True
)

# st.title("🎈 My new app")
st.title("Compass Chronicles: Kingston")
st.write("Welcome to Compass Chronicles: Kingston")
st.image("res/Kingston-Overview.JPG")
