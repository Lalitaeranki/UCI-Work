
# coding: utf-8

# In[4]:


from splinter import Browser
from bs4 import BeautifulSoup as bs


# # Mac Users

# In[ ]:


# https://splinter.readthedocs.io/en/latest/drivers/chrome.html
get_ipython().system('which chromedriver')


# In[ ]:


executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
browser = Browser('chrome', **executable_path, headless=False)


# # Windows Users

# In[2]:


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[6]:


url = 'http://quotes.toscrape.com/'
browser.visit(url)


# In[7]:


for x in range(1, 6):
    html = browser.html
    soup = bs(html, 'lxml')
    quotes = soup.find_all('span', class_='text')
    
    for quote in quotes:
        print(f"page: {x}-----------------")
        print(quote.text)
        
    browser.click_link_by_partial_text('Next')

