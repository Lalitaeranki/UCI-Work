
# coding: utf-8

# In[4]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests


# In[2]:


# URL of page to be scraped
url = 'https://newjersey.craigslist.org/search/sss?sort=rel&query=guitar'


# In[3]:


response = requests.get(url)


# In[5]:


soup = bs(response.text, 'lxml')


# In[7]:


print(soup.prettify())


# In[8]:


results = soup.find_all('li', class_="result-row")


# In[10]:


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
    except AttributeError as e:
        print(e)

