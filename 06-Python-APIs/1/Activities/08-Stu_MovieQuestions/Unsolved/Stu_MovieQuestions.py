
# coding: utf-8

# In[1]:


# Dependencies
import requests

url = "http://www.omdbapi.com/?apikey=trilogy&t="


# In[2]:


# Who was the director of the movie Aliens?
movie = requests.get(url + "Aliens").json()
print(f"The director of Aliens was {movie['Director']}")


# In[3]:


# What was the movie Gladiator rated?
movie = requests.get(url + "Gladiator").json()
print(f"The rating of Gladiator was {movie['Rated']}")


# In[4]:


# What year was 50 First Dates released?
movie = requests.get(url + "50 First Dates").json()
print(f"The movie 50 First Dates was released in {movie['Year']}")


# In[5]:


# Who wrote Moana?
movie = requests.get(url + "Moana").json()
print(f"Moana was written by {movie['Writer']}")


# In[6]:


# What was the plot of the movie Sing?
movie = requests.get(url + "Sing").json()
print(f"The plot of Sing was: {movie['Plot']}")

