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
    }
    "Joseph S. Stauffer Library": {
      "Distance": "550m",
      "Fun Fact": "The largest library on Queen’s campus, with room for approximately 1.5 million volumes.",
      "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/s/staufferlibrary/b-stauff.jpg",
      "History": "Constructed with a substantial donation from the Stauffer Foundation, supports Queen's academic community.",
      "Features": "Various study spaces, including group and individual spaces, and home to the Adaptive Technology Centre."
    }
    "Goodwin Hall": {
      "Distance": "230m",
      "Fun Fact": "In 1989, it was connected to Walter Light Hall to create a multi-million dollar technology center.",
      "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/g/goodwinhall/b-goodw.jpg",
      "History": "Completed in 1972 and named after William Lawton Goodwin, the first director of the School of Mining and Agriculture.",
      "Features": "Houses specialized labs including the Human Media Lab, with advanced interactive technology."
    }
    "Jeffery Hall": {
      "Distance": "450m",
      "Fun Fact": "Designed with three floors underground to preserve the view of Grant Hall's tower.",
      "Image": "https://rjbourgon.com/wp-content/uploads/2021/09/Jeffrey-Hall-1-1080x720.jpg",
      "History": "Completed in 1969, named after Ralph L. Jeffery, Head of Mathematics from 1943 to 1960.",
      "Features": "Classrooms with modern technology and flexible seating, offering various room options for teaching."
    }
    "Ellis Hall": {
      "Distance": "400m",
      "Fun Fact": "Houses the Queen's Observatory on its roof.",
      "Image": "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/e/ellishall/b-ellis.jpg",
      "History": "Completed in 1958, named after Douglas Stewart Ellis, former Dean of Applied Science at Queen’s.",
      "Features": "Modern classrooms with teaching technologies, including high-tech active learning classrooms."
    }
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
    }
    "Bellevue House": {
      "Distance": "1400m",
      "Fun Fact": "Home to Canada’s first Prime Minister, Sir John A. Macdonald, during a pivotal period in his career.",
      "Image": "https://media-cdn.tripadvisor.com/media/photo-s/0f/db/05/7c/canada-s-1st-pm-jamacdoanld.jpg",
      "History": "Built in the 1840s, Bellevue House was designated a National Historic Site for its connection to Macdonald.",
      "Features": "Guided tours, restored 1840s rooms, and exhibits about Canada’s early political history."
    }
    "Kingston City Hall": {
      "Distance": "1500m",
      "Fun Fact": "The building’s dome and tholobate are key features of its Neoclassical design.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Kingston_City_Hall.JPG/800px-Kingston_City_Hall.JPG",
      "History": "Completed in 1844, designed by George Browne, and designated a National Historic Site in 1961.",
      "Features": "Municipal offices, self-guided tours, and exhibitions in the Market Wing Cultural Space."
    }
    "Kingston Penitentiary": {
      "Distance": "2200m",
      "Fun Fact": "Canada’s oldest maximum-security prison, housing notorious criminals for 178 years.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Kingston_Penitentiary.jpg",
      "History": "Constructed in 1833-1834, it operated as a self-sustaining facility.",
      "Features": "Guided tours, original cellblocks, workshops, and the Canada’s Penitentiary Museum."
    }
    "Murney Tower": {
      "Distance": "800m",
      "Fun Fact": "One of the finest Martello towers in North America, built during the Oregon Crisis of 1845-46.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/6/60/Murney_Tower.jpg",
      "History": "Originally a military fortification, now a museum since 1925.",
      "Features": "Exhibits of military and domestic artifacts, a circular gun platform with a Blomefield cannon."
    }
    "Martello Alley": {
      "Distance": "1500m",
      "Fun Fact": "Inspired by La Rue du Trésor in Québec City, offering art from local artists.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Martello_Alley_Kingston.jpg",
      "History": "A neglected passageway transformed into a vibrant art gallery.",
      "Features": "Original and printed artwork from local artists, and the chance to meet them in person."
    }
  },
    "Nature": {
    "Lake Ontario Park": {
      "Distance": "3900m",
      "Fun Fact": "Kingston’s largest urban waterfront park, revitalized in 2013.",
      "Image": "https://www.cityofkingston.ca/documents/10180/12235/ontario-park.jpg",
      "History": "Established in 1894, it serves as a major natural space for Kingston residents.",
      "Features": "Sandy beach, walking paths, picnic areas, splash pad, boat launch, and fishing areas."
    }
    "Lemoine Point": {
      "Distance": "12200m",
      "Fun Fact": "Home to a variety of ecosystems, including forests, wetlands, and meadows.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Lemoine_Point_Conservation_Area.jpg",
      "History": "Established in 1992 to protect and showcase the area's natural beauty.",
      "Features": "Over 10 kilometers of trails, scenic views of Lake Ontario, and opportunities for birdwatching and fishing."
    }
    "Little Cataraqui Creek Conservation Area": {
      "Distance": "7000m",
      "Fun Fact": "A 136-hectare park offering diverse ecosystems for exploration.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Little_Cataraqui_Creek_Conservation_Area.jpg",
      "History": "Developed in 1992 to protect the area's natural landscapes.",
      "Features": "Walking and cycling trails, birdwatching, and fishing opportunities."
    }
    "Portsmouth Olympic Harbour": {
      "Distance": "3100m",
      "Fun Fact": "Built for the 1976 Olympics and continues to host Olympic Training Regattas.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Portsmouth_Olympic_Harbour.jpg",
      "History": "Built for the 1976 Olympics, still serving as a major regatta venue.",
      "Features": "250 slip docks, fuel services, pump-out facilities, and meeting rooms."
    }
    "Battery Park": {
      "Distance": "1200m",
      "Fun Fact": "Named after the Mississauga Battery that once occupied the site.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Battery_Park_Kingston.jpg",
      "History": "Developed to revitalize Kingston’s waterfront, with ties to historical military use.",
      "Features": "Waterfront pathways, scenic views, and community events."
    }
    "Grass Creek Park": {
      "Distance": "17100m",
      "Fun Fact": "Home to the MacLachlan Woodworking Museum, hosting exhibits and programming from May to September.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/d/d1/Grass_Creek_Park_Kingston.jpg",
      "History": "A popular natural retreat for locals, established along the St. Lawrence River.",
      "Features": "Sandy beach, picnic tables, hiking trails, and an off-leash dog area."
    }
  },
    "Cultural": {
    "The Grand Theatre": {
      "Distance": "1000m",
      "Fun Fact": "A heritage property, contributing to Kingston's arts scene.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/d/df/The_Grand_Theatre_in_Kingston.jpg",
      "History": "Established in the early 20th century, a cornerstone of Kingston's arts scene.",
      "Features": "Intimate auditorium with 600 seats, state-of-the-art sound and lighting systems."
    }
    "Tett Centre for Creativity and Learning": {
      "Distance": "1700m",
      "Fun Fact": "Home to nine arts organizations and eight Creativity Studio Artists.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Tett_Centre_Kingston.jpg",
      "History": "The J.K. Tett heritage building was renovated in 2015 to house the centre.",
      "Features": "Classes, workshops, exhibitions, and studio spaces for artists."
    }
    "Isabel Bader Centre": {
      "Distance": "1700m",
      "Fun Fact": "Named after philanthropist Isabel Bader, a patron of the arts.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/6/63/Isabel_Bader_Centre_Kingston.jpg",
      "History": "Opened in 2014, it has become a cultural hub in Kingston.",
      "Features": "A 566-seat concert hall, black-box theatre, rehearsal spaces, and classrooms."
    }
    "Skeleton Park": {
      "Distance": "1500m",
      "Fun Fact": "Hosts the annual Skeleton Park Arts Festival.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Skeleton_Park_Kingston.jpg",
      "History": "Once a burial ground, now a community hub for local arts and events.",
      "Features": "Sports facilities, playground, and green spaces, with the Skeleton Park Arts Festival."
    }
    "Slush Puppie Place": {
      "Distance": "1900m",
      "Fun Fact": "The venue’s rebranding in 2023 honors a partnership with Slush Puppie Canada.",
      "Image": "https://upload.wikimedia.org/wikipedia/commons/7/7f/Slush_Puppie_Place_Kingston.jpg",
      "History": "Previously the K-Rock Centre, rebranded in 2023.",
      "Features": "Versatile space with 5,000 seats, premium seating, and modern amenities."
    }
},

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
