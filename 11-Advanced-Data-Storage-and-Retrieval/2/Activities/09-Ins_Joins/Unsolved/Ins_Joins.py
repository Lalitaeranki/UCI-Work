
# coding: utf-8

# # SQLAlchemy Joins

# ## Setup

# In[1]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect


# In[2]:


engine = create_engine("sqlite:///../Resources/mammal_masses.sqlite", echo=False)


# In[3]:


Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()


# In[4]:


EA = Base.classes.ea
NA = Base.classes.na


# In[5]:


session = Session(bind=engine)


# In[7]:


na_mammals = session.query(NA).filter(NA.genus == "Antilocapra").all()
for mammal in na_mammals:
    print(f"Family: {mammal.family}, Genus: {mammal.genus}")


# In[14]:


ea_mammals = session.query(EA).filter(EA.sporder == "Carnivora").all()
for mammal in ea_mammals:
    print(f"Family: {mammal.family}, Genus: {mammal.genus}")


# In[15]:


same_sporder = session.query(EA, NA).filter(EA.sporder == NA.sporder).limit(100).all()
for record in same_sporder:
    (ea, na) = record
    print(f"EA: {ea.sporder}")
    print(f"NA: {na.sporder}")


# In[16]:


selection = [EA.family, EA.genus, EA.species, NA.family, NA.genus, NA.species]
same_sporder = session.query(*selection).filter(EA.sporder == NA.sporder).limit(10).all()


# In[17]:


for record in same_sporder:
    (ea_fam, ea_gen, ea_spec, na_fam, na_gen, na_spec) = record
    print(f"The European animal '{ea_fam} {ea_gen} {ea_spec}' belongs to the same sporder as teh North American animal {na_fam} {na_gen} {na_spec}")

