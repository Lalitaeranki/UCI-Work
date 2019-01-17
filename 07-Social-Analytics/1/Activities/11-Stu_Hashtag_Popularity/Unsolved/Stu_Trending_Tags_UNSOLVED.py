
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import json
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[2]:


# Target Hashtags
target_tags = ["#bigdata", "#ai", "#vr", "#foreverchuck"]
time_between_tweets = []

# Loop through each hashtag
for tag in target_tags:
    
    # Create a list to record all date-times of tweets
    tweet_times = []

    # Get 100 tweets on targeted tag
    public_tweets = api.search(tag, rpp=100)
    print(tag)

    # Loop through all tweets
    for tweet in public_tweets["statuses"]:

        # Store all tweet times into the list
        tweet_times.append(tweet["created_at"])
    
    # Convert all tweet times into datetime objects
    # First, create a list to hold the datetime objects
    tweet_time_objects = []


    # Convert and add each datetime object into the list
    for x in range(len(tweet_times)):
        tweet_datetime = datetime.strptime(tweet_times[x], "%a %b %d %H:%M:%S %z %Y")
        tweet_time_objects.append(tweet_datetime)

    # Calculate the time between tweets
    # First, create a list to hold the time intervals
    time_in_between = []

    # Calculate the time between one tweet to the next, then add it to the list
    for x in range(len(tweet_time_objects) - 1):
        secs_apart = ((tweet_time_objects[x] - tweet_time_objects[x + 1]).seconds)
        time_in_between.append(secs_apart)

    # Seconds Between Tweets
    print(f"Avg. Seconds Between Tweets: {np.mean(time_in_between)}")
    print()

