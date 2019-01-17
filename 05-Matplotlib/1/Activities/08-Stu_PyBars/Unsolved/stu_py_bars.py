
# coding: utf-8

# In[9]:


get_ipython().magic('matplotlib notebook')


# In[10]:


import matplotlib.pyplot as plt
import numpy as np


# In[11]:


cities = ["New Orleans", "Milwaukee", "Omaha", "Pittsburgh", "Toledo"]
bars_in_cities = [8.6, 8.5, 8.3, 7.9, 7.2]
x_axis = np.arange(len(bars_in_cities))


# In[12]:


# Create a bar chart based upon the above data
plt.bar(x_axis, bars_in_cities, color="b", align="center")


# In[13]:


# Create the ticks for our bar chart's x axis
tick_locations = x_axis
plt.xticks(tick_locations, cities)


# In[14]:


# Set the limits of the x axis
plt.xlim(-0.75, len(x_axis)-0.25)


# In[15]:


# Set the limits of the y axis
plt.ylim(0, max(bars_in_cities)+0.4)


# In[16]:


# Give the chart a title, x label, and y label
plt.title("Density of Bars in Cities")
plt.xlabel("Cities")
plt.ylabel("Bars Per 10,000 Households")


# In[17]:


# Save an image of the chart and print it to the screen
plt.savefig("../Images/BarDensity.png")
plt.show()

