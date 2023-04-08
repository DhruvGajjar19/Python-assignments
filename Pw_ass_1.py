#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Explain with an example each when to use a for loop and a while loop.



# In[2]:


# for loop


# In[6]:


sum = 0
for i in range(5):
    sum = sum + i
    print(sum)


# In[3]:


# while loop

n = 6
b = 0

while b<n:
    b = b+1
    print(b)
    


# In[2]:


# q2)-Write a python program to print the sum and product of the first 10 natural numbers using for and while loop.

# Sum of first 10 natural numbers

sum=0
n=11
i =0
while i<n:
    sum = sum + i
    i = i+1
print(sum)

# Product of first 10 natural numbers

a = 1
d=11
p=1

while a<d:
    p = p*a
    a=a+1
print(p)
    

    



# In[1]:


# Q3. Create a python program to compute the electricity bill for a household.
n = int(input("Enter a unit = "))

if n<=100:
    print(" bill ", 4.5*n)

elif 101<=n<200:
    print(" bill ",(6*(n-100) + (4.5*100)))

elif 201<=n<=300:
    print("bill", ((n-200) +6*(100) + (4.5*100) ))

else :
    print("bill",( 20*(n-300)+10*(100) +6*(100) + (4.5*100)))







# In[4]:


# Q4 

# use of 'for loop'
# First we make list of number 1 to 100
n=1
l=[]
for n in range(100):
    n = n+1
    l.append(n)
# print(l)

# find cube of all number
cube = 1
l_cube = []
for i in l:
    cube = i*i*i
    l_cube.append(cube)
# print(l_cube)


l_div_4_5 = []
for i in l_cube:
    if i % 4 == 0 or i % 5 == 0:
        l_div_4_5.append(i)
print(l_div_4_5)


# In[7]:


# Q5

string_1 = "I want to become a data scientist"

string= string_1.lower()

l = []
l.extend("aeiou")
# print(l)

count = 0
for i in string:
    if i in l:
        count = count+1
print(count)


# In[ ]:




