
# coding: utf-8

# In[1]:


import spacy
from spacymoji import Emoji


# In[2]:


# "Miley Cyrus" in emoji-story form
tweet = u"👩->👸->💇->👱->😛->😦"


# In[3]:


nlp = spacy.load("en")
emoji = Emoji(nlp)
nlp.add_pipe(emoji)


# In[4]:


doc = nlp(tweet)


# In[6]:


doc._.emoji

