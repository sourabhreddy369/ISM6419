#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location) 
df.head()


# In[3]:


df.hist(column="age", by="gender")


# In[ ]:




