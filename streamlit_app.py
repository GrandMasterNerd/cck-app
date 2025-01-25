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
st.markdown(
    """
    <style>
    body {
        background-color: #003153 !important;  # Navy Blue
    }
    </style>
    """, unsafe_allow_html=True
)

# st.title("🎈 My new app")
st.title("Compass Chronicles: Kingston")
st.write("Welcome to Compass Chronicles: Kingston")
st.image("res/Kingston-Overview.JPG")
