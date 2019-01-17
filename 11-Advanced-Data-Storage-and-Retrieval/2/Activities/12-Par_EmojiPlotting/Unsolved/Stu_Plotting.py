
# coding: utf-8

# # Plotting Query Results

# ## Setup

# In[1]:


# Import Matplot lib
import matplotlib
from matplotlib import style
style.use('seaborn')
import matplotlib.pyplot as plt


# In[2]:


import pandas as pd


# In[3]:


# Import SQLAlchemy `automap` and other dependencies here
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func


# In[4]:


# Create an engine for the `emoji.sqlite` database
engine = create_engine("sqlite:///../Resources/emoji.sqlite", echo=False)


# ## Explore Database

# In[5]:


# Use the Inspector to explore the database and print the table names
inspector = inspect(engine)
inspector.get_table_names()


# In[6]:


# Use Inspector to print the column names and types
columns = inspector.get_columns('emoji')
for column in columns:
    print(column["name"], column["type"])


# In[7]:


# Use `engine.execute` to select and display the first 10 rows from the emoji table
engine.execute("SELECT * FROM emoji LIMIT 10").fetchall()


# ## Reflect database and Query

# In[8]:


# Reflect Database into ORM class
Base = automap_base()
Base.prepare(engine, reflect=True)
Emoji = Base.classes.emoji


# In[9]:


# Start a session to query the database
session = Session(engine)


# Use Matplotlib to create a horizontal bar chart and plot the emoji `score` in descending order. Use `emoji_char` as the y-axis labels. Plot only the top 10 emojis ranked by score

# In[10]:


# Query Emojis for `emoji_char`, `emoji_id`, and `score` and save the query into results
results = session.query(Emoji.emoji_char, Emoji.emoji_id, Emoji.score).    order_by(Emoji.score.desc()).all()


# Unpack tuples using list comprehensions

# In[11]:


# Unpack the `emoji_id` and `scores` from results and save into separate lists
emoji_id = [result[1] for result in results[:10]]
scores = [int(result[2]) for result in results[:10]]


# ## Plot using Matplotlib

# In[12]:


# Create a horizontal bar chart and plot the `emoji_id` on the y-axis and the `score` on the x-axis
# Challenge: Try to plot the scores in descending order on the graph (The largest score is at the top)
fig, ax = plt.subplots()
ypos = range(1, len(scores)+1)
ax.barh(ypos, scores[::-1])
ax.set_xlabel("score")
ax.set_ylabel("emoji")
ax.set_yticks(ypos)
ax.set_yticklabels(emoji_id[::-1])
ax.set_title("Emoji Scores")
fig.tight_layout()
plt.show()


# 
# ## Plot using Pandas Plotting

# Load the results into a Pandas DataFrame

# In[13]:


# Load the results into a pandas dataframe. Set the index to the `emoji_id`
df = pd.DataFrame(results[:10], columns=['emoji_char', 'emoji_id', 'score'])
df.set_index('emoji_id', inplace=True)
df.head(10)


# Plot using Pandas

# In[14]:


# Plot the dataframe as a horizontal bar chart using pandas plotting
df.iloc[::-1].plot.barh(title="emoji ranking")
plt.tight_layout()
plt.show()


# In[15]:


# BONUS: Use Pandas `read_sql_query` to load a query statement directly into the DataFrame
stmt = session.query(Emoji).    order_by(Emoji.score.desc()).statement
df2 = pd.read_sql_query(stmt, session.bind)
df2.head()

