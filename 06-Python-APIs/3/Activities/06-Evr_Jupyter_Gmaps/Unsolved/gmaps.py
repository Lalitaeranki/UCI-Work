
# coding: utf-8

# In[1]:


import gmaps

# Google developer API key
from config import gkey

gmaps.configure(api_key=gkey)


# In[2]:


coordinates = [
    (40.71, -74.00),
    (30.26, -97.74),
    (46.87, -96.78),
    (47.60, -122.33),
    (32.71, -117.16)
]


# In[3]:


figure_layout = {
    "width": "400px",
    "height": "300px",
    "border": "1px solid black",
    "padding": "1px",
    "margin": "0 auto 0 auto"
}
fig = gmaps.figure(layout=figure_layout)


# In[4]:


markers = gmaps.marker_layer(coordinates)
fig.add_layer(markers)
fig


# In[ ]:


get_ipython().system('jupyter nbconvert --to ')

