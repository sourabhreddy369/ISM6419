#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,95,77,78,99] 
bsdegrees = [1,1,0,0,1] 
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]
Degrees = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grades','BS','MS','PhD'] 
df = pd.DataFrame(data = Degrees, columns=columns)
print('Count of given Data')
print(df.count())
print('\nMean of given Data')
print(df.mean())
print('\nStandard Deviation of given Data')
print(df.std())
print('\nmin of given Data')
print(df.min())
print('\nmax of given Data')
print(df.max())
print('\nfirst quartile of given Data')
print(df.quantile(0.25))
print('\nsecond quartile of given Data')
print(df.quantile(0.5))
print('\nthird quartile of given Data')
print(df.quantile(0.75))
print('\nvar of given Data')
print(df.var())


# In[ ]:




