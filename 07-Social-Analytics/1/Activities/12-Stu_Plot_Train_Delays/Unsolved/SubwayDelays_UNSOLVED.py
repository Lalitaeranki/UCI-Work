
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import json
import pandas as pd
import matplotlib.pyplot as plt
from config import consumer_key, consumer_secret, access_token, access_token_secret

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[2]:


# Create an empty dictionary that will hold delayed trains
delayed_trains = {}
    
# Target User = A Twitter account that sends tweets regarding delayed trains
target_user = "SubwayStats"

# Loop through 50 pages of statuses
for x in range(1, 51):

    # Get all tweets from home feed. Set pagination to "x"
    public_tweets = api.user_timeline(target_user, page=x)

    # Loop through all tweets
    for tweet in public_tweets:
        
        # Break tweet text into a list of lowercase words
        tweet_text = tweet["text"].lower().split(" ")
        
        # Print the tweet text only if it contains the word "delays" or "change"
        if("delays" in tweet_text or "change" in tweet_text):
            print(tweet["text"].lower())
            
            # Loop through hashtags to extract the train names
            # Hint: try ["entities"] and ["hashtags]
            for hashtag in tweet["entities"]["hashtags"]:
                
                # Extract the hashtag's text, and set it to lower case
                train_name = hashtag["text"].lower()
                
                # Remove all hashtags that are extraneous
                if (train_name != "nycsubway" and train_name != "mta" and train_name != "nyc"):
                                        
                    # If train is new, i.e. not in the dictionary, add it to the dictionary, and set its value to 1
                    if(train_name not in delayed_trains):
                        delayed_trains[train_name] = 1
                    
                    # If it already exists add 1 to its count
                    else:    
                        delayed_trains[train_name] += 1


# In[3]:


# Print the Train Delay counts
print(delayed_trains)

# Convert Train Delay object into a pandas series
delayed_trains_pd = pd.Series(delayed_trains)

# Preview the results
delayed_trains_pd


# In[4]:


# Create a plot  
plt.bar(range(len(delayed_trains_pd.index)), delayed_trains_pd.values)
plt.xticks(range(len(delayed_trains_pd.index)), delayed_trains_pd.index, rotation=45)
plt.ylabel("Number of Delays")
plt.xlabel("Train Name")
plt.title("Number of Train Delays According to 1000 Subway Status Tweets")
plt.show()

