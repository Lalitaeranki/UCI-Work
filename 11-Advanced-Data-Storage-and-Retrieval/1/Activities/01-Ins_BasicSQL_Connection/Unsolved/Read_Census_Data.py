
# coding: utf-8

# In[1]:


# SQL Alchemy
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[5]:


engine = create_engine("sqlite:///../Resources/Census_Data.sqlite")


# In[6]:


data = engine.execute("SELECT * FROM census_data")


# In[7]:


for record in data:
    print(record)

