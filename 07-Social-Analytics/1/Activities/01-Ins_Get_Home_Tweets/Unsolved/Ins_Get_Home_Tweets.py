
# coding: utf-8

# In[1]:


# Dependencies
import json
import tweepy


# In[2]:


# Import Twitter API Keys
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[3]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[4]:


# Get all tweets from home feed
public_tweets = api.home_timeline()


# In[5]:


# Loop through all tweets
for tweet in public_tweets:
    print(json.dumps(tweet, sort_keys=True, indent=4))

