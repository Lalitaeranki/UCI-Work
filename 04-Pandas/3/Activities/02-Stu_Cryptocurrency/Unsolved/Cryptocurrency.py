
# coding: utf-8

# In[1]:


# Import Dependencies
import pandas as pd


# In[2]:


bitcoin_csv = "Resources/bitcoin_cash_price.csv"
dash_csv = "Resources/dash_price.csv"


# In[3]:


bitcoin_df = pd.read_csv(bitcoin_csv)
dash_df = pd.read_csv(dash_csv)


# In[4]:


bitcoin_df.head()


# In[5]:


dash_df.head()


# In[6]:


# Merge the two DataFrames together based on the Dates they share
crypto_df = pd.merge(bitcoin_df, dash_df, on="Date")
crypto_df.head()


# In[7]:


# Rename columns so that they are differentiated
crypto_df = crypto_df.rename(columns={
    "Open_x": "Bitcoin Open", "High_x": "Bitcoin High", "Low_x": "Bitcoin Low",
    "Close_x": "Bitcoin Close", "Volume_x": "Bitcoin Volume", "Market Cap_x": "Bitcoin Market Cap"
})

crypto_df = crypto_df.rename(columns={
    "Open_y": "Dash Open", "High_y": "Dash High", "Low_y": "Dash Low",
    "Close_y": "Dash Close", "Volume_y": "Dash Volume", "Market Cap_y": "Dash Market Cap"
})

crypto_df.head()


# In[8]:


# alternatively you can set your suffixes when the merge occurs
alt_merge = pd.merge(bitcoin_df, dash_df, on="Date", suffixes=("_Bitcoin", "_Dash"))
alt_merge.head()


# In[9]:


# Collecting best open for Bitcoin and Dash
bitcoin_open = crypto_df["Bitcoin Open"].max()
dash_open = crypto_df["Dash Open"].max()

# Collecting best close for Bitcoin and Dash
bitcoin_close = crypto_df["Bitcoin Close"].max()
dash_close = crypto_df["Dash Close"].max()

# Collecting the total volume for Bitcoin and Dash
bitcoin_volume = round(crypto_df["Bitcoin Volume"].sum()/1000000, 2)
dash_volume = round(crypto_df["Dash Volume"].sum()/1000000, 2)


# In[11]:


# Creating a summary DataFrame using above values
summary_df = pd.DataFrame({
    "Best Bitcoin Open": [bitcoin_open],
    "Best Bitcoin Close": [bitcoin_close],
    "Total Bitcoin Volume": [str(bitcoin_volume) + " million"],
    "Best Dash Open": [dash_open],
    "Best Dash Close": [dash_close],
    "Total Dash Volume": [str(dash_volume) + " million"]
})
summary_df


# In[ ]:


get_ipython().system('jupyter nbconvert --to script Cryt.ipynb')

