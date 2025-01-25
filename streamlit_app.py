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
from streamlit.components.v1 import html
import asyncio
import websockets
from threading import Thread

def main():
    st.set_page_config(page_title="Compass Chronicles: Kingston", layout="wide")
    st.markdown(
        """
        <style>
            body {
                background-color: #f5deb3; /* Light brown background */
                color: #4b2e05; 
                font-family: 'Papyrus', sans-serif; 
            }
            .stButton>button {
                background-color: #d4af37; 
                color: #4b2e05;
                border: 2px solid #b8860b;
                border-radius: 10px;
            }
            .stButton>button:hover {
                background-color: #b8860b; 
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.title("🧭 Compass Chronicles: Kingston")

    # Sidebar for navigation
    st.sidebar.title("Navigate")
    st.sidebar.markdown(
        "<style>.sidebar .sidebar-content { background-color: #f5deb3; }</style>",
        unsafe_allow_html=True
    )
    st.button("Start Exploring", key="start_button", on_click=show_category_selection)

def show_category_selection():
    st.header("Select a Theme")
    theme = st.radio("Choose a theme:", [
        "Historical Landmarks", "Cultural Hotspots", "Nature Trails", "Engineering Feats"])
    show_theme_locations(theme)

def show_theme_locations(theme):
    st.header(f"Explore {theme}")
    st.markdown("Search for a location within this theme:")
    locations = {
        "Historical Landmarks": ["Fort Henry", "Kingston City Hall", "St. George's Cathedral"],
        "Cultural Hotspots": ["The Isabel Bader Centre", "Grand Theatre", "Agnes Etherington Art Centre"],
        "Nature Trails": ["Lemoine Point", "Little Cataraqui Creek", "Kingston Waterfront"],
        "Engineering Feats": ["Beamish-Munro Hall", "Stauffer Library", "Goodwin Hall"]
    }

    location = st.selectbox("Search Locations:", locations[theme])
    st.markdown(f"**Selected Location:** {location}")
    st.image("https://via.placeholder.com/800x400", caption=location, use_container_width=True)

    # Example description for the location
    descriptions = {
        "Fort Henry": "Fort Henry is a 19th-century military fortification and a UNESCO World Heritage Site.",
        "Kingston City Hall": "A historic building that is a symbol of Kingston's heritage.",
        "St. George's Cathedral": "A prominent religious site with stunning architecture.",
        "The Isabel Bader Centre": "A modern venue for arts and cultural events.",
        "Grand Theatre": "A historic theatre hosting performances and events.",
        "Agnes Etherington Art Centre": "An art gallery showcasing a range of collections.",
        "Lemoine Point": "A beautiful nature area with trails and wildlife.",
        "Little Cataraqui Creek": "A conservation area with scenic views and activities.",
        "Kingston Waterfront": "A vibrant area with parks and stunning waterfront views.",
        "Beamish-Munro Hall": "The heart of innovation at Queen's University.",
        "Stauffer Library": "A hub for knowledge and research in Kingston.",
        "Goodwin Hall": "Home to advanced engineering and applied science facilities."
    }

    st.markdown(f"**Description:** {descriptions.get(location, 'No description available.')}")

# Footer with Credits
st.markdown(
    """
    ---
    **Developed by Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan, and Aidan Murray**
    """
)

if __name__ == "__main__":
    main()
