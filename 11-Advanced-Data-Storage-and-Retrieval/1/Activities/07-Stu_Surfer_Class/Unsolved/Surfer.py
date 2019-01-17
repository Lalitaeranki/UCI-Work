
# coding: utf-8

# In[2]:


# Define the Surfer Class
class Surfer():
    def __init__(self, name, hometown, rank):
        self.name = f"{name} Dude"
        self.hometown = f"{hometown} Waves"
        self.rank = rank


# In[4]:


# Create an instance of the Surfer Class
kelly_surfer = Surfer("Kelly Slater", "Cocoa Beach", 1)


# In[3]:


# Print the object's attributes
def print_surfer(surfer):
    print(surfer.name)
    print(surfer.hometown)
    print(surfer.rank)


# In[5]:


print_surfer(kelly_surfer)


# In[7]:


# ----BONUS----
# Variable to keep track of changes to while loop
go = True
while go:
    name = input("What is the surfer's name? ")
    hometown = input("What is the surfer's hometown? ")
    rank = input("What is the surfer's rank? ")
    
    surfer = Surfer(name, hometown, rank)
    
    print_surfer(surfer)
    
    check = input("Do you want to continue? (y/n)")
    if check.lower() != "y":
        go = False

