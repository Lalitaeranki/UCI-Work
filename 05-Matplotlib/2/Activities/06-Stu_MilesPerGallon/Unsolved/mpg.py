
# coding: utf-8

# # Miles Per Gallon
# 
# There are many different features of a car that can help determine how many miles per gallon it has. In this activity, we will be creating a scatterplot to chart some of these relationships.
# 
# * The scatterplot that we want to create will compare 'mpg' to 'horsepower'. A reference image can be found at the bottom of this notebook, but how we go about creating this chart is completely up to you!
# 
#     * When reading in the data, there are 6 rows that are missing values in 'horsepower'. It is up to you to figure out what the author put in their place and drop the rows.

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[4]:


car_data = pd.read_csv('../Resources/mpg.csv')
car_data.head(1000)


# In[5]:


car_data = car_data.loc[car_data["horsepower"] != "?"]
car_data.head()


# In[6]:


car_data = car_data.set_index("car name")
del car_data["origin"]
car_data.head()


# In[7]:


car_data["horsepower"] = pd.to_numeric(car_data["horsepower"])


# In[10]:


car_data.plot(kind="scatter", x="horsepower", y="mpg", grid=True, figsize=(10,5), title="Horsepower vs MPG")
plt.show()
plt.tight_layout()

