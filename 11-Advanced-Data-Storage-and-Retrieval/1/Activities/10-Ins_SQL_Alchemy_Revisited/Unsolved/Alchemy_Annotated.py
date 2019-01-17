
# coding: utf-8

# In[1]:


# Dependencies
# ----------------------------------
# Imports the method used for connecting to DBs
from sqlalchemy import create_engine

# Imports the methods needed to abstract classes into tables
from sqlalchemy.ext.declarative import declarative_base

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float 

# PyMySQL 
import pymysql
pymysql.install_as_MySQLdb()


# In[2]:


# Create Dog and Cat Classes
# ----------------------------------

# Sets an object to utilize the default declarative base in SQL Alchemy
Base = declarative_base()


# Creates Classes which will serve as the anchor points for our Tables
class Dog(Base):
    __tablename__ = 'dog'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)


class Cat(Base):
    __tablename__ = 'cat'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    color = Column(String(255))
    age = Column(Integer)


# In[3]:


# Create a Specific Instance of the Dog and Cat classes
# ----------------------------------

# Calls the Pet Constructors to create "Dog" and "Cat" objets
dog = Dog(name="Rex", color="Brown", age=4)
cat = Cat(name="Felix", color="Gray", age=7)


# In[5]:


engine = create_engine("sqlite:///pets.sqlite")


# In[6]:


Base.metadata.create_all(engine)


# In[7]:


from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[8]:


session.add(dog)
session.add(cat)
session.commit()


# In[9]:


dog_list = session.query(Dog)
for record in dog_list:
    print(record.name)


# In[10]:


cat_list = session.query(Cat)
for record in cat_list:
    print(record.name)

