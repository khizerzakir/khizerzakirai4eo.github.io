import streamlit as st
import geemap.foliumap as geemap
import folium
import ee
from streamlit_folium import st_folium

# Initialize Earth Engine
ee.Initialize()

# Define your dictionary for land cover names and colors
landcover_dict = {
    "names": [
        "Water", "Trees", "Flooded Vegetation", "Crops", "Built Area",
        "Bare Ground", "Snow/Ice", "Clouds", "Rangeland"
    ],
    "colors": [
        "#1A5BAB", "#358221", "#87D19E", "#FFDB5C", "#ED022A",
        "#EDE9E4", "#F2FAFF", "#C8C8C8", "#C6AD8D"
    ]
}

# Remapper function to adjust class values
def remapper(image):
    return image.remap([1,2,4,5,7,8,9,10,11], [1,2,3,4,5,6,7,8,9])

# Streamlit setup
st.title("Landuse Change of Pakistan From 2017 to 2023")

# Initialize Folium map
m = geemap.Map(center=[33.6844, 73.0479], zoom=5)

# Add LULC layers for each year
years = range(2017, 2023)
for year in years:
    image = ee.ImageCollection("projects/sat-io/open-datasets/landcover/ESRI_Global-LULC_10m_TS").filterDate(f'{year}-01-01', f'{year}-12-31').mosaic().clip(ee.Geometry.Polygon([
        [[60.8728, 35.6929], [60.8728, 23.6345], [77.8375, 23.6345], [77.8375, 35.6929], [60.8728, 35.6929]]
    ]))
    remapped_image = remapper(image)
    m.addLayer(remapped_image, {'min': 1, 'max': 9, 'palette': landcover_dict['colors']}, f'LULC {year}')

# Create a custom legend as an HTML element
legend_html = """
    <div style="position: fixed;
                bottom: 50px; left: 50px; width: 200px; height: 350px;
                background-color: white; z-index:1000; font-size:14px;
                border:2px solid grey; border-radius:10px; padding: 10px;">
    <h4 style='margin-top:10px;'>Legend</h4>
"""
for i, name in enumerate(landcover_dict['names']):
    color = landcover_dict['colors'][i]
    legend_html += f"<i style='background:{color}; width:18px; height:18px; float:left; opacity:0.7;'></i><span>{name}</span><br>"

legend_html += "</div>"

m.get_root().html.add_child(folium.Element(legend_html))

# Display the map in Streamlit
st_data = st_folium(m, width=700)

# Add checkboxes to toggle the visibility of LULC layers
with st.sidebar:
    st.header('Year Wise Classification Layers')
    for year in years:
        st.checkbox(f'LULC {year}', value=True, on_change=lambda: m.find_layer(f'LULC {year}').toggle_layer())

# Render the map
st_folium(m, width=700)
