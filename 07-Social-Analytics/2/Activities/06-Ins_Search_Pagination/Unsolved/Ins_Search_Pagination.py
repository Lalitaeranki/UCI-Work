
# coding: utf-8

# In[1]:


# Dependencies
import tweepy

# Twitter API Keys
from config import (consumer_key, 
                    consumer_secret, 
                    access_token, 
                    access_token_secret)

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[3]:


# Search for People Tweeting about Mark Hamill
search_term = "Mark Hamill"

# Create variable for holding the oldest tweet
oldest_tweet = None

# List to hold unique IDs
unique_ids = []

# Counter to keep track of the number of tweets retrieved
counter = 0


# Loop through 5 times (total of 500 tweets)
for x in range(5):
    
    public_tweets = api.search(search_term, 
                               count=100, 
                               result_type="recent", 
                               max_id=oldest_tweet)

    # Print Tweets
    for tweet in public_tweets["statuses"]:

        # Print the username
        print(tweet["user"]["screen_name"])  

        # Print the tweet id
        print(f"Tweet ID: {tweet_id}")  

        # Print the tweet text
        print(tweet["text"]) 
        
        # Append tweet_id to ids list if it doesn't already exist
        # This allows checking for duplicate tweets
        tweet_id = tweet["id"]
        if tweet_id not in unique_ids:
            unique_ids.append(tweet_id)
       
        # Reassign the the oldest tweet (i.e. the max_id)
        # Subtract 1 so the previous oldest isn't included
        # in the new search
        oldest_tweet = tweet_id - 1
        
        # Increase counter by 1
        counter += 1 


# In[6]:


# Print total number of tweets retrieved
print(counter)


# In[5]:


# Print the number of unique ids retrieved
print(len(unique_ids))


# In[7]:


get_ipython().system('jupyter nbconvert --to script Ins_Tweets_No_Filter.ipynb')

