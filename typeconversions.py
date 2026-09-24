Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
###TYPE CONVERSION//TYPECASTING
int(2)
2
int(2.8)
2
int("geetha")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    int("geetha")
ValueError: invalid literal for int() with base 10: 'geetha'
int(6+7J)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int(6+7J)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
###STRING
str(2)
'2'
str(4.6)
'4.6'
str(6+7J)
'(6+7j)'
str("geetha")
'geetha'
str(True)
'True'
str(False)
'False'
###FLOAT
float(6)
6.0
float(6.8)
6.8
>>> float("geetha")
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    float("geetha")
ValueError: could not convert string to float: 'geetha'
>>> float(9+8J)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    float(9+8J)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> float(True)
1.0
>>> float(False)
0.0
>>> ####complex
>>> complex(3)
(3+0j)
>>> complex(3.7)
(3.7+0j)
>>> complex("geetha")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("geetha")
ValueError: complex() arg is a malformed string
>>> complex(6+8J)
(6+8j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> ####BOOLEAN
>>> bool(8)
True
>>> bool(7.90)
True
>>> bool(7+8J)
True
>>> bool("geetha")
True
>>> bool(6+7J)
True
>>> bool(True)
True
>>> bool(False)
False
