
# coding: utf-8

# In[2]:


# Dependencies
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
from census import Census

# Census API Key
from config import api_key
censusObj = Census(api_key, year=2013)


# In[4]:


# Run Census Search to retrieve data on all zip codes (2013 ACS5 Census)
# See: https://github.com/CommerceDataService/census-wrapper for library documentation
# See: https://gist.github.com/afhaque/60558290d6efd892351c4b64e5c01e9b for labels
census_data = censusObj.acs5.get((
    "NAME", "B19013_001E", "B01003_001E", "B01002_001E", "B19301_001E", "B17001_002E"
), {"for": 'zip code tabulation area:*'})

census_pd = pd.DataFrame(census_data)

census_pd = census_pd.rename(columns={
    "B19013_001E": "Population",
    "B01003_001E": "Median Age",
    "B01002_001E": "Household Income",
    "B19301_001E": "Per Capita Income",
    "B17001_002E": "Poverty Count",
    "NAME": "Name",
    "zip code tabulation area": "Zipcode"
})

census_pd["Poverty Rate"] = 100 * census_pd["Poverty Count"].astype(int) / census_pd["Population"]
census_pd.head()

