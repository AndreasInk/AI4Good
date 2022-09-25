#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[2]:


df1 = pd.read_table('./data//hourly_weather_data_202207_test.csv',delimiter=',')


# In[3]:


df1['Coverage 1'] = df1['HourlySkyConditions'].str[:3]
df1.head()


# In[4]:


df1['Layer 1'] = df1['HourlySkyConditions'].str[4:6].replace(":", "")
df1.head()


# In[5]:


df1['Cloud Height 1'] = df1['HourlySkyConditions'].str[7:9].replace(":", "")
df1.head()


# In[6]:


df1['Coverage 2'] = df1['HourlySkyConditions'].str[10:13]
df1.head()


# In[7]:


df1['Layer 2'] = df1['HourlySkyConditions'].str[14:16].replace(":", "")
df1.head()


# In[9]:


df1['Cloud Height 2'] = df1['HourlySkyConditions'].str[17:19].replace(":", "")
df1.head()


# In[10]:


df1['Coverage 3'] = df1['HourlySkyConditions'].str[20:23]
df1.head()


# In[11]:


df1['Layer 3'] = df1['HourlySkyConditions'].str[24:26].replace(":", "")
df1.head()


# In[12]:


df1['Cloud Height 3'] = df1['HourlySkyConditions'].str[27:29].replace(":", "")
df1.head()


# In[13]:


df1.to_csv("./data/Parsed_Hourly_Weather_Data_Test.csv", index=False, sep=',', mode='a')


# In[3]:


## Test Data Parsing
