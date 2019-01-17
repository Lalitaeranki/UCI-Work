
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import json
import numpy as np
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)


# In[2]:


# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# In[3]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[27]:


# Target Search Term
target_term = "@UN_News_Centre"


# In[28]:


# Lists to hold sentiments
compound_list = []
positive_list = []
negative_list = []
neutral_list = []


# In[29]:


# Grab 25 tweets
public_tweets = api.search(target_term, count=25, result_type="recent")


# In[30]:


# Loop through all tweets
for tweet in public_tweets["statuses"]:
    # Run Vader Analysis on each tweet
    results = analyzer.polarity_scores(tweet["text"])
    compound = results["compound"]
    positive = results["pos"]
    negative = results["neg"]
    neutral = results["neu"]

    # Add each value to the appropriate array
    compound_list.append(compound)
    positive_list.append(positive)
    negative_list.append(negative)
    neutral_list.append(neutral)


# In[31]:


# Store the Average Sentiments
sentiments = {
    "Compound": np.mean(compound_list),
    "Positive": np.mean(positive_list),
    "Negative": np.mean(negative_list),
    "Neutral": np.mean(neutral_list)
}


# In[32]:


# Print the Sentiments
print(sentiments)

