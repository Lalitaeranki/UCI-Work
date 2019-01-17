
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[2]:


search_term = input("Which term would you like to search for? ")
public_tweets = api.search(search_term)
public_tweets


# In[3]:


for tweet in public_tweets["statuses"]:
    print(tweet["text"])

