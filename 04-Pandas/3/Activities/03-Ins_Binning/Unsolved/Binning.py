
# coding: utf-8

# In[7]:


# Import Dependencies
import pandas as pd


# In[8]:


raw_data = {
    'Class': ['Oct', 'Oct', 'Jan', 'Jan', 'Oct', 'Jan'], 
    'Name': ["Cyndy", "Logan", "Laci", "Elmer", "Crystle", "Emmie"], 
    'Test Score': [90, 56, 72, 88, 98, 67]}
df = pd.DataFrame(raw_data)
df


# In[12]:


bins = [0, 60, 70, 80, 90, 100]
group_names = ["F", "D", "C", "B", "A"]


# In[13]:


df["Test Score Summary"] = pd.cut(df["Test Score"], bins, labels=group_names)
df


# In[5]:


df = df.groupby("Test Score Summary")
df.max()


# In[ ]:


get_ipython().system('')

