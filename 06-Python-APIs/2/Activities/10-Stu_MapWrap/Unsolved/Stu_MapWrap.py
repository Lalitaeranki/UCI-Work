
# coding: utf-8

# In[1]:


# Dependencies
import csv
import matplotlib.pyplot as plt
import openweathermapy as ow
import pandas as pd

# import api_key from config file
from config import api_key


# In[2]:


# Create a settings object with your API key and preferred units
settings = {"units": "metrics", "appid": api_key}


# In[3]:


# Get data for each city in cities.csv
weather_data = []
with open("../Resources/cities.csv") as cities_file:
    cities_reader = csv.reader(cities_file)
    cities = [city[0] for city in cities_reader]
    weather_data = [ow.get_current(city, **settings) for city in cities]


# In[4]:


# Create an "extracts" object to get the temperature, latitude,
# and longitude in each city
summary = ["main.temp", "coord.lat", "coord.lon"]
data = [response(*summary) for response in weather_data]

# Create a Pandas DataFrame with the results
weather_data = pd.DataFrame(data, index=cities)
weather_data


# In[5]:


column_names = ["Temperature", "Latitude", "Longitude"]
weather_data = pd.DataFrame(data, index=cities, columns=column_names)
weather_data

