
# coding: utf-8

# In[5]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import pymongo


# In[2]:


# Initialize PyMongo to work with MongoDBs
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[3]:


# Define database and collection
db = client.craigslist_db
collection = db.items


# In[6]:


# URL of page to be scraped
url = 'https://newjersey.craigslist.org/search/sss?sort=rel&query=guitar'

# Retrieve page with the requests module
response = requests.get(url)
# Create BeautifulSoup object; parse with 'lxml'
soup = bs(response.text, 'lxml')


# In[7]:


results = soup.find_all('li', class_="result-row")


# In[9]:


for result in results:
    try:
        title = result.find('a', class_="result-title").text
        price = result.a.span.text
        link = result.a['href']
        
        if (title and price and link):
            print('-'*12)
            print(title)
            print(price)
            print(link)
            
            post = {
                'title': title,
                'price': price,
                'url': link
            }
            
            collection.insert_one(post)
    except AttributeError as e:
        print(e)


# In[10]:


listings = db.items.find()
for listing in listings:
    print(listing)

