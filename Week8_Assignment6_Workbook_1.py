#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location)
#df.drop_duplicates(['name'], keep='last')
df = df.sort_values(by=['fname','age','grade'],ascending=[True, True, True])
df


# In[ ]:




