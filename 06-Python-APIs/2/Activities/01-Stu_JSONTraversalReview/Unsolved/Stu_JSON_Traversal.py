
# coding: utf-8

# In[3]:


# Dependencies
import json
import os

# Load JSON
filepath = os.path.join("..", "Resources", "youtube_response.json")
with open(filepath) as jsonfile:
    json_data = json.load(jsonfile)
json_data


# In[4]:


data = json_data['data']
data_items = data['items']


# In[5]:


title = data_items[0]['title']
print(f"Title: {title}")


# In[6]:


rating = data_items[0]['rating']
print(f"Rating: {rating}")


# In[7]:


default_thumbnail = data_items[0]['thumbnail']['default']
print(f"Thumbnail: {default_thumbnail}")


# In[8]:


view_count = data_items[0]['viewCount']
print(f"View Count: {view_count}")

