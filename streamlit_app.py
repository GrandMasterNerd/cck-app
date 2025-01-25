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

# Set the background color for the application
st.markdown(
    """
    <style>
    body, .block-container {
        background-color: #003153 !important;  # Prussian Blue color code
    }
    </style>
    """, unsafe_allow_html=True
)

# Create 3 columns
col1, col2, col3 = st.columns(3)

# Place content in the columns
col1.write("This is Column 1")
col2.write("This is Column 2")
col3.write("This is Column 3")

st.title("Compass Chronicles: Kingston")
st.write("Welcome to Compass Chronicles: Kingston")
st.image("res/Kingston-Overview.JPG")
