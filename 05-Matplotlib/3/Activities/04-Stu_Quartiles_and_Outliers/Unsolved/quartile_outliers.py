
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


# Dependencies
import matplotlib.pyplot as plt
from stats import median
import numpy as np


# In[3]:


### Data Points
arr = np.array([2.3, 10.2,11.2, 12.3, 14.5, 14.6, 15.0, 15.1, 19.0, 24.0])
arr


# In[4]:


# Find the median
mid = median(arr)
mid


# In[7]:


# Use numpy to create quartiles
lower_quartile = np.percentile(arr, 25)
upper_quartile = np.percentile(arr, 75)


# In[8]:


# Print the quartiles
print(f"Q1 is {lower_quartile}")
print(f"Q3 is {upper_quartile}")


# In[10]:


# Calculate the interquartile range
interquartile_range = (upper_quartile - lower_quartile)
interquartile_range


# In[11]:


# Find upper boundary
# Q3 + (1.5 * IQR)
upper_boundary = upper_quartile + (1.5 * interquartile_range)
upper_boundary


# In[13]:


# Find upper boundary
# Q1 - (1.5 * IQR)
lower_boundary = lower_quartile - (1.5 * interquartile_range)
lower_boundary


# In[14]:


# Check for any lower outliers
lower_outliers = arr[arr <= lower_boundary]
lower_outliers


# In[15]:


# Check for any upper outliers
upper_outliers = arr[arr >= upper_boundary]
upper_outliers


# In[16]:


# Create box plot
plt.boxplot(arr, showmeans=True)
plt.grid()
plt.show()


# In[ ]:


get_ipython().system('jupyter nbconvert --to script ')

