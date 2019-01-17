
# coding: utf-8

# In[8]:


# Dependencies
import tweepy
import json
import time
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[2]:


# Twitter API Keys
consumer_key = consumer_key
consumer_secret = consumer_secret
access_token = access_token
access_token_secret = access_token_secret


# In[3]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[1]:


def tweet_out(tweet_number):
    print(f"Iteration #{tweet_number+1}")
    api.update_status(f"Hey! This is tweet #{tweet_number+1}, but with a timer")


# In[9]:


#Iterate Forever
counter = 0
while(True):
    tweet_out(counter)
    
    time.sleep(60)
    
    counter += 1

