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

def main():
    st.set_page_config(page_title="Compass Chronicles: Kingston", layout="wide")
    st.title("🧭 Compass Chronicles: Kingston")
    
    # Sidebar for navigation
    st.sidebar.title("Navigate")
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
    st.image("res/Make a logo for this app_ Use your phone as a compass to uncover landmarks, collect badges, and access local deals, all while discovering the city’s rich history and culture. Make a logo. Include the words _Compass.jpg", use_container_width=True)
    
    st.markdown("### Features")
    st.markdown("- **Explore landmarks** and learn their history.")
    st.markdown("- **Collect badges** for your achievements.")
    st.markdown("- **Get local deals** from participating businesses.")
    st.markdown("- **Navigate** with ease and uncover hidden gems.")
    
    st.button("Get Started", key="start_button")

# Landmarks Page
def explore_landmarks():
    categories = {
        "Engineering": ["Beamish-Munro Hall", "Stauffer Library", "Goodwin Hall", "Jeffery Hall", "Ellis Hall", "Dupuis Hall"],
        "Historical": ["Fort Henry", "Bellevue House", "Kingston City Hall", "Kingston Penitentiary", "Murney Tower", "Martello Alley"],
        "Nature": ["Lake Ontario Park", "Lemoine Point", "Little Cataraqui Creek", "Portsmouth Olympic Harbour", "Battery Park", "Grass Creek Park"],
        "Cultural": ["The Grand Theatre", "Tett Centre", "Isabel Bader Centre", "Skeleton Park", "Slush Puppie Place"]
    }
    
    st.header("Explore Landmarks")
    category = st.selectbox("Choose a category:", categories.keys())
    
    for landmark in categories[category]:
        st.subheader(landmark)
        st.markdown(f"**Distance:** {random.randint(100, 1000)}m")
        st.markdown("**Fun Fact:** Did you know? This is one of Kingston's most iconic landmarks.")
        if st.button(f"Learn More about {landmark}"):
            display_landmark_details(landmark)

# Landmark Details
def display_landmark_details(landmark):
    st.sidebar.title(landmark)
    st.markdown(f"### Welcome to {landmark}!")
    st.image("https://via.placeholder.com/800x400", caption=f"{landmark}", use_column_width=True)
    st.markdown("- **History:** This landmark has a rich history.")
    st.markdown("- **Features:** Beautiful architecture, great stories, and more.")

# Badges Page
def view_badges():
    st.header("Your Badges")
    st.markdown("Keep exploring to collect more badges!")
    badges = [
        "Engineering Explorer", "Nature Enthusiast", "History Buff", "Culture Connoisseur"
    ]
    
    for badge in badges:
        st.markdown(f"- {badge}")

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

