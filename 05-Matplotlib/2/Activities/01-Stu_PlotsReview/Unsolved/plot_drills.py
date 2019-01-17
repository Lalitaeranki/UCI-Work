
# coding: utf-8

# In[3]:


# Import Dependencies
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


# DATASET 1
gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
members = [49, 92, 84, 53]


# In[5]:


x_axis = np.arange(0, len(gyms))

plt.title("NYC Gym Popularity")
plt.xlabel("Gym Name")
plt.ylabel("Number of Members")

plt.xlim(-0.75, len(gyms)-0.25)
plt.ylim(0, max(members) + 5)

plt.bar(x_axis, members, facecolor="red", alpha=0.75, align="center")
plt.xticks(x_axis, gyms)
plt.show()


# In[6]:


# DATASET 2
x_lim = 2 * np.pi
x_axis = np.arange(0, x_lim, 0.1)
sin = np.sin(x_axis)


# In[7]:


plt.plot(x_axis, sin, marker='o', color='red', linewidth=1)
plt.hlines(0, 0, x_lim, alpha=0.2)


# In[8]:


# DATASET 3
gyms = ["Crunch", "Planet Fitness", "NY Sports Club", "Rickie's Gym"]
members = [49, 92, 84, 53]
x_axis = np.arange(0, len(gyms))
colors = ["yellowgreen", "red", "lightcoral", "lightskyblue"]
explode = (0, 0.05, 0, 0)


# In[10]:


plt.pie(members, explode=explode, colors=colors, labels=gyms, autopct="%1.1f%%", shadow=True, startangle=90)
plt.axis("equal")


# In[11]:


# DATASET 4
x_axis = np.arange(0, 10, 0.1)
times = []
for x in x_axis:
    times.append(x * x + np.random.randint(0, np.ceil(max(x_axis))))


# In[12]:


plt.scatter(x_axis, times, marker="o", color="red")

