
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd


# In[2]:


# Create a path to the csv and read it into a Pandas DataFrame
csv_path = "Resources/ted_talks.csv"
ted_df = pd.read_csv(csv_path)

ted_df.head()


# In[3]:


# Figure out the minimum and maximum views for a TED Talk
print(ted_df["views"].max())
print(ted_df["views"].min())


# In[5]:


# Create bins in which to place values based upon TED Talk views
bins = [0, 200000, 400000, 600000, 800000, 1000000, 2000000, 3000000, 4000000, 5000000, 50000000]
# Create labels for these bins
group_labels = ["0 to 200k", "200k to 400k", "400k to 600k", "600k to 800k",
               "800k to 1mil", "1mil to 2mil", "2mil to 3mil", "3mil to 4mil", "4mil to 5mil", "5mil to 50mil"]


# In[7]:


# Slice the data and place it into bins
pd.cut(ted_df["views"], bins, labels=group_labels).head()


# In[8]:


# Place the data series into a new column inside of the DataFrame
ted_df["View Group"] = pd.cut(ted_df["views"], bins, labels=group_labels)
ted_df.head()


# In[10]:


# Create a GroupBy object based upon "View Group"
ted_group = ted_df.groupby("View Group")


# Find how many rows fall into each bin
print(ted_group["comments"].count())


# Get the average of each column within the GroupBy object
ted_group[["comments", "duration", "languages"]].mean()


# In[ ]:


get_ipython().system('jupyter nbconvert --t')

