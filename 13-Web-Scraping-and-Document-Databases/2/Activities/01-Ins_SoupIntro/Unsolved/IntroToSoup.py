
# coding: utf-8

# In[1]:


# Dependencies
from bs4 import BeautifulSoup as bs


# In[2]:


html_string = """
<html>
<head>
<title>
A Simple HTML Document
</title>
</head>
<body>
<p>This is a very simple HTML document</p>
<p>It only has two paragraphs</p>
</body>
</html>
"""


# In[3]:


soup = bs(html_string, "html.parser")
type(soup)


# In[4]:


print(soup.prettify())


# In[5]:


soup.title


# In[6]:


soup.title.text


# In[7]:


soup.title.text.strip()


# In[8]:


soup.body


# In[9]:


soup.body.p.text


# In[10]:


soup.body.find_all('p')


# In[11]:


soup.body.find_all('p')[0].text.strip()


# In[12]:


soup.body.find('p').text


# In[ ]:


get_ipython().system('jupt')

