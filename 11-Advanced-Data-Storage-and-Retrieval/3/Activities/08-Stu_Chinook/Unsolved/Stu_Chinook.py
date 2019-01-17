
# coding: utf-8

# In[1]:


# Ignore SQLITE warnings related to Decimal numbers in the Chinook database
import warnings
warnings.filterwarnings('ignore')


# In[7]:


# Import Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect


# In[3]:


# Create an engine for the chinook.sqlite database
engine = create_engine("sqlite:///../Resources/chinook.sqlite")


# In[4]:


# Reflect Database into ORM classes
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()


# In[5]:


# Save a reference to the invoices table as `Invoices`
Invoices = Base.classes.invoices


# In[6]:


# Create a database session object
session = Session(bind=engine)


# In[8]:


inspector = inspect(engine)
columns = inspector.get_columns('invoices')
columns


# In[9]:


# List all of the countries found in the invoices table
session.query(Invoices.BillingCountry).all()


# In[11]:


# Design a query that lists the invoices totals for each billing country 
# and sort the output in descending order.
session.query(Invoices.BillingCountry, func.sum(Invoices.Total)).    group_by(Invoices.BillingCountry).    order_by(func.sum(Invoices.Total).desc()).    all()


# In[12]:


# Save a reference to the invoice_items table as `Items`
Items = Base.classes.invoice_items


# In[14]:


# List all of the Billing Postal Codes for the USA.
session.query(Invoices.BillingPostalCode).    filter(Invoices.BillingCountry == "USA").    group_by(Invoices.BillingPostalCode).    all()


# In[15]:


# Calculate the Item Totals (sum(UnitPrice * Quantity)) for the USA
session.query(func.sum(Items.UnitPrice * Items.Quantity)).    filter(Invoices.InvoiceId == Items.InvoiceId).    filter(Invoices.BillingCountry == "USA").scalar()


# In[17]:


# Calculate the Item Totals `sum(UnitPrice * Quantity)` for each Billing Postal Code in the USA
# Sort the results in descending order by Total
session.query(Invoices.BillingPostalCode, func.sum(Items.UnitPrice * Items.Quantity)).    filter(Invoices.InvoiceId == Items.InvoiceId).    filter(Invoices.BillingCountry == "USA").    group_by(Invoices.BillingPostalCode).    order_by(func.sum(Items.UnitPrice * Items.Quantity).desc()).    all()

