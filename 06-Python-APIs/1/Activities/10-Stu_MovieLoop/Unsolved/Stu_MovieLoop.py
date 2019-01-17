
# coding: utf-8

# In[1]:


# Dependencies
import requests

url = "http://www.omdbapi.com/?apikey=trilogy&t="

movies = ["Aliens", "Sing", "Moana"]


# In[2]:


response_list = []
for movie in movies:
    movie_data = requests.get(url + movie).json()
    response_list.append(movie_data)
    print(f"The director of {movie} is {movie_data['Director']}")


# In[3]:


response_list

