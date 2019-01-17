
# coding: utf-8

# In[2]:


# Dependencies
import json
import requests
from config import api_key


# In[3]:


# Save config information
url = "http://api.openweathermap.org/data/2.5/weather?"
city = "London"

# Build query URL
query_url = f"{url}appid={api_key}&q={city}"
print(query_url)


# In[4]:


# Get weather data
weather_data = requests.get(query_url)
weather_json = weather_data.json()

# Get the temperature from the response
print(f"The weather in {city} is {weather_json}")

