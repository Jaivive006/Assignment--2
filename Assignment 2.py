#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import numpy as np


# In[3]:


pip install seaborn


# In[4]:


import seaborn as sb


# In[5]:


import pandas


# In[6]:


from bs4 import BeautifulSoup


# In[8]:


mb=pandas.read_csv("C:\\Users\\aedpu\\OneDrive\\Desktop\\honda_car_selling.csv")


# In[9]:


mb


# In[13]:


mpp=mb.head()


# In[14]:


mpp


# In[17]:


plt.scatter(mpp['Year'],mpp['Price'])


# In[20]:


plt.bar(mpp['Year'],mpp['Price'])


# In[22]:


plt.plot(mpp['Year'],mpp['Price'],linestyle='dotted')


# In[29]:


plt.pie(mpp['Year'],labels=mpp['Price'])


# In[24]:


time =np.arange(1,10,0.09)


# In[25]:


time


# In[26]:


amplitude=np.sin(time)


# In[27]:


amplitude


# In[28]:


plt.plot(time,amplitude)


# In[30]:


plt.plot(mpp['Year'],mpp['Price'])


# In[31]:


sb.set(style='darkgrid')


# In[33]:


sb.distplot(mpp['Year'])


# In[34]:


mpp


# In[57]:


sb.relplot(x="Price",y="kms Driven",data=mpp,col="Car Model",hue="Year",style="Year",kind="scatter")


# In[40]:


sb.catplot(x='Year',y='Price',kind='box',data=mpp)


# In[43]:


sb.relplot(x='Year',y='Price',data=mpp)


# In[53]:


sb.pairplot(mb)


# In[52]:


sb.pairplot(mb,hue='Price',palette='Set1')


# In[ ]:




