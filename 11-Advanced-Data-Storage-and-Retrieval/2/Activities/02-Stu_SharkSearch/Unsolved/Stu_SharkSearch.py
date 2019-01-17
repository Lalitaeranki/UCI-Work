
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import Column, Integer, String, Float

from config import dbuser, dbpasswd, dburi, dbport, dbname

from sqlalchemy import create_engine


# In[2]:


from sqlalchemy import create_engine
engine = create_engine(f"mysql://{dbuser}:{dbpasswd}@{dburi}:{dbport}/{dbname}")
Base.metadata.create_all(engine)


# In[ ]:


#In case your sql server doesn't require a password
#from sqlalchemy import create_engine
#engine = create_engine(f"mysql://{dbuser}@{dburi}:{dbport}/{dbname}")
#Base.metadata.create_all(engine)


# In[3]:


from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[5]:


# create your shark class
class Sharks(Base):
    __tablename__ = 'sharks'
    id = Column(Integer, primary_key=True)
    case_number = Column(String)
    date = Column(String)
    year = Column(Integer)
    type = Column(String)
    country = Column(String)
    area = Column(String)
    location = Column(String)
    activity = Column(String)
    name = Column(String)
    sex = Column(String)
    age = Column(Integer)
    injury = Column(String)
    fatal_y_n = Column(String)
    time = Column(String)
    species = Column(String)
    investigator_or_source = Column(String)
    pdf = Column(String)
    original_order = Column(Integer)


# In[15]:


# print all locations of shark attacks
attacks = session.query(Sharks)
for attack in attacks:
    print(attack.country)


# In[7]:


# find the number of provoked attacks
provoked_count = session.query(Sharks).filter_by(type="provoked").count()
provoked_count


# In[8]:


# find the number of attacks in USA
usa_count = session.query(Sharks).filter_by(country="USA").count()
usa_count


# In[9]:


# find the number of attacks in 2017
attack_2017_count = session.query(Sharks).filter_by(year=2017).count()
attack_2017_count


# In[10]:


# find the number of attacks while surfing
attack_surfing_count = session.query(Sharks).filter_by(activity="surfing").count()
attack_surfing_count


# In[11]:


# find the number of fatal attacks
fatal_count = session.query(Sharks).filter_by(fatal_y_n="y").count()
fatal_count


# In[12]:


# find the number of fatal attacks while surfing
attack_surfing_count = session.query(Sharks).    filter_by(activity="surfing").    filter_by(fatal_y_n="y").    count()
attack_surfing_count


# In[16]:


# find the number of fatal attacks in 2017 in Australia
attack_surfing_count = session.query(Sharks).    filter(Sharks.fatal_y_n == "y").    filter_by(country="AUSTRALIA").    filter_by(year=2017).    count()
attack_surfing_count

