Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=" i am in class"
a[8]+a[9]+a[10]+a[11]
' cla'
a="i am in class"
a[8]+a[9]+a[10]+a[11]
'clas'
a[2]+a[3]
'am'
a[5]+a[6]
'in'
a[1]
' '
a[4]
' '
a[7]
' '
a[1]
' '
+
a[1]+a[4]
'  '
a[2]+a[3]+a[8]+a[9]+a[10]+a[11]
'amclas'
a="vijayawada is a royal city"
a[16]+a[17]+a[18]+a[19]+a[20]
'royal'
a[22]+a[23]+a[24]+a[25]
'city'
a[11]+a[12]+a[13]
'is '
a[11]+a[12]
'is'
###negative indexing
a="vizag is a city of destiny"
a[-11]+a[-12]+a[-13]+a[-14]
' yti'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'destiny'
a[-15]+a[-14]+a[-13]+a[12]
'citi'

a[-15]+a[-14]+a[-13]+a[-12]
'city'
a="simple is better than complex"
a[-19]+a[-18]+a[-17]+a[-16]+a[-15]+a[-14]
'better'
a[-7]+a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'complex'
a[-28]+a[-27]+a[-26]+a[-25]+a[-24]+a[-23]
'imple '
a+[29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a+[29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
TypeError: can only concatenate str (not "list") to str
a[29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a[29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
IndexError: string index out of range
a+[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    a+[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
TypeError: can only concatenate str (not "list") to str
a[-29]+a[-28]+a[-27]+a[-26]+a[-25]+a[-24]
'simple'
####SLICING
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
a[:4]
'code'
a[4:]
'gnan'
a[2:5]
'deg'
a="work hard until you succed"
a[10:15]
'until'
a[5:9]
'hard'
a[0:4]
'work'
a[16:19]
'you'
a[20:26]
'succed'
a="time is very precious"
a[13:21]
'precious'
a[8:12]
'very'
a[:4]
'time'
###NEGATIVE SCLICING
a="this is python class"
a="i love python"
a[-11:-7]
'love'
a[-6:]
'python'
a[-16:]
'i love python'
a="today is weekend"
a[-16]
't'
a[-16:-11]
'today'
a[-10:-8]
'is'
a[-7:]
'weekend'
a[-7:-1]
'weeken'
>>> a[-7:0]
''
>>> ###striding
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a="machine learning"
>>> a[::4]
'miln'
>>> a[::6]
'men'
>>> a[::2]
'mcielann'
>>> a[5:]
'ne learning'
>>> a[:9]
'machine l'
>>> a[::7]
'm n'
>>> a="cloud computing"
>>> a[1:11:2]
'lu op'
>>> a[2:14:4]
'ocu'
>>> a[5:13:3]
' mt'
>>> a[4:12:2]
'dcmu'
>>> ###NEGATIVE STRIDING
>>> a="python course"
>>> a[-1:-11:-2]
'ero o'
>>> a[-2:-12:-3]
'sont'
>>> 
>>> #in positive striding highest to lowest not possiable
>>> #in negative striding lowest to highest not possiable
>>> a[::1]
'python course'
>>> a[::-1]
'esruoc nohtyp'
