
# coding: utf-8

# In[1]:


# Dependencies
import openweathermapy.core as owm

#config
from config import api_key


# In[2]:


settings = {"units": "metric", "appid": api_key}


# In[4]:


current_weather_paris = owm.get_current("Paris", **settings)
print(f"Current weather object for Paris: {current_weather_paris}")


# In[5]:


summary = ["name", "main.temp"]
data = current_weather_paris(*summary)
print(f"The current weather summary for Paris is: {data}")


# In[ ]:


def parser(some_dict):
    if type(some_dict) is dict:
        #do some stuff

