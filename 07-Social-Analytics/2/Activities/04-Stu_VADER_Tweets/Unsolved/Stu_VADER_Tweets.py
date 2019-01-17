
# coding: utf-8

# In[11]:


# Dependencies
import tweepy
import numpy as np
import pandas as pd

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


# In[12]:


# Target User Account
target_user = ("@DalaiLama", "@realdonaldtrump", "@katyperry")

# Variables for holding sentiments
result_list = []

for user in target_user:
    score_results = {
        "compound": [],
        "positive": [],
        "neutral": [],
        "negative": []
    }
    
    # Loop through 10 pages of tweets (total 200 tweets)
    for x in range(1, 11):

        # Get all tweets from home feed
        public_tweets = api.user_timeline(user, page=x)

        score_results = get_results(public_tweets, score_results)
            
    
    user_results = {
        "Username": user,
        "Compound Score": np.mean(score_results["compound"]),
        "Positive Score": np.mean(score_results["positive"]),
        "Negative Score": np.mean(score_results["negative"]),
        "Neutral Score": np.mean(score_results["neutral"])
    }
    
    result_list.append(user_results)
    
    # Print the Averages
    print(f"User: {user_results['Username']}")
    print(f"Compound: {user_results['Compound Score']:.3f}")
    print(f"Positive: {user_results['Positive Score']:.3f}")
    print(f"Neutral: {user_results['Neutral Score']:.3f}")
    print(f"Negative: {user_results['Negative Score']:.3f}")


# In[13]:


results_df = pd.DataFrame(result_list).set_index("Username").round(3)
results_df


# In[8]:


def run_vader(text, score_results):
    results = analyzer.polarity_scores(text)
    # Add each value to the appropriate list
    score_results["compound"].append(results["compound"])
    score_results["positive"].append(results["pos"])
    score_results["negative"].append(results["neg"])
    score_results["neutral"].append(results["neu"])
    return score_results


# In[10]:


def get_results(tweet_timeline, score_results):
    # Loop through all tweets
    for tweet in tweet_timeline:
        # Run Vader Analysis on each tweet
        score_results = run_vader(tweet["text"], score_results)
        
    return score_results


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Stu_VADER_Gutenberg.ipynb')

