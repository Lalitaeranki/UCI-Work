
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[3]:


# Load in csv
rain_df = pd.read_csv("../Resources/avg_rain_state.csv")
rain_df.head()


# In[4]:


# Set x axis and tick locations
x_axis = np.arange(len(rain_df))
tick_locations = [value for value in x_axis]


# In[5]:


# Create a list indicating where to write x labels and set figure size to adjust for space
plt.figure(figsize=(20,3))
plt.bar(x_axis, rain_df["Inches"], color='r', alpha=0.5, align="center")
plt.xticks(tick_locations, rain_df["State"], rotation="vertical")


# In[6]:


# Set x and y limits
plt.xlim(-0.75, len(x_axis))
plt.ylim(0, max(rain_df["Inches"])+10)


# In[7]:


# Set a Title and labels
plt.title("Average Rain per State")
plt.xlabel("State")
plt.ylabel("Average Amount of Rainfall in Inches")


# In[8]:


# Save our graph and show the grap
plt.tight_layout()
plt.savefig("../Images/avg_state_rain.png")
plt.show()


# In[9]:


state_and_inches = rain_df[["State", "Inches"]]
state_and_inches = state_and_inches.set_index("State")
state_and_inches.head()


# In[10]:


state_and_inches.plot(kind="bar", figsize=(20, 3))
plt.title("Average Rain Per State")
plt.show()
plt.tight_layout()


# In[11]:


multi_plot = rain_df.plot(kind='bar', figsize=(20, 5))
multi_plot.set_xticklabels(rain_df["State"], rotation=45)
plt.show()
plt.tight_layout()

