
# coding: utf-8

# In[1]:


# Dependencies
import requests
import json


# In[4]:


# Base URL for GET requests to retrieve number/date facts
url = "http://numbersapi.com/"


# In[8]:


# Ask the user what kind of data they would like to search for
question = "What type of data would you like to search for? [Trivia, Math, Date, or Year] "
kind_of_search = input(question)


# In[9]:


# Create code to return a number fact
if (kind_of_search.lower() == "date"):
    month = input("What month you would like to search for? ")
    day = input("What day would you like to search for? ")
    request_str = f"{url}{month}/{day}/{kind_of_search.lower()}?json"
    response = requests.get(request_str).json()
    print(response['text'])
else:
    number = input("What number would you like to search for? ")
    request_str = f"{url}{number}/{kind_of_search.lower()}?json"
    response = requests.get(request_str).json()
    print(response['text'])

