
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


x_axis =np.arange(0, 5, 0.1)
x_axis


# In[3]:


e_x = [np.exp(x) for x in x_axis]
e_x


# In[4]:


plt.plot(x_axis, e_x)


# In[5]:


plt.show()


# In[6]:


plt.xlabel("Time with Matplotlib")
plt.ylabel("How cool Matplotlib seems")

plt.plot(x_axis, e_x)


# In[ ]:


get_ipython().system('jupyter')

