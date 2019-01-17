
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json


# In[2]:


# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v2/launchpads"


# In[3]:


# Print the response object to the console
print(requests.get(url))


# In[4]:


# Retrieving data and converting it into JSON
print(requests.get(url).json())


# In[5]:


# Pretty Print the output of the JSON
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))

