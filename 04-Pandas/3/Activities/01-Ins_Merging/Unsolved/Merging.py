
# coding: utf-8

# In[1]:


# Dependencies
import pandas as pd


# In[2]:


raw_data_info = {
    "customer_id": [112, 403, 999, 543, 123],
    "name": ["John", "Kelly", "Sam", "April", "Bobbo"],
    "email": ["jman@gmail", "kelly@aol.com", "sports@school.edu", "April@yahoo.com", "HeyImBobbo@msn.com"]
}
info_pd = pd.DataFrame(raw_data_info, columns=["customer_id", "name", "email"])
info_pd


# In[3]:


# Create DataFrames
raw_data_items = {
    "customer_id": [403, 112, 543, 999, 654],
    "item": ["soda", "chips", "TV", "Laptop", "Cooler"],
    "cost": [3.00, 4.50, 600, 900, 150]
}
items_pd = pd.DataFrame(raw_data_items, columns=[
                        "customer_id", "item", "cost"])
items_pd


# In[4]:


merge_table = pd.merge(info_pd, items_pd, on="customer_id")
merge_table


# In[5]:


merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="outer")
merge_table


# In[6]:


merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="left")
merge_table


# In[7]:


merge_table = pd.merge(info_pd, items_pd, on="customer_id", how="right")
merge_table


# In[8]:


merge_table = info_pd.merge(items_pd, on="customer_id", how="left")
merge_table


# In[9]:


merge_table = items_pd.merge(info_pd, on="customer_id", how="left")
merge_table

