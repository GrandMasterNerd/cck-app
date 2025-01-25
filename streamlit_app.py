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

completion = 0      # Percent of "badges" earned by visiting different city locations

st.title("Compass Chronicles: Kingston")
st.write("Welcome to Compass Chronicles: Kingston")
st.image("res/Kingston-Overview.JPG")

message = "You have found {}% of badges".format(completion)
st.write(message)
st.progress(completion)

