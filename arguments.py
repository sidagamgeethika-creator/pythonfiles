#14-10-2026#
#ARGUMENTS#
#key-word and positional aruguments
'''def Details (id,name,mailid) :
    id=10
    name="pooja"
    mailid="pooja@gmail.com"
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")'''

'''def Details(id,name,mailid) :
    print(id,name,mailid)
Details(id="id",name="name",mailid="mailid")
Details(id=20,name="revathi",mailid="r@gmai.com")
Details(id=30,name="mastan Bee",mailid="m@gmail.com")
Details(30,"Venkat","v@gmail.com")
Details("Gowtham","g@gmail.com",40)
Details(name="Gowtham",mailid="g@gamil.com",id=50)'''

#task
'''def details(id,name,mailid,salary,designation):
    print(id,name,mailid,salary,designation)
details(id="id",name="name",mailid="mailid",salary="salary",designation="designation")
details(id=1,name="revathi",mailid="r@gmail.com",salary=12000,designation="Maths teacher")
details(id=2,name="mastanbee",mailid="m@gmail.com",salary=80000,designation="Principal")
details(3,"venkat","v@gmail.com",30000,"science teacher")
details("gowtham","g@gamil.com","telugu teacher",45000,4)
details(name="gowtham",mailid="g@gamil.com",designation="telugu teacher",salary=45000,id=4)'''

#default arguments
'''def grocery (item,price) :
    print("item is %s", %item)
    print("Price is %.2f",%price)
grocery("rice",2000)'''

'''def grocery(item="sugar",price=100):
    print("items is %s", %item)
    print("price is %.2f", %price)
grocery()'''

'''def grocery(item,price=200):
    print("item is %s" %item)
    print("Price is %.2f" %price)
grocery("dhal")'''

'''def grocery(item="ghee",price) : #error --> non-default arg must not follow default argument
    print("item is %s", %item)
    print("price is %.2", %price)
print(500)'''


#task
'''def cake(cakename,price,qty) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d kgs" %qty)
cake("choclate",600,1)'''

'''def cake(cakename,price,qty=1.5) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d kgs" %qty)
cake("red valvet",600)'''

'''def cake(cakename,price=900,qty=0.5) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d kgs" %qty)
cake("almonds")'''

'''def cake(cakename="choco crunch",price=1000,qty=5) :
    print("cakename is %s" %cakename)
    print("price is %.2f" %price)
    print("qty is %d" %qty)
cake()'''

#task
'''
while True:
    def splitbill():
        persons=int(input("enter no.of persons:"))
        ammount=int(input("enter the total ammount:"))
        perhead=ammount/persons
        print(perhead)
    splitbill()'''
    
'''
def splitbill(persons,amount) :
    print("The amount for each person is %.2f" %(amount/persons))
    print(f"the amount for each person is {(amount/persons)}")
    print("The amount for each person is {}".format(amount/persons))
persons=int(input("enter no.of persons:"))
amount=int(input("enter the total amount:"))
splitbill(persons,amount)'''
'''
while True:
    def splitbill():
        persons=int(input("enter no.of persons:"))
        ammount=int(input("enter the total ammount:"))
        print("ammount per head :",ammount//persons)
    splitbill()'''



###15-10-2026#####

##  * arguments ---> *is used  to unpack the elements\
'''
a=[1,2,3,4,5,6]
print(a)
print(*a)

a=(1,2,3,4,5,6)
print(a)
print(*a)'''

'''
a={1,2,3,4,5,6}
print(a)
print(*a)'''
'''
a={"year":2026,"month":10}
print(a)
print(*a)'''

'''a={"year":2026,"month":10}
print(a)
print(*a.items())'''
'''
a,b,c=1,2,3,4,5,6
print(a)
print(*a)'''
'''
a,b,c=1,2,3,4,5,6
print(a)
print(b)
print(c)'''

'''
a,b,c=1,2,3
print(a)
print(b)
print(c)'''

'''
a,b,*c=1,2,3,4,5,6
print(a)
print(b)
print(*c)

a,*b,c=1,2,3,4,5,6
print(a)
print(*b)
print(c)'''
'''
a="codegnan"
print(a)
print(*a)'''
'''
a="cod"
print(a)
print(*a)'''
'''
a,b,c="cod"
print(a)
print(b)
print(c)'''
'''
*a,b,c="codegnan"
print(*a)
print(b)
print(c)'''


#VARIABLE LENGTH ARGUMENTS
#It Automatically stores in tuple  we use * arguments
'''
def check(*a):
    print(a)
    print(type(a))
check()
b=[2,3,4,5,6,7]
check(*b)
c=(2,3,4,5)
check(*c)
d={1,2,3,4,5}
check(*d)
e={"city":"hyd"}
check(*e)'''

'''
def check1(*a):
    d=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        d=d+i
        print(d)
check1()
check1(2,3,4,5,6)
check1(2,3,4,5.3)
check1(1,2,3,5,2.3,4.2,"geetha")'''
'''
def check1(*a):
    d=2 #creating a variable
    print(a)
    print(type(a))
    for i in a:
        if type(i) in (int,float):
         d=d+i
         print(d)
check1()
check1(1,2,3,5,2.3,4.2,"geetha")'''

##ticket price calculator##
'''
while True:
    def railway_ticket():
        ticket =1000
        gender=input("enter the gender")
        age=int(input("enter the age "))
        if gender =="m":
            if age>=60:
                print("senior citizen")
                ticket=ticket-30/100*ticket
                print(ticket)
            elif age <60:
                    print("normal person")
                    print(ticket)
        elif gender =="f":
            if age>=60:
                print("senior citizen")
                ticket=ticket-50/100*ticket
                print(ticket)
            elif age <60:
                    print("normal person")
                    ticket=ticket-300/100*ticket
                    print(ticket)
    railway_ticket()'''


#####16-10-2026####

#KWARGS(**)
'''
def check(**a):
    print(a)
    print(type(a))
check()
details={"idnos":[10,20,30],
         "names":["prasad","venkat","ajay"],
         "status":["p","a""p"]}
check(**details)
         

def check(**a):
    print(a)
    print(type(a))
    for i in a:
        print(i)
    for i in a.keys():
        print(i)
    for i in a:
        print(a[i])
    for i in a.values():
        print(a[i])
    for i in a:
        print(i,a[i])
    for i in a.items():
        print(i)
check()'''

#both * and ** usage
'''

def check1(*a,**b):
    d=2 #creating a variable
    print(a)
    print(b)
    print(type(a))
    print(type(b))
    for i in a:
        d=d+i
        print(d)
    for i,j in b.items():
        print("key is",i)
        print("values is",j)
check1()
data=(2,3,4,5,6)
check1(*data)
details={"idnos":[10,20,30],
         "names":["prasad","venkat","ajay"],
         "status":["p","a""p"]}
check1(**details)
check1(*data,**details) '''        


#ASCII ---> AMERICAN STANDAED

#CHR()_--> ONLY NUMBERS IT WILL TAKE
'''print(chr(90))
print(chr(65))
print(chr(91))'''

#ord() --> ONLY STRING IN it
'''print(ord("A"))
print(ord("Z"))'''

'''
for i in range (65,91):
    print(chr(i),end =" ")


for i in range (67,123):
    print(chr(i),end=" ")'''
'''
a=input("eneter the name:")
for i in a :
    print(a,ord(i))'''






###22-10-26###
#global and local variables(functions)
#first case of global variable
'''a=4
def check():
    print("inside value is",a)
check()
print("outside value is",a)'''
#second case
'''a=2
def check2():
    a=6
    a=a**2
    print("inside value is",a)
check2()
print("outside value is",a)'''
#third case
'''a=3
def check3():
    a=3
    print("inside value is",a)
    a=5
    print("updated value is",a+5)
    b=12
    b=b+a#local variable
    print("value of b is",b)
check3()
print("a value is",a)
# error b is not defined print("b value is",b)'''
#usage of global keyword
'''a=6
def final():
    global a,b
    print("a value is",a)
    a=7
    print("updated value is",a)
    b=12
    b=b+a
    print("b value is ",b)
final()
print("a value is ",a)
print("b value is",b)'''

#23-10-26
#GENERATORS
# No tuple comprehention in above cases if we remove those braces[] and keep parayanthsis() then the out come is generators.

#syntax
#a=[expr for var in collection/range]
'''a=[i for i in range(10)]
print(a)
print(type(a))'''

a=(i for i in range(21))
'''
print(a)
print(*a)
print(type(a))  '''
'''
#print(list(a))
print(type(a))
#print(tuple(a))
print(set(a))'''

#GENERATOR
#A generator is also a function which can be used as an iterator (loop) by producing group of values where we can use yield keyword

#YIELD VS RETURN

#return will terminate the function yield can pass the function and go on with every successive iteration

'''
a,b=[int(x) for x in input("enter the values:").split(",")]
def check(a,b):
     while a<b:
         yield a
         a=a+1
         yield a
print(*check(a,b))'''
      
'''
a,b=[int(x) for x in input("enter the values:").split(",")]
def check(a,b):
     while a<b:
         yield a
         a=a+1
         #return a
     return a
print(*check(a,b))'''

#yield vs return
'''
def mygen():
    #return "vij"
    #return "hyd"
    #return "vzg"
    return "vij","hyd","vzg"
print(*mygen())'''
'''
def mygen():
    yield "apple"
    yield "mango"
    yield "grapes"
print(*mygen())

## next()
d=mygen()
print(next(d))
print(next(d))
print(next(d))'''

#BMI value
'''                                      
while True:
    h=float(input("Enter your height : "))
    w=float(input("Enter your Weight : "))

    bmi=w/(h*h)
    print("BMI Calculated is:  ",bmi)
    if bmi <=18.5:
        print("You are underweight")
    elif(bmi>18.5 and bmi<=24.5):
            print("You are Healthy")
    elif(bmi > 24.5 and bmi<=29.5):
            print("You are overweight")
    elif bmi>=30:
        print("You are obesity")'''

###24-10-26 ######

#BUILT IN FUNCTIONS
#fromkeys()
'''
a="codegnan"
print(list(a))
print(tuple(a))
print(set(a))
print(dict(a))'''

'''
a="codegnan"
b=dict.fromkeys(a)
print(b)

b=dict.fromkeys(a,"geetha")
print(b)
b["o"]="ntg"
print(b)'''

## evaluate  -->  eval()  it accept all the data type without using them
'''
while True:
    a=int(input(" a value is:"))
    b=int(input(" b value is:"))
    print(a+b)'''
'''
while True:
    a=float(input(" a value is:"))
    b=float(input(" b value is:"))
    print(a+b)'''
'''
while True:
    a=(" a value is:")
    b=(" b value is:")
    print(a+b)'''
'''
while True:
    a=eval(input("a value:"))
    b=eval(input("b value:"))
    print(a+b)'''

## zip () --> we can cobine mulriple collections into one collection
'''
a=[10,20,30,40,50]
names=["geetha","priya","ram","lassy","raj"]
print(a+names)

b=zip(a,names)
print(b)
print(*b)
c=list(zip(a,names))
print(c)
d=tuple(zip(a,names))
print(d)
f=set(zip(a,names))
print(f)
g=dict(zip(a,names))
print(g)'''


#enumerate() -->  we can give counter to the collection
'''
names=["geetha","shalini","debjani","swetha","neethu"]
for i in range(len(names)):
    print(i,names[i])


b=list(enumerate(names,100))
print(b)

d=dict(enumerate(names,100))
print(d)

f=set(enumerate(names,100))
print(f)

g=tuple(enumerate(names,100))
print(g)'''


#map() -->  each object from collection and forms a new collection

'''
a=[2,3,4,22,32,45,68]
b=[1,2,6,21,55,67,90]
c=list(map(max,a,b))
print(c)

a=[2,3,4,22,32,45,68]
b=[1,2,6,21,55,67,90]
c=list(map(min,a,b))
print(c)'''

##27-10-26###
#annonymous##
#annoymous functions are nameless functions and we will use a keyword called as lambda to create anonumous functions.

# write a function to calculate 2*x+5 where x=5
'''
def solveing():
    x=5
    print(2*x+5)
solveing()

#syntax
#a=lambda arg :expr
a=lambda x:2*x+5
print(a(5))

a=int(input("emter a number:"))
b=lambda  x:2*x+5
print(b(a))'''

'''
a="python"
b=lambda x:str(x)
print(b(a.upper()))'''

'''
a="hello world"
b=lambda x:x.title()
print(b(a))'''

#fname+lname=fulname
'''
a=(input("enter fname:"))
b=(input("enter lname:"))
c=lambda a,b:a+" "+b
print(c(a,b))'''

'''
a,b=[x for x in input ("enter the names").split(",")]
c=lambda a,b:(a+" "+b).title()
print(c(a,b))'''
'''
a=int(input("enter value:"))
b=int(input("enter value:"))
c=lambda a,b:a**b    
print(c(a,b)) '''
'''
a=lambda x,y:x**y
print(a(2,4))'''
'''    
n=[2,6,8,10,13,15,20,27,40,60,87,100]
for i in n:
    if i%2 == 0:
        print(i)'''
####FILTER()
'''
n=[2,6,8,10,13,15,20,27,40,60,87,100]
b=list(filter(lambda x:x%2==0,a))
print(b)'''
##29-10-2026##

#None()
'''
a=[[],(),{},set(),None,"",3,3.3,"python",4+2J,True,False]
b=list(filter(None,a))
print(b)'''

###run time input types
'''
a=input("data1")
b=input("data2")
print(a+b)'''
'''
a,b=input("enter the names").split(" ")
print(a+b)'''
'''
a=[x for x in input("enter the names:").split(",")]
print(a)'''

#map()
'''
a,b=map(str,input("enter names").split(" "))
print(a+b)'''

'''
a,b=int(input("enter the values").split(" "))
print(a+b)'''#error
'''
a=[int(x) for x in input("enter the values:").split(",")]
print(a)'''
#map()
'''
a,b=map(int,input("enter values").split(" "))
print(a+b)'''
#n no.of inputs we can take
#map
'''
a=list(map(int,input("enter values").split(" ")))
print(a)'''

'''
a=tuple(map(int,

input("enter values").split(" ")))
print(a)'''
'''
a=set(map(int,input("enter values").split(" ")))
print(a)'''
'''
a,b=map(eval,input("enter the values").split(" "))
print(a+b)'''

'''
a=input("enter the key and values pairs")
b=dict(i.split(":") for i in a.split(","))
print(b)'''










