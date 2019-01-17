
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json


# In[3]:


# Performing a GET Request and saving the 
# API's response within a variable
url = "https://api.spacexdata.com/v2/rockets/falcon9"
response = requests.get(url).json()
print(json.dumps(response, indent=4, sort_keys=True))


# In[4]:


# It is possible to grab a specific value 
# from within the JSON object
print(response["cost_per_launch"])


# In[5]:


# It is also possible to perform some
# analyses on values stored within the JSON object
number_of_payloads = len(response["payload_weights"])
print(f"There are {number_of_payloads} payloads.")


# In[6]:


# Finally, it is possible to reference the
# values stored within sub-dictionaries and sub-lists
payload_weight = response["payload_weights"][0]["kg"]
print(f"The first payload weighed {payload_weight} Kilograms")

