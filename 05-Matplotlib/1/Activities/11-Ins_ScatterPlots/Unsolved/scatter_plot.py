
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


# Import Dependencies
import random
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


x_limit = 100
x_axis = np.arange(0, x_limit, 1)
data = [random.random() for value in x_axis]


# In[4]:


plt.scatter(x_axis, data, marker="o", facecolors="red", edgecolors="black",
           s=x_axis, alpha=0.75)


# In[6]:


plt.xlim(0, 100)


# In[7]:


plt.ylim(0, 1)


# In[8]:


plt.show()


# In[ ]:


get_ipython().system('jupyter nbconvert --to script scatter_plot.ipy')

