#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Replacing a String in a file

A = open("Test.txt","wt")

A.write("This is a placement assignment")

A.close()

def replace():
  A=open("Test.txt","rt")
  data = A.read()

  data = data.replace("placement","screening")

  A.close()

  A = open("Test.txt","wt")
  A.write(data)

  A.close()
replace()
print("Please check in the Test.txt file for output")

# In[ ]:




