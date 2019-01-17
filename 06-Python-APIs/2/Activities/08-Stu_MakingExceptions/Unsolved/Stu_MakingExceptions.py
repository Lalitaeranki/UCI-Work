
# coding: utf-8

# In[5]:


# Your assignment is to get the last line to print without changing any
# of the code below. Instead, wrap each line that throws an error in a
# try/except block.

try:
    print("Infinity looks like + " + str(10 / 0) + ".")
except ZeroDivisionError:
    print("You can't divide by 0")

try:
    print("I think her name was + " + name + "?")
except NameError:
    print("name undefined")

try:
    print("Your name is a nonsense number. Look: " + int("Gabriel"))
except ValueError:
    print("Name cannot be converted to a integer")

print("You made it through the gauntlet--the message survived!")

