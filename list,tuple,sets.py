Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
###LIST [] IT IS MUTABLE IT IS A COLLECTION OF DIFFERENT DATA TYPES
a=[3,3.4,"python",6+3j,True,False]
print(a)
[3, 3.4, 'python', (6+3j), True, False]
type(a)
<class 'list'>
a=3.5
type(a)
<class 'float'>
a[3.5]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    a[3.5]
TypeError: 'float' object is not subscriptable
a=[3.5]
type(a)
<class 'list'>
#methods in it
#APPEND
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("c++","ds")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a.append("c++","ds")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["c++","ds"])
a
['python', 'java', 'c', 'c++', ['c++', 'ds']]
###extend
a=["ds","ai"]
a.extend("ml")
a
['ds', 'ai', 'm', 'l']
a.extend(["ml","ece"])
a
['ds', 'ai', 'm', 'l', 'ml', 'ece']
##insert()
a=["ece","cse","eee"]
a.insert(1,"ds")
a
['ece', 'ds', 'cse', 'eee']
##index
a=["viz","vij","hyd"]
a.index("vij")
1
##copy
a.copy()
['viz', 'vij', 'hyd']
c=a.copy()
c
['viz', 'vij', 'hyd']
###sort() - arrage
a=["mamgo","apple","grape","bannana"]
a.sort()
a
['apple', 'bannana', 'grape', 'mamgo']
a=["1,3,4,5,6,111,22,33,]
   
SyntaxError: unterminated string literal (detected at line 1)
a=["1,3,4,5,6,111,22,33"]
   
a.sort()
   
a
   
['1,3,4,5,6,111,22,33']
a=[1,3,4,5,6,111,22,33]
   
a.sort()
   
a
   
[1, 3, 4, 5, 6, 22, 33, 111]
a=["Grape","Apple","Cherry","berry","merry"]
   
a.sort()
   
a
   
['Apple', 'Cherry', 'Grape', 'berry', 'merry']
b=["apple","bannana","cherry","Berry","Cat","Dragon"]
   
b.sort()
   
b
   
['Berry', 'Cat', 'Dragon', 'apple', 'bannana', 'cherry']
###reverse
   
a=["black","pink","blue","yellow"]
   
a.reverse()
   
a
   
['yellow', 'blue', 'pink', 'black']
b=[1,2,3,4]
   
b.reverse()
   
b
   
[4, 3, 2, 1]
##pop() --> deleting
   
a=["java","python","ai","ml"]
   
a.pop()
   
'ml'
a
   
['java', 'python', 'ai']
a.pop("java")
   
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a.pop("java")
TypeError: 'str' object cannot be interpreted as an integer
a.pop(0)
   
'java'
##remove
   
a.remove("python")
   
a
   
['ai']
b=["chair","table"]
   
b.remove("chair")
   
b
   
['table']
##clear
   
b=["cat","rat","dog"]
   
b.clear()
   
b
   
[]
c=[]
   
c.append("geetha")
   
c
   
['geetha']
##length
   
a=["hi","hello"]
   
len(a)
   
2
b="hello"
   
len(b)
   
5
c=["hello"]
   
len(c)
   
1
a.count()
   
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.count()
TypeError: list.count() takes exactly one argument (0 given)
##count
   
c=["hello"]
   
c.count()
   
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    c.count()
TypeError: list.count() takes exactly one argument (0 given)
#####TUPLE () IT IS UNMUTABLE  REPRESENTED BY()
   
a=(3,5.6,"geetha",5+6j,True,False)
   
type(a)
   
<class 'tuple'>
a.count(True)
   
1
a.index(True)
   
4
len(a)
   
6
##### SETS {}--> unorder,semi-mutable,it will duplicate values
   
a={4,5.6,"geetha","3+2j",True,False}
   
print(a)
   
{False, True, 'geetha', 4, 5.6, '3+2j'}
type(a)
   
<class 'set'>
##add
   
a={1,2,3,4,5}
   
a.add(23)
   
a
   
{1, 2, 3, 4, 5, 23}
a={1,2,3,4,5}
   
b={4,5,6,7,8}
   
a.issubset(b)
   
False
b.issubset(a)
   
False
a={1,2,3,4,5,6,7,8}
   
b={5,6,7,8}
   
a.issubset(b)
   
False
b.issubset(a)
   
True
###SUPERSET
   
a={4,5,6,7,8}
   
b={6,7,8}
   
a.issuperset(b)
   
True
b.issuperset(a)
   
False
##it eill duplicate the values
   
a={1,2,3,4,5,6,6,5,4,3}
   
print(a)
   
{1, 2, 3, 4, 5, 6}
##UNION-->merging of two sets
   
a={10,21,32,43,54,65}
   
b={12,36,78,98,76,99}
   
a.union(b)
   
{32, 65, 98, 99, 36, 10, 43, 12, 76, 78, 21, 54}
##intersection --->snme values will be printed
   
a={3,4,5,6,7,8}
   
b={9,1,2,6,7,8}
   
a.intersection(b)
   
{8, 6, 7}
##update
   
a={2,3,4,5,6,7}
   
b={6,7,8,9,10}
   
a.update(b)
   
a
   
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b
   
{6, 7, 8, 9, 10}
b.update(a)
   
b
   
{2, 3, 4, 5, 6, 7, 8, 9, 10}
b
   
{2, 3, 4, 5, 6, 7, 8, 9, 10}
##difference
   
a={5,6,7,8,9,10,11}
   
b={9,10,11,12,13,14}
   
a.difference(b)
   
{8, 5, 6, 7}
b.difference(a)
   
{12, 13, 14}
##symmetric difference
   
a={3,4,5,6,7,8}
   
b={5,6,7,8,9,10}
   
a.symmetric_difference(b)
   
{3, 4, 9, 10}
##difference update
   
a={4,5,6,7,8,9}
   
b={6,7,8,9,10,11,12,13}
   
a.difference_update(b)
   
a
   
{4, 5}
b.difference_update(a)
   
b
   
{6, 7, 8, 9, 10, 11, 12, 13}
a
   
{4, 5}
b
   
{6, 7, 8, 9, 10, 11, 12, 13}
##intersection update
   
a={5,6,7,8,9,10,11}
   
b={9,10,11,12,13,14}
   
a.intersection_update(b)
   
a
   
{9, 10, 11}
b.difference_update(a)
   
b
   
{12, 13, 14}
##symmetric difference update
   
a={10,20,30,40,50}
   
b={30,40,50,60,70}
   
a.symmetric_difference_update(b)
   
a
   
{20, 70, 10, 60}
b.symmetric_difference_update(a)
   
b
   
{50, 20, 40, 10, 30}
a
   
{20, 70, 10, 60}
b
   
{50, 20, 40, 10, 30}
##pop and remove
   
a{2,3,4,5,6,7}
   
SyntaxError: invalid syntax
a.pop()
   
20
a={2,3,4,5,6,7}
   
a.pop()
   
2
a
   
{3, 4, 5, 6, 7}
a.remove(5)
   
a
   
{3, 4, 6, 7}
a.pop(7)
   
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    a.pop(7)
TypeError: set.pop() takes no arguments (1 given)
##dicard
   
a.discard(4)
   
a
   
{3, 6, 7}
##copy,clear, add
   
a={1,2,3,4,5}
   
a.copy()
   
{1, 2, 3, 4, 5}
a.clear()
...    
>>> a
...    
set()
>>> b=set()
...    
>>> b.add(70)
...    
>>> b
...    
{70}
>>> ###disjoin
...    
>>> a={1,2,3,4,5}
...    
>>> b={6,7,8,9,0}
...    
>>> a.isdisjoint(b)
...    
True
>>> a={1,2,3,4,5}
...    
>>> b={1,2,3,4,5}
...    
>>> a.isdisjoint(b)
...    
False
>>> ##length,count,index
...    
>>> a={1,2,3,4,5,6}
...    
>>> len(a)
...    
6
>>> a.count(3)
...    
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    a.count(3)
AttributeError: 'set' object has no attribute 'count'
>>> a.index(2)
...    
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    a.index(2)
AttributeError: 'set' object has no attribute 'index'
