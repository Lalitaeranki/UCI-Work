
# coding: utf-8

# In[8]:


from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
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


# In[3]:


url = 'http://books.toscrape.com/'
browser.visit(url)


# In[ ]:


html = browser.html
soup = bs(html, 'lxml')

sidebar = soup.find('ul', class_='nav-list')
categories = sidebar.find_all('li')

category_list = []
url_list = []
book_url_list = []

for category in categories:
    title = category.text.strip()
    category_list.append(title)
    book_url = category.find('a')['href']
    url_list.append(book_url)
    
book_url_list = [f"http://books.toscrape.com/{url}" for url in url_list]

titles_and_urls = zip(category_list, book_url_list)

try:
    for title_url in titles_and_urls:
        browser.click_link_by_partial_text('next')
except ElementDoesNotExist:
        print('Scaping Complete')

