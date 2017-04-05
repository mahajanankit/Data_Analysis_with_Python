
# coding: utf-8

# # Question2_Part1

# In[35]:

import pandas


# In[36]:

rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"


# In[37]:

fields = ["Organization Group","Department","Total Compensation"]
df = pandas.read_csv(rpath+"/employee_compensation.csv", sep="," ,usecols=fields)


# In[38]:

df = df.groupby(["Organization Group","Department"]).mean()


# In[39]:

df = df.sort_values(by='Total Compensation', ascending=0)
df.to_csv("./Output/Question2_Part1.csv")
df.head()

