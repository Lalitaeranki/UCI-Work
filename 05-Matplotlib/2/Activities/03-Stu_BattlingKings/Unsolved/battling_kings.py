
# coding: utf-8

# In[10]:


get_ipython().magic('matplotlib notebook')


# In[11]:


# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[12]:


# Read CSV
got_data = pd.read_csv("Resources/got.csv")
got_data.head()


# In[13]:


# Get attacker and defender data
attacker_data = got_data["attacker_king"].value_counts()
defending_data = got_data["defender_king"].value_counts()


# In[14]:


# Get total battle data
battle_data = attacker_data.add(defending_data, fill_value=0)


# In[15]:


battle_data.head()


# In[21]:


# Configure plot and ticks
battle_data.plot(kind="bar", facecolor="red", rot=45)


# In[17]:


# Set textual properties
plt.title("The Bloodthirst of Kings")
plt.ylabel("Number of battles Participated In")
plt.xlabel("King")


# In[19]:


# Show plot
plt.tight_layout()

