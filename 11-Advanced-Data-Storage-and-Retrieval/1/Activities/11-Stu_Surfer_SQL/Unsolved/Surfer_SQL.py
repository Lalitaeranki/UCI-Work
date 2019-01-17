
# coding: utf-8

# In[1]:


# Import SQL Alchemy
from sqlalchemy import create_engine

# Import PyMySQL (Not needed if mysqlclient is installed)
import pymysql
pymysql.install_as_MySQLdb()


# In[2]:


# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# In[3]:


# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float


# In[4]:


# Create Surfer and Board classes
# ----------------------------------
class Surfer(Base):
    __tablename__ = 'surfers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    hometown = Column(String(255))
    wipeouts = Column(Integer)
    rank = Column(Integer)

class Board(Base):
    __tablename__ = 'surfboards'
    id = Column(Integer, primary_key=True)
    surfer_id = Column(Integer)
    board_name = Column(String(255))
    color = Column(String(255))
    length = Column(Integer)


# In[5]:


# Create specific instances of the Surfer and Board classes
# ----------------------------------
# Create a new surfer named "Bruno"
# Create a new board and associate it with a surfer's ID
bruno = Surfer(name="Bruno", hometown="LA", rank=10)
bruno_board = Board(surfer_id=1, board_name="Awwwyeah", color="Blue", length=68)


# In[6]:


# Create Database Connection
# ----------------------------------
# Establish Connection to MySQL
engine = create_engine("sqlite:///surfer.sqlite")


# In[7]:


# Create both the Surfer and Board tables within the database
Base.metadata.create_all(engine)


# In[8]:


# To push the objects made and query the server we use a Session object
from sqlalchemy.orm import Session
session = Session(bind=engine)


# In[9]:


# Add "Bruno" to the current session
# Add "Awwwyeah" to the current session
# Commit both objects to the database
session.add(bruno)
session.add(bruno_board)
session.commit()


# In[10]:


# Query the database and collect all of the surfers in the Surfer table
surfer_list = session.query(Surfer)
for bro in surfer_list:
    print(bro.name)
    print(bro.hometown)
    print(bro.rank)


# In[12]:


board_list = session.query(Board)
for board in board_list:
    print(board.board_name)
    print(board.color)
    print(board.length)

