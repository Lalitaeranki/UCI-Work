
# coding: utf-8

# In[12]:


from sqlalchemy import create_engine, and_, or_
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[2]:


class BaseballPlayer(Base):
  __tablename__ = "player"
  player_id = Column(String, primary_key=True)
  birth_year = Column(Integer)
  birth_month = Column(Integer)
  birth_day = Column(Integer)
  birth_country = Column(String)
  birth_state = Column(String)
  birth_city = Column(String)
  name_first = Column(String)
  name_last = Column(String)
  name_given = Column(String)
  weight = Column(Integer)
  height = Column(Integer)
  bats = Column(String)
  throws = Column(String)
  debut = Column(String)
  final_game = Column(String)


# In[3]:


# Create Database Connection
engine = create_engine('sqlite:///../Resources/database.sqlite')
Base.metadata.create_all(engine)


# In[4]:


from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[5]:


players = session.query(BaseballPlayer)
for player in players:
    print(player.name_given)


# In[7]:


usa = session.query(BaseballPlayer).    filter(BaseballPlayer.birth_country == "USA").count()
print(f"There are {usa} players from the USA")


# In[8]:


born_before_1990 = session.query(BaseballPlayer).    filter(BaseballPlayer.birth_year < 1990).count()
print(f"{born_before_1990} players were born before 1990")


# In[14]:


born_after_1989 = session.query(BaseballPlayer).    filter(or_(BaseballPlayer.birth_year > 1989, BaseballPlayer.birth_country == "USA")).    count()
print(f"{born_after_1989} USA players were born after 1989")


# In[15]:


born_on_1990 = session.query(BaseballPlayer).    filter_by(birth_year = 1990).first()
print(born_on_1990.name_given)

