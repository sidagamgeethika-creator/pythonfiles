Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
###dict{} ---> i will in key and pair format
a={"name": "geetha","age":21,"year":2026}
print(a)
{'name': 'geetha', 'age': 21, 'year': 2026}
type(a)
<class 'dict'>
a={"name","age","year"}
type(a)
<class 'set'>
###methods in dict{}
a.keys()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    a.keys()
AttributeError: 'set' object has no attribute 'keys'
a={"name": "geetha","age":21,"year":2026}
a.keys()
dict_keys(['name', 'age', 'year'])
a.values()
dict_values(['geetha', 21, 2026])
a.items()
dict_items([('name', 'geetha'), ('age', 21), ('year', 2026)])
###accessing[] and get
a["name]
  
SyntaxError: unterminated string literal (detected at line 1)
a["name"]
  
'geetha'
a.get("name")
  
'geetha'
a.get("geetha")
  
a
  
{'name': 'geetha', 'age': 21, 'year': 2026}
a["geetha"]
  
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a["geetha"]
KeyError: 'geetha'
##pop() and popitem()
  
a.pop("geetha")
  
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a.pop("geetha")
KeyError: 'geetha'
a.pop("name")
  
'geetha'
a
  
{'age': 21, 'year': 2026}
a.popitem()
  
('year', 2026)
a
  
{'age': 21}
a={"course":"python","duration":100}
  
a.update({"year":2026})
  
a
  
{'course': 'python', 'duration': 100, 'year': 2026}
a.update({"month":"sep","time":10})
  
a
  
{'course': 'python', 'duration': 100, 'year': 2026, 'month': 'sep', 'time': 10}
a.update({"month":"sep"},{"time":10})
  
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a.update({"month":"sep"},{"time":10})
TypeError: update expected at most 1 argument, got 2
##setdefault
  
a={"date":30,"time":12}
  
a.setdefault("hour",1)
  
1
a
  
{'date': 30, 'time': 12, 'hour': 1}
a.setdefault(1,"hour")
  
'hour'
a
  
{'date': 30, 'time': 12, 'hour': 1, 1: 'hour'}
#copy ,clear,length,index
  
a={"colour":"pink","food":"briyani"}
  
a.copy()
  
{'colour': 'pink', 'food': 'briyani'}
a.count()
  
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a.count()
AttributeError: 'dict' object has no attribute 'count'
a.index("food")
  
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.index("food")
AttributeError: 'dict' object has no attribute 'index'
>>> a.clear()
...   
>>> a
...   
{}
>>> a={"name":"geetha","city":"hyd","name":"geetha"}
...   
>>> print(a)
...   
{'name': 'geetha', 'city': 'hyd'}
>>> a={"name":"geetha","city":"hyd","name":"geetha"}
...   
>>> a
...   
{'name': 'geetha', 'city': 'hyd'}
>>> a={"name1":"geetha","city":"hyd","name2":"geetha"}
...   
>>> a
...   
{'name1': 'geetha', 'city': 'hyd', 'name2': 'geetha'}
>>> a={"name":"geetha","city":"hyd","name":"chandu"}
...   
>>> a
...   
{'name': 'chandu', 'city': 'hyd'}
>>> a={"id.nos":10,20,30}
...   
SyntaxError: ':' expected after dictionary key
>>> a={"id.nos":[10,20,30],"names":["geetha","tulasi","chandu"]}
...   
>>> a
...   
{'id.nos': [10, 20, 30], 'names': ['geetha', 'tulasi', 'chandu']}
>>> type(a)
...   
<class 'dict'>
>>> a.keys()
...   
dict_keys(['id.nos', 'names'])
>>> a.values()
...   
dict_values([[10, 20, 30], ['geetha', 'tulasi', 'chandu']])
>>> a.items()
...   
dict_items([('id.nos', [10, 20, 30]), ('names', ['geetha', 'tulasi', 'chandu'])])
