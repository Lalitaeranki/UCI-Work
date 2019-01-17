
# coding: utf-8

# In[1]:


# Pandas
import pandas as pd

# SQL Alchemy
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[5]:


# Create Engine and Pass in MySQL Connection
engine1 = create_engine("sqlite:///../Resources/Census_Data.sqlite")
conn1 = engine1.connect()

engine2 = create_engine("sqlite:///../Resources/zip_census.sqlite")
conn2 = engine2.connect()


# In[6]:


# Query All Records in the the Census_Data Table
census_data = pd.read_sql("SELECT * FROM Census_Data;", conn1)


# In[7]:


# Query All Records in the Zip Table
zip_data = pd.read_sql("SELECT * FROM zip_census;", conn2)


# In[ ]:


# Merge the columns
combined_data = pd.merge(census_data, zip_data, on="CityState", h)


# In[ ]:


# Combined Data

