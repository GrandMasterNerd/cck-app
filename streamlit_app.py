import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
import firebase_admin
from firebase_admin import credentials, db
import json

# Setting custom page config
st.set_page_config(
    page_title="Compass Chronicles: Kingston",
    page_icon="🧭",
    layout="centered",
)

# Initialize session state for progress tracking
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if "visited_landmarks" not in st.session_state:
    st.session_state["visited_landmarks"] = {}

# Custom CSS for styling and animations
st.markdown("""
    <style>
        body {
            background-color: #f8f4e3;
            font-family: 'Arial', sans-serif;
        }
        .main {
            color: #3e2723;
            font-size: 18px;
            animation: fadeIn 2s ease-in;
        }
        h1, h2, h3 {
            color: #3e2723;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            animation: bounce 1.5s infinite alternate;
        }
        .stButton button {
            background-color: #8d6e63;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 8px 16px;
            cursor: pointer;
            transition: transform 0.2s;
        }
        .stButton button:hover {
            background-color: #5d4037;
            transform: scale(1.1);
        }
        .stImage img {
            border: 4px solid #6d4c41;
            border-radius: 10px;
        }
        .info-card {
            background-color: #f9f4ec;
            border-radius: 10px;
            padding: 15px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
            animation: slideIn 2s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes bounce {
            from { transform: translateY(0); }
            to { transform: translateY(-10px); }
        }
        @keyframes slideIn {
            from { transform: translateX(-100%); }
            to { transform: translateX(0); }
        }
    </style>
""", unsafe_allow_html=True)

# Landmarks data in the four categories
landmarks_data = {
    "Engineer": {
        "Beamish-Munro Hall": {
            "Distance": "0m",
            "Fun Fact": "Beamish-Munro Hall contains the Integrated Learning Centre and is the home of the Stephen J.R. Smith Faculty of Engineering and Applied Science at Queen’s University.",
            "History": "Beamish-Munro Hall opened its doors in May 2004 and was recognized by the Sustainable Buildings '05 Canadian Team as one of the most environmentally advanced buildings in Canada in 2005.",
            "Features": "Beamish-Munro Hall was designed as a 'live building' to lean into the integrated learning component for engineering students. The building is constructed so that students can see structural elements of the building that are typically hidden and monitor systems such as air quality, heating, lighting, and cooling via specially designed software, demonstrating how sustainable practices can be integrated into building design. Contained in the building is a design studio, a prototyping centre, group rooms, a multimedia facility, a site investigation facility, active learning centre and plazas or lab facilities.",
            "Latitude": 44.2280082,
            "Longitude": -76.4927247
        },
        "Joseph S. Stauffer Library": {
            "Distance": "550m",
            "Fun Fact": "Stauffer Library is the biggest library on Queen’s campus, with five floors and room for approximately 1.5 million volumes, six kilometres of bookstacks, and study and research space for over 1,200 students.",
            "History": "The library was constructed with a substantial donation from the Stauffer Foundation, enabling the creation of a state-of-the-art facility to support the university's academic community.",
            "Features": "Stauffer Library provides a variety of study spaces, including group study tables and individual study carrels. It also offers computers, scanners, photocopiers, and printers for student use. The library is home to the Adaptive Technology Centre, which includes Library Accessibility Services, an Adaptive Technology Lab, and offices for the Adaptive Technologist and Accessibility Coordinator. Elevators in the library are wheelchair accessible, with controls inside the elevators being Brailled.",
            "Latitude": 44.2285509,
            "Longitude": -76.496171
        },
        "Goodwin Hall": {
            "Distance": "230m",
            "Fun Fact": "In 1989, Goodwin Hall was connected to the newly constructed Walter Light Hall, creating a multi-million dollar technology center to accommodate the growing needs of the Department of Electrical and Computer Engineering.",
            "History": "Completed in 1972, it is named after William Lawton Goodwin, the first director of the School of Mining and Agriculture, the precursor to the Faculty of Engineering and Applied Science. Goodwin Hall houses the Robert M. Buchan Department of Mining, the School of Computing, and the Human Mobility Research Centre, a collaboration between Queen's University and Kingston Health Sciences Centre.",
            "Features": "The building offers specialized laboratories, including the Human Media Lab, which features a 16-by-9 feet interactive flexible display with gesture technology.",
            "Latitude": 44.2279564,
            "Longitude": -76.492418
        },
        "Jeffery Hall": {
            "Distance": "450m",
            "Fun Fact": "The building was designed with three floors underground and three floors above ground to preserve the view of Grant Hall's tower across University Avenue.",
            "History": "Completed in 1969, it is named after Ralph L. Jeffery, Head of Mathematics and Chair of Graduate Studies from 1943 to 1960. Jeffery Hall houses the Department of Mathematics and Statistics, providing specialized facilities for students and faculty.",
            "Features": "The building offers a variety of classrooms equipped with modern technology and flexible seating arrangements to accommodate different teaching and learning styles. From tiered lecture halls to active learning spaces, Jeffery Hall provides a range of room options to support educational activities.",
            "Latitude": 44.2259069,
            "Longitude": -76.4960893
        },
        "Ellis Hall": {
            "Distance": "400m",
            "Fun Fact": "Ellis Hall houses the Queen's Observatory, which is situated on its roof.",
            "History": "Completed in 1958, it is named after Douglas Stewart Ellis, a distinguished professor of Civil Engineering and former Dean of Applied Science at Queen's. Constructed to alleviate the pressure on the Engineering faculty due to increased demand for scientific courses post-World War II, Ellis Hall has long been home to the Department of Civil Engineering and the Queen's Observatory.",
            "Features": "The building offers several classrooms equipped with modern teaching technologies, including document cameras, lecture capture systems, wireless presentation capabilities, and room PCs. Notably, Room 324 is designed as a high-tech, team-based active learning classroom, featuring a height-adjustable podium with microphones and display cables.",
            "Latitude": 44.2263388,
            "Longitude": -76.4962195
        },
        "Dupuis Hall": {
            "Distance": "220m",
            "Fun Fact": "The exterior of Dupuis Hall features decorative limestone facing, a design choice made to appease those who preferred traditional architectural elements on campus.",
            "History": "Dupuis Hall was completed in 1966 and is named after Nathan Fellowes Dupuis, an influential professor of mathematics at Queen's in the late 19th and early 20th centuries, and a founder of the engineering and applied science faculty.",
            "Features": "The building houses several classrooms and an auditorium, including Room 215, which is equipped with a podium, microphones, and a document camera. The auditorium is accessible for students, featuring a podium with lecture capture capabilities and display cables.",
            "Latitude": 44.2285734,
            "Longitude": -76.492709
        }
    },
    "Historical": {
        "Fort Henry": {
            "Distance": "4600m",
            "Fun Fact": "The fort and Point Henry are named after Henry Hamilton, who was the Lieutenant Governor of Quebec. The fort cost 70,000 British pounds sterling to build, which is about $35 million in modern Canadian currency.",
            "Image": "https://www.tripsavvy.com/thmb/_Jk2Q-Mww_1DvT68onhqZX_QmaQ=/2573x2038/filters:no_upscale():max_bytes(150000):strip_icc()/FortHenry-59f0e1d8d088c00010f2c09a.jpg",
            "History": "Fort Henry in Kingston, Ontario, Canada is a 19th-century British military fortress that protected the Rideau Canal and the town of Kingston. The fort was built to replace an earlier fortification from the War of 1812.",
            "Features": "Fort Henry offers guided tours that immerse visitors in the daily life of a 19th-century military fort. Guests can explore interactive exhibits, watch live demonstrations of artillery drills, and enjoy stunning views of the Kingston waterfront from the fort's ramparts. The site also features a museum, gift shop, and on-site café to complete the experience."
        },
        "Bellevue House": {
            "Distance": "1400m",
            "Fun Fact": "Bellevue House was once home to Sir John A. Macdonald, Canada’s first Prime Minister, and is one of the few remaining examples of Italianate villa architecture in the country. The house’s unique design includes a picturesque tower, decorative verandas, and a sprawling garden.",
            "Image": "https://media-cdn.tripadvisor.com/media/photo-s/0f/db/05/7c/canada-s-1st-pm-jamacdoanld.jpg",
            "History": "Built in the 1840s, Bellevue House served as the residence of Macdonald during a pivotal period in his political career. The house was later designated a National Historic Site to commemorate its connection to one of Canada’s most influential leaders.",
            "Features": "Bellevue House offers guided tours that delve into the life and legacy of Sir John A. Macdonald, with interpreters dressed in period attire. Visitors can explore restored rooms furnished to reflect the 1840s, stroll through beautifully landscaped grounds, and engage with exhibits that highlight Canada’s early political history. A visitor center and gift shop are also available on-site."
        },
        "Kingston City Hall": {
            "Distance": "1500m",
            "Fun Fact": "Kingston City Hall, completed in 1844, was designed by architect George Browne in the Neoclassical style, featuring a prominent dome and tholobate. It was designated a National Historic Site of Canada in 1961.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Kingston_City_Hall_%28NHSC_chart%29.jpg/1200px-Kingston_City_Hall_%28NHSC_chart%29.jpg",
            "History": "Originally serving as a city hall, market, custom house, post office, police station, and jail, the building reflects Kingston's status as the capital of the Province of Canada at the time of its construction.",
            "Features": "Kingston City Hall houses municipal offices and the council chambers. The building is open to the public during regular business hours, offering self-guided tours of public spaces on the first and second floors. Visitors can explore the Market Wing Cultural Space, which hosts exhibitions and programming that share diverse and inclusive stories of Kingston. The adjacent Confederation Park features a large arch with a fountain and the Confederation Basin Marina, enhancing the city's waterfront experience."
        },
        "Kingston Penitentiary": {
            "Distance": "2200m",
            "Fun Fact": "Kingston Penitentiary, established in 1835, is Canada's oldest maximum-security prison and housed some of the nation's most notorious criminals over its 178-year history.",
            "Image": "https://www.kingstonpentour.com/wp-content/uploads/sites/5/2022/02/Tours.jpg",
            "History": "Constructed in 1833-1834 and opening its doors on June 1, 1835, Kingston Penitentiary was designed to be self-sustaining, featuring its own quarries and farm.",
            "Features": "Visitors can explore the penitentiary's original cellblocks, workshops, and guard towers, offering a glimpse into the daily life of inmates and the prison's operations. Guided tours provide in-depth insights into the facility's history, architecture, and the stories of its former inhabitants. The site also includes the former warden's residence, now the Canada’s Penitentiary Museum, and the former deputy warden’s house, now the Isabel McNeil House."
        },
        "Murney Tower": {
            "Distance": "800m",
            "Fun Fact": "Murney Tower, constructed in 1846, is one of the finest Martello towers in North America. It was designed to defend Kingston Harbour during the Oregon Crisis of 1845-46.",
            "Image": "https://static1.squarespace.com/static/602d209dc643b55054f0eef8/t/6081b63a843276355a5f4024/1619113532445/Main+Image.jpg?format=1500w",
            "History": "Originally built as a military fortification, Murney Tower has served various purposes over the years, including as a barracks and a prison. Since 1925, it has operated as a museum, showcasing artifacts from 19th-century Kingston.",
            "Features": "The tower features a circular gun platform designed to hold two cannons, a 24-pounder and a 32-pounder. Only the 32-pounder Blomefield cannon was ever installed, and it remains at the tower today. Visitors can explore three floors displaying military and domestic artifacts, including a gunpowder magazine and various store rooms. The lower level also features the gunpowder magazine and various store rooms. The museum offers guided tours, audio tours, educational programs, special events, and exhibits."
        },
        "Martello Alley": {
            "Distance": "1500m",
            "Fun Fact": "Martello Alley, located at 203 B Wellington Street in downtown Kingston, is an art-themed historic alley inspired by La Rue du Trésor in Québec City. It offers a unique art shopping experience designed for any budget and any style or size of space.",
            "Image": "https://images.squarespace-cdn.com/content/v1/63f148e1dcd0c50bed93395b/1691435652600-7TKOT9YNUV2KWRS01ZE0/Martello-Alley-Wedding-Venue-2.PNG?format=1000w",
            "History": "Once a neglected passageway, Martello Alley has been transformed into a vibrant art gallery showcasing the works of local artists. The alley features original and printed artwork, providing a space to meet the artists and see their work in progress.",
            "Features": "Visitors can explore a variety of art forms, including paintings, prints, and other creative works, all displayed in a charming courtyard rich with local history and seasonal landscape design. The gallery is open daily from 10:00 am to 5:00 pm, with artists on duty to engage with visitors. For those unable to visit in person, Martello Alley offers a virtual shop accessible through their website."
        }
    },
    "Nature": {
        "Lake Ontario Park": {
            "Distance": "3900m",
            "Fun Fact": "Kingston’s largest urban waterfront park, revitalized in 2013.",
            "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToeBGnbApsWb-0CEmHeUTtPTE4N1fpYdpOOQ&s",
            "History": "Established in 1894, the park has evolved into a significant natural landscape, drawing both visitors and residents for picnicking and scenic walks along the waterfront.",
            "Features": "The park offers a sandy beach area, a splash pad, and a playground for children. Visitors can enjoy walking and cycling paths, a boat launch, picnic tables, and barbecue facilities. The park also features a waterfront terrace lookout, public fishing areas, and accessible washrooms."
        },
        "Lemoine Point": {
            "Distance": "12200m",
            "Fun Fact": "Home to a variety of ecosystems, including forests, wetlands, and meadows.",
            "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRxdtnpNDXuemnsf2lip7EWAawpk2RYVIjZsw&s",
            "History": "Established in 1992, Lemoine Point Conservation Area was developed to protect and showcase the area's natural beauty. It serves as a vital green space for both wildlife and the local community.",
            "Features": "The park offers over 10 kilometers of trails suitable for walking, cycling, and birdwatching. Visitors can enjoy scenic views of Lake Ontario, access to the waterfront, and opportunities for fishing. The area also features picnic spots and educational signage about local flora and fauna."
        },
        "Little Cataraqui Creek Conservation Area": {
            "Distance": "7000m",
            "Fun Fact": "A 136-hectare park offering diverse ecosystems for exploration.",
            "Image": "https://crca.ca/wp-content/uploads/LilCatOutdoorCentre04.jpg",
            "History": "Developed in 1992 to protect the area's natural landscapes.",
            "Features": "Walking and cycling trails, birdwatching, and fishing opportunities."
        },
        "Portsmouth Olympic Harbour": {
            "Distance": "3100m",
            "Fun Fact": "Built for the 1976 Olympics and continues to host Olympic Training Regattas.",
            "Image": "https://img.marinas.com/v2/cc7741f3d34d79990c5f24b991f474f8fc5a8c978ed63222ac787d1b946568cc.jpg",
            "History": "Built for the 1976 Olympics, still serving as a major regatta venue.",
            "Features": "250 slip docks, fuel services, pump-out facilities, and meeting rooms."
        },
        "Battery Park": {
            "Distance": "1200m",
            "Fun Fact": "Named after the Mississauga Battery that once occupied the site.",
            "Image": "https://i2.wp.com/media.globalnews.ca/videostatic/news/z6qxetas8j-ngnobyrtt6/051_9954.MXF.07_49_30_19.Still001.jpg?w=1040&quality=70&strip=all",
            "History": "Developed to revitalize Kingston’s waterfront, with ties to historical military use.",
            "Features": "Waterfront pathways, scenic views, and community events."
        },
        "Grass Creek Park": {
            "Distance": "17100m",
            "Fun Fact": "Home to the MacLachlan Woodworking Museum, hosting exhibits and programming from May to September.",
            "Image": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/14/08/27/0e/lake-ontario-park-kingston.jpg?w=300&h=300&s=1",
            "History": "A popular natural retreat for locals, established along the St. Lawrence River.",
            "Features": "Sandy beach, picnic tables, hiking trails, and an off-leash dog area."
        }
    },
    "Cultural": {
        "The Grand Theatre": {
            "Distance": "1000m",
            "Fun Fact": "A heritage property, contributing to Kingston's arts scene.",
            "Image": "https://www.kingstongrand.ca/sites/kingstongrand.ca/files/img/page/teaser/how-to-book-tickets-teaser.jpg",
            "History": "Established in the early 20th century, a cornerstone of Kingston's arts scene.",
            "Features": "Intimate auditorium with 600 seats, state-of-the-art sound and lighting systems."
        },
        "Tett Centre for Creativity and Learning": {
            "Distance": "1700m",
            "Fun Fact": "Home to nine arts organizations and eight Creativity Studio Artists.",
            "Image": "https://akimbo.ca/wp-content/uploads/2021/10/oct27_tettcentre1.jpg",
            "History": "The J.K. Tett heritage building was renovated in 2015 to house the centre.",
            "Features": "Classes, workshops, exhibitions, and studio spaces for artists."
        },
        "Isabel Bader Centre": {
            "Distance": "1700m",
            "Fun Fact": "Named in honor of Isabel Bader, a patron of the arts.",
            "Image": "https://www.mgac.com/wp-content/uploads/2022/12/Isabel-Bader_feature.jpg",
            "History": "Opened in 2014, it has become a cornerstone of Kingston's cultural landscape.",
            "Features": "566-seat concert hall, studio theatre, rehearsal spaces, and educational programs."
        },
        "Skeleton Park": {
            "Distance": "1500m",
            "Fun Fact": "Hosts the annual Skeleton Park Arts Festival.",
            "Image": "https://lh5.googleusercontent.com/p/AF1QipOT2hoQXEL7DalHmKKJwvggDNHhIdlEZt_ngmMF",
            "History": "Formerly a burial ground, now a vibrant community space.",
            "Features": "Playground, sports facilities, open green spaces, and annual arts festival."
        },
        "Slush Puppie Place": {
            "Distance": "1900m",
            "Fun Fact": "Reflects a partnership between Slush Puppie Canada and Kingston.",
            "Image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRL8Vl2kJQOgpPo7EylYBuoNe35QzeMR0JB3w&s",
            "History": "Opened as the K-Rock Centre in 2008, rebranded in 2023.",
            "Features": "5,000-seat venue with premium seating, concessions, and modern amenities."
        }
    }
}
# Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
    
# Function to calculate progress percentage
def calculate_progress(category):
    visited = len(st.session_state.visited_landmarks.get(category, []))
    total = len(landmarks_data[category])
    return int((visited / total) * 100) if total > 0 else 0
    
# Home Page
if st.session_state["page"] == "Home":
    st.image(
        "res/Make a logo for this app_ Use your phone as a compass to uncover landmarks, collect badges, and access local deals, all while discovering the city’s rich history and culture. Make a logo. Include the words _Compass.jpg",  # Replace with actual logo URL
        caption="\U0001F6F1 Compass Chronicles: Kingston",
        use_container_width=True
    )
    st.header("🧭 Welcome to Compass Chronicles: Kingston")
    st.write("""
        **Embark on an Adventure!**  
        Use your phone as a compass to uncover hidden treasures around Kingston.  
        Discover landmarks, collect badges, unlock deals, and immerse yourself in history and culture!
    """)
    if st.button("Start Exploring"):
        st.session_state["page"] = "Categories"
    elif st.button("Promotions"):
        st.session_state["page"] = "Promotions"
    elif st.button("Project Details"):
        st.session_state["page"] = "Details"

# Promotions Page
if st.session_state["page"] == "Promotions":
    st.header("\U0001F3F7 Exclusive Deals!")
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg", 
        caption="\U0001F4F1 Scan to Redeem Deals", 
        use_container_width=True
    )
    st.write("\U0001F389 Show this screen to claim your treasure:")
    st.write("- **Common Ground Coffeehouse:** 10% off any drink today!")
    st.write("- **The Grad Club:** Free appetizer with any meal!")
    if st.button("Back to Home"):
        st.session_state["page"] = "Home"

# Project Details Page
if st.session_state["page"] == "Details":
    st.header("📜 Project Details")
    st.markdown("""
        #### 🚀 Elevator Pitch
        Explore Kingston with Compass Chronicles! Use your phone as a compass to uncover landmarks, collect badges, and access local deals, all while discovering the city’s rich history and culture.
        
        #### 🌟 Inspiration
        Inspired by Kingston's rich history, vibrant culture, and unique landmarks, we created an interactive experience that blends exploration, education, and gamified rewards. Our goal is to encourage locals and visitors to discover the city in a fun and engaging way.
        
        #### 🔍 What It Does
        Compass Chronicles: Kingston acts as your personal tour guide, utilizing GPS and compass functionalities to navigate you to landmarks. Key features include:

        - Unlocking historical insights and fun facts.
        - Earning badges for visiting specific locations.
        - Accessing exclusive local deals.
        - Navigating to the next landmark or exploring nearby spots.
        
        #### 🛠️ How We Built It
        - **Frontend:** Built with Streamlit for an intuitive and user-friendly interface.
        - **Backend:** Powered by Python scripts for GPS integration, badge tracking, and deal distribution.
        - **Hosting:** Deployed using GoDaddy for reliable online accessibility.
        - **Hardware:** Implemented an ESP8266-based proximity beacon for location-triggered notifications.
        
        #### 🎯 Challenges
        - Integrating real-time GPS data with compass navigation.
        - Designing a seamless badge-earning system.
        - Ensuring accurate proximity detection using the ESP8266 beacon.
        - Balancing functionality with a clean, user-friendly interface.
        
        #### 🏆 Accomplishments
        - Created an engaging and educational user experience.
        - Developed a gamified system to motivate exploration.
        - Set up an ESP8266 beacon for proximity-triggered notifications.
        - Partnered with local businesses to offer exclusive deals to users.
        
        #### 🌟 What's Next?
        - Expanding the app to include more landmarks and historical data.
        - Collaborating with additional local businesses for more deals.
        - Adding multi-language support for international visitors.
        - Integrating AR (Augmented Reality) features for an even more immersive experience.
        - Enhancing the notification system for improved proximity detection and customization.
    """)


    # Meet the Founders Section
    st.subheader("🤝 Meet the Founders")
    founders = {
        "Nolan Verboomen": "res/nolanheadshot.jpg",
        "Adam Likogiannis": "res/IMG_0116.2.jpg",
        "Aidan Murray": "res/image (10).png",
        "Eiqan Ahsan": "res/eiqanheadshot.png"
    }
    cols = st.columns(len(founders))
    for col, (name, img_url) in zip(cols, founders.items()):
        with col:
            st.image(img_url, caption=name, use_container_width=True)

    if st.button("Back to Home"):
        st.session_state["page"] = "Home"

# Categories and Landmarks Page
if st.session_state["page"] == "Categories":
    st.header("\U0001F5FA Choose Your Adventure")
    category = st.selectbox("\U0001F4C2 Select a Category", list(landmarks_data.keys()))

    if category:
        # Display progress bar
        st.subheader(f"Progress in {category}")
        progress = calculate_progress(category)
        st.progress(progress / 100)

        # Reset progress button
        if st.button("Reset Progress"):
            st.session_state.visited_landmarks[category] = []
            st.success(f"Progress for {category} has been reset!")

        st.subheader(f"\U0001F4CD Landmarks in {category}")
        landmark = st.selectbox("\U0001F3DB Select a Landmark", list(landmarks_data[category].keys()))

        if landmark:
            details = landmarks_data[category][landmark]
            st.image(details["Image"], caption=landmark, use_container_width=True)
            st.write(f"**Distance:** {details['Distance']}")
            st.write(f"**Fun Fact:** {details['Fun Fact']}")
            st.write(f"**History:** {details['History']}")
            st.write(f"**Features:** {details['Features']}")

            # Mark as visited
            if category not in st.session_state.visited_landmarks:
                st.session_state.visited_landmarks[category] = []

            if landmark not in st.session_state.visited_landmarks[category]:
                st.session_state.visited_landmarks[category].append(landmark)
                st.success(f"You've visited {landmark}!")

        if st.button("Back to Home"):
            st.session_state["page"] = "Home"


# Access Firebase credentials from Streamlit secrets
firebase_cred = {
    "type": st.secrets["firebase_credentials"]["type"],
    "project_id": st.secrets["firebase_credentials"]["project_id"],
    "private_key_id": st.secrets["firebase_credentials"]["private_key_id"],
    "private_key": st.secrets["firebase_credentials"]["private_key"],
    "client_email": st.secrets["firebase_credentials"]["client_email"],
    "client_id": st.secrets["firebase_credentials"]["client_id"],
    "auth_uri": st.secrets["firebase_credentials"]["auth_uri"],
    "token_uri": st.secrets["firebase_credentials"]["token_uri"],
    "auth_provider_x509_cert_url": st.secrets["firebase_credentials"]["auth_provider_x509_cert_url"],
    "client_x509_cert_url": st.secrets["firebase_credentials"]["client_x509_cert_url"]
}

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_cred)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://cck-app-91eee-default-rtdb.firebaseio.com/'
    })

# Function to write data to Firebase
def write_number_to_firebase(number):
    ref = db.reference('numbers/score')
    ref.set(number)

# Function to read data from Firebase
def read_number_from_firebase():
    ref = db.reference('numbers/score')
    return ref.get()

# Streamlit UI
st.title('Firebase Realtime Database with Streamlit')

# Input to enter a number
user_input = st.number_input('Enter a number:', min_value=0, max_value=100, step=1)

# Button to save the number to Firebase
if st.button('Save Number to Firebase'):
    write_number_to_firebase(user_input)
    st.success(f'Number {user_input} saved to Firebase.')

# Button to read the number from Firebase
if st.button('Read Number from Firebase'):
    number = read_number_from_firebase()
    st.write(f'Number from Firebase: {number}')
