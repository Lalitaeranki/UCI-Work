
# coding: utf-8

# In[14]:


# Define the Surfer Class
class Surfer():
    
    surfer_count = 0
    
    def __init__(self, name, hometown, rank, wipeouts=0):
        self.name = name
        self.hometown = hometown
        self.rank = rank
        self.wipeouts = wipeouts
        Surfer.surfer_count += 1
        
    def speak(self):
        print("Hang loose bruh!")
        
    def biography(self):
        print(f"My name is {self.name}, I am from {self.hometown} and rank #{self.rank}, I've wiped out {self.wipeouts} times!")
    
    def cheer(self):
        if self.wipeouts == 0:
            print("I totally rock man, no wipe outs!")
        else:
            print("Bummer bruh, keep on keeping on!")
            
    def print_surfer(self):
        print(self.name)
        print(self.hometown)
        print(self.rank)
        print(self.wipeouts)
        
    def count_surfers(self):
        print(f"Total surfers shredding waves {Surfer.surfer_count}")


# In[15]:


# Create Surfers
# --------------------------------------------------------------------------------
kelly = Surfer("Kelly Slater", "Cocoa Beach", 1)
kelly.print_surfer()
kelly.speak()
kelly.biography
kelly.cheer()
kelly.count_surfers()


# In[9]:


john = Surfer("John Breezy", "Spring Lake", 1, 10)
john.print_surfer()
john.speak()
john.biography
john.cheer()
john.count_surfers()


# In[ ]:


get_ipython().system('juypter nbconvert --to script Surfer_Extended.ipynb')

