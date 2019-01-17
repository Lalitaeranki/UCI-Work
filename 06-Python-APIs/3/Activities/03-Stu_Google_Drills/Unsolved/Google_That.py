
# coding: utf-8

# In[1]:


# Create code to answer each of the following questions.
# Hint: You will need multiple target URLs and multiple API requests.

# Dependencies
import requests
import json

# Retrieve Google API key from config.py
from config import gkey


# In[2]:


# 1. What are the geocoordinates (latitude/longitude) of Seattle, Washington?
target_city = "Seattle, Washington"
params = {"address": target_city, "key": gkey}
base_url = "https://maps.googleapis.com/maps/api/geocode/json"
response = requests.get(base_url, params=params)
seattle_geo = response.json()

lat = seattle_geo["results"][0]["geometry"]["location"]["lat"]
lng = seattle_geo["results"][0]["geometry"]["location"]["lng"]
print(f"{target_city}: {lat}, {lng}")


# In[3]:


# 2. What are the geocoordinates (latitude/longitude) of The White House?
target_city = "The White House"
params = {"address": target_city, "key": gkey}
base_url = "https://maps.googleapis.com/maps/api/geocode/json"
response = requests.get(base_url, params=params)
seattle_geo = response.json()

lat = seattle_geo["results"][0]["geometry"]["location"]["lat"]
lng = seattle_geo["results"][0]["geometry"]["location"]["lng"]
print(f"{target_city}: {lat}, {lng}")


# In[4]:


# 3. Find the name and address of a bike store in Seattle, Washington.
#    Hint: See https://developers.google.com/places/web-service/supported_types
target_coords = "47.6062095, -122.3320708"
target_type = "bicycle_store"
radius = 8000

params = {
    "location": target_coords,
    "types": target_type,
    "radius": radius,
    "key": gkey
}

base_url ="https://maps.googleapis.com/maps/api/place/nearbysearch/json"
response = requests.get(base_url, params)

seattle_bikes = response.json()

print(seattle_bikes["results"][0]["name"])
print(seattle_bikes["results"][0]["vicinity"])


# In[5]:


# 4. Find a balloon store near the White House.
target_coords = "38.8976763, -77.0365298"
target_search = "Balloon Store"
radius = 8000

params = {
    "location": target_coords,
    "keyword": target_search,
    "radius": radius,
    "key": gkey
}

base_url ="https://maps.googleapis.com/maps/api/place/nearbysearch/json"
response = requests.get(base_url, params)

seattle_bikes = response.json()

print(seattle_bikes["results"][0]["name"])
print(seattle_bikes["results"][0]["vicinity"])


# In[ ]:


# 5. Find the nearest dentist to your house.
#    Hint: Use Google Maps to find your latitude and Google Places to find the
#    dentist. You will also need the rankby property.


# In[7]:


# 6. Bonus: Find the names and addresses of the top five restaurants in your home city.
#    Hint: Read about "Text Search Results"
# (https://developers.google.com/places/web-service/search#TextSearchRequests)

my_phrase = "best restaurants in Irvine, CA"
base_url ="https://maps.googleapis.com/maps/api/place/textsearch/json"

params = {
    "query": my_phrase,
    "key": gkey
}

response = requests.get(base_url, params)

food_places = response.json()

counter = 0

for place in food_places["results"]:
    print(place["name"])
    print(place["formatted_address"])
    counter += 1
    if counter == 5:
        break

