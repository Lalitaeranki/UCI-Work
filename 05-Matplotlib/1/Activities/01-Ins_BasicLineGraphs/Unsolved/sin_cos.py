
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x_axis = np.arange(0, 6, 0.1)


# In[3]:


sin = np.sin(x_axis)


# In[4]:


cos = np.cos(x_axis)


# In[5]:


plt.plot(x_axis, sin)
plt.plot(x_axis, cos)

