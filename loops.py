###       LOOPS      ####
#for,while,range,break,continue,pass

##FOR LOOP (sequence iterations)
a=[10,20,30,30,40,50]
'''print(a)'''

'''for i in a:
    print(a)'''

'''for i in a:
    print(i)'''

'''for i in a:
    print(i,end="")'''

'''for i in a:
    print(i,end=" ,")'''
#list
'''a=[5,6,7,8,9,10]
for i in a:
    print(i)
print (type(a))
print(type(i))'''

'''## tuple
a=(5,6,7,8,9,10)
for i in a:
    print(i)
print (type(a))
print(type(i))'''

## dicnory
'''
a={"name":"geethika","city":"vij","year":2026}
for i in a:
    print(i)
print (type(a))
print(type(i))'''
'''
a={"name":"geethika","city":"vij","year":2026}
for i in a:
    print(i)
for i in a.keys():
    print (type(a))
    print(type(i))
for i in a.values():
    print(i)
    print (type(a))
    print(type(i))
for i in a.items():
    print(i)
    print (type(a))
    print(type(i))'''
#set
'''
a={5,6,7,8,9,10}
for i in a:
    print(i)
print (type(a))
print(type(i))'''

#float
'''
a=[1.2,2.3,5.3,4.4,5.5]
for i in a:
    print(i)
    print (type(a))
    print(type(i))'''

#string
'''
a=["geetha","sidagam","chandu"]
for i in a:
    print(i)
    print (type(a))
    print(type(i))'''
#complex
'''
a=[2+3j,2+3j]
for i in a:
    print(i)
    print (type(a))
    print(type(i))'''

#bool
'''
a=[True,False]
for i in a:
    print(i)
    print (type(a))
    print(type(i))'''
'''
a={3,5.5,"geetha",2+3j,True,False}
for i in a:
    print(i)
    print (type(a))
    print(type(i))'''
'''
a={3,5.5,"geetha",2+3j,True,False}
print(a)
print(type(a))'''


####TASK on FOR loop
#input:["vij","hyd","vig"] output:['VIJ', 'HYD', 'VIG']
'''
a=["vij","hyd","vig"]
for i in a:
    print(i.upper(),end=" ")'''
''''
a=["vij","hyd","vig"]
b=str(a)
print(b.upper())'''


'''
a=["vij","hyd","vig"]
b=[]
for i in a:
    b.append(i.upper())
print(b)'''


############ WHILE LOOP  ##################
'''
a=10
while a>1:
    print(a)'''
'''
a=10
while a>1:
    print(a)
    a=a-1'''
'''
a=10
while a>=1:
    print(a)
    a=a-1'''
''''
a=10
while a>1:5
    print(a)
    a+=1'''
'''
a=10
while a>1:
    print(a)
    a-=1'''
'''
a=10
while a>1:
    a=a-1
    print(a)'''
'''   
a=10
while a>1:
    a=a-1
print(a)'''

##tasks on while ##
#bakery
'''
while True:
    price=int(input("enter the price:"))
    if price == 1200:
        print("Red velvet cake")
    elif price == 1000:
        print("choco almond cake")
    elif price == 800:
          print("chocolate cake")
    elif price == 600:
          print("butterscotch cake")
    else:
          print(" cake is not available")'''
# guests
'''
while True:
    names = ["Pooja", " Riya " , "Priya", "Noshad", "Satya"]
    name = input("Enter name of guest: ")
    if name in names:
        print(f" Welcome {name}")
    else:
        print("Welcome Guest")'''


###attendence tracker

'''
num = int(input("enter no.of students:"))
p = 0
a = 0
for i in range(1,num+1):
    status = input(f"num {i} p/a")
    if status == "p":
        p +=1
    elif status == "a":
        a += 1
    
print("no.of students:",num)
print("presentes:",p)
print("adsentes:",a)'''

#08-10-2026
#### RANGE ################
#The Range function returns a sequence of numbers, starting from 0 by default and increments my one by one and stops before a specified number
#we have to follow start-stop-step
'''for i in range(10):
    print(i)'''

'''for i in range(5,10):
    print(i)'''
'''for i in range(10):
    print(i,end=" ")'''
'''
for i in range(0,20,2):
    print(i,end=" ")
    

for i in range(5,50,5):
    print(i,end=" ")
    
for i in range(3,30,3):
    print(i,end=" ")'''


## tasks ##
### students marks ##
'''
while True:
    
    i =int(input("enter marks of the students:"))
    if i in range(91,101):
        print("Grade A")
    elif i in range(81,91):
        print("grade B")
    elif i in range(71,81):
        print("Grade C")
    elif i in range (51,71):
        print("Grade D")
    else:
        print("FAIL")'''

###Difference Between Break ,Continue and Pass
#The Break is used to terminate the entire loop
#The Continue statement is used to skip the current iteration and rest of the code will continue
#A pass is a null statement it does noting but syentatically we need.(IT IS A PLACE HOLDER)

##BREAK
'''
a=10
while a>1:
    print(a)
    a=a-1
    if a==6:
        break'''
'''
a=20
while a>1:
    a=a-1
    if a==6:
        break
    print(a)'''
'''
for i in range(25):
    if i==18:
        break
    print(i)'''

'''
a="python"
for i in a:
    if i=="h":
        break
    print(i)'''

##continue
'''
a=30
while a>10:
    a=a-1
    if a==20:
        continue
    print(a)'''
'''
for i in range (15):
    if i==10:
        continue
    print(i)'''

'''
a="python"
for i in a:
    if i=="o":
        continue
    print(i)'''

#pass

'''
for i in range(10):
    if i==5:
        pass
    print(i)'''

a=20
while a>5:
    print(a)
    a=a-1
    if a==10:
        pass
    

    
    
    
    
 
         
    
    










          






    
    

