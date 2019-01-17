
# coding: utf-8

# In[1]:


import gmaps
import pandas as pd

# Configure gmaps
from config import gkey

gmaps.configure(api_key=gkey)


# In[2]:


# Create aiport dataframe
airport_df = pd.read_csv("../Resources/Airport_Output.csv")
airport_df.dropna()
airport_df.head()


# In[3]:


# Store latitude and longitude in locations
locations = airport_df[["Lat", "Lng"]]

# Filla NaN values and convert to float
rating = airport_df["Airport Rating"].astype(float)


# In[5]:


# Plot Heatmap
fig = gmaps.figure()
heat_layer = gmaps.heatmap_layer(locations, weights=rating, dissipating=False, max_intensity=10, point_radius=1)

fig.add_layer(heat_layer)
fig


# In[6]:


fig = gmaps.figure(map_type="HYBRID")
heat_layer = gmaps.heatmap_layer(locations, weights=rating, dissipating=False, max_intensity=10, point_radius=1)

fig.add_layer(heat_layer)
fig


# In[7]:


fig = gmaps.figure(map_type="TERRAIN")
heat_layer = gmaps.heatmap_layer(locations, weights=rating, dissipating=False, max_intensity=10, point_radius=1)

fig.add_layer(heat_layer)
fig

