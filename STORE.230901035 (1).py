#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
df=pd.DataFrame([[2,4,6],[1,3,5],[5,7,8]],index=['one','two','three'],columns=['a','b','c'])
print(df)


# In[5]:


df.to_excel("/Users/student/Downloads/excel sheet1.xlsx")
df.to_excel("/Users/student/Downloads/excelsheet2.xlsx")


# In[10]:


df.to_excel("/Users/student/Downloads/excel sheet1.xlsx")
df=pd.DataFrame([[10,20,30],[40,50,60,],[70,80,90]],index=['one','two','three'],columns=['X','Y','Z'])
df.to_excel("/Users/student/Downloads/excel sheet1.xlsx",sheet_name='sheet1')


# In[7]:


df=pd.DataFrame([[6,7,8],[9,10,11,],[12,13,14]],index=['one','two','three'],columns=['A','B','C'])
df.to_excel("/Users/student/Downloads/excelsheet2.xlsx",sheet_name='sheet1')


# In[12]:


x=pd.read_excel("/Users/student/Downloads/excel sheet1.xlsx")
y=pd.read_excel("/Users/student/Downloads/excelsheet2.xlsx")
z=pd.concat([x,y])
z.to_excel("/Users/student/Downloads/excelsheet3.xlsx",sheet_name='sheet1')


# In[14]:


df=z.sort_values(["X"])
print(df)
df.to_excel("/Users/student/Downloads/excelsheet3.xlsx")


# In[15]:


df=pd.read_excel("/Users/student/Downloads/excelsheet3.xlsx")
print(df)
print(list(df))
print(format(len(df)))


# In[ ]:


a

