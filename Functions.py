# FUNCTION---
#1) function is a block of organized,reusable code and that is used to perform a single or multiple tasks
#2) python gives in built func like print or u can make ur own functions and these are called user defined func
#3) func block begins with a def follwed by a func name and paranthesis(())---a,b are arguments 10,20 are parameters

'''a=10
b=20
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=100
b=200
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)

a=1000
b=2000
print("the sum is",a+b)
print("the diff is",a-b)
print("the product is",a*b)'''

#func
'''def calculate(a,b):
    print("the sum is",a+b)
    print("the diff is",a-b)
    print("the product is",a*b)
calculate(10,20)
calculate(100,200)
calculate(1000,2000)'''

#pow **
#modulus %
#int division //

'''def cal(a,b):
    print("the pow is",a**b)
    print("the modulus is",a%b)
    print("the intdiv is",a//b)
cal(2,5)
cal(10,2)'''

'''def add(a,b):
    c=a+b
    print(c)
add(7,8)'''

'''def add():
    a=int(input())
    b=int(input())
    print(a+b)
add()'''

#fullname
'''def fullname():
    fname=input("enter fname")
    lname=input("enter lname")
    print((fname+" "+lname).title())
fullname()'''

#diff b/w print and return
#print just shows human user o/p in a console
#return is used to terminate the func gives back value from a func

'''def sub(a,b):
    print(a-b)
sub(4,8)'''

'''def sub(a,b):
    return a-b
sub(4,8)'''# no o/p is shown we need print to show


'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    print(c)
    print(d)
    print(e)
cal(5,2)'''

'''def cal(a,b):
    c=a+b
    d=a-b
    e=a*b
    #return c
    #return d
    #return e
    return c,d,e #we need to give in 1 line

print(cal(5,2))'''



##TASK----
'''while True:
    def cal():
        a=int(input("enter a value"))
        b=int(input("enter b value"))
        option=int(input("choose:\n1.Add\n2.Sub\n3.Mul"))
        if option==1:
            print(a+b)
        elif option==2:
            print(a-b)
        elif option==3:
            print(a*b)
        else:
            print("Invalid Option")
    cal()'''
#another method
'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("enter a value"))
    b=int(input("enter b value"))
    option=int(input("choose:\n1.Add\n2.Sub\n3.Mul"))
    if option==1:
        add()
    elif option==2:
        sub()
    elif mul():
        mul()
    else:
        print("Invalid Option")'''
                
        
        
        
                

    
            

        







