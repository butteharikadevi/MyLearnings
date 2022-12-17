#1.Difference between is operator and == operator:
'''l1=[10,20,30,40]
l2=[10,20,30,40]
print('is:',l1 is l2)
print('== :',l1==l2)
l3=l1
print('is:',l1 is l3)
print('== :',l1==l3)'''

#2,ternary :
'''a=int(input("Enter first value: "))
b=int(input("Enter second value:"))
max=a if a>b else b
print("Maximum value is:",max)'''

'''a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
c=int(input("Enter Third value:"))
biggestValue=a if a>b and a>c else b if b>c else c
print(f'Biggest Value : {biggestValue}')'''

#mutable and immutable:
#mutable:list
'''print("Before Modification:",l)
l=[10,20,30,40]
print("Before modification:",id(l))
l[2]=7777
print("After modification:",l)
print("After modification:",id(l))'''
#immutable:tuple
'''l=(10,20,30,40)
print("Before modification:",id(l))
l[2]=7777
print("After modification:",l)
print("After modification:",id(l))'''

import sys
'''l=[10,20,30,40,50,60,70,80,90,100]
t=(10,20,30,40,50,60,70,80,90,100)
print("The size of List:",sys.getsizeof(l))
print("The size of tuple:",sys.getsizeof(t))'''

'''l1=[10,20,30,40,50,60,70,80,90,100]
l2=[10,20,30,40,50,60,70,80,90,100]
t1=(10,20,30,40,50,60,70,80,90,100)
t2=(10,20,30,40,50,60,70,80,90,100)
print(id(l1))
print(id(l2))
print(id(t1))
print(id(t2))'''

'''s={10,20,30,40,50}
s.add(60)
fs=frozenset(s)
fs.add(60)
print(s)
print(fs)'''

'''s='abcdefghij'
print(s[1:6:2])
print(s[7:4:-1])
print(s[::-1])'''
#*args vs *kwargs
'''def f1(*args):
    print(args)
f1()
f1(10)
f1(10,20)
f1(10,20,30)'''

'''def sum(*args):
    total=0
    for n in args:
        total=total+n
    print("the sum :",total)
sum()
sum(10)
sum(10,20)
sum(10,20,30)'''

#**kwargs:
'''def f1(**kwargs):
    print(kwargs)
f1(name='Harika',age=30,addr='Canada')'''

#dir() vs help():
'''import math
print(dir(math))'''

#help('math')
#help()
#help('keywords')

'''x=10
y=20
def f1():
    pass
print(dir())'''

#lambda function:

'''s=lambda n:n*n
print("square of 4 :",s(4))'''

#filter fun:
'''l1=[0,5,10,15,20,25,30]
l2=list(filter(lambda x:x%2==0,l1))
print(l2)'''
#map fun:
'''l1=[1,2,3,4]
l2=list(map(lambda x:x*2,l1))
print(l2)'''
'''l1=[1,2]
l2=[3,4,5]
l3=list(map(lambda x,y:x+y,l1,l2))
print(l3)'''
#reduce fun:
'''from functools import  *
l1=[10,20,30,40]
l2=reduce(lambda x,y:x+y,l1)
l3=reduce(lambda x,y:x*y,l1)
print(l2)
print(l3)'''
#print without newline
'''print('HI...',end='')
print('Harika...')'''

#help('keywords')

#reverse string using for loop:

'''def reverse(s):
    result=""
    for i in s:
        result=i+result
    #print(result)
    return result
s='Harika'
print(reverse(s))'''
#reverse string using reversed() fun:

'''s='HARIKA'
result="".join(reversed(s))
print((result))'''

#reverse string using slice operator:
'''s="HARIKA"
print(s[::-1])'''

#program 1:
#sum of n numbers:
'''n=10
sum=0
for i in range(1,11):
    sum=i+sum
print("The sum of n values:",sum)'''

#fibonacci series using generator:
'''def fib_gen():
    a=0
    b=1
    while True:
        c=a
        a=b
        b=c+a
        yield c
f=fib_gen()
for i in range(20):
    print(next(f),end=' ')'''


#How to reverse a list using slice:
'''l=[1,2,3,4,5]
l2=l[::-1]
print(l2)'''

#How to reverse a list using reverse fun:
'''l=[1,2,3,4,5]
l.reverse()
print(l)'''
#How to reverse a list using reversed() fun:
'''l=[1,2,3,4,5]
l2=list(reversed(l))
print(l2)'''
#How to reverse a list using loop:
'''l1=[1,2,3,4,5]
l2=[]
for i in range(len(l1)-1,-1,-1):
    l2.append(l1[i])
print(l2)'''
#HWP to get current system date and time:
'''import datetime
today=datetime.datetime.now()
print(today.strftime("%y-%m-%d %H:%M:%S"))
#print(datetime.datetime.now())'''


#WAP to Remove duplicates from a list:
#using set function:
'''l1=[1,4,2,5,2,3,4,1,4,5,2,3]
l2=list(set(l1))
print(l2)'''
#using array:
'''l1=[1,4,2,5,2,3,4,1,4,5,2,3]
arr=[]
for i in l1:
    if i not in arr:
        arr.append(i)
print(arr)'''
#using lambda fun:
'''l1=[1,4,2,5,2,3,4,1,4,5,2,3]
re_dup_fun=lambda l1:set(l1)
print(re_dup_fun(l1))'''
#WAP to delete duplicates from dictionary:
'''dict1={'fruits':['Apple',"Banana",'Apple','Banana'],
       'Veg_tab':['tomato','potato','tomato','potato']}
dict2={}
for key,value in dict1.items():
    dict2[key]=set(value)
print((dict2))'''

#symmetric difference:
'''s1={1,2,3,4,5}
s2={3,4,5,6,7}
s3=s1.symmetric_difference(s2)
print(s3)'''

#how can we merge one dictionary with other:
#1
'''d1={1:"Apple",2:"Banana"}
d2={3:'Mango',4:'orange'}
d1.update(d2)
print(d1)'''
#2
'''d1={1:"Apple",2:"Banana"}
d2={3:'Mango',4:'orange'}
d3={**d1,**d2}
print(d3)'''

'''fp=open("C:/Users/Admin/Documents/textfile.txt",'r')
data=fp.read()
print(data)
words=data.split(" ")
dict1={}
for word in words:
    if word not in dict1.keys():
        dict1[word]=1
    else:
        value = dict1[word]+1
        dict1[word] = value
print(dict1)'''
from collections import *
'''fp=open("C:/Users/Admin/Documents/textfile.txt",'r')
data=fp.read()
print(data)
lines=data.split()
dict1={}
for line in lines:
    words=line.split()
    for word in words:
        if word not in dict1.keys():
            dict1[word]=1
        else:
            value=dict1[word]+1
            dict1[word]=value
print(dict1)
dict2 = dict(sorted(dict1.items()))
print(dict2)
dict3= dict(sorted(dict1.items(), key=lambda item: item[1],  reverse=True))
print(dict3)'''

'''l1=[1,2,3]
l2=['hh','gg','rr']
result=dict(zip(l1,l2))
print(result )'''

'''def freq_words():
    str=input("Enter your string: ")
    words=str.split(' ')
    print(words)
    d={}
    for word in words:
        if word not in d.keys():
            d[word]=1
        else:
            d[word]=d[word]+1
    print(d)
freq_words()'''
#program to find first non repeated index:
'''def first_non_rep(str1):
     dict1={}
     size=len(str1)
     for i in range(size):
         key=str1[i]
         if key not in dict1:
             dict1[key]=1
         else:
             dict1[key]=dict1[key]+1

     for index in range(size):
         if(dict1[str1[index]]==1):
             return str1[index],index
print(first_non_rep('ababca'))'''

#program to find max and minimum value in a list:

'''l1=[1,23,14,36,72]
max=l1[0]
min=l1[0]

size=len(l1)
for i in range(size):
    if l1[i]>max:
        max=l1[i]
    if l1[i]<min:
        min=l1[i]

print('Maximum value:',max)
print('Minium value:',min)'''

'''l1=input("enter your list:").split(",")
max=l1[0]
min=l1[0]
for i in l1:
    if i>max:
        max=i
    if i<min:
        min=i
print('max val:',max)
print('MIn val:',min)'''

'''def sub_str(s1,n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(s1[i:j])
s1='HARIKA'
n=len(s1)
sub_str(s1,n)'''
#program to check given number is prime or not:
'''number=int(input("Enter your number:"))
if number>1:
    for i in range(2,number):
        if (number%i)==0:
            print(number,"is not a prime number")
            break
    else:
        print(number,"is a prime number")
else:
    print(number,"is not a prime number")'''

'''l=["Harika","Ganesh","Ruthu"]
sear_ele="Ruthu"
size=len(l)
isItemFound = False
for i in range(size):
    if l[i]=="Ruthu":
        isItemFound = True
if(isItemFound):
    print('Your search item {} is at index {}'.format(sear_ele, i))
else:
    print('iteam is not found')'''

'''import requests
city='Hyderabad'
url='https://samples.openweathermap.org/data/2.5/weather?q=London&mode=html&appid=b6907d289e10d714a6e88b30761fae22'
res=requests.get(url)
print(res)'''

'''l=[10,2,3,4,5,12]
l2=list(filter(lambda x:x%2==0,l))
print(l2)
l3=list(filter(lambda x:x%2!=0,l))
print(l3)'''

print("Harika"+"Ganesh"+"Ruthu ")