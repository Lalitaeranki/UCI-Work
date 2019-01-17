
# coding: utf-8

# In[3]:


# Dependencies
import requests
import json

# Google developer API key
from config import gkey

# Target city
target_city = "Boise, Idaho"

# Build the endpoint URL
url = "https://maps.googleapis.com/maps/api/geocode/json?"
query_url = f"{url}address={target_city}&key={gkey}"


# In[4]:


# Run a request to endpoint and convert result to json
geo_data = requests.get(query_url).json()

# Print the json
print(geo_data)


# In[5]:


# Print the json (pretty printed)
print(json.dumps(geo_data, indent=4, sort_keys=True))


# In[6]:


# Extract latitude and longitude
lat = geo_data["results"][0]["geometry"]["location"]["lat"]
lng = geo_data["results"][0]["geometry"]["location"]["lng"]


# Print the latitude and longitude
print(f"City: {target_city}, Latitude: {lat} Longitude: {lng}")


# In[10]:


get_ipython().system('jupyter nbconvert --to script Google_Geocode%20.ipynb')

