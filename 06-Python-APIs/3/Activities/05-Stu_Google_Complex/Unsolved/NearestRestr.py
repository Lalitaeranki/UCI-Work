
# coding: utf-8

# In[1]:


# Dependencies
# Dependencies
import pandas as pd
import numpy as np
import requests
import json

# Google API Key
from config import gkey


# In[2]:


types_df = pd.read_csv("../Resources/ethnic_restr.csv")
types_df.head()


# In[3]:


types_df["name"] = ""
types_df["address"] = ""
types_df["price_level"] = ""
types_df["rating"] = ""
types_df.head()


# In[4]:


base_url ="https://maps.googleapis.com/maps/api/place/nearbysearch/json"
params = {
    "location": "39.952583, -75.16522",
    "rankby": "distance",
    "type": "restaurant",
    "key": gkey
}

for index, row in types_df.iterrows():
    restr_type = row["ethnicity"]
    params["keyword"] = restr_type
    print(f"Retrieving Results for Index {index}: {restr_type}")
    response = requests.get(base_url, params).json()
    
    results = response["results"]
    
    try:
        print(f"Closest {restr_type} restaurant is {results[0]['name']}.")
        types_df.loc[index, 'name'] = results[0]['name']
        types_df.loc[index, 'address'] = results[0]['vicinity']
        types_df.loc[index, 'price_level'] = results[0]['price_level']
        types_df.loc[index, 'rating'] = results[0]['rating']
    except (KeyError, IndexError):
        print("Missing field/result... skipping")
    
    print("-------------------")


# In[5]:


types_df

