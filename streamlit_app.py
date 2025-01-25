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

# WebSocket server to handle messages
async def handle_message(websocket, path):
    async for message in websocket:
        st.write(f"Received message: {message}")
        await websocket.send("Message received")

# Start WebSocket server in a separate thread
def run_websocket_server():
    asyncio.get_event_loop().run_until_complete(websockets.serve(handle_message, "0.0.0.0", 8765))
    asyncio.get_event_loop().run_forever()

# Start WebSocket server in a separate thread
ws_thread = Thread(target=run_websocket_server)
ws_thread.start()

def main():
    st.set_page_config(page_title="Compass Chronicles: Kingston", layout="wide")
    st.markdown(
        """
        <style>
            body {
                background-color: #f8e8c1; 
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
    landmarks = {
        "Beamish-Munro Hall": {
            "distance": 0,
            "image": "https://via.placeholder.com/400x300",
            "description": "Welcome to Beamish-Munro Hall, the heart of innovation at Queen's University."
        },
        "Stauffer Library": {
            "distance": 500,
            "image": "https://via.placeholder.com/400x300",
            "description": "A hub for knowledge and research, Stauffer Library stands tall in Kingston."
        },
        "Goodwin Hall": {
            "distance": 300,
            "image": "https://via.placeholder.com/400x300",
            "description": "Goodwin Hall is home to advanced engineering and applied science facilities."
        }
    }
    
    st.header("Explore Landmarks")
    for name, details in landmarks.items():
        st.subheader(name)
        st.image(details["image"], caption=name, use_container_width=True)
        st.markdown(f"**Distance:** {details['distance']}m")
        st.markdown(f"**Description:** {details['description']}")

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
    qr_image_path = "https://via.placeholder.com/300"  # Replace with the actual path to your QR code image
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

