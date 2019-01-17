
# coding: utf-8

# # Bike Trippin
# 
# For this assignment, you will be taking "Cycle Share" data from Seattle and creating charts to determine which gender borrows and uses bikes more often.
# 
# * Import your dependencies and then import your data into a pandas data frame from the CSV within the 'Data' folder
# * Split up your data into groups based upon the gender column
#     * NOTE: There will be a garbage row with a gender of 'stoptime' which you will have to remove!
# * Chart your data using a bar graph, giving it both a title and labels for the axes

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[4]:


bike_trips_df = pd.read_csv("../Resources/trip.csv", low_memory=False)
bike_trips_df.head()


# In[9]:


gender_groups = bike_trips_df.groupby("gender")
gender_trips = gender_groups['gender'].count()
gender_trips


# In[10]:


gender_trips = gender_trips.drop(gender_trips.index[3])
gender_trips


# In[11]:


gender_chart = gender_trips.plot(kind="bar", title="Bike Trips by Gender")
gender_chart.set_xlabel("Gender")
gender_chart.set_ylabel("Number of Trips Taken")
plt.show()
plt.tight_layout()


# # Bonus!
# 
# You will now take the same base data frame before and create some code that will allow you to create individual pie charts for each bike. For this part of the activity, we want you to chart the total 'Trip Duration' of each bike, sorted by gender. Bonus points if you can come up with a method to do this without using loc or iloc to filter the original data frame! You can use loc to filter group data though.

# In[15]:


bike_groups = bike_trips_df.groupby(["bikeid", "gender"])
bike_sum = bike_groups.sum()
bike_sum.head()


# In[16]:


bike_id = "SEA00001"
one_bike = bike_sum.loc[bike_id]
one_bike


# In[17]:


gender_list = one_bike.keys()
gender_list


# In[18]:


bike_pie = one_bike.plot(kind="pie", y=gender_list, title=("Trips of " + bike_id))
bike_pie.set_ylabel("Trip Duration")
plt.show()
plt.tight_layout()
plt.axis("equal")

