
# coding: utf-8

# In[10]:


# Dependencies
import json
import requests 


# In[11]:


# Specify the URL
url = "http://nyt-mongo-scraper.herokuapp.com/api/headlines"

# Make request and store response
response = requests.get(url)

print(response.status_code)


# In[12]:


# JSON-ify response
response_json = response.json()
response_json


# In[13]:


# Print first and last articles
print(f"The first response is {json.dumps(response_json[0], indent=2)}")


# In[14]:


print(f"The last response is {json.dumps(response_json[-1], indent=2)}")


# In[15]:


#Print the number of responses received.
print(f"We recieved {len(response_json)} responses")

