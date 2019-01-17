
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# The path to our CSV file
file = "Resources/KickstarterData.csv"

# Read our Kickstarter data into pandas
df = pd.read_csv(file)
df.head()


# In[3]:


# Get a list of all of our columns for easy reference
df.columns


# In[4]:


# Extract "name", "goal", "pledged", "state", "country", "staff_pick",
# "backers_count", and "spotlight"
reduced_kickstarter_df = df.loc[:, ["name", "goal", "pledged", "state", "country",
                                   "staff_pick", "backers_count", "spotlight"]]
reduced_kickstarter_df


# In[5]:


# Query and select the projects that had pledges greater than 0
reduced_kickstarter_df = reduced_kickstarter_df.loc[
    (reduced_kickstarter_df["pledged"] > 0)
]
reduced_kickstarter_df.head()


# In[6]:


# Collect only those projects that were hosted in the US
hosted_in_us = reduced_kickstarter_df.loc[
    (reduced_kickstarter_df["country"] == "US")
]
hosted_in_us.head()


# In[7]:


# Create a new column that finds the average amount pledged to a project
hosted_in_us["average donation"] = hosted_in_us["pledged"] / hosted_in_us["backers_count"]
hosted_in_us.head()


# In[8]:


# First convert "average_donation", "goal", and "pledged" columns to float
# Then Format to go to two decimal places, include a dollar sign, and use comma notation
hosted_in_us["average donation"] = hosted_in_us["average donation"].astype(float).map("${:,.2f}".format)
hosted_in_us["goal"] = hosted_in_us["goal"].astype(float).map("${:,.2f}".format)
hosted_in_us["pledged"] = hosted_in_us["pledged"].astype(float).map("${:,.2f}".format)
hosted_in_us.head()


# In[9]:


# Calculate the total number of backers for all US projects
hosted_in_us["backers_count"].sum()


# In[10]:


# Calculate the average number of backers for all US projects
hosted_in_us["backers_count"].mean()


# In[11]:


# Collect only those US campaigns that have been picked as a "Staff Pick"
picked_by_staff = hosted_in_us.loc[hosted_in_us["staff_pick"] == True]
picked_by_staff


# In[12]:


# Group by the state of the campaigns and see if staff picks matter (Seems to matter quite a bit)
state_groups = picked_by_staff.groupby("state")
state_groups["name"].count()

