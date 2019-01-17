
# coding: utf-8

# In[1]:


class Dog():
    def __init__(self, name, color):
        self.name = name
        self.color = color


# In[2]:


dog = Dog("Fido", "Brown")


# In[3]:


print(dog.name)
print(dog.color)


# In[4]:


ruby = Dog("Ruby", "Tan")
print(ruby.name)
print(ruby.color)

