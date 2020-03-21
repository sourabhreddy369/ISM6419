#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[48]:


import pandas as pd
from sqlalchemy import create_engine
# Connect to sqlite db 
db_file = r'C:/Users/soura/OneDrive/Desktop/Data Visualization/datasets/salesdata.db' 
engine = create_engine(r"sqlite:///{}"
                       .format(db_file)) 
sql = "select name from sqlite_master"    
"where type = 'table';"
test = pd.read_sql(sql, engine) 
print(test.iloc[0])
sql = 'SELECT * from {};'.format(test.iloc[0].iloc[0])
sales_data_df = pd.read_sql(sql, engine) 
sales_data_df


# In[ ]:




