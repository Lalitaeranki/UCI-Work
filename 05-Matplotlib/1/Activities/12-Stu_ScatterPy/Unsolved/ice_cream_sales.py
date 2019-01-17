
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


import matplotlib.pyplot as plt
import numpy as np


# In[3]:


temp = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
sales = [215, 325, 185, 332, 406, 522, 412, 614, 544, 421, 445, 408]


# In[4]:


# Tell matplotlib to create a scatter plot based upon the above data
scoop_price = [89, 18, 10, 28, 79, 46, 29, 38, 89, 26, 45, 62]
plt.scatter(temp, sales, marker="o", facecolors="red", edgecolors="black", s=scoop_price)


# In[5]:


# Set the upper and lower limits of our y axis
plt.ylim(180, 620)


# In[6]:


# Set the upper and lower limits of our x axis
plt.xlim(11, 26)


# In[7]:


# Create a title, x label, and y label for our chart
plt.title("Ice Cream Sales v Temperature")
plt.xlabel("Temperature (Celcius)")
plt.ylabel("Sales (Dollars)")


# In[8]:


# Save an image of the chart and print to screen
# NOTE: If your plot shrinks after saving an image,
# update matplotlib to 2.2 or higher,
# or simply run the above cells again.
plt.savefig("../ImagesIceCreamSales.png")
plt.show()


# In[ ]:


get_ipython().system('jupyter nbconvert')

