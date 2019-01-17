
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json


# In[3]:


# URL for GET requests to retrieve Star Wars character data
base_url = "https://swapi.co/api/people/"


# In[4]:


# Create a url with a specific character id
character_id = '4'
url = base_url + character_id
print(url)


# In[5]:


# Perform a get request for this character
response = requests.get(url)
print(response.url)


# In[7]:


# Storing the JSON response within a variable
data = response.json()
print(json.dumps(data, indent=4, sort_keys=True))


# In[11]:


# Collecting the name of the character collected
character_name = data["name"]


# In[14]:


# Print the character and the number of films that they were in
film_number = len(data["films"])
print(f"{character_name} was in {film_number} films")


# In[13]:


# Figure out what their first starship was and print the ship
first_ship_url = data["starships"][0]
ship_response = requests.get(first_ship_url).json()
#ship_response
print(f"{character_name} first ship was {ship_response['name']}")


# In[18]:


films = []
for film in data["films"]:
    current_film = requests.get(film).json()
    #print(json.dumps(current_film, indent=4, sort_keys=True))
    film_title = current_film["title"]
    films.append(film_title)

print(f"{character_name} was in:")
print(films)


# In[ ]:


# Print what their first ship was
# YOUR CODE HERE

