
# coding: utf-8

# In[3]:


get_ipython().magic('matplotlib notebook')


# In[9]:


# Dependencies
from random import randint
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem, ttest_ind


# In[5]:


high_prices = [randint(1, 5) * 1000 for x in range(1, 10)]
high_means = np.mean(high_prices)
high_sem = sem(high_prices)


# In[6]:


low_prices = [randint(1, 5) * 200 for x in range(1, 10)]
low_means = np.mean(low_prices)
low_sem = sem(low_prices)


# In[7]:


means = [high_means, low_means]
sems = [high_sem, low_sem]
labels = ["High Prices", "Low Prices"]


# In[8]:


fig, ax = plt.subplots()
x_axis = np.arange(0, len(means))
ax.errorbar(x_axis, means, sems, fmt="o")
ax.set_xlim(-0.5, 2.5)
ax.set_xticklabels(labels)
ax.set_xticks([0, 1, 2])
ax.set_ylabel("Mean House Price")
plt.show()


# In[11]:


(t_stat, p) = ttest_ind(high_prices, low_prices, equal_var=False)
if p < 0.05:
    print("The differences between the high and low prices are significant")
else:
    print("The differences between the high and low prices are due to chance")

