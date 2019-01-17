
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


# Target User
target_user = "realdonaldtrump"

# Create array to record all date-times of tweets
tweet_times = []

# Loop through 500 tweets
for x in range(1, 26):
    
    # Get all tweets from target user
    public_tweets = api.user_timeline(target_user, page=x)

    # Loop through all tweets
    for tweet in public_tweets:
        tweet_times.append(tweet["created_at"])
        

# Confirm tweet counts
len(tweet_times)


# In[3]:


# Convert all tweet times into datetime objects
tweet_time_objects = []

# Add each datetime object into the array
for x in range(len(tweet_times)):
    tweet_datetime = datetime.strptime(tweet_times[x], "%a %b %d %H:%M:%S %z %Y")
    tweet_time_objects.append(tweet_datetime)
    # Preview that datetimes are matching
    if x % 100 == 0:
        print(tweet_times[x])
        print(tweet_datetime)


# In[5]:


# Calculate the time between tweets
time_in_between = []

# Calculate the time in between each tweet, then append the difference to the list
# Hint: use a construction like the following: for x in range(len(tweet_time_objects)-1):
for x in range(len(tweet_time_objects) - 1):
    hours_apart = ((tweet_time_objects[x] - tweet_time_objects[x + 1]).seconds) / 3600
    time_in_between.append(hours_apart)

# Hours Between Tweets
print(f"Avg. Hours Between Tweets: {np.mean(time_in_between)}")


# In[6]:


time_in_between[:10]


# In[8]:


# Use MatPlotLib to plot the time between Tweets
plt.plot(range(len(time_in_between)), time_in_between, marker="o")
plt.xlim([0, len(time_in_between)])
plt.ylabel("Hours Apart")
plt.xlabel("Tweets Ago")
plt.title(f"Tweet Velocity: {target_user}")
plt.show()

