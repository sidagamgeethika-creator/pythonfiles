Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
####STRING METHODS
## length is calles no.of characters in a string
a="python"
len(a)
6
1
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1
### count() no.of repeated characters
#in this we should give with a variable
a="twinkle twinkle little star"
a.count("twinkle")
2
count(a)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count(" ")
3
a.count("t")
5
## FIND
# IT WILL find postion of a character
a="python"
a.find("h")
3
a.find("d")
-1
b="hello"
b.find("l")
2
b[2:4]
'll'
##escape sequesnces
#\n-->new line
#\t-->tab space
a="name\nmobile\tcollagename\nmailid\tbranch
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobile\tcollagename\nmailid\tbranch"
print(a)
name
mobile	collagename
mailid	branch
a="name:Geetha\nmobile:7569000466\tcollagename:aliet\nmailid:sidagamgeethika91@gmail.com\tbranch:ece"
print(a)
name:Geetha
mobile:7569000466	collagename:aliet
mailid:sidagamgeethika91@gmail.com	branch:ece
##REPLACE
#we can replace one word with other word
#only 1 time it will replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="python c"
b.replace("c","dsa")
'python dsa'
##UPPERCASE
a="code"
a.upper()
'CODE'
a.upper
<built-in method upper of str object at 0x00007FFB3EAFEC58>
a="python"
a.captalize()
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.captalize()
AttributeError: 'str' object has no attribute 'captalize'. Did you mean: 'capitalize'?
a.capitalize()
'Python'
a="python course"
a.title()
'Python Course'
a.lower()
'python course'
a="PYTHON"
a.lower()
'python'
##conditions in string
a="java"
##isupper,islower
a.isupper()
False
a.islower()
True
a="PYTHON"
a.isupper()
True
a.isupper()
False
a.islower()
SyntaxError: multiple statements found while compiling a single statement
a.islower()
False
d=123
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="123"
d.isdigit()
True
b="geetha123"
b.alnum()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    b.alnum()
AttributeError: 'str' object has no attribute 'alnum'. Did you mean: 'isalnum'?
b="geetha123"
b.isalnum()
SyntaxError: multiple statements found while compiling a single statement
b="geetha123"
b.isalnum()
True
g="geetha@123"
g.isalnum
<built-in method isalnum of str object at 0x00000238EB272C30>
type(g)
<class 'str'>
a="data  science"
a.startwith()
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.startwith()
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a="data  science"
a.startwith("d")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a.startwith("d")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("d")
True
a.endswith("e")
True
a.startwith("e")
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    a.startwith("e")
AttributeError: 'str' object has no attribute 'startwith'. Did you mean: 'startswith'?
a.startswith("e")
False
###strip()
#leftstrip and rightstrip (lstrip,rstrip)
a="     geetha         "
a.strip()
'geetha'
a.lstrip()
'geetha         '
a.rstrip()
'     geetha'
###concatenation
a="code"
b="gnan"
print(a+b)
codegnan
print(a+" "+b)p
SyntaxError: invalid syntax
print(a+" "+b)
code gnan
fname="geetha")
SyntaxError: unmatched ')'
fname="geetha"
lname="sidagam"
print(fname+lname)
geethasidagam
print(fname+" "+lname)
geetha sidagam
print(fname.title()+lname.title())
GeethaSidagam
print(fname+" "+lname).title()
geetha sidagam
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    print(fname+" "+lname).title()
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
Geetha Sidagam
##SPLIT()
a="c c++ java python"
a.split()
['c', 'c++', 'java', 'python']
a="i am a good girl"
a.split()
['i', 'am', 'a', 'good', 'girl']
###JOIN
a="apple","grape","mango"
"".join(a)
'applegrapemango'
" ".join(a)
'apple grape mango'
"a".join(a)
'appleagrapeamango'
"w "join(a)
SyntaxError: invalid syntax
"w ".join(a)
'applew grapew mango'
###FORMATING
#ADDING ADDITIONAL DATA
a=1
b=3
print(a+b)
4
print("the sum is ", a+b)
the sum is  4
city="vija"
print ("city is ",city)
city is  vija
###FORMAT METHOD
a="mottu"
b="pathlu"
print("hello {}{}".format(a,b))
hello mottupathlu
print("hello {} {}".format(a,b))
hello mottu pathlu
print("hello {}hello {}".format(a,b))
hello mottuhello pathlu
print("hello {} hello {}".format(a,b))
hello mottu hello pathlu
print("hello {} title {}".format(a,b))
hello mottu title pathlu
print("hello {}{}".format(a,b).title)
<built-in method title of str object at 0x00000238EB2735F0>
print("hello {} {}".format(a,b)).title())
SyntaxError: unmatched ')'
print(("hello {} {}".format(a,b)).title())
Hello Mottu Pathlu
###formating string (fstring)
a="geetha"
b="sida"
print(f"hello {a}{b}")
hello geethasida
>>> print(f"hello {a}b}")
SyntaxError: f-string: single '}' is not allowed
>>> print(f"hello {a}{b}").title())
SyntaxError: unmatched ')'
>>> print((f"hello {a}{b}").title)
<built-in method title of str object at 0x00000238EB2735F0>
>>> print((f"hello {a}{b}").title())
Hello Geethasida
>>> print(f"hello {a}{b}")
KeyboardInterrupt
>>> print(f"hello {a} hello {b}")
hello geetha hello sida
>>> a=123
>>> a=2
>>> b=2
>>> print(f"mul {a} {b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"mul {a}*b})
...       
SyntaxError: f-string: single '}' is not allowed
>>> print(f"mul {a}*{b})
... 
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"mul {a}*{b}")
...       
mul 2*2
>>> print(f"mul ({a}*{b})")
...       
mul (2*2)
>>> .................................................
...       
SyntaxError: invalid syntax
>>> c=a*b
...       
>>> print(f"the product is{c}")
...       
the product is4
>>> print(f"the product us{a*b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> KeyboardInterrupt
>>> print(f"the product us{a*b}")
...       
the product us4
