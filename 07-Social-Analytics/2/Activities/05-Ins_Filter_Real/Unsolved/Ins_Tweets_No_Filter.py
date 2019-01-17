
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import numpy as np

# Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[8]:


# Search for People Tweeting about Mark Hamill
search_term = "Mark Hamill"

human_tweets = []

# Retrieve 100 tweets
public_tweets = api.search(search_term, count=100)

# Print Tweets
for tweet in public_tweets["statuses"]:

    if (filter_human(tweet["user"])):
        human_tweets.append(tweet["text"])
        # Print the username
        print(tweet["user"]["screen_name"])

        # Print the tweet text
        print(tweet["text"])
        print()


# In[10]:


# Print total number of tweets
print(len(human_tweets))


# In[7]:


def filter_human(user):
    min_tweets = 5
    max_tweets = 10000
    max_followers = 2500
    max_following = 2500
    lang = "en"
    
    return user["followers_count"] < max_followers and        user["statuses_count"] > min_tweets and        user["statuses_count"] < max_tweets and        user["friends_count"] < max_following and        user["lang"] == lang

