
# coding: utf-8

# In[1]:


# Pandas
import pandas as pd

# SQL Alchemy
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[2]:


# Create Engine and Pass in MySQL Connection
engine = create_engine("sqlite:///../Resources/Census_Data.sqlite")
conn = engine.connect()


# In[3]:


data = pd.read_sql("SELECT * FROM Census_Data", conn)


# In[4]:


data.head()


# In[ ]:


get_ipython().system('jupyter nbconvert --to script ')

