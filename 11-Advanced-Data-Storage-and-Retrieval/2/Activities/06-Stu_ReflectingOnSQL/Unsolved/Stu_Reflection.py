
# coding: utf-8

# In[1]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


# In[2]:


# Create engine using the `demographics.sqlite` database file
engine = create_engine("sqlite:///../Resources/demographics.sqlite")


# In[3]:


# Declare a Base using `automap_base()`
Base = automap_base()


# In[4]:


# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)


# In[5]:


# Print all of the classes mapped to the Base
Base.classes.keys()


# In[6]:


# Assign the demographics class to a variable called `Demographics`
Demographics = Base.classes.demographics


# In[7]:


# Create a session
session = Session(bind=engine)


# In[9]:


first_row = session.query(Demographics).first()
first_row.__dict__


# In[12]:


# Use the session to query Demographics table and display the first 5 locations
rows = session.query(Demographics.location).limit(5).all()
for row in rows:
    print(row)


# In[17]:


# BONUS: Query and print the number of unique Locations
# Hints: Look into counting and grouping operations in SQLAlchemy
locations = session.query(Demographics.location).group_by(Demographics.location).all()
for location in locations:
    print(location)

