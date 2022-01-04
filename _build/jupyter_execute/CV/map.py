#!/usr/bin/env python
# coding: utf-8

# # Map CV

# ### Map in construction
# 
# 

# In[1]:


from ipywidgets import HTML

from ipyleaflet import Map, Marker, Popup, Icon, AwesomeIcon

# read csv file
import pandas as pd
field_activity = pd.read_csv('field.csv')

center = (37.500000, 15.090278)
m = Map(center=center, zoom=3, close_popup_on_click=False)

icon1 = AwesomeIcon(
    name='fa-user-circle',
    marker_color='blue',
    icon_color='white',
    spin=False
)


field_sites = []
for i, coords in enumerate(zip(field_activity['Lat'],field_activity['Long'])):
    lt, lg = coords
    field_sites.append((lt, lg))
    marker = Marker(location=(lt, lg), icon=icon1)
    message = HTML()
    message.value = field_activity['Location_name'].to_numpy()[i]
    message.description = field_activity['Purpose'].to_numpy()[i]
    marker.popup = message

    m.add_layer(marker)
m


# In[2]:



field_activity.dropna(subset=['Lat', 'Long'],inplace=True)
field_activity

