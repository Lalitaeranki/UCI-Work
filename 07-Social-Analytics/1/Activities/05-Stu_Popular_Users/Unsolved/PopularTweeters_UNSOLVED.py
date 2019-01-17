
# coding: utf-8

# In[1]:


# Dependencies
import tweepy
import json
import pandas as pd
from config import consumer_key, consumer_secret, access_token, access_token_secret
# Your Twitter API Keys


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[2]:


# Import CSV file into Data Frame
popular_tweeters = pd.read_csv("../Resources/PopularAccounts.csv", dtype=str)

# Iterate through DataFrame
for index, row in popular_tweeters.iterrows():
    
    # Error handling
    try:
        # Grab the username
        target_user = row["Screen Name"]
        # print(target_user)

        # Use the username with the Twitter API get_user
        user_account = api.get_user(target_user)
        user_real_name = user_account["name"]

        # Get the specific column data
        user_tweets = user_account["statuses_count"]
        # Do the same for "followers_count", "friends_count", and "favourites_count"
        followers_count = user_account["followers_count"]
        friends_count = user_account["friends_count"]
        favourites_count = user_account["favourites_count"]
        
        # Replace the row information for each
        popular_tweeters.at[index, "Real Name"] = user_real_name
        # Do the same for "Tweets", "Followers", "Following, and "Favorites Count"
        popular_tweeters.at[index, "Tweets"] = user_tweets
        popular_tweeters.at[index, "Followers"] = followers_count
        popular_tweeters.at[index, "Following"] = friends_count
        popular_tweeters.at[index, "Favorites Count"] = favourites_count
    # If an error is encountered, move on with the next iteration of the loop
    except tweepy.TweepError as e:
        print(f"Exception for {row['Screen Name']}: {e}")
        popular_tweeters.drop(labels=index, inplace=True)
        
# Export the new CSV as "PopularAccounts_New.csv"
# Hint: use the to.csv() method
    
# View the DataFrame
# Hint: use the head() method


# In[3]:


popular_tweeters.to_csv("PopularAccounts_New.csv", index=False)
popular_tweeters.head()


# In[4]:


# Calculate Averages of the following: "Tweets"; "Followers"; "Follwing"; "Favorites Count"
# See "Create DataFrame" below for the variable names you should use
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

