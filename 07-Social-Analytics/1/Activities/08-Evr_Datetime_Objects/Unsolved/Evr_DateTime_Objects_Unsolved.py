
# coding: utf-8

# In[1]:


# New Dependency
from datetime import datetime


# In[2]:


# Dependencies
import tweepy
import json
import numpy as np
import matplotlib.pyplot as plt
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[3]:


# Target User
target_user = 'latimes'

# Get all tweets from home feed
public_tweets = api.user_timeline(target_user)

# A list to hold tweet timestamps
tweet_times = []

# Loop through all tweets
for tweet in public_tweets:
    raw_time = tweet["created_at"]
    print(raw_time)
    tweet_times.append(raw_time)


# In[4]:


# Convert tweet timestamps to datetime objects that can be manipulated by
# Python
converted_timestamps = []
for raw_time in tweet_times:
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
    # http://strftime.org/
    converted_time = datetime.strptime(raw_time, "%a %b %d %H:%M:%S %z %Y")
    converted_timestamps.append(converted_time)


# In[5]:


print(tweet_times[0])
print(tweet_times[1])


# In[6]:


print(converted_timestamps[0])
print(converted_timestamps[1])


# In[7]:


# Calculate the time difference in seconds
diff = converted_timestamps[0] - converted_timestamps[1]
print(f"Time difference: {diff}")
print("seconds: {}".format(diff.seconds))


# In[8]:


converted_length = len(converted_timestamps)
print(f"length of converted timestamps list: {converted_length}")

time_diffs = []

for x in range(converted_length - 1):
    time_diff = converted_timestamps[x] - converted_timestamps[x + 1]
    time_diff = time_diff.seconds / 3600
    time_diffs.append(time_diff)

print(f"Avg. Hours Between Tweets: {np.mean(time_diffs)}")

