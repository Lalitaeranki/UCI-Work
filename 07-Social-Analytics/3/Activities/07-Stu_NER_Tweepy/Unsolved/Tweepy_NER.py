
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib inline')
import tweepy
import spacy
import pandas as pd


# In[2]:


# Import Twitter API Keys
from config import consumer_key, consumer_secret, access_token, access_token_secret


# In[3]:


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# In[4]:


nlp = spacy.load("en")


# In[5]:


tweet_dict = {
    "text": [],
    "label": []
}


# In[6]:


user_tweets = api.user_timeline("PaulONeillYES")


# In[7]:


for tweet in user_tweets:
    doc = nlp(tweet["text"])
    
    if not doc.ents:
        print("No entities to visualize")
        print("------------------------")
    else:
        for ent in doc.ents:
            tweet_dict["text"].append(ent.text)
            tweet_dict["label"].append(ent.label_)
            
        spacy.displacy.render(doc, style="ent", jupyter=True)
        print("------------------------")


# In[8]:


tweet_df = pd.DataFrame(tweet_dict)
tweet_df


# In[9]:


label_frequency = tweet_df.groupby(["label"]).count()


# In[10]:


label_frequency.plot.bar()

