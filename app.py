import streamlit as st
import folium
from streamlit_folium import folium_static
import pandas as pd

# Define hospitals data for Tamil Nadu
import pandas as pd

hospitals = pd.DataFrame({
    'name': ['Apollo Hospitals Chennai', 'Fortis Hospital Coimbatore', 'Government Rajaji Hospital Madurai',
             'MIOT Hospital Trichy', 'Salem Medical Mission Hospital'],
    'city': ['Chennai', 'Coimbatore', 'Madurai', 'Trichy', 'Salem'],
    'lat': [13.0827, 11.0168, 9.9252, 10.7905, 11.6643],
    'lon': [80.2707, 76.9558, 78.1198, 78.7047, 78.1460],
    'beds': [2000, 400, 3500, 1000, 1000]
})

# Sort hospitals by number of beds and select the top ten
top_hospitals = hospitals.sort_values('beds', ascending=False).head(10)

# Create a map centered on Minnesota
m = folium.Map(location=[45.0, -94.0], zoom_start=7)

# Add markers for each hospital
for i, hospital in top_hospitals.iterrows():
    folium.Marker(
        location=[hospital['lat'], hospital['lon']],
        popup=f"{hospital['name']}<br>{hospital['city']}<br>{hospital['beds']} beds",
        icon=folium.Icon(color='red')
    ).add_to(m)

# Add waypoints for each hospital
waypoints = [(hospital['lat'], hospital['lon']) for i, hospital in top_hospitals.iterrows()]
folium.plugins.AntPath(waypoints, delay=3000).add_to(m)

# Function to update the map when a button is clicked
def update_map(hospital_data):
    m.location = [hospital_data['lat'], hospital_data['lon']]
    m.zoom_start = 13
    folium_static(m)

# Create a grid of buttons for selecting hospitals
cols = st.columns(5)
for i, hospital in top_hospitals.iterrows():
    with cols[i % 5]:
        if st.button(hospital['name']):
            update_map(hospital)

# Display the map in Streamlit
folium_static(m)
