#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df2 = df.take(np.random.permutation(len(df))[:500])
df2


# In[ ]:




