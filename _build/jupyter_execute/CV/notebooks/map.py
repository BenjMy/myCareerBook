#!/usr/bin/env python
# coding: utf-8

# # Map CV

# ```{warning}
# 🚧 This page is still under construction 🚧
# ```
# 

# ```{admonition} Note
# The map display all the field surveys I conducted or participated in the data processing. It starts from 2013 to now. Other metadatas are attached in the table such as the type of survey, the ancillary data collected, the PI of the field site.
# ```
# 
# 

# In[1]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup, Icon, AwesomeIcon
from ipyleaflet import  LegendControl, basemaps
from IPython.display import Markdown

# read csv file
import pandas as pd
field_activity = pd.read_csv('../field.csv')
field_activity.dropna(subset=['Lat', 'Long'],inplace=True)
field_activity = field_activity.sort_values(by='Date',ascending=False)
field_activity
Purposes = field_activity['Purpose'].unique()
Purposes

from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))

    
total_field = len(field_activity) 

printmd('''
        Total Number of field activities: {total_field}, among with
        '''.format(total_field=total_field)
        )
for i in Purposes:
    #printmd('''{i}'''.format(i=i))
    printmd('''* {} in {}'''.format(sum(field_activity['Purpose']==i),i))
# In[2]:


center = (43.500000, 15.090278)
m = Map(basemap=basemaps.Esri.WorldTopoMap, center=center, zoom=4, zoom_control=False, 
        close_popup_on_click=False)

# define icon for different field activities: archeology, risk assessement, hydrology, ECZ plant soil interaction

icon_archeo = AwesomeIcon(
            name='hammer',
            marker_color='beige',
            icon_color='black',
            spin=False
        )

icon_risk = AwesomeIcon(
            name='exclamation-circle',
            marker_color='red',
        )

icon_hydro = AwesomeIcon(
            name='hand-holding-water',
            marker_color='blue',
        )

icon_vegetation = AwesomeIcon(
            name='seedling',
            marker_color='green',
        )

icon_type = {
            'Archeology': icon_archeo,
            'Geohazard': icon_risk,
            'Hydrology': icon_hydro,
            'Interaction soil-plant-atmosphere': icon_vegetation,
            }


field_sites = []
for i, coords in enumerate(zip(field_activity['Lat'],field_activity['Long'])):
    lt, lg = coords
    field_sites.append((lt, lg))
      
    marker = Marker(location=(lt, lg), icon= icon_type[field_activity['Purpose'].to_numpy()[i]])
    message = HTML()
    message.value = field_activity['Location_name'].to_numpy()[i]
    message.description = field_activity['Purpose'].to_numpy()[i]
    marker.popup = message
    #marker.dragging.disable()
    

    m.add_layer(marker)
    
legend = LegendControl({"Interactions Soil-Plant-Atmosphere":"green", "Geohazards":"red", "Hydrology":"blue",  "Archeology":"beige"}, 
                       name="Field network", 
                       position="topright")
m.add_control(legend)


# In[3]:


m


# In[4]:


display(field_activity)

