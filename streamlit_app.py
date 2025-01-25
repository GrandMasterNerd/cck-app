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

    # Add custom styling for a game-like aesthetic
    st.markdown(
        """
        <style>
            body {
                background-image: url('https://via.placeholder.com/1920x1080');
                background-size: cover;
                background-attachment: fixed;
                color: #f1f1f1;
                font-family: 'Trebuchet MS', sans-serif;
            }
            .stButton>button {
                background-color: #007ACC;
                color: #f1f1f1;
                font-size: 1.2rem;
                border-radius: 12px;
                padding: 10px 20px;
                transition: transform 0.3s;
            }
            .stButton>button:hover {
                transform: scale(1.1);
                background-color: #005A99;
            }
            .sidebar .sidebar-content {
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 15px;
                padding: 20px;
            }
            .stMarkdown h1 {
                color: #FFD700;
                font-family: 'Papyrus', fantasy;
                text-align: center;
                text-shadow: 2px 2px 5px #000;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Header with a fun logo
    st.markdown(
        """
        <h1>🎮 Welcome to Compass Chronicles: Kingston 🗺️</h1>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for navigation with a game-like menu
    st.sidebar.title("📜 Quest Log")
    st.sidebar.markdown("Choose your next adventure:")
    page = st.sidebar.radio("Navigate:", [
        "Home", "Explore Landmarks", "Your Badges", "Local Deals", "About"])

    # Conditional navigation
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
    st.markdown(
        """
        <h2>⚔️ Start Your Adventure!</h2>
        <p>Use your phone as a compass to uncover landmarks, collect badges, and uncover Kingston's mysteries!</p>
        <img src="https://via.placeholder.com/800x400" alt="Explore" style="width: 100%; border-radius: 15px;"/>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 🏆 Features")
    st.markdown("- **Explore landmarks** and unlock hidden secrets.")
    st.markdown("- **Collect badges** for completing quests.")
    st.markdown("- **Earn rewards** at participating businesses.")
    st.markdown("- **Navigate** and become a local hero.")

    if st.button("⚡ Begin Adventure"):
        st.balloons()

# Landmarks Page
def explore_landmarks():
    st.markdown(
        """
        <h2>📍 Explore Landmarks</h2>
        """,
        unsafe_allow_html=True
    )

    # Simulated landmarks with dynamic styling
    landmarks = {
        "Beamish-Munro Hall": {
            "distance": 0,
            "image": "https://via.placeholder.com/400x300",
            "description": "A hub of innovation and creativity at Queen's University."
        },
        "Stauffer Library": {
            "distance": 500,
            "image": "https://via.placeholder.com/400x300",
            "description": "A grand library for knowledge seekers."
        },
        "Goodwin Hall": {
            "distance": 300,
            "image": "https://via.placeholder.com/400x300",
            "description": "Home of advanced engineering at Queen's."
        }
    }

    for name, details in landmarks.items():
        st.markdown(f"**{name}**")
        st.image(details["image"], caption=name, use_container_width=True)
        st.markdown(f"**Distance:** {details['distance']}m")
        st.markdown(f"**Description:** {details['description']}")

# Badges Page
def view_badges():
    st.markdown(
        """
        <h2>🏅 Your Badges</h2>
        <p>Track your achievements and unlock new challenges!</p>
        """,
        unsafe_allow_html=True
    )

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
                st.markdown(
                    f"<img src='{badge['image']}' style='filter: grayscale(100%); width: 100%; border-radius: 15px;'>\n<div style='text-align: center;'>{badge['name']} (Locked)</div>",
                    unsafe_allow_html=True
                )

# Deals Page
def view_deals():
    st.markdown(
        """
        <h2>💰 Local Deals</h2>
        <p>Discover rewards from participating locations:</p>
        """,
        unsafe_allow_html=True
    )

    deals = [
        "Show this screen at Common Ground Coffeehouse for 10% off any drink!",
        "Get 20% off at The Grad Club after collecting 5 badges.",
        "Exclusive discounts at participating Kingston shops!"
    ]

    for deal in deals:
        st.markdown(f"- {deal}")

    st.markdown("### Your QR Code")
    qr_image_path = "https://via.placeholder.com/300"  # Replace with the actual QR code image
    st.image(qr_image_path, caption="Scan this to redeem rewards!", use_container_width=True)

# About Page
def about_page():
    st.markdown(
        """
        <h2>📜 About Compass Chronicles</h2>
        <p>Immerse yourself in Kingston's rich history and culture with our interactive app!</p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("- Built using Python, Streamlit, and GoDaddy.")
    st.markdown("- Uses ESP8266 modules for precise location tracking.")
    st.markdown("- Designed to make exploring fun and engaging!")
    
    st.markdown("### Our Mission")
    st.markdown("To create unforgettable city exploration experiences for all ages.")

if __name__ == "__main__":
    main()

# Footer with Credits
st.markdown(
    """
    ---
    **Developed by Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan, and Aidan Murray**
    """,
    unsafe_allow_html=True
)
