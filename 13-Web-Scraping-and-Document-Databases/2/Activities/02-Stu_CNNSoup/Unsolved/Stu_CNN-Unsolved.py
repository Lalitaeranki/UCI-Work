
# coding: utf-8

# In[1]:


# Dependencies
import os
from bs4 import BeautifulSoup as bs


# In[2]:


# Read HTML from file
filepath = os.path.join("..", "Resources", "template.html")
with open(filepath) as file:
    html = file.read()


# In[3]:


# Create a Beautiful Soup object
soup = bs(html, 'lxml')


# In[4]:


# Extract title text
title = soup.title.text
title


# In[5]:


# Print all paragraph texts
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)


# In[10]:


# Print all ten headlines
tds = soup.find_all('td')
headlines = []

for td in tds:
    if(td.a):
        if(td.a.text):
            headlines.append(td)


# In[7]:


# Print only the headlines
for x in range(10):
    print(headlines[x].text)

