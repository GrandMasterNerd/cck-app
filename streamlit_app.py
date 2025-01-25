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
import random
from io import BytesIO
from PIL import Image

def main():
    st.set_page_config(page_title="Compass Chronicles: Kingston", layout="wide")
    st.markdown(
        "<style>body { background-color: #f5deb3; color: #4b2e05; font-family: 'Papyrus', sans-serif; }</style>",
        unsafe_allow_html=True
    )
    st.title("🗺️ Compass Chronicles: Kingston")

    # Sidebar for navigation
    st.sidebar.title("Navigate")
    st.sidebar.markdown(
        "<style>.sidebar .sidebar-content { background-color: #d2b48c; }</style>",
        unsafe_allow_html=True
    )
    page = st.sidebar.radio("Go to:", [
        "Home", "Explore Landmarks", "Your Badges", "Local Deals", "About"])

    if page == "Home":
        home_page()
    elif page == "Explore Landmarks":
        explore_landmarks()
    elif page == "Your Badges":
        view_badges()
    elif page == "Local Deals":
        view_deals()
    elif page == "About":
        about_page()

# Home Page
def home_page():
    st.header("Welcome to Compass Chronicles!")
    st.markdown("Use your phone as a compass to uncover landmarks, collect badges, and discover Kingston's rich history and culture.")
    st.image("https://via.placeholder.com/800x400", caption="Explore Kingston like never before!", use_container_width=True)
    
    st.markdown("### Features")
    st.markdown("- **Explore landmarks** and learn their history.")
    st.markdown("- **Collect badges** for your achievements.")
    st.markdown("- **Get local deals** from participating businesses.")
    st.markdown("- **Navigate** with ease and uncover hidden gems.")
    
    st.button("Get Started", key="start_button")

# Landmarks Page
def explore_landmarks():
    categories = {
        "Engineer": [
            {"name": "Beamish-Munro Hall", "distance": 0},
            {"name": "Stauffer Library", "distance": 500},
            {"name": "Goodwin Hall", "distance": 300},
            {"name": "Jeffery Hall", "distance": 450},
            {"name": "Ellis Hall", "distance": 250},
            {"name": "Dupuis Hall", "distance": 600}
        ],
        "Historical": [
            "Fort Henry", "Bellevue House", "Kingston City Hall", "Kingston Penitentiary", "Murney Tower", "Martello Alley"
        ],
        "Nature": [
            "Lake Ontario Park", "Lemoine Point", "Little Cataraqui Creek Conservation Area", "Portsmouth Olympic Harbour", "Battery Park", "Grass Creek Park"
        ],
        "Cultural": [
            "The Grand Theatre", "Tett Centre for Creativity and Learning", "Isabel Bader Centre", "Skeleton Park", "Slush Puppie Place"
        ]
    }
    
    st.header("Explore Landmarks")
    category = st.selectbox("Choose a category:", categories.keys())
    
    for landmark in categories[category]:
        if isinstance(landmark, dict):
            name, distance = landmark["name"], landmark["distance"]
            st.subheader(name)
            st.markdown(f"**Distance:** {distance}m")
            st.markdown("**Fun Fact:** Did you know? This is one of Kingston's most iconic landmarks.")
            if st.button(f"Learn More about {name}"):
                display_landmark_details(name)
        else:
            st.subheader(landmark)
            st.markdown("**Fun Fact:** Did you know? This is one of Kingston's most iconic landmarks.")
            if st.button(f"Learn More about {landmark}"):
                display_landmark_details(landmark)

# Landmark Details
def display_landmark_details(landmark):
    st.sidebar.title(landmark)
    st.markdown(f"### Welcome to {landmark}!")
    st.image("https://via.placeholder.com/800x400", caption=f"{landmark}", use_container_width=True)
    st.markdown("- **History:** This landmark has a rich history.")
    st.markdown("- **Features:** Beautiful architecture, great stories, and more.")

# Badges Page
def view_badges():
    st.header("Your Badges")
    st.markdown("Keep exploring to collect more badges!")
    badges = [
        {"name": "Engineering Explorer", "image": "https://via.placeholder.com/100", "collected": True},
        {"name": "Nature Enthusiast", "image": "https://via.placeholder.com/100", "collected": False},
        {"name": "History Buff", "image": "https://via.placeholder.com/100", "collected": False},
        {"name": "Culture Connoisseur", "image": "https://via.placeholder.com/100", "collected": True}
    ]
    
    col1, col2, col3, col4 = st.columns(4)
    columns = [col1, col2, col3, col4]
    for idx, badge in enumerate(badges):
        with columns[idx % 4]:
            if badge["collected"]:
                st.image(badge["image"], caption=badge["name"], use_container_width=True)
            else:
                st.markdown(f"<img src='{badge['image']}' style='filter: grayscale(100%); width: 100%;' alt='{badge['name']}'><div style='text-align: center;'>{badge['name']} (Locked)</div>", unsafe_allow_html=True)

# Deals Page
def view_deals():
    st.header("Local Deals")
    st.markdown("Discover exclusive promotions around Kingston:")
    
    deals = [
        "Show this screen at Common Ground Coffeehouse for 10% off any drink!",
        "Get 20% off at The Grad Club after collecting 5 badges.",
        "Exclusive discounts at participating Kingston shops!"
    ]
    
    for deal in deals:
        st.markdown(f"- {deal}")

    st.markdown("### Your QR Code")
    qr_image_path = "your_qr_code_image.png"  # Replace with the actual path to your QR code image
    st.image(qr_image_path, caption="Scan this QR code to redeem your deals!", use_container_width=True)

# About Page
def about_page():
    st.header("About Compass Chronicles")
    st.markdown("Compass Chronicles: Kingston is an immersive app that helps locals and visitors discover the city in a fun and engaging way.")
    st.markdown("- Built with Python, Streamlit & GoDaddy.")
    st.markdown("- Uses ESP8266 Kintone Wi-Fi modules for location-based experiences.")
    st.markdown("- Designed for seamless navigation and discovery.")
    st.markdown("### Our Vision")
    st.markdown("To make Compass Chronicles: Kingston the go-to app for exploring the city’s rich history, culture, and local charm!")

if __name__ == "__main__":
    main()
    
# Footer with Credits
st.markdown(
    """
    ---
    **Developed by Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan, and Aidan Murray**
    """
)

