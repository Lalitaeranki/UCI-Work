
# coding: utf-8

# In[1]:


class Film():
    def __init__(self, name, length, release_year, language):
        self.name = name
        self.length = length
        self.release_year = release_year
        self.language = language


# In[2]:


star_wars = Film("Star Wars", 121, 1977, "English")


# In[3]:


class Expert():
    def __init__(self, name):
        self.name = name
        
    def boast(self, obj):
        print(f"Hi! My name is {self.name}")
        print(f"I know a lot about {obj.name}")
        print(f"It is {obj.length} minutes long")
        print(f"It was released in {obj.release_year}")
        print(f"It is in {obj.language}")


# In[4]:


superfan = Expert("Dustin")


# In[5]:


superfan.boast(star_wars)


# In[6]:


toy_story = Film("Toy Story", 120, 1995, "English")


# In[7]:


superfan.boast(toy_story)


# In[8]:


fan2 = Expert("Stefanie")


# In[9]:


fan2.boast(star_wars)

