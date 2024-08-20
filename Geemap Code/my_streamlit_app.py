
# Import Libraries
import streamlit as st
import geemap.foliumap as geemap
import ee
from streamlit_folium import st_folium
import folium

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

legend_dict = {
    "Water": "#1A5BAB",
    "Trees": "#358221",
    "Flooded Vegetation": "#87D19E",
    "Crops": "#FFDB5C",
    "Built Area": "#ED022A",
    "Bare Ground": "#EDE9E4",
    "Snow/Ice": "#F2FAFF",
    "Clouds": "#C8C8C8",
    "Rangeland": "#C6AD8D",
}

# Streamlit app title
st.title("Land Cover Classification Map")

# Remapper function to adjust class values
def remapper(image):
    return image.remap([1, 2, 4, 5, 7, 8, 9, 10, 11], [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Initialize the map
m = geemap.Map(center=[31, 72], zoom=5.3)

# Define the country and region of interest (ROI)
country = "Pakistan"
roi = ee.FeatureCollection('USDOS/LSIB_SIMPLE/2017').filter(ee.Filter.eq('country_na', country))

# Function to add landcover layer
def add_landcover_layer(year):
    image = ee.ImageCollection("projects/sat-io/open-datasets/landcover/ESRI_Global-LULC_10m_TS").filterDate(f"{year}-01-01", f"{year}-12-31")
    remapped_image = remapper(image.median()).clip(roi)
    layer = geemap.ee_tile_layer(remapped_image, {'min': 1, 'max': 9, 'palette': landcover_dict['colors']}, f"Landcover {year}")
    return layer

# Add checkboxes for each year in a Streamlit sidebar
years = list(range(2017, 2024))
layers = {}

st.sidebar.header("Select Landcover Year")
for year in years:
    checkbox = st.sidebar.checkbox(f"Show Landcover {year}", key=f"checkbox_{year}")
    if checkbox:
        layer = add_landcover_layer(year)
        m.add_child(layer)
        layers[year] = layer

# Add instructions to the sidebar
st.sidebar.header("Instructions")
st.sidebar.write("""
1. Use the checkboxes above to select the land cover layer for different years.
2. The map will update to show the selected year's land cover classification.
3. Use the zoom and pan tools on the map to explore different areas.
4. The legend below explains the color coding of the land cover types.
""")
# Add the legend to the map
def add_legend(map, legend_dict):
    legend_html = """
    <div id='maplegend' style="position: fixed; 
                bottom: 30px; left: 50px; width: 150px; height: auto; 
                border:2px solid grey; z-index:9999; font-size:14px;
                background-color: white; padding: 10px;">
                <b>Land Cover Classification</b> <br>
    """
    for name, color in legend_dict.items():
        legend_html += f"<i style='background:{color}; width: 20px; height: 20px; display: inline-block; margin-right: 8px;'></i>{name}<br>"
    legend_html += """
    </div>
    <style type='text/css'>
      @media only screen and (max-width: 600px) {
        #maplegend {
          bottom: 20px;
          left: 20px;
          width: 120px;
        }
      }
    </style>
    """
    map.get_root().html.add_child(folium.Element(legend_html))


add_legend(m, legend_dict)

# Display the map in Streamlit
st_folium(m, width=900, height=600)

# Add Creative Commons license notice to the sidebar
st.sidebar.markdown("""
---
#### License
This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
""")


