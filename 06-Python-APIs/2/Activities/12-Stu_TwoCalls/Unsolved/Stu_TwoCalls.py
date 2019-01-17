
# coding: utf-8

# In[1]:


# Dependencies
import requests

url = "http://api.worldbank.org/v2/"


# In[4]:


# Get the list of lending types the world bank has
lending_response = requests.get(f"{url}lendingTypes?format=json").json()
lending_types = [lending_type["id"] for lending_type in lending_response[1]]
lending_types


# In[5]:


# Next, determine how many countries fall into each lending type.
# Hint: Look at the first element of the response array.
country_count_by_type = {}
for lending_type in lending_types:
    query_url = f"{url}countries?lendingType={lending_type}&format=json"
    response = requests.get(query_url).json()
    country_count_by_type[lending_type] = response[0]["total"]


# In[6]:


# Print the number of countries of each lending type
for key, value in country_count_by_type.items():
    print(f"The number of countries with lending type {key} is {value}")

