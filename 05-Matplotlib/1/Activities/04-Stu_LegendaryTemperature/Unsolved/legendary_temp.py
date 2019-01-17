
# coding: utf-8

# In[13]:


# Include this line to make plots interactive
get_ipython().magic('matplotlib notebook')


# In[14]:


import numpy as np
import matplotlib.pyplot as plt


# In[15]:


x_axis = np.arange(1, 13, 1)
x_axis


# In[16]:


points_F = [39, 42, 51, 62, 72, 82, 86, 84, 77, 65, 55, 44]


# In[17]:


points_C = [(x-32) * 0.56 for x in points_F]
points_C


# In[18]:


fahrenheit, = plt.plot(x_axis, points_F, marker="+", color="blue", linewidth=1, label="Fahrenheit")
celcius, = plt.plot(x_axis, points_C, marker="s", color="red", linewidth=1, label="Celcius")


# In[19]:


plt.legend(handles=[fahrenheit, celcius], loc="best")


# In[20]:


plt.xlabel("Months")
plt.ylabel("Degrees")


# In[21]:


plt.savefig('../Images/avg_temp.png')

