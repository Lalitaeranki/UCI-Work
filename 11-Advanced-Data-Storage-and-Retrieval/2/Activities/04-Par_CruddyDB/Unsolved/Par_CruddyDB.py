
# coding: utf-8

# In[1]:


# Import SQL Alchemy
from sqlalchemy import create_engine

# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float


# In[2]:


# Create the Garbage class
class Garbage(Base):
    __tablename__ = "garbage_collection"
    id = Column(Integer, primary_key=True)
    item = Column(String(255))
    weight = Column(Float)
    collector = Column(String(255))


# In[3]:


# Create a connection to a SQLite database
engine = create_engine("sqlite:///garbage.sqlite")


# In[4]:


# Create the garbage_collection table within the database
Base.metadata.create_all(engine)


# In[5]:


# To push the objects made and query the server we use a Session object
from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[6]:


# Create some instances of the Garbage class
garbage1 = Garbage(item="Sofa", weight=90.5, collector="Jacob")
garbage2 = Garbage(item="Broken TV", weight=10.75, collector="Paul")
garbage3 = Garbage(item="Burger", weight=0.55, collector="Phil")


# In[7]:


# Add these objects to the session
session.add(garbage1)
session.add(garbage2)
session.add(garbage3)
session.commit()


# In[8]:


# Update two rows of data
update1 = session.query(Garbage).filter_by(id=1).first()
update1.collector = "Jacob Deming"
update2 = session.query(Garbage).filter_by(id=2).first()
update2.weight = 11.25
session.commit()


# In[9]:


# Delete the row with the lowest weight
session.query(Garbage).filter_by(id=3).delete()
session.commit()


# In[10]:


# Collect all of the items and print their information
items = session.query(Garbage)
for item in items:
    print("-"*12)
    print(f"ID: {item.id}")
    print(f"Item: {item.item}")
    print(f"Weight: {item.weight}")
    print(f"Collector: {item.collector}")

