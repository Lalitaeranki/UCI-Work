
# coding: utf-8

# In[5]:


# Dependencies
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


# In[3]:


# Read in data
general_height = pd.read_csv("../Resources/general_heights.csv")
wba_data = pd.read_csv("../Resources/wba_data.csv")
wba_heights = wba_data.iloc[:, -1]


# In[6]:


# Run the t-test
(t_stat, p) = ttest_ind(general_height, wba_heights, equal_var=False)


# In[7]:


# Report the data
print("The mean height of the WBA Players is {}.".format(wba_heights.mean()))
print("The mean height of the women sampled is {}.".format(general_height.values.mean()))
print("p is {}.".format(p[0]))
if p < 0.05:
    print("The differences in the sample means is significant")
else:
    print("The differences in the sample means is not significant")


# In[9]:


# Plot sample means with error bars
tick_labels = ["General Public", "WBA Players"]
means = [general_height.mean().values[0], wba_heights.mean()]
x_axis = np.arange(0, len(means))
sem = [general_height.sem().values[0], wba_heights.sem()]


# In[10]:


# Plot mean height of players
fig, ax = plt.subplots()
fig.suptitle("Mean hight of women in the general population and WBA players",
            fontsize=12, fontweight="bold")
ax.errorbar(x_axis, means, sem, fmt="o")
ax.set_xlim(-0.5, 1.5)
ax.set_ylim(64, 73)

ax.set_xticklabels(tick_labels)
ax.set_xticks([0, 1])

ax.set_ylabel("Height (Inches)")
plt.show()

