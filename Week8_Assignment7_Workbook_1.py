#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel'] 
grades = [76,83,77,78,95] 
GradeList = zip(names,grades) 
df = pd.DataFrame(data = GradeList, columns=['Names', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df.plot()


# In[2]:


import matplotlib.pyplot as plt
df.plot()
displayText = "my annotation" 
xloc = 1 
yloc = df['Grades'].max() 
xtext = 8 
ytext = 0
plt.annotate(displayText, 
             xy=(xloc, yloc),
             xytext=(xtext,ytext),
             xycoords=('axes fraction', 'data'),
             textcoords='offset points')


# In[3]:


df.plot() displayText = "my annotation"
xloc = 1
yloc = df['Grades'].max()
xtext = 8
ytext = -150  
plt.annotate(displayText,           
             xy=(xloc, yloc),         
             arrowprops=dict(facecolor='black',  
                             shrink=0.05), 
             xytext=(xtext,ytext),     
             xycoords=('axes fraction', 'data'),      
             textcoords='offset points')


# In[13]:


import matplotlib.pyplot as plt
df.plot()
displayText = "Wow" 
xloc = 0
yloc = 76
xtext = 8
ytext = 0
plt.annotate(displayText, 
             xy=(xloc, yloc),
             xytext=(xtext,ytext),
             xycoords=('axes fraction', 'data'),
             textcoords='offset points')


# In[ ]:




