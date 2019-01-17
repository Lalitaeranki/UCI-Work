
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import time
import json
import random
import requests as req
import datetime
from config import consumer_key, consumer_secret, access_token, access_token_secret, weather_api_key


# In[2]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[3]:


def get_tweepy_api():
    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[8]:


def get_weather():
    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather?"
    city = "London"
    units = "imperial"
    query_url = url + "appid=" + weather_api_key + "&q=" + city + "&units=" + units
    
    weather_response = req.get(query_url)
    return weather_response.json()


# In[6]:


# Create a function that gets the weather in London and Tweets it
def WeatherTweet():

    # Perform the API call to get the weather
    weather = get_weather()

    # Twitter credentials
    api = get_tweepy_api()

    # Tweet the weather
    now = datetime.datetime.now().strftime("%H:%M %p")
    api.update_status(f"London Weather: {now} {weather['main']['temp']}F")

    # Print success message
    print("Tweeted Successfully")


# In[ ]:


# Set timer to run every 1 hour
#while(True):
    #WeatherTweet()
    #time.sleep(3600)


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Weather_Tweets.ipynb')

