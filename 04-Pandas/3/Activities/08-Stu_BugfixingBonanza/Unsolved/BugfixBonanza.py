
# coding: utf-8

# In[40]:


import pandas as pd


# In[41]:


# Create a reference to the CSV and import it into a Pandas DataFrame
csv_path = "Resources/EclipseBugs.csv"
eclipse_df = pd.read_csv(csv_path)
eclipse_df.head()


# In[42]:


eclipse_df.columns


# In[43]:


eclipse_df = eclipse_df.rename(columns={
    "Bug\nID": "Bug ID",
    "Assignee\nReal\nName": "Assignee Real Name",
    "Number of\nComments": "Number of Comments",
    "Reporter\nReal\nName": "Reporter Real Name",
    "Target\nMilestone": "Target Milestone"
})
eclipse_df.columns


# In[44]:


# Finding the average number of comments per bug
average_comments = eclipse_df["Number of Comments"].mean()
average_comments


# In[45]:


# Grouping the DataFrame by "Assignee"
assignee_group = eclipse_df.groupby("Assignee")

# Count how many of each component Assignees worked on and create DataFrame
assignee_work = pd.DataFrame(assignee_group["Component"].value_counts())
assignee_work.head()


# In[46]:


# Rename the "Component" column to "Component Bug Count"
assignee_work = assignee_work.rename(columns={
    "Component": "Component Bug Count"
})
assignee_work.head()


# In[47]:


assignee_group.head()


# In[48]:


assignee_group["Assignee"].count()


# In[49]:


# Find the percentage of bugs overall fixed by each Assignee
total_bugs = eclipse_df["Assignee"].count()
bugs_per_user = assignee_group["Assignee"].count()

user_bug_percent = pd.DataFrame((bugs_per_user/total_bugs)*100)
user_bug_percent.head()


# In[50]:


user_bug_percent = user_bug_percent.rename(columns={
    "Assignee": "Percent of Total Bugs Assigned"
})
user_bug_percent = user_bug_percent.reset_index()
user_bug_percent.head()


# In[51]:


assignee_work = assignee_work.reset_index()
assignee_work.head()


# In[52]:


# Merge the "Percent of Total Bugs Assigned" into the DataFrame
assignee_work_merged = assignee_work.merge(user_bug_percent, on="Assignee")

assignee_work_merged = assignee_work_merged[["Assignee", "Percent of Total Bugs Assigned", "Component", "Component Bug Count"]]

# Remove the extra columns

assignee_work_merged.head()


# In[ ]:


get_ipython().system('jupyter nbconv')

