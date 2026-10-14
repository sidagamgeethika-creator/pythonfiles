##List Comprehension--
#every list comp can be re-written as a for loop but every for loop cannot be re-written in list comp
'''a=["python","dsa","java"]'''
#['PYTHON','DSA','JAVA']
#print(a.upper())-----#error

'''b=str(a)
print(b.upper())'''

'''for i in a:
    print(i.upper(),end=",")'''
######---SYNTAX----####
#a=[expression for variable in collection/range
'''b=[i.upper() for i in a]
print(b)'''



#TASK----
'''a=["hyd","vja","vzg"]
b=[i.capitalize() for i in a]
print(b)'''


'''a=[1,3,4,5,6,8,12,13]
b=[i*i for i in a]--#1 
b=[i**2 for i in a]--#2
b=[pow(i,2) for i in a]-#3
print(b)'''


'''b=[i for i in range(21)]
print(b)'''

# using conditions--- no elif is used in list comp
#if
'''b=[i for i in range(16) if i%2==0]
print(b)--#even num'''

'''b=[i*i for i in range(16) if i%2==0]
print(b)--#even num squares'''

'''a=["apple","kiwi","grapes","mango","dragon","berry"]
b=[i for i in a if "a" in i]
print(b)'''

'''a=["apple","kiwi","grapes","mango","dragon","berry"]
b=[i for i in a if "a" not in i]
print(b)'''

#if-else
'''a=[i*i if i%2==0 else i*5 for i in range(31)]
print(a)'''


'''a=[1,2,3,4,5]
b=[5,4,3,2,1]'''
#[6,6,6,6,6,6]

'''c=[a[i]+b[i] for i in range(len(a))]
print(c)'''

'''c=[a[i]+b[i] for i in range(5)]
print(c)'''

#Bulit in--max(),min(),sum()

'''print(max(7,10,20,49,58,67))
print(min(7,10,20,49,58,67))'''


'''a=7,10,20,49,58,67
print(max(a))
print(min(a))
print(sum(a))'''


#TASK----Marks Analysis Report
student=int(input("enter total students"))
marks=[]----#list is taken here to store data
for i in range(1,student+1):
    mark = int(input(f"Enter marks for student {i}: "))
    marks.append(mark)

print("-----Marks Analysis Report-----")    
print("Maximum Marks",max(marks))
print("Minimum Marks",min(marks))
print("Sum",sum(marks))
print("Average",sum(marks)/student)
    















   
