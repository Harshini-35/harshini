#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr=np.array([1,6,2,7,6,4])
x=np.where(arr==4)
print(x)


# In[2]:


import numpy as np
arr=np.array([1,6,2,7,6,4])
x=np.where(arr%2==0)
print(x)


# In[3]:


import numpy as np
arr=np.array([0,1,2,2,7,8,9])
x=np.searchsorted(arr,3,side='left')
print(x)


# In[4]:


import numpy as np
arr=np.array([0,1,5,3,6,7,2])
x1=np.searchsorted(arr,3,side='left')
print(x1)


# In[5]:


import numpy as np
arr=np.array([0,1,2,2,7,8,9])
x3=np.searchsorted(arr,8,side='right')
print(x3)


# In[6]:


import numpy as np
arr=np.array([9,5,2,7,6,4])
print(np.sort(arr))


# In[7]:


import numpy as np
arr=np.array([[7,4,9],[9,1,4]])
print(np.sort(arr))


# In[8]:


import numpy as np
arr=np.array([41,42,43,44])
x=[True,False,True,False]
narr=arr>42
newarr=arr[narr]
print(arr)
print(x)
print(narr)
print(newarr)


# In[9]:


import numpy as np
arr=np.array([31,78,69,88])
x=[False,True,True,False]
newarr=arr[x]
print(x)
print(newarr)


# In[ ]:




