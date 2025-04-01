#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
xpoints= np.array([0,10])
ypoints= np.array([20,100])
print(plt.plot(xpoints,ypoints))
print(plt.show())


# In[6]:


x= np.array([0,5])
y= np.array([0,25])
print(plt.plot(x,y,marker='p'))
print(plt.show())


# In[7]:


xpoints= ([1,2,6,8])
ypoints= ([3,8,1,10])
print(plt.plot(xpoints,ypoints))
print(plt.show())


# In[8]:


xpoints= np.array([3,8,1,4,9])
ypoints= np.array([5,7,1,0,3])
print(plt.plot(xpoints,ypoints))
print(plt.show())


# In[9]:


ypoints= np.array([5,7,1,0,3])
print(plt.plot(ypoints))
print(plt.show())


# In[ ]:




