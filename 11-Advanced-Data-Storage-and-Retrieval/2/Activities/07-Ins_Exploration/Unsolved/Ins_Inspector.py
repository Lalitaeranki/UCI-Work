
# coding: utf-8

# In[1]:


# Import SQLAlchemy `automap` and other dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect


# In[2]:


# Create the connection engine
engine = create_engine("sqlite:///../Resources/dow.sqlite")


# In[3]:


inspector = inspect(engine)


# In[4]:


inspector.get_table_names()


# In[5]:


columns = inspector.get_columns('dow')
for column in columns:
    print(column["name"], column["type"])

