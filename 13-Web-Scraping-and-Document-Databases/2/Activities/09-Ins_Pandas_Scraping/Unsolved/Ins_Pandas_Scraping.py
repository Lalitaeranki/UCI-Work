
# coding: utf-8

# # Scraping with Pandas

# In[1]:


import pandas as pd


# We can use the `read_html` function in Pandas to automatically scrape any tabular data from a page.

# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States'


# In[3]:


tables = pd.read_html(url)
tables


# In[4]:


type(tables)


# In[5]:


tables[0]


# In[6]:


df = tables[0]
df.columns = ['State', 'Abr.', 'State-hood Rank', 'Capital', 'Capital Since', 'Area (sq-mi)', 'Municipal Population', 'Metropolitan', 'Metropolitan Population', 'Population Rank', 'Notes']
df.head()


# In[7]:


df = df.iloc[2:]
df.head()


# In[8]:


df.set_index('State', inplace=True)
df.head()


# In[9]:


df.loc["Alabama"]


# In[10]:


html_table = df.to_html()
html_table


# In[11]:


html_table.replace('\n', '')


# In[12]:


df.to_html('tables.html')


# In[ ]:


get_ipython().system('jupyter nbconvert --to script ')

