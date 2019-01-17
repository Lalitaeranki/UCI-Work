
# coding: utf-8

# # Doctor Decoder
# 
# Use Pandas scraping to help decode the medical abbreviations that a doctor might use.

# In[1]:


import pandas as pd


# Use Pandas to scrape the following site and decode the medical abbreviations in the list

# In[2]:


url = 'https://en.wikipedia.org/wiki/List_of_medical_abbreviations'
med_abbreviations = ['BMR', 'BP', 'ECG', 'MRI', 'qid', 'WBC']


# In[5]:


# Use Panda's `read_html` to parse the url
tables = pd.read_html(url)
tables


# In[6]:


# Find the medical abbreviations DataFrame in the list of DataFrames as assign it to `df`
# Assign the columns `['abb', 'full_name', 'other']`
df = tables[2]
df.columns = ['abb', 'full_name', 'other']
df.head()


# Cleanup of extra row

# In[7]:


# drop the `other` column
del df['other']


# In[8]:


# Drop the first row and set the index to the `abb` column
df = df.iloc[1:]
df.set_index('abb', inplace=True)
df.head()


# In[9]:


# Loop through the list of medical abbreviations and print the abbreviation
# along with the full description.
# Use the DataFrame to perform the lookup.
# YOUR CODE HERE
for abb in med_abbreviations:
    print(abb, df.loc[abb].full_name)

