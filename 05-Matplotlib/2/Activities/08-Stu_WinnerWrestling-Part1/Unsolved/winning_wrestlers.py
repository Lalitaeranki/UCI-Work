
# coding: utf-8

# # Winnining Wrestlers Entertainment
# 
# In this activity you will be taking four seperate csvs that were scraped down from a wrestling database, merging them together, and then creating charts to visualize a wrestler's wins and losses over the course of four years.
# 
# ### Part 1 - Macho Merging
# 
# * You will likely need to perform three different merges over the course of this activity, changing the names of your columns as you go along.

# In[1]:


# Import the necessary modules
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[2]:


# Bring each CSV into a separate data frame
wrestling_2013 = "../Resources/WWE-Data-2013.csv"
wrestling_2014 = "../Resources/WWE-Data-2014.csv"
wrestling_2015 = "../Resources/WWE-Data-2015.csv"
wrestling_2016 = "../Resources/WWE-Data-2016.csv"

wrestling_2013_df = pd.read_csv(wrestling_2013)
wrestling_2014_df = pd.read_csv(wrestling_2014)
wrestling_2015_df = pd.read_csv(wrestling_2015)
wrestling_2016_df = pd.read_csv(wrestling_2016)


# In[4]:


# Merge the first two datasets (2013 and 2014) on "Wrestler" so that no data is lost (should be 182 rows)
combined_wrestler_df = pd.merge(wrestling_2013_df, wrestling_2014_df, how="outer", on="Wrestler")
combined_wrestler_df.head()


# In[6]:


# Rename our _x columns to "2013 Wins", "2013 Losses", and "2013 Draws"
combined_wrestler_df = combined_wrestler_df.rename(columns={
    "Wins_x": "2013 Wins",
    "Losses_x": "2013 Losses",
    "Draws_x": "2013 Draws"
})

# Rename our _y columns to "2014 Wins", "2014 Losses", and "2014 Draws"
combined_wrestler_df = combined_wrestler_df.rename(columns={
    "Wins_y": "2014 Wins",
    "Losses_y": "2014 Losses",
    "Draws_y": "2014 Draws"
})
combined_wrestler_df.head()


# In[7]:


# Merge our newly combined dataframe with the 2015 dataframe
combined_wrestler_df = pd.merge(combined_wrestler_df, wrestling_2015_df, how="outer", on="Wrestler")
combined_wrestler_df.head()


# In[8]:


# Rename "wins", "losses", and "draws" to "2015 Wins", "2015 Losses", and "2015 Draws"
combined_wrestler_df = combined_wrestler_df.rename(columns={
    "Wins": "2015 Wins",
    "Losses": "2015 Losses",
    "Draws": "2015 Draws"
})
combined_wrestler_df.head()


# In[9]:


# Merge our newly combined dataframe with the 2016 dataframe
combined_wrestler_df = pd.merge(combined_wrestler_df, wrestling_2016_df, how="outer", on="Wrestler")
combined_wrestler_df.head()


# In[10]:


# Rename "wins", "losses", and "draws" to "2016 Wins", "2016 Losses", and "2016 Draws"
combined_wrestler_df = combined_wrestler_df.rename(columns={
    "Wins": "2016 Wins",
    "Losses": "2016 Losses",
    "Draws": "2016 Draws"
})
combined_wrestler_df.head()


# In[12]:


combined_wrestler_df = combined_wrestler_df.fillna(0)


# In[13]:


combined_wrestler_df["Total Wins"] = combined_wrestler_df["2013 Wins"] + combined_wrestler_df["2014 Wins"] + combined_wrestler_df["2015 Wins"] + combined_wrestler_df["2016 Wins"]


# In[14]:


combined_wrestler_df["Total Losses"] = combined_wrestler_df["2013 Losses"] + combined_wrestler_df["2014 Losses"] + combined_wrestler_df["2015 Losses"] + combined_wrestler_df["2016 Losses"]


# In[15]:


combined_wrestler_df["Total Draws"] = combined_wrestler_df["2013 Draws"] + combined_wrestler_df["2014 Draws"] + combined_wrestler_df["2015 Draws"] + combined_wrestler_df["2016 Draws"]


# In[16]:


combined_wrestler_df["Total Matches"] = combined_wrestler_df["Total Wins"] + combined_wrestler_df["Total Losses"] + combined_wrestler_df["Total Draws"]


# In[17]:


combined_wrestler_df.head()


# In[18]:


wrestled_over_hundred = combined_wrestler_df.loc[(combined_wrestler_df["Total Matches"] >= 100) &
                                                (combined_wrestler_df["2013 Wins"] > 0) &
                                                (combined_wrestler_df["2016 Wins"] > 0)]
wrestled_over_hundred = wrestled_over_hundred.set_index("Wrestler")
wrestled_over_hundred.head()


# In[20]:


wrestler_name = input("What wrestler's career would you like to look at?")


# In[24]:


wins_over_time = wrestled_over_hundred.loc[wrestler_name, ["2013 Wins", "2014 Wins", "2015 Wins", "2016 Wins"]]
wins_over_time


# In[25]:


losses_over_time = wrestled_over_hundred.loc[wrestler_name, ["2013 Losses", "2014 Losses", "2015 Losses", "2016 Losses"]]
losses_over_time


# In[ ]:


years = [2013, 2014, 2015, 2016]
plt.plot(years, wins_over_time, color="green", label="Wins")
plt.plot(years, losses_over_time, color="green", label="Wins")


# In[19]:


get_ipython().system('jupyter nbconvert --to script winning_wrestlers.ipynb')

