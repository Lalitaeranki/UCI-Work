
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


users = [13000, 26000, 52000, 30000, 9000]
x_axis = np.arange(len(users))


# In[4]:


plt.bar(x_axis, users, color='r', alpha=0.5, align="center")


# In[5]:


tick_locations = [value for value in x_axis]
plt.xticks(tick_locations, ["Java", "C++", "Python", "Ruby", "Clojure"])


# In[6]:


plt.xlim(-0.75, len(x_axis)-0.25)


# In[7]:


plt.ylim(0, max(users)+5000)


# In[8]:


plt.title("Popularity of Programming Languages")
plt.xlabel("Programming Languages")
plt.ylabel("Number of People Using Programming Language")

