#
# Streamlit App
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

# Add custom CSS to change the background color to Prussian Blue
# Example CSS code to change background color
# Add custom CSS to change background color to Prussian Blue
st.markdown(
    """
    <style>
    body, .block-container {
        background-color: #003153 !important;  # Prussian Blue color code
        margin: 0 !important;  # Remove default margin
        padding: 0 !important;  # Remove default padding
    }
    </style>
    """, unsafe_allow_html=True
)

# st.title("🎈 My new app")
st.title("Compass Chronicles: Kingston")
st.write("Welcome to Compass Chronicles: Kingston")
st.image("res/Kingston-Overview.JPG")
