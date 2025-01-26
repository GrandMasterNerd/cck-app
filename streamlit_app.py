import streamlit as st
import pydeck as pdk
import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate({
        "type": st.secrets["firebase_credentials"]["type"],
        "project_id": st.secrets["firebase_credentials"]["project_id"],
        "private_key_id": st.secrets["firebase_credentials"]["private_key_id"],
        "private_key": st.secrets["firebase_credentials"]["private_key"],
        "client_email": st.secrets["firebase_credentials"]["client_email"],
        "client_id": st.secrets["firebase_credentials"]["client_id"],
        "auth_uri": st.secrets["firebase_credentials"]["auth_uri"],
        "token_uri": st.secrets["firebase_credentials"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebase_credentials"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase_credentials"]["client_x509_cert_url"],
    })
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://cck-app-91eee-default-rtdb.firebaseio.com/'
    }
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
if "visited_landmarks" not in st.session_state:
    st.session_state["visited_landmarks"] = {}
if "badges" not in st.session_state:
    st.session_state["badges"] = set()

# Firebase References
db_ref = db.reference("users")  # Store user progress and leaderboard
badges_ref = db.reference("badges")  # Store badge criteria

# Update Progress
def mark_landmark_visited(category, landmark):
    st.session_state["visited_landmarks"].setdefault(category, []).append(landmark)
    db_ref.child("progress").set(st.session_state["visited_landmarks"])
    update_leaderboard()

# Update Leaderboard
def update_leaderboard():
    user_score = sum(len(v) for v in st.session_state["visited_landmarks"].values())
    db_ref.child("leaderboard").child(st.secrets["user_id"]).set({"name": st.secrets["user_name"], "score": user_score})

# Unlock Badges
def unlock_badge(badge_name):
    if badge_name not in st.session_state["badges"]:
        st.session_state["badges"].add(badge_name)
        badges_ref.child(st.secrets["user_id"]).push(badge_name)
        st.success(f"🎉 Unlocked Badge: {badge_name}!")

# Map Component
def render_map(selected_landmark=None):
    pins = [
        {"name": lm, "lat": details["Latitude"], "lon": details["Longitude"]}
        for cat in landmarks_data.values()
        for lm, details in cat.items()
    ]
    current_pin = next((p for p in pins if p["name"] == selected_landmark), None)
    initial_view = pdk.ViewState(
        latitude=current_pin["lat"] if current_pin else 44.2312,
        longitude=current_pin["lon"] if current_pin else -76.486,
        zoom=12,
    )
    layer = pdk.Layer(
        "ScatterplotLayer",
        data=pins,
        get_position="[lon, lat]",
        get_radius=100,
        get_color="[255, 0, 0]" if current_pin else "[0, 0, 255]",
    )
    st.pydeck_chart(pdk.Deck(initial_view_state=initial_view, layers=[layer]))

# Leaderboard
def display_leaderboard():
    leaderboard_data = db_ref.child("leaderboard").order_by_child("score").get()
    sorted_leaderboard = sorted(leaderboard_data.items(), key=lambda x: x[1]["score"], reverse=True)
    st.header("🏆 Leaderboard")
    for idx, (user_id, data) in enumerate(sorted_leaderboard[:10]):
        st.write(f"#{idx + 1} {data['name']}: {data['score']} points")

# Streamlit Pages
st.sidebar.title("Navigation")
page = st.sidebar.radio("Pages", ["Home", "Map", "Progress", "Leaderboard", "Badges"])

if page == "Home":
    st.title("🧭 Welcome to Compass Chronicles!")
    st.write("Discover Kingston by visiting landmarks and earning rewards.")
elif page == "Map":
    st.title("📍 Explore the Map")
    category = st.selectbox("Select Category", list(landmarks_data.keys()))
    if category:
        landmark = st.selectbox("Select Landmark", list(landmarks_data[category].keys()))
        if landmark:
            render_map(landmark)
            if st.button("Mark as Visited"):
                mark_landmark_visited(category, landmark)
elif page == "Progress":
    st.title("📊 Your Progress")
    for cat, visited in st.session_state["visited_landmarks"].items():
        st.write(f"**{cat}**: {', '.join(visited)}")
elif page == "Leaderboard":
    display_leaderboard()
elif page == "Badges":
    st.title("🏅 Badges")
    for badge in st.session_state["badges"]:
        st.write(f"- {badge}")
