# Map CV

```{warning}
🚧 This page is still under construction 🚧
```

```{code-cell} ipython3
# map_folium.py
import pandas as pd
import folium
from IPython.display import display, HTML, Markdown

# -------------------------------
# Read CSV file
# -------------------------------
field_activity = pd.read_csv('../field.csv')
field_activity.dropna(subset=['Lat', 'Long'], inplace=True)
field_activity = field_activity.sort_values(by='Date', ascending=False)

# -------------------------------
# Display summary
# -------------------------------
Purposes = field_activity['Purpose'].unique()
total_field = len(field_activity)
display(Markdown(f"**Total Number of field activities:** {total_field}"))

for p in Purposes:
    count = sum(field_activity['Purpose'] == p)
    display(Markdown(f"* {count} in {p}"))

# -------------------------------
# Create Folium map
# -------------------------------
center = [43.500000, 15.090278]
m = folium.Map(location=center, zoom_start=4, tiles="Stamen Terrain")

# -------------------------------
# Define icon colors for field activity types
# -------------------------------
icon_colors = {
    'Archeology': 'beige',
    'Geohazard': 'red',
    'Hydrology': 'blue',
    'Interaction soil-plant-atmosphere': 'green'
}

# Optionally, use FontAwesome icons similar to AwesomeIcon
fa_icons = {
    'Archeology': 'hammer',
    'Geohazard': 'exclamation-circle',
    'Hydrology': 'tint',  # hand-holding-water substitute
    'Interaction soil-plant-atmosphere': 'seedling'
}

# -------------------------------
# Add markers to map
# -------------------------------
for idx, row in field_activity.iterrows():
    lat, lon = row['Lat'], row['Long']
    purpose = row['Purpose']
    location_name = row['Location_name']
    
    popup_html = f"<b>{location_name}</b><br>{purpose}"
    
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_html, max_width=250),
        icon=folium.Icon(color=icon_colors.get(purpose, 'gray'),
                         icon=fa_icons.get(purpose, 'info-sign'),
                         prefix='fa')
    ).add_to(m)

# -------------------------------
# Add legend using HTML overlay
# -------------------------------
legend_html = """
<div style="
position: fixed; 
bottom: 50px; left: 50px; width: 220px; height: 140px; 
background-color: white; z-index:9999; font-size:14px;
border:2px solid grey; border-radius:5px; padding: 10px;">
<b>Field Network Legend</b><br>
&mdash; Archeology: beige<br>
&mdash; Geohazards: red<br>
&mdash; Hydrology: blue<br>
&mdash; Interaction soil-plant-atmosphere: green
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

# -------------------------------
# Display map and table
# -------------------------------
# Save map to an HTML file in the _static folder
m.save("_static/field_map.html")
display(field_activity)
```
```{raw} html
<iframe src="_static/field_map.html" width="100%" height="600px" style="border:none;"></iframe>
```
