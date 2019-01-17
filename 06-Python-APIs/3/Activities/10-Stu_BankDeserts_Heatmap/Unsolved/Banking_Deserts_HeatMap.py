
# coding: utf-8

# # Banking and Unemployment
# ---

# In[7]:


# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import time
from census import Census
from us import states
import gmaps

# census key
from config import (census_key, gkey)

# Census API Key
c = Census(census_key, year=2013)


# ## Data Retrieval

# In[2]:


# Run Census Search to retrieve data on all zip codes (2013 ACS5 Census)
# See: https://github.com/CommerceDataService/census-wrapper for library documentation
# See: https://gist.github.com/afhaque/60558290d6efd892351c4b64e5c01e9b for labels
census_data = c.acs5.get(("B01003_001E", "B23025_005E"), {
                         'for': 'zip code tabulation area:*'})

# Convert to DataFrame
census_pd = pd.DataFrame(census_data)

# Column Reordering
census_pd = census_pd.rename(columns={"B01003_001E": "Population",
                                      "B23025_005E": "Unemployment Count",
                                      "zip code tabulation area": "Zipcode"})

# Add in Unemployment Rate (Unemployment Count / Population)
census_pd["Unemployment Rate"] = 100 * census_pd["Unemployment Count"].astype(int) / census_pd["Population"].astype(int) 

# Final DataFrame
census_pd = census_pd[["Zipcode", "Population", "Unemployment Rate"]]


# Visualize
census_pd.head()


# ## Combine Data

# In[3]:


# Import the original data we analyzed earlier. Use dtype="object" to match other
census_data_original = pd.read_csv(
    "../Resources/zip_bank_data.csv", dtype="object", encoding="utf-8"
)

# Visualize
census_data_original.head()


# In[5]:


# Merge the two data sets along zip code
census_complete = pd.merge(census_data_original, census_pd, how="left", on="Zipcode")

# Save the revised Data Frame as a csv
census_complete.to_csv(
    "../Resources/bank_data_with_unemployment.csv", encoding="utf-8", index=False
)

# Visualize
census_complete.head()


# ## Heatmap of poverty rate

# In[8]:


# Configure gmaps with API key
gmaps.configure(api_key = gkey)


# In[9]:


# Store 'Lat' and 'Lng' into  locations 
locations = census_complete[["Lat", "Lng"]].astype(float)

# Convert Poverty Rate to float and store
# HINT: be sure to handle NaN values
poverty_rate = census_complete["Poverty Rate"].astype(float)


# In[10]:


# Create a poverty Heatmap layer
fig = gmaps.figure()
heatmap_layer = gmaps.heatmap_layer(locations, weights=poverty_rate, dissipating=False, max_intensity=100, point_radius=1)

fig.add_layer(heatmap_layer)
fig


# In[13]:


# Convert bank rate to list
bank_rate = census_complete["Bank Count"].tolist()


# In[14]:


# Create bank symbol layer
bank_layer = gmaps.symbol_layer(
    locations,
    fill_color="rgba(0, 150, 0, 0.4)",
    stroke_color="rgba(0, 150, 0, 0.4)",
    scale=2,
    info_box_content=[f"Bank Amount: {bank}" for bank in bank_rate]
)

fig = gmaps.figure()
fig.add_layer(bank_layer)
fig


# In[15]:


# Create a combined map
fig = gmaps.figure()
fig.add_layer(heatmap_layer)
fig.add_layer(bank_layer)
fig

