
# coding: utf-8

# In[1]:


# Dependencies
import json


# In[2]:


# Read JSONs
sample = "../Resources/SampleX.json"


# In[3]:


def load_json(jsonfile):
    """Load JSON from a file"""
    with open(jsonfile) as file_handle:
        return json.load(file_handle)


# In[4]:


sample_data = load_json(sample)
print(json.dumps(sample_data[0], indent=4, sort_keys=True))


# In[5]:


print("------------------------------------------------------------------")

# Using the Sample_Data provided above, write code to answer each of the
# following questions:


# In[6]:


# Question 1: What user account is the tweets in the Sample associated
# with?
user_account = sample_data[0]["user"]["name"]
print(f"User Account: {user_account}")


# In[8]:


# Question 2: How many followers does this account have associated with it?
follower_count = sample_data[0]["user"]["followers_count"]
print(f"Followers : {follower_count}")


# In[9]:


# Question 3: How many tweets are included in the Sample?
print(f"Number of tweets: {len(sample_data)}")


# In[10]:


# Question 4: How many tweets total has this account made?
total_tweets = sample_data[0]["user"]["statuses_count"]
print(f"The number of tweets total: {total_tweets}")


# In[11]:


# Question 5: What was the text in the most recent tweet?
recent_tweet = sample_data[0]['text']
print(f"The most recent tweet: {recent_tweet}")


# In[12]:


# Question 6: What was the text associated with each of the tweets
# included in this sample data?
print("All tweets")
for tweet in sample_data:
    print(f"{tweet['text']}")


# In[13]:


# Question 7 (Bonus): Which of the user's tweets was most frequently
# retweeted? How many retweets were there?
top_tweet = ""
top_tweet_follower_count = 0

for tweet in sample_data:
    if(tweet["retweet_count"] > top_tweet_follower_count):
        top_tweet = tweet["text"]
        top_tweet_follower_count = tweet["retweet_count"]

print(f"Most popular tweet: {top_tweet}")
print(f"Number of retweets: {top_tweet_follower_count}")

