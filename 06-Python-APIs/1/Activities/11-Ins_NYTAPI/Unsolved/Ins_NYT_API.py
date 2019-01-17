
# coding: utf-8

# In[1]:


# Dependencies
import requests
from pprint import pprint
from config import api_key

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"


# In[2]:


# Search for articles that mention granola
query = "granola"


# In[6]:


# Build query URL
query_url = url + "api-key=" + api_key + "&q=" + query
print(query_url)


# In[4]:


# Request articles
articles = requests.get(query_url).json()

# The "response" property in articles contains the actual articles
# list comprehension
articles_list = [article for article in articles["response"]["docs"]]
pprint(articles_list)


# In[5]:


# Print the web_url of each stored article
print("Your reading list")
for article in articles_list:
    print(article["web_url"])

