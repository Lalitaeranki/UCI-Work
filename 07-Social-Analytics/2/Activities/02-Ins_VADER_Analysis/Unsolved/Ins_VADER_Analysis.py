
# coding: utf-8

# In[1]:


# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# In[16]:


# Sample Strings
happy_string = "Your humble instructor is smart, beautiful, and funny!"
angry_string = ("Ugh. I am feeling so distraught! "
                 "I hate everything. "
                 "I am mad at everyone.")
happy_emoticon_string = ":-) :) :-D  ;-) :-P"
angry_emoticon_string = ":-( :( D-< :'("
funny_slang_string = "lol rofl haha"
angry_slang_string = "Sux meh grr"

# Target String Setting
target_string = angry_slang_string


# In[14]:


# Run analysis
results = analyzer.polarity_scores(angry_slang_string)
results


# In[15]:


# Parse results
compound = results["compound"]
pos = results["pos"]
neu = results["neu"]
neg = results["neg"]


# In[17]:


# Print Analysis
print(target_string)
print(f"Compound: {compound}")
print(f"Positive: {pos}")
print(f"Neutral: {neu}")
print(f"Negative: {neg}")

