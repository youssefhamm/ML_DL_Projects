#!/usr/bin/env python
# coding: utf-8

# In[122]:


import numpy as np 
import matplotlib.pyplot as plt
import random
from math import *


# In[123]:


def f(x):
    return 1/(1+x**2)
f=np.vectorize(f)


# In[124]:


def marticeX(xi,m):
    n = len(xi)
    A = np.zeros((n,m+1))
    for i in range(n):
        for j in range(m+1):
            A[i,j]=xi[i]**j
    return A


# In[137]:


def coef(xi,yi,m):
    A = marticeX(xi,m)
    X=(A.T)@A
    b=(A.T)@yi
    w=np.linalg.solve(X,b)
    return w


# In[145]:


def horner(w,x):
    n=len(w)-1
    b=w[n]
    
    for k in range(n-1,-1,-1):
        b=w[k]+b*x
    return b


# In[146]:


def poly_Regression(w,x):
    y=horner(w,x)
    return y


# In[ ]:





# In[177]:





# In[ ]:





# In[118]:





# In[ ]:




