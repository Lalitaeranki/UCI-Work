
# coding: utf-8

# In[1]:


# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()


# In[2]:


def get_sample(sample_file):
    with open(sample_file) as sample:
        return sample.read()


# In[3]:


# Placeholder for sample text
sample1 = get_sample("../Resources/Sample1.txt")
sample2 = get_sample("../Resources/Sample2.txt")
sample3 = get_sample("../Resources/Sample3.txt")

# Create a tuple of the samples
samples = (sample1, sample2, sample3)


# In[4]:


# Run Vader Sentiment Analysis on Each of the Samples

# Loop through each sample and print the scores
for sample in samples:
    results = analyzer.polarity_scores(sample)
    print(sample)
    print(f"Compound Score: {results['compound']}")
    print(f"Positive Score: {results['pos']}")
    print(f"Neutral Score: {results['neu']}")
    print(f"Negative Score: {results['neg']}")
    print()

