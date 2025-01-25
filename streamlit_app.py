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
            "Features": "Designed as a 'live building', showing structural elements and sustainable practices, with a design studio, prototyping center, multimedia facility, and more."
        },
        "Joseph S. Stauffer Library": {
            "Distance": "550m",
            "Fun Fact": "The largest library on Queen’s campus, with room for approximately 1.5 million volumes.",
            "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/s/staufferlibrary/b-stauff.jpg",
            "History": "Constructed with a substantial donation from the Stauffer Foundation, supports Queen's academic community.",
            "Features": "Various study spaces, including group and individual spaces, and home to the Adaptive Technology Centre."
        },
        "Goodwin Hall": {
            "Distance": "230m",
            "Fun Fact": "In 1989, it was connected to Walter Light Hall to create a multi-million dollar technology center.",
            "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/g/goodwinhall/b-goodw.jpg",
            "History": "Completed in 1972 and named after William Lawton Goodwin, the first director of the School of Mining and Agriculture.",
            "Features": "Houses specialized labs including the Human Media Lab, with advanced interactive technology."
        },
        "Jeffery Hall": {
            "Distance": "450m",
            "Fun Fact": "Designed with three floors underground to preserve the view of Grant Hall's tower.",
            "Image": "https://rjbourgon.com/wp-content/uploads/2021/09/Jeffrey-Hall-1-1080x720.jpg",
            "History": "Completed in 1969, named after Ralph L. Jeffery, Head of Mathematics from 1943 to 1960.",
            "Features": "Classrooms with modern technology and flexible seating, offering various room options for teaching."
        },
        "Ellis Hall": {
            "Distance": "400m",
            "Fun Fact": "Houses the Queen's Observatory on its roof.",
            "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/e/ellishall/b-ellis.jpg",
            "History": "Completed in 1958, named after Douglas Stewart Ellis, former Dean of Applied Science at Queen’s.",
            "Features": "Modern classrooms with teaching technologies, including high-tech active learning classrooms."
        },
        "Dupuis Hall": {
            "Distance": "220m",
            "Fun Fact": "Its exterior features decorative limestone facing, chosen to maintain traditional campus aesthetics.",
            "Image": "https://th.bing.com/th/id/R.1efb7fab84ec14ec22c695c1f91bcdd5?rik=Y1BRXb2AkVTf9w&riu=http%3a%2f%2feeu.on.ca%2fp%2fwp-content%2fuploads%2f2013%2f03%2fHistory-1.jpg&ehk=V0IWAbyfO2SVt0o4zrmWUgyF8PJiKR5PLM0YI%2b2W7fw%3d&risl=&pid=ImgRaw&r=0",
            "History": "Completed in 1966 and named after Nathan Fellowes Dupuis, an influential professor at Queen's.",
            "Features": "Classrooms and an auditorium, with modern lecture capture systems and display cables."
        }
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
    }
    # Other categories can follow this same format...
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
