
# coding: utf-8

# # SQLAlchemy, Sqlite, and Dates

# ## Setup

# In[4]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# In[5]:


engine = create_engine("sqlite:///dow.sqlite", echo=False)


# In[6]:


inspector = inspect(engine)
inspector.get_table_names()


# In[7]:


columns = inspector.get_columns('dow')
for column in columns:
    print(column["name"], column["type"])


# In[8]:


engine.execute("SELECT * FROM dow LIMIT 5").fetchall()


# In[11]:


Base = automap_base()
Base.prepare(engine, reflect=True)
Dow = Base.classes.dow
session = Session(bind=engine)


# In[12]:


session.query(func.count(Dow.date)).all()


# In[13]:


session.query(Dow.date).order_by(Dow.date).first()


# In[14]:


session.query(Dow.date).order_by(Dow.date.desc()).first()


# In[15]:


session.query(Dow.date).    filter(Dow.date > '2011-03-01').    order_by(Dow.date).all()


# In[16]:


import datetime as dt


# In[17]:


print(dt.date.today())


# In[18]:


week_ago = dt.date.today() - dt.timedelta(days=7)


# In[19]:


week_ago


# In[20]:


query_date = dt.date(2011, 4, 8) - dt.timedelta(days=7)
session.query(Dow.date, Dow.close_price).    filter(Dow.stock == "CSCO").    filter(Dow.date == query_date).all()


# In[21]:


dt.date.today().strftime("%d")


# In[ ]:


date_str = "14"
session.query(Dow.date).    filter(fi)

