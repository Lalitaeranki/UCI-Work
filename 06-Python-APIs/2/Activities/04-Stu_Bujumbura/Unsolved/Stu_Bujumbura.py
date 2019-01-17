
# coding: utf-8

# In[1]:


# Dependencies
import requests
from config import api_key
from pprint import pprint

url = "http://api.openweathermap.org/data/2.5/weather?"
city = "Chicago"
units = "metric"


# In[2]:


# Build query URL and request your results in Celsius
query_url = f"{url}appid={api_key}&q={city}&units={units}"

# Get weather data
weather_json = requests.get(query_url).json()
pprint(weather_json)


# In[3]:


# Get temperature from JSON response
temperature = weather_json["main"]["temp"]


# In[4]:


# Report temperature
print(f"The temperature in {city} is {temperature} C.")


# In[6]:


units = ["metric", "imperial"]
temperatures = []

for unit in units:
    query_url = f"{url}appid={api_key}&q={city}&units={unit}"
    weather_json = requests.get(query_url).json()
    temp = weather_json["main"]["temp"]
    temperatures.append(temp)

print(f"The temperature in {city} is {temperatures[0]}C or {temperatures[1]}F")


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Stu_Bujumbura.ipynb')

