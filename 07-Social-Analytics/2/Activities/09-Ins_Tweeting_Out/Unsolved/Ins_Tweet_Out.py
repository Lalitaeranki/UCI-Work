
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


# In[2]:


# Create a status update
api.update_status("Hey Programming on my Birthday!")


# In[3]:


api.update_with_media("../Resources/too-much-big-data.jpg", "Added an image")


# In[4]:


api.create_friendship(screen_name="@NB_ED4ever", follow=True)


# In[18]:


api.send_direct_message(screen_name="@NB_ED4ever", text="Hey Edward!")

