
# coding: utf-8

# In[1]:


#Dependencies
import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


#list of tv show titles to query
tv_shows = ["Altered Carbon", "Grey's Anatomy", "This is Us", "The Flash", "Vikings", "Shameless", "Arrow", "Peaky Blinders", "Dirk Gently"]

# make iterative requests to TVmaze search endpoint
base_url = "http://api.tvmaze.com/search/shows?q="

ratings = []

for show in tv_shows:
    response = requests.get(base_url+show).json()
    ratings.append(response[0]['show']['rating']['average'])


# In[3]:


# create dataframe
show_dict = {
    "title": tv_shows,
    "rating": ratings
}

shows_df = pd.DataFrame(show_dict)
shows_df


# In[4]:


# use matplotlib to create a bar chart from the dataframe
shows_df.plot(kind="bar")


# In[ ]:


get_ipython().system('jupyter')

