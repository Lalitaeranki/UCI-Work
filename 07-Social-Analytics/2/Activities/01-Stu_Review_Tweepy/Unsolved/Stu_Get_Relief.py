
# coding: utf-8

# In[3]:


# Dependencies
import tweepy
import json
from config import (consumer_key, consumer_secret,
                    access_token, access_token_secret)

# Setup Tweepy API Authentication
def get_tweepy_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return tweepy.API(auth, parser=tweepy.parsers.JSONParser())

api = get_tweepy_api()


# In[4]:


# Target User Account
target_user = "@TheStressGuys"

# Counter
counter = 1

# Loop through 5 pages of tweets (total 100 tweets)
for x in range(1, 6):

    # Get all tweets from home feed
    public_tweets = api.user_timeline(target_user, page=x)

    # Loop through all tweets and print the tweet text
    for tweet in public_tweets:
        print(f"Tip {counter}: {tweet['text']}")
        
        counter += 1

