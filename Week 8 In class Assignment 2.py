#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
import numpy as np
import folium
import matplotlib.pyplot as plt
Location = "C:/Users/soura/OneDrive/Desktop/Data Visualization/time_series_covid19_confirmed_global.csv"
df = pd.read_csv(Location)
df.head()


# In[69]:


m = folium.Map(location=[0, 0], tiles="Stamen Toner", zoom_start=2)
data = df
# I can add marker one by one on the map
for i in range(0,len(data)):
   radi = data.iloc[i]['4/1/20']
   folium.Circle(
      location=[data.iloc[i]['Lat'], data.iloc[i]['Long']],
      popup=data.iloc[i]['Country/Region'],
      radius=float(radi*5),
      color='red',
      fill=True
   ).add_to(m)
m


# In[ ]:





# In[10]:





# In[ ]:




