
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


# Mapping lets you format an entire DataFrame
file = "../Solved/Resources/sample_data.csv"
file_df = pd.read_csv(file)
file_df.head()


# In[7]:


file_df["avg_cost"] = file_df["avg_cost"].map("${:.2f}".format)
file_df["population"] = file_df["population"].map("{:,}".format)
file_df["other"] = file_df["other"].map("{:.2f}".format)
file_df.head()


# In[ ]:


get_ipython().system('')

