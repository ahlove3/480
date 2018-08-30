
# coding: utf-8

# # my first notebook

# In[1]:


print ('my first notebook')


# In[2]:


1+2


# In[4]:


a = 3


# In[5]:


print (a)


# In[3]:


get_ipython().system('pip install xlrd')


# In[4]:


import xlrd
book = xlrd.open_workbook("Diamonds.xls")
sheet = book.sheet_by_name("Diamonds")


# In[5]:


for row_index in range(1,5): # read the first 4 rows, skip the first row
    id_, weight, color,_,_,price = sheet.row_values(row_index)
    print(id_,weight,color,price)

