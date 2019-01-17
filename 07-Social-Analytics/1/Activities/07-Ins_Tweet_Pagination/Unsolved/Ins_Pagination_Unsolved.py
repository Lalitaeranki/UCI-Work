
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


# In[6]:


# Target User
target_user = "WhiteHouse"

# Tweet Texts
tweet_texts = []

for x in range(1, 11):
    public_tweets = api.user_timeline(target_user, page=x)
    
    for tweet in public_tweets:
        print(tweet["text"])
        tweet_texts.append(tweet["text"])


# In[7]:


print(f"Tweet Count: {len(tweet_texts)}")

