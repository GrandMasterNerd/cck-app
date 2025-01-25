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

# Landmarks data in the four categories
landmarks_data = {
    "Engineer": {
        "Beamish-Munro Hall": {
            "Distance": "0m",
            "Fun Fact": "Contains the Integrated Learning Centre and the Stephen J.R. Smith Faculty of Engineering and Applied Science.",
            "Image": "https://bharchitects.com/wp-content/uploads/2017/01/Queens-University-Beamish-Munro_Hero.jpg",
            "History": "Opened in 2004, recognized as one of the most environmentally advanced buildings in Canada in 2005.",
            "Features": "Designed as a 'live building', showing structural elements and sustainable practices."
        },
        "Joseph S. Stauffer Library": {
            "Distance": "550m",
            "Fun Fact": "The largest library on Queen’s campus, with room for approximately 1.5 million volumes.",
            "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/s/staufferlibrary/b-stauff.jpg",
            "History": "Constructed with a substantial donation from the Stauffer Foundation, supports Queen's academic community.",
            "Features": "Various study spaces, including group and individual spaces, and home to the Adaptive Technology Centre."
        }
        # More landmarks can be added here
    },
    "Historical": {
        "Fort Henry": {
            "Distance": "4600m",
            "Fun Fact": "Built to protect the Rideau Canal.",
            "Image": "https://www.tripsavvy.com/thmb/_Jk2Q-Mww_1DvT68onhqZX_QmaQ=/2573x2038/filters:no_upscale()/max_bytes(150000):strip_icc()/FortHenry-59f0e1d8d088c00010f2c09a.jpg",
            "History": "19th-century British military fortress, replacing an earlier fortification from the War of 1812.",
            "Features": "Guided tours, live demonstrations of artillery drills, and interactive exhibits."
        },
        "Bellevue House": {
            "Distance": "1400m",
            "Fun Fact": "Home to Canada’s first Prime Minister, Sir John A. Macdonald, during a pivotal period in his career.",
            "Image": "https://media-cdn.tripadvisor.com/media/photo-s/0f/db/05/7c/canada-s-1st-pm-jamacdoanld.jpg",
            "History": "Built in the 1840s, Bellevue House was designated a National Historic Site for its connection to Macdonald.",
            "Features": "Guided tours, restored 1840s rooms, and exhibits about Canada’s early political history."
        }
        # More landmarks can be added here
    },
    "Nature": {
        # Add nature landmarks data here in a similar structure
    },
    "Cultural": {
        # Add cultural landmarks data here in a similar structure
    }
}

if menu == "Home":
    # Home page: Introduction to Compass Chronicles and what it offers
    st.header("Welcome to Compass Chronicles: Kingston!")
    st.write("""
        Use your phone as a compass to uncover Kingston's landmarks, collect badges, 
        access local deals, and learn about the city’s rich history and culture.
    """)
    st.image("https://cck-app.streamlit.app/home_image.png", caption="Discover Kingston")

elif menu == "Categories":
    # Categories page: Allow the user to select a category to explore
    st.header("Choose a Category")
    categories = ["Engineer", "Historical", "Nature", "Cultural"]
    category = st.selectbox("Explore by Category", categories)
    st.write(f"You selected the {category} category.")

elif menu == "Landmarks":
    # Landmarks page: Allow the user to select a category and landmark to see details
    st.header("Landmarks")
    category = st.selectbox("Select a Category", list(landmarks_data.keys()))  # Category selection
    landmark = st.selectbox("Select a Landmark", list(landmarks_data[category].keys()))  # Landmark selection
    
    details = landmarks_data[category][landmark]  # Retrieve selected landmark details
    
    # Display landmark image and information
    st.image(details["Image"], caption=landmark)
    st.write(f"**Distance:** {details['Distance']}")
    st.write(f"**Fun Fact:** {details['Fun Fact']}")
    st.write(f"**History:** {details['History']}")
    st.write(f"**Features:** {details['Features']}")

elif menu == "Your Badges":
    # Your Badges page: Display a list of badges the user has unlocked
    st.header("Your Badges")
    st.write("Collect badges by visiting landmarks!")
    badges = ["Engineering Explorer", "History Buff", "Nature Lover"]
    st.write("You have unlocked the following badges:")
    for badge in badges:
        st.write(f"- {badge}")

elif menu == "Local Deals":
    # Local Deals page: Display a list of current local deals the user can claim
    st.header("Local Deals")
    st.write("Show these screens to claim your deals:")
    st.write("- **Common Ground Coffeehouse:** 10% off any drink today!")
    st.write("- **The Grad Club:** Free appetizer with any meal!")

elif menu == "About the App":
    # About the App page: Information about the app's purpose and technology stack
    st.header("About Compass Chronicles")
    st.write("""
        Compass Chronicles: Kingston is your ultimate guide to exploring the city. 
        Discover landmarks, learn fascinating facts, collect badges, and unlock local deals.
        Built with Python and Streamlit.
    """)
