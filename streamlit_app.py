import streamlit as st
from PIL import Image
import requests

# Setting custom page config
st.set_page_config(
    page_title="Compass Chronicles: Kingston",
    page_icon="🧭",
    layout="centered",
)

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f8f4e3;
            font-family: 'Arial', sans-serif;
        }
        .main {
            color: #3e2723;
        }
        h1, h2, h3 {
            color: #3e2723;
        }
        .stButton button {
            background-color: #8d6e63;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 8px 16px;
            cursor: pointer;
        }
        .stButton button:hover {
            background-color: #5d4037;
        }
        .stImage img {
            border: 4px solid #6d4c41;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

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
            "Fun Fact": "The fort and Point Henry are named after Henry Hamilton, who was the Lieutenant Governor of Quebec. The fort cost 70,000 British pounds sterling to build, which is about $35 million in modern Canadian currency.",
            "Image": "https://www.tripsavvy.com/thmb/_Jk2Q-Mww_1DvT68onhqZX_QmaQ=/2573x2038/filters:no_upscale()/max_bytes(150000):strip_icc()/FortHenry-59f0e1d8d088c00010f2c09a.jpg",
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
            "Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/Kingston_City_Hall.JPG/800px-Kingston_City_Hall.JPG",
            "History": "Originally serving as a city hall, market, custom house, post office, police station, and jail, the building reflects Kingston's status as the capital of the Province of Canada at the time of its construction.",
            "Features": "Kingston City Hall houses municipal offices and the council chambers. The building is open to the public during regular business hours, offering self-guided tours of public spaces on the first and second floors. Visitors can explore the Market Wing Cultural Space, which hosts exhibitions and programming that share diverse and inclusive stories of Kingston. The adjacent Confederation Park features a large arch with a fountain and the Confederation Basin Marina, enhancing the city's waterfront experience."
        },
        "Kingston Penitentiary": {
            "Distance": "2200m",
            "Fun Fact": "Kingston Penitentiary, established in 1835, is Canada's oldest maximum-security prison and housed some of the nation's most notorious criminals over its 178-year history.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/3/3a/Kingston_Penitentiary.jpg",
            "History": "Constructed in 1833-1834 and opening its doors on June 1, 1835, Kingston Penitentiary was designed to be self-sustaining, featuring its own quarries and farm.",
            "Features": "Visitors can explore the penitentiary's original cellblocks, workshops, and guard towers, offering a glimpse into the daily life of inmates and the prison's operations. Guided tours provide in-depth insights into the facility's history, architecture, and the stories of its former inhabitants. The site also includes the former warden's residence, now the Canada’s Penitentiary Museum, and the former deputy warden’s house, now the Isabel McNeil House."
        },
        "Murney Tower": {
            "Distance": "800m",
            "Fun Fact": "Murney Tower, constructed in 1846, is one of the finest Martello towers in North America. It was designed to defend Kingston Harbour during the Oregon Crisis of 1845-46.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/6/60/Murney_Tower.jpg",
            "History": "Originally built as a military fortification, Murney Tower has served various purposes over the years, including as a barracks and a prison. Since 1925, it has operated as a museum, showcasing artifacts from 19th-century Kingston.",
            "Features": "The tower features a circular gun platform designed to hold two cannons, a 24-pounder and a 32-pounder. Only the 32-pounder Blomefield cannon was ever installed, and it remains at the tower today. Visitors can explore three floors displaying military and domestic artifacts, including a gunpowder magazine and various store rooms. The lower level also features the gunpowder magazine and various store rooms. The museum offers guided tours, audio tours, educational programs, special events, and exhibits."
        },
        "Martello Alley": {
            "Distance": "1500m",
            "Fun Fact": "Martello Alley, located at 203 B Wellington Street in downtown Kingston, is an art-themed historic alley inspired by La Rue du Trésor in Québec City. It offers a unique art shopping experience designed for any budget and any style or size of space.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/4/4d/Martello_Alley_Kingston.jpg",
            "History": "Once a neglected passageway, Martello Alley has been transformed into a vibrant art gallery showcasing the works of local artists. The alley features original and printed artwork, providing a space to meet the artists and see their work in progress.",
            "Features": "Visitors can explore a variety of art forms, including paintings, prints, and other creative works, all displayed in a charming courtyard rich with local history and seasonal landscape design. The gallery is open daily from 10:00 am to 5:00 pm, with artists on duty to engage with visitors. For those unable to visit in person, Martello Alley offers a virtual shop accessible through their website."
        }
    },
    "Nature": {
        "Lake Ontario Park": {
            "Distance": "3900m",
            "Fun Fact": "Kingston’s largest urban waterfront park, revitalized in 2013.",
            "Image": "https://www.cityofkingston.ca/documents/10180/12235/ontario-park.jpg",
            "History": "Established in 1894, the park has evolved into a significant natural landscape, drawing both visitors and residents for picnicking and scenic walks along the waterfront.",
            "Features": "The park offers a sandy beach area, a splash pad, and a playground for children. Visitors can enjoy walking and cycling paths, a boat launch, picnic tables, and barbecue facilities. The park also features a waterfront terrace lookout, public fishing areas, and accessible washrooms."
        },
        "Lemoine Point": {
            "Distance": "12200m",
            "Fun Fact": "Home to a variety of ecosystems, including forests, wetlands, and meadows.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/d/d8/Lemoine_Point_Conservation_Area.jpg",
            "History": "Established in 1992, Lemoine Point Conservation Area was developed to protect and showcase the area's natural beauty. It serves as a vital green space for both wildlife and the local community.",
            "Features": "The park offers over 10 kilometers of trails suitable for walking, cycling, and birdwatching. Visitors can enjoy scenic views of Lake Ontario, access to the waterfront, and opportunities for fishing. The area also features picnic spots and educational signage about local flora and fauna."
        },
        "Little Cataraqui Creek Conservation Area": {
            "Distance": "7000m",
            "Fun Fact": "A 136-hectare park offering diverse ecosystems for exploration.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/0/09/Little_Cataraqui_Creek_Conservation_Area.jpg",
            "History": "Developed in 1992 to protect the area's natural landscapes.",
            "Features": "Walking and cycling trails, birdwatching, and fishing opportunities."
        },
        "Portsmouth Olympic Harbour": {
            "Distance": "3100m",
            "Fun Fact": "Built for the 1976 Olympics and continues to host Olympic Training Regattas.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Portsmouth_Olympic_Harbour.jpg",
            "History": "Built for the 1976 Olympics, still serving as a major regatta venue.",
            "Features": "250 slip docks, fuel services, pump-out facilities, and meeting rooms."
        },
        "Battery Park": {
            "Distance": "1200m",
            "Fun Fact": "Named after the Mississauga Battery that once occupied the site.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/c/ce/Battery_Park_Kingston.jpg",
            "History": "Developed to revitalize Kingston’s waterfront, with ties to historical military use.",
            "Features": "Waterfront pathways, scenic views, and community events."
        },
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
        },
        "Tett Centre for Creativity and Learning": {
            "Distance": "1700m",
            "Fun Fact": "Home to nine arts organizations and eight Creativity Studio Artists.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/9/9a/Tett_Centre_Kingston.jpg",
            "History": "The J.K. Tett heritage building was renovated in 2015 to house the centre.",
            "Features": "Classes, workshops, exhibitions, and studio spaces for artists."
        },
        "Isabel Bader Centre": {
            "Distance": "1700m",
            "Fun Fact": "Named in honor of Isabel Bader, a patron of the arts.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Isabel_Bader_Centre_Kingston.jpg",
            "History": "Opened in 2014, it has become a cornerstone of Kingston's cultural landscape.",
            "Features": "566-seat concert hall, studio theatre, rehearsal spaces, and educational programs."
        },
        "Skeleton Park": {
            "Distance": "1500m",
            "Fun Fact": "Hosts the annual Skeleton Park Arts Festival.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/3/31/Skeleton_Park_Kingston.jpg",
            "History": "Formerly a burial ground, now a vibrant community space.",
            "Features": "Playground, sports facilities, open green spaces, and annual arts festival."
        },
        "Slush Puppie Place": {
            "Distance": "1900m",
            "Fun Fact": "Reflects a partnership between Slush Puppie Canada and Kingston.",
            "Image": "https://upload.wikimedia.org/wikipedia/commons/4/47/Slush_Puppie_Place_Kingston.jpg",
            "History": "Opened as the K-Rock Centre in 2008, rebranded in 2023.",
            "Features": "5,000-seat venue with premium seating, concessions, and modern amenities."
        }
    }
}
if menu == "Home":
    # Home page: Introduction to Compass Chronicles and what it offers
    st.header("Welcome to Compass Chronicles: Kingston!")
    st.write("""
        Use your phone as a compass to uncover Kingston's landmarks, collect badges, 
        access local deals, and learn about the city’s rich history and culture.
    """)

    if st.button("Start Exploring"):  # Large button to navigate to categories
        st.session_state["navigate_to_categories"] = True

    if st.session_state.get("navigate_to_categories", False):
        st.header("Choose a Category")
        categories = ["Engineer", "Historical", "Nature", "Cultural"]
        category = st.selectbox("Explore by Category", categories)
        st.write(f"You selected the {category} category.")

        if category in landmarks_data:
            st.subheader(f"Landmarks in {category}")
            landmark = st.selectbox("Select a Landmark", list(landmarks_data[category].keys()))
            details = landmarks_data[category][landmark]

            # Display landmark details
            st.image(details["Image"], caption=landmark, use_container_width=True)
            st.write(f"**Distance:** {details['Distance']}")
            st.write(f"**Fun Fact:** {details['Fun Fact']}")
            st.write(f"**History:** {details['History']}")
            st.write(f"**Features:** {details['Features']}")

elif menu == "Your Badges":
    # Your Badges page: Display a list of badges the user has unlocked
    st.header("Your Badges")
    st.write("Collect badges by visiting landmarks!")

    badges = {
        "Engineering Explorer": {"Image": "https://placeholder-for-engineering-badge", "Collected": True},
        "History Buff": {"Image": "https://placeholder-for-history-badge", "Collected": False},
        "Nature Lover": {"Image": "https://placeholder-for-nature-badge", "Collected": True},
        "Cultural Enthusiast": {"Image": "https://placeholder-for-cultural-badge", "Collected": False},
    }

    cols = st.columns(4)
    for col, (badge, data) in zip(cols, badges.items()):
        image = data["Image"]
        collected = data["Collected"]
        if collected:
            col.image(image, caption=badge, use_container_width=True)
        else:
            greyed_out = Image.open(requests.get(image, stream=True).raw).convert("LA")
            col.image(greyed_out, caption=f"{badge} (Locked)", use_container_width=True)

elif menu == "Local Deals":
    # Local Deals page: Display a list of current local deals the user can claim
    st.header("Local Deals")
    st.image("https://placeholder-for-qr-code", caption="Scan to Redeem Deals", use_container_width=True)
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
    st.subheader("Meet the Founders")
    founder_images = [
        "https://placeholder-for-nolan", 
        "https://placeholder-for-adam", 
        "https://placeholder-for-eiqan", 
        "https://placeholder-for-aidan"
    ]
    founder_names = ["Nolan Verboomen", "Adam Likogiannis", "Eiqan Ahsan", "Aidan Murray"]

    cols = st.columns(len(founder_images))
    for col, img, name in zip(cols, founder_images, founder_names):
        col.image(img, caption=name, use_container_width=True)

