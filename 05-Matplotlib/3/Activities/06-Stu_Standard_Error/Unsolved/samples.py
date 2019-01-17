
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


# Dependencies
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


# In[3]:


# Read and shuffle data
housing_data = pd.read_csv("../Resources/housing_data.csv")
housing_data = housing_data.sample(frac=1).reset_index(drop=True)


# In[4]:


# Create a bunch of samples, each with div items
div = 20
lim = len(housing_data) // div
samples = [housing_data.iloc[(i * div):(i * div + div), 13]
           for i in range(0, lim)]


# In[5]:


means = [s.mean() for s in samples]
sem = [s.sem() for s in samples]


# In[7]:


fig, ax = plt.subplots()
x_axis = np.arange(0, len(means))
ax.errorbar(x_axis, means, sem, fmt="o", color="b", alpha=0.5, label="Mean of House Prices")
ax.set_xlim(-0.5, len(means))
ax.set_xlabel("Sample Number")
ax.set_ylabel("Mean of Median House Prices")
plt.legend(loc="best", fontsize="small", fancybox=True)
plt.show()

