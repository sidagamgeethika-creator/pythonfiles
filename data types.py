Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#DATA TYPES
a=10
type(a)
<class 'int'>
b=7.8
>>> type(b)
<class 'float'>
>>> a='python'
>>> type(a)
<class 'str'>
>>> a="code"
>>> type(a)
<class 'str'>
>>> a='''code'''
>>> type(a)
<class 'str'>
>>> a=1+2J
>>> type(a)
<class 'complex'>
>>> b=2J+1
>>> type(a)
<class 'complex'>
>>> c=1J
>>> type(c)
<class 'complex'>
>>> type(b)
<class 'complex'>
>>> k=4I
SyntaxError: invalid decimal literal
>>> l=j
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    l=j
NameError: name 'j' is not defined
>>> m="j"
>>> type(m)
<class 'str'>
>>> x=True
>>> type(x)
<class 'bool'>
>>> x=False
>>> type(x)
<class 'bool'>
>>> x=true
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x=true
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> x="true"
>>> type(x)
<class 'str'>
