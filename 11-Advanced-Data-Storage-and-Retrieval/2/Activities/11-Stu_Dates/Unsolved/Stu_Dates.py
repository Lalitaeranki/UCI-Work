
# coding: utf-8

# # SQLAlchemy, Sqlite, and Dates

# ## Setup

# In[1]:


import matplotlib
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt


# In[2]:


import pandas as pd


# In[3]:


# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# In[4]:


engine = create_engine("sqlite:///../Resources/dow.sqlite", echo=False)


# In[5]:


engine.execute('SELECT * FROM dow LIMIT 5').fetchall()


# In[6]:


inspector = inspect(engine)
columns = inspector.get_columns('dow')
for c in columns:
    print(c['name'], c["type"])


# ## Reflect and query dates

# In[7]:


# Reflect Database into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)
Dow = Base.classes.dow


# In[8]:


session = Session(engine)


# ## Analysis

# Analyze the Average prices (open, high, low, close) for all stocks in the Month of May

# In[9]:


# Query for the stock and average prices (open, high, low, close) 
# for all stock in the month of May
# Sort the result by stock name
# YOUR CODE HERE
sel = [Dow.stock, 
       func.avg(Dow.open_price), 
       func.avg(Dow.high_price), 
       func.avg(Dow.low_price), 
       func.avg(Dow.close_price)]

may_averages = session.query(*sel).    filter(func.strftime("%m", Dow.date) == "05").    group_by(Dow.stock).    order_by(Dow.stock).all()
may_averages


# In[10]:


# Plot the Results in a Matplotlib bar chart
df = pd.DataFrame(may_averages, columns=['stock', 'open_avg', 'high_avg', 'low_avg', 'close_avg'])
df.set_index('stock', inplace=True)
df.plot.bar()
plt.tight_layout()
plt.show()


# ### Bonus
# Calculate the high-low peak-to-peak (PTP) values for `IBM` stock after `2011-05-31`. 
# * Note: high-low PTP is calculated using `high_price` - `low_price`
# * Use a DateTime.date object in the query filter
# * Use a list comprehension or numpy's ravel method to unpack the query's list of tuples into a list of PTP values.
# * Use matplotlib to plot the PTP values as a boxplot

# In[13]:


# Design a query to calculate the PTP for stock `IBM` after May, 2011
import datetime as dt
import numpy as np

date = dt.datetime(2011, 5, 31)

results = session.query(Dow.high_price - Dow.low_price).    filter(Dow.date > date).filter(Dow.stock == 'IBM').all()
    
#ptps = list(np.ravel(results))

ptps = [result[0] for result in results]
ptps


# In[14]:


# Load the query into a dataframe, set the index to the date, and plot the ptps
fig, ax = plt.subplots()

x = range(len(ptps))
ax.boxplot(ptps, patch_artist=True)
ax.set_title("IBM PTPs")
fig.tight_layout()
plt.show()

