#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()
bins = [0,80,100]
group_names = ['Fail', 'Pass']
df['Pass/Fail'] = pd.cut(df['grade'], bins,        labels=group_names)
df


# In[ ]:




