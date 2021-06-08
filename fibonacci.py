#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return fibonacci(n-1)+fibonacci(n-2)

    from math import sqrt
def fibonacci(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))    

def fibonacci():
    a,b = 0,1
    while True:
        yield a
        a, b = b, a + b

def Fib(startNumber, endNumber):
    for cur in fibonacci():
        if cur > endNumber: return
        if cur >= startNumber:
            yield cur

for i in Fib(10, 100):
    print (i)


# In[ ]:




