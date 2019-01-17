
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x_axis_data = np.arange(1, 13, 1)
x_axis_data


# In[3]:


points = [39, 42, 51, 62, 72, 82, 86, 84, 77, 65, 55, 44]


# In[4]:


plt.plot(x_axis_data, points)
plt.show()


# In[5]:


points_C = [(x-32)*0.56 for x in points]
points_C


# In[6]:


plt.plot(x_axis_data, points_C)
plt.show()


# In[7]:


plt.plot(x_axis_data, points)
plt.plot(x_axis_data, points_C)
plt.show()

