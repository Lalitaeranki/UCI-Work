
# coding: utf-8

# In[1]:


# Dependencies
import random
import json
import requests


# In[2]:


# Let's get the JSON for 100 posts sequentially.
url = "http://jsonplaceholder.typicode.com/posts/"


# In[4]:


# Create an empty list to store the responses
response_json = []


# In[3]:


# Create random indices representing
# a user's choice of posts
indices = random.sample(list(range(1, 100)), 10)
indices


# In[5]:


# Make a request for each of the indices
for x in range(len(indices)):
    print(f"Making request number: {x} for ID: {indices[x]}")
    post_response = requests.get(url + str(indices[x]))
    response_json.append(post_response.json())


# In[6]:


# Now we have 10 post objects, 
# which we got by making 100 requests to the API.
print(f"We have {len(response_json)} posts!")


# In[7]:


# preview the json
response_json

