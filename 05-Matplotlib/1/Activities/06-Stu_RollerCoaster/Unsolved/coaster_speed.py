
# coding: utf-8

# In[9]:


get_ipython().magic('matplotlib notebook')


# In[10]:


import numpy as np
import matplotlib.pyplot as plt


# In[11]:


time = np.arange(0, 130, 10)
speed_chain = [9, 8, 90, 85, 80, 70, 70, 65, 55, 60, 70, 65, 50]
speed_launch = [75, 70, 60, 65, 60, 45, 55, 50, 40, 40, 35, 35, 30]


# In[12]:


danger_drop, = plt.plot(time, speed_chain, color="red", label="Danger Drop")
railgun, = plt.plot(time, speed_launch, color="blue", label="RailGun")


# In[13]:


plt.title("Coaster Speed Over Time")
plt.xlabel("Coaster Runtime")
plt.ylabel("Speed (MPH)")


# In[14]:


plt.xlim(0, 120)
plt.ylim(5, 95)


# In[18]:


plt.legend(handles=[danger_drop, railgun], loc="lower right")


# In[16]:


plt.grid()


# In[17]:


plt.show()

