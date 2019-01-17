
# coding: utf-8

# In[2]:


# Dependencies
import requests

url = "http://api.worldbank.org/v2/"
format = "json"

# Get country information in JSON format
countries_response = requests.get(f"{url}countries?format={format}").json()

# First element is general information, second is countries themselves
countries = countries_response[1]


# In[3]:


# Report the names
for country in countries:
    print(country["name"])

