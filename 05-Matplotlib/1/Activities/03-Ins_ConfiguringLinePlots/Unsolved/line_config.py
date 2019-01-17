
# coding: utf-8

# In[10]:


# https://stackoverflow.com/questions/43027980/purpose-of-matplotlib-inline/43028034
get_ipython().magic('matplotlib notebook')


# In[11]:


import numpy as np
import matplotlib.pyplot as plt


# In[12]:


x_axis = np.arange(0, 10, 0.1)
sin = np.sin(x_axis)
cos = np.cos(x_axis)


# In[13]:


plt.hlines(0, 0, 10, alpha=0.25)


# In[20]:


sine_handle, = plt.plot(x_axis, sin, marker='o', color='blue', label='Sine')
cosine_handle, = plt.plot(x_axis, cos, marker='^', color='red', label='Cosine')


# In[21]:


plt.legend(handles=[sine_handle, cosine_handle], loc="lower right")


# In[17]:


plt.savefig('../Images/lineConfig.png')

