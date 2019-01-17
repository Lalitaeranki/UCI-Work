
# coding: utf-8

# In[7]:


# Dependencies
import tweepy
import numpy as np
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

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


# Target Search Term
target = "@SouthwestAir"

# "Real Person" Filters
min_tweets = 5
max_tweets = 10000
max_followers = 2500
max_following = 2500
lang = "en"

counter = 0

# List to hold sentiment
results_list = []


# Variable for holding the oldest tweet
oldest_tweet = None

# Variables for holding sentiments
compound_list = []
positive_list = []
negative_list = []
neutral_list = []

# Loop through 5 times
for x in range(5):

    # Run search around each tweet
    public_tweets = api.user_timeline(target, max_id=oldest_tweet)

    # Loop through all tweets
    for tweet in public_tweets:

        # Run Vader Analysis on each tweet
        results = analyzer.polarity_scores(tweet["text"])
        results_list.append({
            "Date": tweet["created_at"],
            "Compound": results["compound"],
            "Positive": results["pos"],
            "Negative": results["neg"],
            "Neutral": results["neu"],
            "Tweets Ago": counter
        })

        # Set the new oldest_tweet value
        oldest_tweet = tweet["id"] - 1

        counter += 1


# In[9]:


# Create a DataFrame using results_list and display
airline_df = pd.DataFrame().from_dict(results_list)
airline_df


# In[10]:


x_vals = airline_df["Tweets Ago"]
y_vals = airline_df["Compound"]
plt.plot(x_vals, y_vals, marker="o", linewidth=0.5, alpha=0.8)

now = datetime.now()
now = now.strftime("%Y-%m-%d %H:%M")
plt.title(f"Sentiment Analysis of Tweets({now}) for {target}")
plt.xlim([x_vals.max(), x_vals.min()])
plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")
plt.show()

