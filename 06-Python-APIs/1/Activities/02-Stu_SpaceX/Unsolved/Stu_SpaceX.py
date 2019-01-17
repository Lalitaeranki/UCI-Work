
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json


# In[2]:


# URL for GET requests to retrieve vehicle data
url = "https://api.spacexdata.com/v2/launchpads"


# In[3]:


# Pretty print JSON for all launchpads
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))


# In[5]:


# Pretty print JSON for a specific launchpad
response = requests.get(url + "/kwajalein_atoll").json()
print(json.dumps(response, indent=4, sort_keys=True))

