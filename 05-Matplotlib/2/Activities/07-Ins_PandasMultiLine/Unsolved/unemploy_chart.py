
# coding: utf-8

# In[1]:


# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[2]:


# Read CSV
unemployed_data_one = pd.read_csv("../Resources/unemployment_2010-2011.csv")
unemployed_data_two = pd.read_csv("../Resources/unemployment_2012-2014.csv")

# Merge our two data frames together
combined_unemployed_data = pd.merge(unemployed_data_one, unemployed_data_two, on="Country Name")
combined_unemployed_data.head()


# In[3]:


del combined_unemployed_data["Country Code_y"]
combined_unemployed_data = combined_unemployed_data.rename(columns={"Country Code_x": "Country Code"})
combined_unemployed_data.head()


# In[4]:


combined_unemployed_data = combined_unemployed_data.set_index("Country Code")


# In[5]:


average_unemployment = combined_unemployed_data.mean()
years = average_unemployment.keys()


# In[6]:


world_avg, = plt.plot(years, average_unemployment, color="blue", label="World Average")
country_one, = plt.plot(years, combined_unemployed_data.loc['USA', ["2010", "2011", "2012", "2013", "2014"]],
                       color="green", label=combined_unemployed_data.loc["USA", "Country Name"])

plt.legend(handles=[world_avg, country_one], loc="best")
plt.show()


# In[7]:


average_unemployment.plot(label="World Average")
combined_unemployed_data.loc["USA", "2010":"2014"].plot(label="United States")
plt.legend()
plt.show()


# In[ ]:


get_ipython().system('jupyter nbconvert --to script unemploy_chart.ipyn')

