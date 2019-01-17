
# coding: utf-8

# In[1]:


# SQL Alchemy
from sqlalchemy import create_engine

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[13]:


# Create Engine and Pass in MySQL Connection
engine = create_engine("sqlite:///../Resources/icecreamstore.sqlite")


# In[15]:


# Query All Records in the the Database
data = engine.execute("SELECT * FROM icecreamstore")
for record in data:
    print(record)


# In[9]:


# Query Single Record in the the Database
data = engine.execute("SELECT * FROM icecreamstore WHERE Price >= 1.25")
for record in data:
    print(record)

