#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/gradedata.csv"
df = pd.read_csv(Location) 
df.head()

plt.scatter(df['hours'], df['grade'])
plt.xlabel("Hours")
plt.ylabel("Grades")
plt.title("Scatter plot between hours and grades of students")


# In[6]:


#Yes, There is a pattern in data, with the increasing number of hours the grades of students are increasing


# In[ ]:




