
# coding: utf-8

# In[2]:


# Dependencies
import tweepy
import json
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[4]:


# Import Twitter API Keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[6]:


# Get all tweets from home feed
public_tweets = api.user_timeline()


# In[7]:


# Loop through all tweets and print a prettified JSON of each tweet
for tweet in public_tweets:
    print(json.dumps(tweet, sort_keys=True, indent=4))

