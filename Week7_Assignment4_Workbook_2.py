#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import numpy as np
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours'] > 17),'Busy','Not Busy' )
df
df.tail(10)


# In[ ]:




