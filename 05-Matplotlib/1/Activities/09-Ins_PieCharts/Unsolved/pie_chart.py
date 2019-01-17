
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[19]:


labels = ["Humans", "Smurfs", "Hobbits", "Ninjas"]
sizes = [220, 95, 80, 100]
color = ["red", "orange", "lightcoral", "lightskyblue"]
explode_values = (0.1, 0, 0, 0)


# In[20]:


plt.pie(sizes, explode=explode_values, labels=labels, colors=color,
       autopct="%1.1f%%", shadow=True, startangle=140)


# In[21]:


plt.axis("equal")

