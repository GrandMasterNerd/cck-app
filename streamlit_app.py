import streamlit as st
import pandas as pd

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Compass Chronicles: Kingston", layout="wide")

# Global state to store theme and location data
if 'theme' not in st.session_state:
    st.session_state.theme = None
if 'location' not in st.session_state:
    st.session_state.location = None

def main():
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
    if st.sidebar.button("Start Exploring", key="start_button"):
        show_category_selection()
    if st.session_state.theme and st.session_state.location:
        show_theme_locations(st.session_state.theme)

def show_category_selection():
    st.header("Select a Theme")
    st.session_state.theme = st.radio("Choose a theme:", [
        "Historical Landmarks", "Cultural Hotspots", "Nature Trails", "Engineering Feats"])
    show_theme_locations(st.session_state.theme)

def show_theme_locations(theme):
    st.header(f"Explore {theme}")
    st.markdown("Search for a location within this theme:")

    locations = {
        "Historical Landmarks": ["Fort Henry", "Kingston City Hall", "St. George's Cathedral"],
        "Cultural Hotspots": ["The Isabel Bader Centre", "Grand Theatre", "Agnes Etherington Art Centre"],
        "Nature Trails": ["Lemoine Point", "Little Cataraqui Creek", "Kingston Waterfront"],
        "Engineering Feats": ["Beamish-Munro Hall", "Stauffer Library", "Goodwin Hall"]
    }

    # Update session_state to reflect the selected location
    st.session_state.location = st.selectbox("Search Locations:", locations.get(theme, []))
    if st.session_state.location:
        show_location_details(st.session_state.location)

def show_location_details(location):
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

    st.markdown(f"**Selected Location:** {location}")
    st.image("https://via.placeholder.com/800x400", caption=location, use_container_width=True)
    st.markdown(f"**Description:** {descriptions.get(location, 'No description available.')}")

    # Map integration
    coordinates = {
        "Fort Henry": (44.2296, -76.4746),
        "Kingston City Hall": (44.2312, -76.4787),
        "St. George's Cathedral": (44.2305, -76.4833),
        "The Isabel Bader Centre": (44.2241, -76.4957),
        "Grand Theatre": (44.2331, -76.4864),
        "Agnes Etherington Art Centre": (44.2256, -76.4951),
        "Lemoine Point": (44.2387, -76.5794),
        "Little Cataraqui Creek": (44.2633, -76.5483),
        "Kingston Waterfront": (44.2298, -76.4816),
        "Beamish-Munro Hall": (44.2255, -76.4949),
        "Stauffer Library": (44.2260, -76.4958),
        "Goodwin Hall": (44.2270, -76.4946)
    }

    coord = coordinates.get(location)
    if coord:
        st.map(pd.DataFrame([coord], columns=["lat", "lon"]))

# Footer with Credits
st.markdown(
    """
    ---
    **Developed by Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan, and Aidan Murray**
    """
)

if __name__ == "__main__":
    main()
