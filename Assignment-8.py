#!/usr/bin/env python
# coding: utf-8

# In[1]:


cheese =['chheddar', 'Gouda', 'Edam']


# In[2]:


numbers = [1,12,32]


# In[3]:


empty = []


# In[4]:


print(cheese,numbers,empty)


# In[5]:


print(cheese[0])


# In[6]:


numbers[2]=5


# In[7]:


print(numbers)


# In[8]:


'Edam' in cheese


# In[9]:


'Brie' in cheese


# In[10]:


#Traversing a List
for i in cheese:
    print(i)


# In[11]:


for i in range(len(numbers)):
    numbers[i] = numbers[i]*2
    print(numbers[i])


# In[12]:


for x in empty:
    print('This will never happen')


# In[13]:


# List Operations
a = [2, 4, 1]


# In[14]:


b = [4,2,1]


# In[15]:


c = a+b


# In[16]:


print(c)


# In[17]:


d = a + b


# In[18]:


d = a*3


# In[19]:


print(d)


# In[20]:


# List Slices


# In[21]:


t = ['a', 'b', 'c', 'd', 'e', 'f']


# In[22]:


print(t[1:4])


# In[23]:


print(t[:4])


# In[24]:


print(t[:4])


# In[25]:


print(t[:])


# In[26]:


t[1:3] = ['x', 'y']


# In[27]:


print(t)


# In[28]:


#List Methods
t.append(5)


# In[29]:


print(t)


# In[30]:


t2 = [2, 4, 6]


# In[31]:


t.append(t2)


# In[32]:


print(t)


# In[33]:


t.extend(t2)


# In[34]:


print(t)


# In[35]:


x= 1


# In[36]:


str = ['b','a','c','e','d']


# In[37]:


str.sort()


# In[38]:


print(str)


# In[39]:


#Deleting Elements
x = str.pop(3)


# In[40]:


print(str)


# In[41]:


print(x)


# In[42]:


del str[2]


# In[43]:


print(str)


# In[44]:


str.remove('a')


# In[45]:


print(str)


# In[46]:


astr = ['a', 'd', 't', 'x']


# In[47]:


str.extend(astr)


# In[48]:


del str[1:3]


# In[49]:


print(str)


# In[50]:


# Functions
nums = [3, 41, 12, 9, 74, 15]


# In[51]:


print(len(nums))


# In[52]:


print(max(nums))


# In[53]:


print(min(nums))


# In[54]:


print(sum(nums))


# In[55]:


print(sum(nums)/len(nums))


# In[56]:


print(sum(nums)/len(nums))


# In[58]:


total = 0
count = 0
while(True):
    inp = input("Enter a Number: ")
    if inp == 'done':break
    value = float(inp)
    total = total + value
    count = count +1
avg = total/count
print("Average: ",avg)


# In[59]:


numlist = list()
while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('Average:', average)


# In[60]:


print(numlist)


# In[61]:


# Lists and Strings
s = 'spam'


# In[62]:


t = list(s)


# In[63]:


print(t)


# In[64]:


s = 'A dark brown fox'


# In[65]:


print(t)


# In[66]:


print(t[2])


# In[67]:


s = 'spam-spam-spam'


# In[68]:


delimiter = '-'


# In[69]:


s.split(delimiter)


# In[70]:


t = ['spam', 'spam', 'spam']


# In[71]:


delimiiter = ' '


# In[72]:


delimiter.join(t)


# In[73]:


# Objects and Values
a = 'banana'
b = 'banana'


# In[74]:


a is b


# In[75]:


a = [1,2,3]


# In[76]:


b = [1,2,3]


# In[77]:


a is b


# In[78]:


b = a


# In[79]:


a is b


# In[80]:


b[0] = 7


# In[81]:


print(a)


# In[82]:


# List Arguments
def delete_head(t):
    del t[0]


# In[83]:


letters = ['a', 'd', 'r', 't']
delete_head(letters)


# In[84]:


print(letters)


# In[85]:


t1 = [1,2,3]


# In[86]:


t2 = t1.append(4)


# In[87]:


print(t1)


# In[88]:


print(t2)


# In[ ]:




