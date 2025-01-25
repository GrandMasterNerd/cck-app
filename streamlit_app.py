import streamlit as st
import pandas as pd

# Get the query parameters
query_params = st.experimental_get_query_params()

# Check for the "signal" parameter
if "signal" in query_params:
    signal = query_params["signal"][0]  # Retrieve the first value of "signal"
    st.success(f"Received signal: {signal}")
else:
    st.info("No signal received yet.")

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Compass Chronicles: Kingston", layout="wide")

# Global state to store theme and location data
if 'theme' not in st.session_state:
    st.session_state.theme = None
if 'location' not in st.session_state:
    st.session_state.location = None

def main():
    st.markdown(
        """
        <style>
            body {
                background-color: #f5deb3; /* Light brown background */
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
    if st.sidebar.button("Start Exploring", key="start_button"):
        show_category_selection()
    if st.session_state.theme and st.session_state.location:
        show_theme_locations(st.session_state.theme)

def show_category_selection():
    st.header("Select a Theme")
    st.session_state.theme = st.radio("Choose a theme:", [
        "Engineering Feats", "Historical Landmarks", "Nature Trails", "Cultural Hotspots"])
    show_theme_locations(st.session_state.theme)

def show_theme_locations(theme):
    st.header(f"Explore {theme}")
    st.markdown("Search for a location within this theme:")

    locations = {
        "Engineering Feats": [
            ("Beamish-Munro Hall", "https://bharchitects.com/wp-content/uploads/2017/01/Queens-University-Beamish-Munro_Hero.jpg", 0, 
             """Beamish-Munro Hall contains the Integrated Learning Centre and is the home of the Stephen J.R. Smith Faculty of Engineering and Applied Science at Queen’s University.
             
             History: Beamish-Munro Hall opened its doors in May 2004 and was recognized by the Sustainable Buildings '05 Canadian Team as one of the most environmentally advanced buildings in Canada in 2005.
             
             Features: Beamish-Munro Hall was designed as a 'live building' to lean into the integrated learning component for engineering students. The building is constructed so that students can see structural elements of the building that are typically hidden and monitor systems such as air quality, heating, lighting, and cooling via specially designed software, demonstrating how sustainable practices can be integrated into building design. Contained in the building is a design studio, a prototyping centre, group rooms, a multimedia facility, a site investigation facility, active learning centre and plazas or lab facilities.
             
             [More info here](https://www.queensu.ca/encyclopedia/b/beamish-munro-hall)"""),
            
            ("Joseph S. Stauffer Library", "https://www.queensu.ca/encyclopedia/sites/qencwww/files/uploaded_images/s/staufferlibrary/b-stauff.jpg", 550, 
             """Stauffer Library is the biggest library on Queen’s campus, with five floors and room for approximately 1.5 million volumes, six kilometres of bookstacks, and study and research space for over 1,200 students.
             
             History: The library was constructed with a substantial donation from the Stauffer Foundation, enabling the creation of a state-of-the-art facility to support the university's academic community.
             
             Features: Stauffer Library provides a variety of study spaces, including group study tables and individual study carrels. It also offers computers, scanners, photocopiers, and printers for student use. The library is home to the Adaptive Technology Centre, which includes Library Accessibility Services, an Adaptive Technology Lab, and offices for the Adaptive Technologist and Accessibility Coordinator. Elevators in the library are wheelchair accessible, with controls inside the elevators being Brailled."""),
            
            ("Goodwin Hall", "https://via.placeholder.com/800x400", 230, 
             """In 1989, Goodwin Hall was connected to the newly constructed Walter Light Hall, creating a multi-million dollar technology center to accommodate the growing needs of the Department of Electrical and Computer Engineering.
             
             History: Completed in 1972, it is named after William Lawton Goodwin, the first director of the School of Mining and Agriculture, the precursor to the Faculty of Engineering and Applied Science. Goodwin Hall houses the Robert M. Buchan Department of Mining, the School of Computing, and the Human Mobility Research Centre, a collaboration between Queen's University and Kingston Health Sciences Centre.
             
             Features: The building offers specialized laboratories, including the Human Media Lab, which features a 16-by-9 feet interactive flexible display with gesture technology.""")
        ],
        
        "Historical Landmarks": [
            ("Fort Henry", "https://via.placeholder.com/800x400", 4600, 
             """Fort Henry and Point Henry are named after Henry Hamilton, who was the Lieutenant Governor of Quebec. The fort cost 70,000 British pounds sterling to build, which is about $35 million in modern Canadian currency.
             
             History: Fort Henry in Kingston, Ontario, Canada is a 19th-century British military fortress that protected the Rideau Canal and the town of Kingston. The fort was built to replace an earlier fortification from the War of 1812.
             
             Features: Fort Henry offers guided tours that immerse visitors in the daily life of a 19th-century military fort. Guests can explore interactive exhibits, watch live demonstrations of artillery drills, and enjoy stunning views of the Kingston waterfront from the fort's ramparts. The site also features a museum, gift shop, and on-site café to complete the experience."""),
            
            ("Bellevue House", "https://via.placeholder.com/800x400", 1400, 
             """Bellevue House was once home to Sir John A. Macdonald, Canada’s first Prime Minister, and is one of the few remaining examples of Italianate villa architecture in the country. The house’s unique design includes a picturesque tower, decorative verandas, and a sprawling garden.
             
             History: Built in the 1840s, Bellevue House served as the residence of Macdonald during a pivotal period in his political career. The house was later designated a National Historic Site to commemorate its connection to one of Canada’s most influential leaders.
             
             Features: Bellevue House offers guided tours that delve into the life and legacy of Sir John A. Macdonald, with interpreters dressed in period attire. Visitors can explore restored rooms furnished to reflect the 1840s, stroll through beautifully landscaped grounds, and engage with exhibits that highlight Canada’s early political history. A visitor center and gift shop are also available on-site."""),
            
            ("Kingston City Hall", "https://via.placeholder.com/800x400", 1500, 
             """Kingston City Hall, completed in 1844, was designed by architect George Browne in the Neoclassical style, featuring a prominent dome and tholobate. It was designated a National Historic Site of Canada in 1961.
             
             History: Originally serving as a city hall, market, custom house, post office, police station, and jail, the building reflects Kingston's status as the capital of the Province of Canada at the time of its construction.
             
             Features: Kingston City Hall houses municipal offices and the council chambers. The building is open to the public during regular business hours, offering self-guided tours of public spaces on the first and second floors. Visitors can explore the Market Wing Cultural Space, which hosts exhibitions and programming that share diverse and inclusive stories of Kingston. The adjacent Confederation Park features a large arch with a fountain and the Confederation Basin Marina, enhancing the city's waterfront experience.""")
        ],
        
        "Nature Trails": [
            ("Lake Ontario Park", "https://via.placeholder.com/800x400", 3900, 
             """Lake Ontario Park, Kingston's largest urban waterfront park, underwent a complete revitalization and reopened in June 2013.
             
             History: Established in 1894, the park has evolved into a significant natural landscape, drawing both visitors and residents for picnicking and scenic walks along the waterfront.
             
             Features: The park offers a sandy beach area, a splash pad, and a playground for children. Visitors can enjoy walking and cycling paths, a boat launch, picnic tables, and barbecue facilities. The park also features a waterfront terrace lookout, public fishing areas, and accessible washrooms."""),
            
            ("Lemoine Point", "https://via.placeholder.com/800x400", 12200, 
             """Lemoine Point Conservation Area, located in Kingston, Ontario, is a 136-hectare natural park offering diverse ecosystems, including forests, wetlands, and meadows. The area is named after the Lemoine Point, a notable point in geometry, though the park's name is coincidental.
             
             History: Established in 1992, Lemoine Point Conservation Area was developed to protect and showcase the natural beauty of the area. It serves as a vital green space for both wildlife and the local community.
             
             Features: The park offers over 10 kilometers of trails suitable for walking, cycling, and birdwatching. Visitors can enjoy scenic views of Lake Ontario, access to the waterfront, and opportunities for fishing. The area also features picnic spots and educational signage about local flora and fauna."""),
            
            ("Battery Park", "https://via.placeholder.com/800x400", 1200, 
             """Battery Park, located at the foot of Earl Street in Kingston, Ontario, was officially opened on June 28, 2010. The park's name honors the historic Mississauga Battery that was situated on the site in the early 1800s.
             
             History: The area now known as Battery Park has a rich history, having been home to a native settlement, a small military establishment, and the Canadian Locomotive Company. The park was developed to revitalize the waterfront and provide public access to the shoreline.
             
             Features: Battery Park offers a scenic waterfront pathway, making it ideal for walking, jogging, and cycling. It is a popular spot for families and visitors to enjoy picnicking, community events, and outdoor activities. The park also features benches, sculptures, and beautiful gardens.""")
        ],
        
        "Cultural Hotspots": [
            ("The Grand Theatre", "https://via.placeholder.com/800x400", 1000, 
             """The Grand Theatre is one of Kingston's premier performance venues, offering a diverse range of performances, from plays and concerts to film screenings and comedy.
             
             History: Built in 1900, The Grand Theatre has served as a cultural landmark in Kingston. Originally opened as a vaudeville theatre, it has undergone several renovations to preserve its historic charm and provide state-of-the-art performance spaces.
             
             Features: The Grand Theatre offers a 600-seat auditorium with excellent acoustics, a full-service lobby, and a well-equipped stage. The venue hosts a range of performances, including theatrical productions, music concerts, and special events. The theater also features a historic décor with vintage details and modern amenities."""),
            
            ("Isabel Bader Centre", "https://via.placeholder.com/800x400", 1700, 
             """The Isabel Bader Centre is a state-of-the-art performing arts venue that is the home of Queen’s University’s Dan School of Drama and Music.
             
             History: Opened in 2014, the Isabel Bader Centre is named after philanthropists Isabel and Alfred Bader, who contributed significantly to the construction of the facility. It has since become one of the most important arts centers in Kingston.
             
             Features: The venue houses a 566-seat concert hall, a black box theater, rehearsal spaces, and various classrooms. It is the site for numerous performances, including concerts, plays, and film screenings. The Bader Centre also features a modern design, with cutting-edge technology to enhance the theatrical and musical experience."""),
            
            ("Skeleton Park", "https://via.placeholder.com/800x400", 1500, 
             """Skeleton Park is a beautiful green space located in downtown Kingston, named for its historic ties to a burial ground that once occupied the area.
             
             History: The park’s name refers to the fact that the site was used as a burial ground from the 19th century until the mid-20th century. The park is now an active community space that plays host to various public events and activities.
             
             Features: Skeleton Park features sports fields, a large playground, walking paths, and a central gathering space used for outdoor concerts and arts festivals. The park is also home to a vibrant community of local artists and hosts annual events like Skeleton Park Arts Festival.""")
        ]
    }

    locations_for_theme = locations.get(theme, [])
    st.session_state.location = st.selectbox("Search Locations:", [loc[0] for loc in locations_for_theme])

    for location in locations_for_theme:
        if location[0] == st.session_state.location:
            show_location_details(location)

def show_location_details(location):
    name, image, distance, full_details = location
    st.markdown(f"### {name}")
    st.image(image, caption=name, use_container_width=True)
    st.markdown(f"**Distance:** {distance} meters")
    st.markdown(f"{full_details}")

# Footer with Credits
st.markdown(
    """
    ---
    **Developed by Nolan Verboomen, Adam Likogiannis, Eiqan Ahsan, and Aidan Murray**
    """
)

if __name__ == "__main__":
    main()
