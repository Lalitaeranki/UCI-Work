
# coding: utf-8

# In[1]:


import requests
import json


# In[2]:


# New Dependency! Use this to pretty print the JSON
# https://docs.python.org/3/library/pprint.html
from pprint import pprint


# In[3]:


# Note that the ?t= is a query param for the t-itle of the
# movie we want to search for.
url = "http://www.omdbapi.com/?t="
api_key = "&apikey=trilogy"


# In[4]:


print(url + "Aliens" + api_key)


# In[8]:


# Performing a GET request similar to the one we executed
# earlier
response = requests.get(url + "Toy Story" + api_key)
print(response.url)


# In[9]:


# Converting the response to JSON, and printing the result.
data = response.json()
pprint(data)


# In[7]:


# Print a few keys from the response JSON.
print(f"Movie was directed by {data['Director']}")
print(f"Movie wsa released in {data['Country']}")

