
# coding: utf-8

# In[1]:


# Dependencies
import csv
import matplotlib.pyplot as plt
import requests
import pandas as pd
from config import api_key


# In[2]:


url = "http://api.openweathermap.org/data/2.5/weather?"
units = "metric"
query_url = f"{url}appid={api_key}&units={units}&q="


# In[3]:


cities = ["Paris", "London", "Oslo", "Beijing"]
lat = []
temp = []

for city in cities:
    response = requests.get(query_url + city).json()
    lat.append(response['coord']['lat'])
    temp.append(response['main']['temp'])
    
print(f"The latitude information recieved is: {lat}")
print(f"The temperature information recieved is: {temp}")


# In[4]:


weather_dict = {
    "city": cities,
    "lat": lat,
    "temp": temp
}
weather_data = pd.DataFrame(weather_dict)
weather_data.head()


# In[5]:


plt.scatter(weather_data["lat"], weather_data["temp"], marker="o")

plt.title("Temperature in World Cities")
plt.ylabel("Temperature (Celsius)")
plt.xlabel("Latitude")
plt.grid()

plt.savefig("temp_pic.png")
plt.show()

