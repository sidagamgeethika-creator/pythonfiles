Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
###Arthematic operators
a=4
b=6
print(a+b)
10
print(a-b)
-2
print(a*b)
24
print(a//b)
0
print(a/b)
0.6666666666666666
print(a**b)
4096
print(a%b)
4
###ASSIGNMENT OPERATORS
a=5
b=7
print(a-=b)
SyntaxError: invalid syntax
a+=b
a
12
a-=5
a
7
a*=5
a
35
a**=8
a
2251875390625
a//=7
a
321696484375
a/=4
a
80424121093.75
a%=6

\
a
1.75
b=4
a+=b
b
4
b-+7
-3
b-=6
b
-2
b*=16
b
-32
b**=39
b
-50216813883093446110686315385661331328818843555712276103168
b//=12
b
-4184734490257787175890526282138444277401570296309356341931
b/=88
b
-4.7553801025656674e+55
###COMPARISION OPERATOR
a=5
b=8
a<b
True
a>
SyntaxError: invalid syntax
a>b
False
a<b
True
a>b
False
a<=b
True
a>=b
False
a==b
False
a=7
b=7
a==b
True
###LOGICAL OPERATORS
a=10
b=20
a<b and b>a
True
a<=b and b<=a
False
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or a>=b
True
a!=b or a==b
True
not True
False
not False
True
a>=b and a>=b
False
a<=b or b>= a
True
#### IDENTIFY OPERTORS
a=68
type (a) is not int
False
type(a)is int
True
type (a) is float
False
type(a) is not float
True
b=5.8
type(b) is float
True
type(b) is not float
False
a="geetha"
type(a) is string
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    type(a) is string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(a) is str
True
type(a) is not string
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    type(a) is not string
NameError: name 'string' is not defined. Did you forget to import 'string'?
type(a) is not str
False
a=3+7j
type(a) is complex
True
type(a) is not complex
False
a= True
type(a) is bool
True
type(a) is not bool
False
###MEMEBERSHIP OPERATORS
a=1.2.3.4.5.6.7,8
SyntaxError: invalid syntax
a=1,2,3,4,5,6,7,8,9
9 is a
False
9 in a
True
20 not in a
True
3 not in a
False
####bitwise
a=5
b=6
a&b
4
bin(5)
'0b101'
bin(6)
'0b110'
##in bitwise opposite are there then we have to take 0 when same are there then two 1s are 1 and two 0s are 0
bin(90)
'0b1011010'
a|b
7
##in bitwise for |(or) opposite are there then we have to take 1 when same are there then two 1s are 1 and two 0s are 0
>>> a=8
>>> b=8
>>> bin(a)
'0b1000'
>>> bin(b)
'0b1000'
>>> a|b
8
>>> a=6
>>> ##for  negotion we had a formula that -(a+1)
>>> -(a+1)
-7
>>> ~a
-7
>>> a=-4
>>> ~a
3
>>> ##for exor where the
>>> ##in bitwise for exor(^) opposite are there then we have to take 1 when same are there then two 1s are 0 and two 0s are 0
>>> a=4
>>> b=3
>>> a^b
7
>>> a=20
>>> b=4
>>> a^b
16
>>> ###leftshift for the add no.of zeros on right size
>>> a=2
>>> a<<3
16
>>> a=8
>>> a<<8
2048
>>> #####rightshift for the add no.of zeros on left size
>>> a=2
>>> a>>3
0
>>> a>>8
0
>>> a=8
>>> a>>8
0
>>> a=9
>>> a>>3
1
