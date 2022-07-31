#!/usr/bin/env python
# coding: utf-8

# # Say "Hello, World!" With Python

# ## Task:

# Here is a sample line of code that can be executed in Python:
# 
# `print("Hello, World!")`  
# You can just as easily store a string as a variable and then print it to stdout:
# 
# `my_string = "Hello, World!"`  
# `print(my_string)`  
# The above code will print Hello, World! on your screen. Try it yourself in the editor below!

# ## My Answer:

# In[6]:


print("Hello World!")


# # Python If-Else

# ## Task:

# Given an integer, n, perform the following conditional actions:
# 
# If n is odd, print Weird   
# If n is even and in the inclusive range of 2 to 5, print Not Weird  
# If n is even and in the inclusive range of 6 to 20, print Weird  
# If n is even greater than 20, print Not Weird  

# ## My Answer:

# In[7]:


#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    
if (n % 2 != 0):
    print("Weird")
elif (n % 2 == 0 and (n >= 2 and n <= 5)):
    print("Not Weird")
elif (n % 2 == 0) and (n >= 6 and n <= 20):
    print("Weird")
elif (n % 2 == 0 and n > 20):
    print("Not Weird") 


# # Arithmetic Operators

# ## Task:

# The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:  
# 
# The first line contains the sum of two numbers.  
# The second line contains the difference of the two numbers (first – second).  
# The third line contains the product of two numbers.   

# ## My Answer:

# In[12]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())

print(a+b);
print(a-b);
print(a*b);


# # Python: Division

# ## Task:

# The provided code stub read two integers, a and b, from STDIN.  
# 
# Add logic to print two lines. The first line should contain the result of integer division, a // b. The second line should contain the result of float division, a / b.  
# 
# No rounding or formatting is necessary.

# ## My Answer:

# In[1]:


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b);
print(a/b);


# # Loops

# ## Task:

# The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i2 . 

# ## My Answer:

# In[3]:


if __name__ == '__main__':
    n = int(input())

i = 0;
while (i < n):
    print(i **2)
    i+= 1

