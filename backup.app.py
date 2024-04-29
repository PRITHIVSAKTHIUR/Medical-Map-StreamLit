import streamlit as st
import folium
from streamlit_folium import folium_static

# Define hospitals data for Minnesota
hospitals = [('Mayo Clinic', 'Rochester', 44.023678, -92.466955),
             ('University of Minnesota Medical Center', 'Minneapolis', 44.971389, -93.240556),
             ('Hennepin County Medical Center', 'Minneapolis', 44.972078, -93.261769),
             ('Regions Hospital', 'St. Paul', 44.942936, -93.093457),
             ('Abbott Northwestern Hospital', 'Minneapolis', 44.955447, -93.268543)]

# Create a map centered on Minnesota
m = folium.Map(location=[45.0, -94.0], zoom_start=7)

# Add markers for each hospital
for hospital in hospitals:
    folium.Marker(
        location=[hospital[2], hospital[3]],
        popup=f'{hospital[0]}<br>{hospital[1]}',
        icon=folium.Icon(color='red')
    ).add_to(m)

# Add waypoints for each hospital
waypoints = [(hospital[2], hospital[3]) for hospital in hospitals]
folium.plugins.AntPath(waypoints, delay=3000).add_to(m)

# Function to update the map when a button is clicked
def update_map(hospital_data):
    m.location = [hospital_data[2], hospital_data[3]]
    m.zoom_start = 13
    folium_static(m)

# Create a grid of buttons for selecting hospitals
col1, col2, col3 = st.columns(3)
with col1:
    if st.button(hospitals[0][0]):
        update_map(hospitals[0])
with col2:
    if st.button(hospitals[1][0]):
        update_map(hospitals[1])
with col3:
    if st.button(hospitals[2][0]):
        update_map(hospitals[2])

col4, col5, col6 = st.columns(3)
with col4:
    if st.button(hospitals[3][0]):
        update_map(hospitals[3])
with col5:
    if st.button(hospitals[4][0]):
        update_map(hospitals[4])

# Display the map in Streamlit
folium_static(m)
