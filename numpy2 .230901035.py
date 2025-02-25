#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
slice1=arr[2::6]
print(slice1)
slice2=arr[::2]
print(slice2)


# In[2]:


revarr=arr[::-1]
print(revarr)


# In[3]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[0:3:2])
print(a[0::2])
print(a[1::])
print(a[2::2])
print(a[:2])
print(a[:2:3])


# In[4]:


import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a[0:3:2])
print(a[0::2])
print(a[1::])
print(a[2::2])
print(a[:2])
print(a[:2:3])


# In[5]:


import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
subarray=arr[0:2,1:3]
print(subarray)


# In[6]:


import numpy as np
reversearray=arr[::-1]
print(reversearray)


# In[7]:


import numpy as np
col1=arr[:,0]
print(col1)


# In[9]:


import numpy as np
row1=arr[0,:]
print(row1)


# In[10]:


import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[4])
print(arr[-1])
print(arr[1:4])
print(arr[arr>25])
print(arr[[1,3]])


# In[11]:


#horizontal join
arr1=np.array([[1,2],[3,4]])
arr2=np.array([[5,6],[7,8]])
result=np.hstack((arr1,arr2))
print(result)
#vertical join
result1=np.vstack((arr1,arr2))
print(result)
#depth join
result2=np.dstack((arr1,arr2))
print(result2)


# In[12]:


#numpy.split()
import numpy as np
arr=np.array([1,2,3,4,5,6])
result=np.split(arr,3)
print(result)


# In[13]:


#numpy.array split()
import numpy as np
arr1=np.array([1,2,3,4,5])
result1=np.array_split(arr1,3)
print(result1)


# In[14]:


import numpy as np
arr1=np.array([[3,5],[8,7]])
arr2=np.array([[6,5],[3,1]])
result2=np.dstack((arr1,arr2))
print(result2)


# In[15]:


import numpy as np
arr2=np.array([[1,2,3],[4,5,6]])
result2=np.hsplit(arr2,3)
print(result2)


# In[16]:


import numpy as np
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
result3=np.vsplit(arr3,3)
print(result3)


# In[17]:


import numpy as np
arr4=np.array([[[1,2],[3,4],[5,6],[7,8]]])
result4=np.dsplit(arr4,2)
print(result4)


# In[ ]:




