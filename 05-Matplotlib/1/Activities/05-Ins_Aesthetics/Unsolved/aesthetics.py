
# coding: utf-8

# In[10]:


get_ipython().magic('matplotlib notebook')


# In[11]:


# Dependencies
import matplotlib.pyplot as plt
import numpy as np


# In[12]:


# Generate the x values from 0 to 10 using a step of 0.1
x_axis = np.arange(0, 10, 0.1)
sin = np.sin(x_axis)
cos = np.cos(x_axis)


# In[13]:


# Add a semi-transparent horizontal line at y = 0# Add a 
plt.hlines(0, 0, 10, alpha=0.25)


# In[14]:


# Use dots or other markers for your plots, and change their colors
plt.plot(x_axis, sin, linewidth=0, marker="o", color="blue")
plt.plot(x_axis, cos, linewidth=0, marker="^", color="red")


# In[15]:


plt.title("Juxtaposed Sine and Cosine Curves")
plt.xlabel("Input (Sampled Real Numbers from 0 to 10)")
plt.ylabel("Value of Sine (blue) and Cosine (red)")


# In[16]:


plt.xlim(0, 10)
plt.ylim(-1, 1)


# In[17]:


plt.grid()

