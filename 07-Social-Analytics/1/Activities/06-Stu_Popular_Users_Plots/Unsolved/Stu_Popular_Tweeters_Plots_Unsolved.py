
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


# Import CSV file into Data Frame
popular_tweeters = pd.read_csv("../Resources/PopularAccounts.csv", dtype=str)

# Iterate through DataFrame
for index, row in popular_tweeters.iterrows():

    try:
        # Grab the username
        target_user = row["Screen Name"]
        # print(target_user)

        # Use the username with the Twitter API get_user
        user_account = api.get_user(target_user)
        user_real_name = user_account["name"]

        # Get the specific column data
        user_tweets = user_account["statuses_count"]
        user_followers = user_account["followers_count"]
        user_following = user_account["friends_count"]
        user_favorites = user_account["favourites_count"]

        # Replace the row information for each
        popular_tweeters.at[index, "Real Name"] = user_real_name
        popular_tweeters.at[index, "Tweets"] = user_tweets
        popular_tweeters.at[index, "Followers"] = user_followers
        popular_tweeters.at[index, "Following"] = user_following
        popular_tweeters.at[index, "Favorites Count"] = user_favorites
        
    except tweepy.TweepError as e:
        print(f"exception for {row['Screen Name']}: {e}")
        popular_tweeters.drop(index=index,inplace=True)
    
# Export the new CSV
popular_tweeters.to_csv("PopularAcounts_New.csv", index=False)

# View the DataFrame
popular_tweeters.head()


# In[3]:


# Calculate Averages
average_tweet_count = popular_tweeters["Tweets"].mean()
average_followers = popular_tweeters["Followers"].mean()
average_following_count = popular_tweeters["Following"].mean()
average_favorites_count = popular_tweeters["Favorites Count"].mean()

# Create DataFrame
averages = {"Average Tweet Count": average_tweet_count, 
            "Average Follower Count": average_followers, 
            "Average Following Count": average_following_count,
            "Average Favorites Count": average_favorites_count}

# Create a Dataframe of the averages
pd.DataFrame(averages, index=[0])


# In[4]:


# Extract Tweet Counts and Follower Counts
# YOUR CODE HERE
tweet_counts = popular_tweeters["Tweets"]
follow_count = popular_tweeters["Followers"]


# In[5]:


# Extract Tweet Counts and Follower Counts
plt.scatter(tweet_counts, follow_count)
plt.xlabel("Tweet Counts")
plt.ylabel("Follower Counts")
plt.title("Tweet Counts vs Follower Counts")
plt.show()


# In[6]:


# Plot Tweet Counts vs Follower Counts
# YOUR CODE HERE


# In[7]:


# Plot Number Following vs Following Counts
# YOUR CODE HERE


# In[8]:


# Plot Number of Favorites vs Favorite Counts
# YOUR CODE HERE

