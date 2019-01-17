
# coding: utf-8

# In[1]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


# In[2]:


# Create engine using the `demographics.sqlite` database file
engine = create_engine("sqlite:///../Resources/dow.sqlite")


# In[3]:


Base = automap_base()


# In[5]:


Base.prepare(engine, reflect=True)


# In[6]:


Base.classes.keys()


# In[7]:


Dow = Base.classes[dow


# In[8]:


session = Session(bind=engine)


# In[9]:


first_row = session.query(Dow).first()
first_row.__dict__


# In[10]:


for row in session.query(Dow.stock, Dow.volume).limit(15).all():
    print(row)


# In[ ]:


get_ipython().system('jupyter nbconvert --to script')

