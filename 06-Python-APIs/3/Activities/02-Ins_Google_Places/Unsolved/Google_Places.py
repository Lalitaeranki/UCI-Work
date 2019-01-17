
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json

# Google developer API key
from config import gkey


# In[2]:


# geocoordinates
target_coordinates = "43.6187102, -116.2146068"
target_search = "Chinese"
target_radius = 8000
target_type = "restaurant"


# In[3]:


params = {
    "location": target_coordinates,
    "keyword": target_search,
    "radius": target_radius,
    "type": target_type,
    "key": gkey
}

base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
response = requests.get(base_url, params)


# In[4]:


places_data = response.json()
print(json.dumps(places_data, indent=4, sort_keys=True))


# In[5]:


print(places_data["results"][0]["name"])
print(places_data["results"][0]["vicinity"])


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Google_Places.i')

