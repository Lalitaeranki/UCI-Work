
# coding: utf-8

# In[1]:


get_ipython().magic('matplotlib notebook')


# In[2]:


# Import Dependencies
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:


# Import our data into pandas from CSV
used_string = '../Resources/used_cars.csv'
used_car_df = pd.read_csv(used_string)

used_car_df


# In[4]:


maker_group = used_car_df.groupby("maker")
count_makers = maker_group["maker"].count()
count_makers


# In[6]:


count_chart = count_makers.plot(kind="bar")
count_chart.set_xlabel("Car Manufacturer")
count_chart.set_ylabel("Number of Cars")
plt.tight_layout()

