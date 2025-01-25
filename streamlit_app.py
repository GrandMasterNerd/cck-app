import streamlit as st
from PIL import Image

# Title and logo
st.title("Compass Chronicles: Kingston")
st.image("https://cck-app.streamlit.app/logo.png", caption="Explore Kingston in a new way!")

# Navigation menu
menu = st.sidebar.selectbox("Explore", [
    "Home",
    "Categories",
    "Landmarks",
    "Your Badges",
    "Local Deals",
    "About the App",
])

if menu == "Home":
    st.header("Welcome to Compass Chronicles: Kingston!")
    st.write("""
        Use your phone as a compass to uncover Kingston's landmarks, collect badges, 
        access local deals, and learn about the city’s rich history and culture.
    """)
    st.image("https://cck-app.streamlit.app/home_image.png", caption="Discover Kingston")

elif menu == "Categories":
    st.header("Choose a Category")
    categories = ["Engineer", "Historical", "Nature", "Cultural"]
    category = st.selectbox("Explore by Category", categories)
    st.write(f"You selected the {category} category.")

elif menu == "Landmarks":
    st.header("Landmarks")
    landmarks = {
        "Beamish-Munro Hall": {
            "Distance": "0m",
            "Fun Fact": "Opened in 2002, it features solar panels and energy-efficient systems.",
            "Image": "https://bharchitects.com/wp-content/uploads/2017/01/Queens-University-Beamish-Munro_Hero.jpg",
        },
        "Fort Henry": {
            "Distance": "4600m",
            "Fun Fact": "Built to protect the Rideau Canal.",
            "Image": "https://www.tripsavvy.com/thmb/_Jk2Q-Mww_1DvT68onhqZX_QmaQ=/2573x2038/filters:no_upscale()/FortHenry-59f0e1d8d088c00010f2c09a.jpg",
        },
    }

    landmark = st.selectbox("Select a Landmark", list(landmarks.keys()))
    details = landmarks[landmark]
    st.image(details["Image"], caption=landmark)
    st.write(f"**Distance:** {details['Distance']}")
    st.write(f"**Fun Fact:** {details['Fun Fact']}")

elif menu == "Your Badges":
    st.header("Your Badges")
    st.write("Collect badges by visiting landmarks!")
    badges = ["Engineering Explorer", "History Buff", "Nature Lover"]
    st.write("You have unlocked the following badges:")
    for badge in badges:
        st.write(f"- {badge}")

elif menu == "Local Deals":
    st.header("Local Deals")
    st.write("Show these screens to claim your deals:")
    st.write("- **Common Ground Coffeehouse:** 10% off any drink today!")
    st.write("- **The Grad Club:** Free appetizer with any meal!")

elif menu == "About the App":
    st.header("About Compass Chronicles")
    st.write("""
        Compass Chronicles: Kingston is your ultimate guide to exploring the city. 
        Discover landmarks, learn fascinating facts, collect badges, and unlock local deals.
        Built with Python and Streamlit.
    """)
