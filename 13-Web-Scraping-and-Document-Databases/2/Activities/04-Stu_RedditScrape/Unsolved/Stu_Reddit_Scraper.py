
# coding: utf-8

# In[7]:


# Dependencies
from bs4 import BeautifulSoup as bs
import requests
import os


# In[4]:


# URL of Python reddit
# url = 'https://www.reddit.com/r/Python/'
url = 'https://www.reddit.com/r/ProgrammingHumor/'


# In[5]:


# Retrieve page with the requests module
html = requests.get(url)


# In[14]:


# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(html, 'lxml')


# In[12]:


# Read HTML from file
filepath = os.path.join("Programmer-Humor.html")
with open(filepath, encoding="utf-8") as file:
    html = file.read()


# In[15]:


print(soup.prettify())


# In[23]:


# Find the number of subscribers
number_subscribers = soup.find('span', class_="subscribers").    find('span', class_="number").text
number_subscribers


# In[19]:


# Examine the results, then determine element that contains sought info
# results are returned as an iterable list
results = soup.find_all('div', class_="top-matter")


# In[21]:


# Loop through returned results
for result in results:   
    # Retrieve the thread title
    title = result.find('p', class_="title")
    
    # Access the thread's text content
    title_text = title.a.text
    
    try:
        # Access the thread with CSS selectors
        thread = result.find('li', class_="first")
        
        # The number of comments made in the thread
        comments = thread.text.lstrip()
        
        # Parse string, e.g. '47 comments' for possible numeric manipulation
        comments_num = int(comments.split()[0])
        
        # Access the href attribute with bracket notation
        link = thread.a["href"]

        # Run if the thread has comments
        if (comments_num):
            print('\n-----------------\n')
            print(title_text)
            print('Comments:', comments_num)
            print(link)
    except AttributeError as e:
        print(e)


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Stu_Reddit_Scraper.ipynb')

