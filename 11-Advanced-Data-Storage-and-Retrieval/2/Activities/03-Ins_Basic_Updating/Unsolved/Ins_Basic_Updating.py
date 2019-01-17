
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[2]:


class Pet(Base):
    __tablename__ = 'pet'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)
    age = Column(Integer)


# In[3]:


Base.metadata.tables


# In[4]:


engine = create_engine("sqlite:///pets.sqlite")


# In[5]:


Base.metadata.create_all(engine)


# In[6]:


from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[7]:


session.add(Pet(name="Justin Timbersnake", type="snake", age=2))
session.add(Pet(name="Pawtrick Stewart", type="dog", age=10))
session.add(Pet(name="Godzilla", type="iguana", age=1))
session.add(Pet(name="Marshmallow", type="polar bear", age=4))


# In[12]:


engine.execute("SELECT * FROM pet").fetchall()


# In[9]:


session.new


# In[10]:


session.commit()


# In[11]:


session.new


# In[13]:


session.query(Pet.name, Pet.type, Pet.age).all()


# In[14]:


pet = session.query(Pet).filter_by(name="Marshmallow").first()
pet.age += 1


# In[15]:


session.dirty


# In[16]:


session.commit()


# In[17]:


session.dirty


# In[18]:


session.query(Pet.name, Pet.type, Pet.age).all()


# In[19]:


session.query(Pet).filter_by(id=4).delete()
session.commit()


# In[20]:


session.query(Pet.name, Pet.type, Pet.age).all()

