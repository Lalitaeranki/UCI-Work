
# coding: utf-8

# In[10]:


# Dependencies
from random import random
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem


# In[11]:


sample_size = 100
samples = [[True if random() < 0.5 else False for x in range (0, sample_size)]
           for y in range(0, 10)]
x_axis = np.arange(0, len(samples), 1)


# In[14]:


means = [np.mean(s) for s in samples]
standard_errors = [sem(s) for s in samples]
standard_errors


# In[13]:


fig, ax = plt.subplots()
ax.errorbar(x_axis, means, standard_errors, fmt="o")
ax.set_xlim(-1, len(samples) + 1)
ax.set_xlabel("Sample Number")
ax.set_ylabel("Proportion of People Voting Republican")

