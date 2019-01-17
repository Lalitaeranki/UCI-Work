
# coding: utf-8

# In[9]:


# Dependencies
import requests
from config import api_key
import time

url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?"

# Store a search term
query="fashion"


# Search for articles published between a begin and end date
begin_date = "19900101"
end_date = "19901001"

# Build url
query_url = f"{url}api-key={api_key}&q={query}&begin_date={begin_date}&end_date={end_date}"
print(query_url)


# In[10]:


# Retrieve articles
articles = requests.get(query_url).json()
articles_list = [article for article in articles["response"]["docs"]]

for article in articles_list:
    print(f"A snippet from the article: {article['snippet']}")
    print()


# In[12]:


# BONUS: How would we get 30 results? 
# HINT: Look up the page query param
article_list = []
for page in range(0, 3):
    query_url = f"{url}api-key={api_key}&q={query}&begin_date={begin_date}&end_date={end_date}"
    query_url = f"{query_url}&page={page}"
    articles = requests.get(query_url).json()
    
    time.sleep(1)
    
    for article in articles["response"]["docs"]:
        articles_list.append(article)


# In[13]:


for article in articles_list:
    print(f"A snippet from the article: {article['snippet']}")
    print()

