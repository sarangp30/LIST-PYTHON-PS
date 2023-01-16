'''
#Python program to interchange first and last elements in a list
# a = [3,5,2,4,6]
# output: a = [6,5,2,4,3]
#1) 1st
a = [3, 5, 2, 4, 6]
a[0],a[-1] = a[-1],a[0]
print(a)
---------------------------------------------------------------
# 2)
a = [3, 5, 2, 4, 6]
a.pop()
a.pop(0)
a.append(3)
a.insert(0,6)
print(a)
------------------------------------------------------------------
3)
#  not using builtin function
# Python3 program to swap first
# and last element of a list
# Swap function
b= [12,35,9,56,24]
def swapList(b):
    size = len( b)

    # Swapping
    temp = b[0]
    b[0] = b[size - 1]
    b[size - 1] = temp

    return b
print(swapList(b))
--------------------------------------------------------------------------------------------
4)
b= [12,35,9,56,24]
def swapList(b):
    first = b.pop(0)
    last = b.pop(-1)

    b.insert(0, last)
    b.append(first)

    return b
print(swapList(b))
================================================================================================
##Python program to swap two elements in a list
#1)
a = [3, 5, 2, 4, 6]
a[0],a[4],a[1],a[2],a[3] = a[3],a[1],a[2],a[0],a[4]
print(a)
#-------------------------------------------------------------------------------------------------
#  not using builtin function
# Python3 program to swap first
# and last element of a list
# Swap function
b= [12,35,9,56,24]
def swapList(b):
    size = len(b)

    # Swapping
    t = b[0]
    t1 = b[1]
    t2 = b[4]
    b[0] = b[2]
    b[2] = t
    b[1] = b[3]
    b[3] = t1

    return b
print(swapList(b))
======================================================================================================
### Ways to find length of list
# 1) navie method
a = [3,5,4,6,7,3,2,4,5,6,7]
n = len(a)
print(n)
--------------------------------------------------------------------------------------------
#2) method of for  loop
a = [3,5,7,8,12,1]
c = 0
for i in a:
    c+=1
print('list:',a)
print(' length of list :',c)
-------------------------------------------------------------------
# 3) Using length_hint()
list = ['a','b','s',12,12.5,32+2j]
l1= len(list)
l2= length_hint(list)
print("Length of list using len() is : " + str(l1))
print("Length of list using length_hint() is : " + str(l2))
==================================================================

## Check if element exists in list in Python
1) membership operator( in and not in)
list = ['a','b','s',12,12.5,32+2j]
print(12 in list) # 12 is exists
print(14 in list) # 14 is exists
print('a' in list)
-------------------------------------------------
2) using if and else
list = ['a','b','s',12,12.5,32+2j]
i = 's'
if i in list:
    print('exist')
else:
    print('not exist')
--------------------------------------------------------------------
list = ['a','b','s',12,12.5,32+2j]
if(12 in list):
    print('elements exist')

-------------------------------------------------------------
3) for loop
list = ['a','b','s',12,12.5,32+2j]
for i  in list:
    if (i == 12):
        print('exist')

================================================================
###Different ways to clear a list in Python
1) Using clear() method
# Initializing lists
list1 = [1, 2, 3]
list2 = [5, 6, 7]
print('before list1:',list1)
print('before list2:',list2)
list1.clear()
list2.clear()
print('after list1:',list1)
print('after list2:',list2)
---------------------------------------------------------
2)Using del
list1 = [1, 2, 3]
list2 = [5, 6, 7]
print('before list1:',list1)
print('before list2:',list2)
del list1[:]
del list2[:]
print('after list1:',list1)
print('after list2:',list2)
---------------------------------------------------------------------
3) pop method and while loop
list1 = [1, 2, 3]
print('before list1:',list1)
while(len(list1) != 0):
    list1.pop()
print('after list1:',list1)
==============================================================
### Reversing a List in Python
1) slicing method
lst = [2,3,5,7,9,11]
a = lst[::-1]
print(a)
---------------------------------------------------------------------
2) reverses method
lst = [2,3,5,7,9,11]
lst.reverse()
print("Using reverse() ", lst)

print("Using reversed() ", list(reversed(lst)))
-------------------------------------------------
3)Reversing a list using the insert() function
lst = [2,3,5,7,9,11]
l = [] # empty list
# iterate to reverse the list
for i in lst:
	# reversing the list
	l.insert(0, i)
print(l)
-------------------------------------------------------------
4) Reversing a list using slicing technique
lst = [2,3,5,7,9,11]
def Reverse(lst):
	new_lst = lst[::-1]
	return new_lst
print(Reverse(lst))
----------------------------------------------------------
5)Reversing a list using list comprehension
lst = [2,3,5,7,9,11]
nt = [lst[len(lst) - i]
	   for i in range(1, len(lst)+1)]
print(nt)
=================================================================
###Python program to find sum of elements in list
1) using sum method
l = [2,4,12,14,10,8]
print(sum(l))
------------------------------------------------
2) Using add() function of operator module
l = [2,3,1,54,32,12]
from operator import*
r = 0
for i in l:
    r = add(i,r)
print(r)
------------------------------------------------
3)Using for loop
l1 = [11, 5, 17, 18, 23]
total = 0
for i in range(0, len(l1)):
	total = total + l1[i]
# printing total value
print("Sum of all elements in given list: ", total)
---------------------------------------------------------------
#4)Using enumerate function
l1 = [11, 5, 17, 18, 23]
s=0
for i,a in  enumerate(l1):
    s+=a
print(s)
=======================================================
### Python | Multiply all numbers in the list
1) Using math.prod
import math
l1 = [2,3,4,5]
l2 = [7,6,5]
print(math.prod(l1))
print(math.prod(l2))
--------------------------------------------
2) Using lambda function: Using numpy.array
from functools import reduce
list1 = [1, 2, 3]
list2 = [3, 2, 4]

result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)
--------------------------------------------
3)Using mul() function of operator module.
from operator import*
s1= [2,3,5]
n=1
for i in s1:
    n = mul(i,n)
print(n)
-------------------------------------------------
4)list using lambda function and accumulate()

from itertools import accumulate
s1= [1, 2, 3]
s2= [3, 2, 4]


result1 = list(accumulate(s1, (lambda x, y: x * y)))
result2 = list(accumulate(s2, (lambda x, y: x * y)))
print(result1[-1])
print(result2[-1])
===============================================================
###Python program to find smallest number in a list
1) In Ascending order
a = [3,4,6,12,7,2,3]
a.sort()
print(a)
print('smallest element:',a[0])
---------------------------------------------------------
2) min method
lst = [20, 10, 50, 12, 100]
print(min(lst))
-----------------------------------------------------
3)Using the lambda function
lst = [20, 10, 50, 12, 100]
print(min(lst, key=lambda value: int(value)) )
----------------------------------------------------------------
4) Using the enumerate function
lst = [20, 10, 50, 12, 100]
a,i= min((a,i) for (i,a) in enumerate(lst))
print(a)
====================================================================
###Python program to find highest number in a list
#1) In Ascending order
a = [3,4,6,12,7,2,3]
a.sort()
print(a)
print('smallest element:',a[-1])
-----------------------------------------------------------------------------
#2) max method
lst = [20, 10, 50, 12, 100]
print(max(lst))
------------------------------------------------------------------------------
#3)Using the lambda function
lst = [20, 10, 50, 12, 100]
print(max(lst, key=lambda value: int(value)))
--------------------------------------------------------------------------------
# 4) Using the enumerate function
lst = [20, 10, 50, 12, 100]
a,i= max((a,i) for (i,a) in enumerate(lst))
print(a)
or
x = [a for i,a in enumerate(lst)]
print(max(x))
===================================================================================
###Python program to find second largest number in a list
#1) In Ascending order
a = [3,4,6,12,7,2,3]
a.sort()
print(a)
print('smallest element:',a[-2])
--------------------------------------------------------------------
2)By removing the max element from the list
a = [3,4,6,12,7,2,3]
nl= set(a)
#print(nl)
nl.remove(max(nl))
print(nl)
print(max(nl))
--------------------------------------------
3)Using lambda function
a = [3,4,6,12,7,2,3]
max1 = max(a)
max2 = max(a, key=lambda x: min(a) if (x == max1) else x)
print(max2)
----------------------------------------
4)Using enumerate function
l1 = [3,4,6,12,7,2,3]
m= max(l1)
x =[a for i,a in enumerate(l1) if a<m]
print(max(x))
==============================================================================
###Python program to find N largest elements from a list
1)using sort (ascending order)
l1 = [3,4,6,12,7,2,3]
l1.sort()
print(l1[4:8])
==========================================================================
# Python program to print even numbers in a list
1)Using for loop
a = []
for i in range(1,10):
    if i%2 ==0:
        a.append(i)
print('even no list :',a)
-----------------------------------------------------------------------
2) while loop
l = [2,4,6,3,7,8,9,12]
num = 0
while(num<len(l)):
    if l[num]% 2== 0:
        print(l[num],end=' ')
    num += 1
------------------------------------------------------
3) Using lambda
l = [2,4,6,3,7,8,9,12]
l1 = list(filter(lambda x: ( x % 2==0),l))
print(l1)
-------------------------------------------------------------
4) using enumerate
l = [2,4,6,3,7,8,9,12]
for a,i in enumerate(l):
    if i % 2==0:
        print(i,end=' ')
=======================================================================
# Python program to print odd numbers in a list
1)Using for loop
a = []
for i in range(1,10):
    if i%2 !=0:
        a.append(i)
print('odd no list :',a)
-------------------------------------------------------------------
#2) while loop
l = [2,4,6,3,7,8,9,12]
num = 0
while(num<len(l)):
    if l[num]% 2!= 0:
        print(l[num],end=' ')
    num += 1
---------------------------------------------------------------
3) Using lambda
l = [2,4,6,3,7,8,9,12]
l1 = list(filter(lambda x: ( x % 2!=0),l))
print(l1)
-------------------------------------------------------------
4) using enumerate
l = [2,4,6,3,7,8,9,12]
for a,i in enumerate(l):
    if i % 2!=0:
        print(i,end=' ')
====================================================================
Python program to print all even numbers in a range
1) using loop
x = []
for i in range(2,20,2):
    x.append(i)
print('even no list:',x)
------------------------------------------------------
2)Using the lambda function
z = 2
b = 20
x = []
for i in range(z,b+1):
    x.append(i)
print(list(filter(lambda j:(j%2==0),x)))
---------------------------------------------------
3) using enumerate function
a=2;b=20;x=[]
for i in range(a,b+1):
    x.append(i)
print([a for j,a in enumerate(x) if a%2==0])
-----------------------------------------------
4) pass function
a=2;b=20
for i in range(a,b+1):
    if i%2!=0:
	    pass
    else:
        print(i,end=" ")
============================================================================

###Python program to print all odd numbers in a range
1) using for loop
x = []
for i in range(2,20,1):
    x.append(i)
print('odd no list:',x)
------------------------------------------------------
2)Using the lambda function
z = 1
b = 20
x = []
for i in range(z,b):
    x.append(i)
print(list(filter(lambda j:(j%2!=0),x)))
---------------------------------------------------
3) using enumerate function
a=1;b=20;x=[]
for i in range(a,b):
    x.append(i)
print([a for j,a in enumerate(x) if a%2!=0])
-----------------------------------------------
4) pass function
a=1;b=20
for i in range(a,b+1):
    if i%2==0:
	    pass
    else:
        print(i,end=" ")
============================================================
###Python program to print negative numbers in a list
1) for loop
s = [3,7,-9,2,-4,10,-11]
x = []
for i in s:
    if i <=0:
        x.append(i)
        x.sort()
print(x)
------------------------------------------------------------------------
2) while loop
s = [3,7,-9,2,-4,10,-11]
i = 0
while(i < len(s)):
    if s[i] <= 0:
        print(s[i],end=' ')
    i+=1
-----------------------------------------------------
3) Using lambda expressions
s = [3,7,-9,2,-4,10,-11]
s1= list(filter(lambda x:(x<=0),s))
print(s1)
-------------------------------------------------------------------------
4) using enumerate function
s = [3,7,-9,2,-4,10,-11]
print([a for j,a in enumerate(s) if a<=0])
=================================================================================
###Python program to print all positive numbers in a range
#1) for loop
x = []
for i in range(-5,5):
    if i >=0:
        x.append(i)
        x.sort()
print(x)
-------------------------------------------------------------
# 2)Using the lambda function
z = -12
b = 12
x = []
for i in range(z,b):
    x.append(i)
print(list(filter(lambda j:(j>=0),x)))
----------------------------------------------------------------------------------
# 3) using enumerate function
z = -12
b = 12
x = []
for i in range (-12,12):
    x.append(i)
print([a for j, a in enumerate(x) if a>=0])
----------------------------------------------------------------
#4) using pass function
x = []
for i in range(-12,10):
    if i <= 0:
        pass
    else:
        x.append(i)
print(x,end=' ')
==================================================================
### Remove multiple elements from a list in Python
1)  using slicing(deleted)
a = [2,1,4,3,5,6,7,8]
del a[1:4]
print(a)
-----------------------------------------------------------------------
2)using for loop( but only even and odd no remove)
a = [2,1,4,3,5,6,7,8]
for i in a:
    if i%2==0:
        a.remove(i)
print(a,end=' ')
-------------------------------------------------------------
3) enumerate function
b= [2,1,4,3,5,6,7,8]
b =([a for i,a in enumerate(b) if a % 2 != 0])
print(b)
===================================================================================
### Remove empty List from List
 1) for loop
l =[5, 6, [], 3, [], [], 9]
b = []
for i in l:
    x=str(type(i))
    if(x.find('list')!=-1):
        if(len(i)!=0):
           b.append(i)
    else:
         b.append(i)
print(b)
---------------------------------------------------
2) while loop and remove
l =[5, 6, [], 3, [], [], 9]
while [] in l :
    l.remove([])
    print(l)
-------------------------------------------------------------------
3)enumerate function
l =[5, 6, [], 3, [], [], 9]
l = ([a for i,a in enumerate(l) if a != []])
print(l)
-------------------------------------------------------------------------------
4) filter function
l =[5, 6, [], 3, [], [], 9]
l1 = list(filter(None,l))
print(l1)
===============================================================================
###Count occurrences of an element in a list
1) Using count()
l = [2,4,5,6,3,4,2,5,4,2,6,5,4,2,5,1]
print(l.count(2))
--------------------------------------------------
2) using def and count()
l = [2,4,5,6,3,4,2,5,4,2,6,5,4,2,5,1]
x = 4
def countX(l,x):
    return l.count(x)
print('{} has occurred {} times'.format(x, countX(l, x)))
----------------------------------------------------------
3)Using Counter()
from collections import Counter
l = [2,4,5,6,3,4,2,5,4,2,6,5,4,2,5,1]
x = 5
b = Counter(l)
print('{} has occurred {} times'.format(x,b[x]))
---------------------------------------------------------
4) list Using the panda’s library
import pandas as pd
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

count = pd.Series(l).value_counts()
print("Element Count")
print(count)
======================================================
###Python | Cloning or Copying a list
1)Using the slicing
l = [2,4,5,7,4,1,9]
def Cloning(l):
    lc = l[:]
    return lc
l1= Cloning(l)
print(l)
print(l1)
---------------------------------------------------------------------
2)Using the extend() method
l = [2,4,5,7,4,1,9]
def Cloning(l):
    lc =[]
    lc.extend(l)
    return lc
l1= Cloning(l)
print(l)
print(l1)
------------------------------------------------------------------------
3)using copy
l = [2,4,5,7,4,1,9]
def Cloning(l):
    lc = l
    return lc
l1 = Cloning(l)
print(l)
print(l1)
--------------------------------------------------------
4)Using the method of Shallow Copy
import copy
l = [2,4,5,7,4,1,9]
l2 = l.copy()
print(l)
print(l2)
-----------------------------------------------------
5) deep copy
l = [2,4,5,7,4,1,9]
l1 = l
print(l)
print(l1)
==================================================================
###Python program to find Cumulative sum of a list
1)using def
l = [10, 20, 30, 40, 50]
def Cumulative(l):
	cl= []
	le = len(l)
	cl = [sum(l[0:x:1]) for x in range(0, le+1)]
	return cl[1:]
print (Cumulative(l))
-----------------------------------------------------
2)using for loop
l = [10, 20, 30, 40, 50]
nl= []
j = 0
for i in range(0, len(l)):
	j += l[i]
	nl.append(j)
print(nl)
========================================================================================

###Sort the values of first list using second list in Python
1) for loop ,sort(),list() & and set()
l1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
l2 = [0, 1, 1, 0, 1, 2, 2, 0, 1]
a = list(set(l2))
a.sort()
r= []
for i in a:
	for j in range(0, len(l2)):
		if(l2[j] == i):
			r.append(l1[j])
print(r)
'''
