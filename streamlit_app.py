# Streamlit App
# Authors: Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan 
#          and Aidan Murray
# Purpose: App connects to "beacons" placed at iconic landmarks
#          around the city. Using HTTPS messages, sends data
#          to the app which lets the app know which
#          landmark the user is at. App shows the user 
#          the history of the landmark, including 
#          pictures, videos, audio, etc.

import streamlit as st

# Set the background color for the application
st.markdown(
    """
    <style>
    body, .block-container {
        background-color: #003153 !important;  /* Prussian Blue color code */
        color: #FFFFFF !important; /* White text */
    }
    h1, h2, h3, h4, h5, h6 {
        color: #FFD700 !important; /* Gold text for headings */
    }
    </style>
    """, unsafe_allow_html=True
)

# Initialize badges earned
completion = 0  # Percent of "badges" earned by visiting different city locations

# App Title and Introduction
st.title("Compass Chronicles: Kingston")
st.write("Welcome to Compass Chronicles: Kingston! Use your phone to explore landmarks, learn history, and collect badges as you go!")
st.image("res/Kingston-Overview.JPG", caption="Discover the vibrant city of Kingston", use_column_width=True)

# Badge Completion Progress
message = "You have found {}% of badges".format(completion)
st.write(message)
st.progress(completion)

# Interactive Landmark Feature
def display_landmark(name, description, image_path):
    """Display a landmark with its name, description, and image."""
    st.subheader(name)
    st.image(image_path, use_column_width=True)
    st.write(description)

# Example Landmark: Beamish-Munro Hall
display_landmark(
    "Beamish-Munro Hall",
    "Beamish-Munro Hall is the heart of engineering innovation at Queen's University. Opened in 2002, it is home to advanced labs and collaborative spaces, supporting students in solving real-world challenges.",
    "res/Beamish-Munro-Hall.jpg"
)

# Add more landmarks dynamically
landmark_choice = st.selectbox(
    "Choose a landmark to explore:",
    ["Beamish-Munro Hall", "Fort Henry", "City Hall", "Martello Tower"]
)

if landmark_choice == "Fort Henry":
    display_landmark(
        "Fort Henry",
        "Fort Henry is a historic site and living museum of military life in the 19th century. A UNESCO World Heritage Site, it offers spectacular views and engaging historical reenactments.",
        "res/Fort-Henry.jpg"
    )
elif landmark_choice == "City Hall":
    display_landmark(
        "Kingston City Hall",
        "Kingston's City Hall is an iconic neoclassical building and National Historic Site of Canada, reflecting the city's rich history.",
        "res/City-Hall.jpg"
    )
elif landmark_choice == "Martello Tower":
    display_landmark(
        "Martello Tower",
        "The Martello Towers are unique defensive structures built during the 19th century, showcasing Kingston's strategic military significance.",
        "res/Martello-Tower.jpg"
    )

# Footer with Credits
st.markdown(
    """
    ---
    **Developed by Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan, and Aidan Murray**
    """
)

