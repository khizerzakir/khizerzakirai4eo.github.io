import streamlit as st
import geemap.foliumap as geemap
from folium import Map, features

# Initialize a Folium map
m = geemap.Map(center=(0, 0), zoom=2)

# Create a custom HTML legend
legend_html = """
 <div style="
   position: fixed;
   top: 10px;
   right: 10px;
   z-index: 1000;
   background-color: white;
   padding: 10px;
   border-radius: 5px;
   border: 1px solid #ccc;
   box-shadow: 0 0 10px rgba(0,0,0,0.2);
 ">
   <h4>Legend</h4>
   <i style="background: #FF0000; width: 18px; height: 18px; display: inline-block;"></i> Red Color <br>
   <i style="background: #00FF00; width: 18px; height: 18px; display: inline-block;"></i> Green Color <br>
   <i style="background: #0000FF; width: 18px; height: 18px; display: inline-block;"></i> Blue Color <br>
 </div>
"""

# Add the custom legend to the map using folium
m.get_root().html.add_child(features.Element(legend_html))

# Display the map in Streamlit
st.title("Map with Custom Legend")
m.to_streamlit()
