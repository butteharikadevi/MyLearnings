#for 2 numbers:
'''x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
if x>y:
    print("The biggest number amoung {} and {} is {}".format(x,y,x))
else:
    print("The biggest number amoung {} and {} is {}".format(x, y, y))'''

#for 3 numbers:
'''x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
if x>y and x>z:
    print("Amoung {},{} and {} {} is biggest".format(x,y,z,x))
elif y>x and y>z:
    print("Amoung {},{} and {} {} is biggest".format(x,y,z,y))
else:
    print("Amoung {},{} and {} {} is biggest".format(x,y,z,z))'''
#program to find given number is even or odd:
'''x=int(input("Enter your number : "))
if x%2==0:
    print("the number {} is even".format(x))
else:
    print("the number {} is odd".format(x))'''

'''x=int(input("Enter your number : "))
if 1<x<100:
    print("The given number {} is in between 1 to 100".format(x))
else:
    print("The given number {} is out of 1 to 100".format(x))'''

#find the sum of 1st n numbers:
#using for loop

'''n=int(input("Enter value of n:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)'''

#using while loop:

'''n=int(input("Enter value of n:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
print(sum)'''

'''i=0
while True:
    i=i+1
    print("hello")'''


'''n=int(input('Enter value for n:'))
for i in range(n+1):
    for j in range(i):
        print('*',end=' ')
    print()'''
'''n=int(input("Enter no of rows:"))
for i in range(n):
    print('R'*n)'''
'''n=int(input("Enter no of rows:"))
for i in range(n):
    print("Ruthu Ganesh Harika "*n)'''

'''n=int(input("enter n value:"))
for i in range(n):
    for j in range(n):
        print("$",end=' ')
    print()'''
'''n=int(input("enter no of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print('@',end=" ")
    print()'''
'''n=int(input("enter no of rows:"))
for i in range(n):
    print("RUTHU  "*n)'''

''''n=int(input("Enter no of rows:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=' ')
    print()'''

'''srt=input("Enter your string:")

size=len(srt)
for i in range(size):
    print("The character {} is at index {}".format(srt[i],i))
print("Length of srt is",size)'''

#WAP to access each character of a string in forward and backward dir:

'''s=input("Enter your string:")
print("The Forward dir is :",s[::])
print("The Backward dir is :",s[::-1])'''

#using while loop:
'''s=input("Enter your string:")
n=len(s)
i=0
print("Data in forward direction:")
while i<n:
    print(s[i],end=' ')
    i=i+1
print()
i=-1
print("Data in backward direction:")
while i>=-n:
    print(s[i],end=' ')
    i=i-1'''
'''s=input("Enter your string:")
n=len(s)
i=0
print("Data in forward direction")
while i<n:
    print(s[i],end=' ')
    i=i+1
print()
i=-1
print("Data in Backward direction")
while i>=-n:
    print(s[i],end=' ')
    i=i-1'''

'''s=input("Enter your string:")
l=[]
size=len(s)
i=0
for i in range(size):
    if s[i] not in l:
        l.append(s[i])
print(l)'''

'''s=input("Enter your string:")
st=set()
size=len(s)
i=0
for i in range(size):
    st.add(s[i])
print(st)'''

'''s1='HARIKA'
s2='RUTHU'
print(s1,s2)
del s1
print(s1)
print(s2)'''
#HARIKA
'''s=input("Enter your string:")
d={}
for ele in s:
   if ele in d:
       d[ele]=d[ele]+1
   else:
       d[ele]=1

print(d)'''

'''s='mississippi'
d={}
for e in s:
    if e in d:
        d[e]=d[e]+1
    else:
        d[e]=1
print(d)'''

'''s="harika Devi"
subs="Devi"
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    else:
        print("found at index",pos)
        flag=True
    if flag == True:
        for i in range(pos, pos + len(subs)):
            print(i)
if flag==False:
    print("substr not found")'''

'''def is_even(eleList):
    count=0
    flag=False
    for i in eleList:
        if i%2==0:
            flag=True
            count=count+1
    return flag,count
l=is_even([11,12,13,14,15])
print(l)
print(is_even([11,13,15,17]))'''

'''s='ABABABAB'
print(s)
print(id(s))
s=s.replace('A','B')
print(s)
print(id(s))'''

'''s="HArika Ruhtu Ganesh"
l=s.split()
print(l)
for i in l:
    print(i)'''
'''s="Durga software Solutions hyd  telangana India "
l=s.split(" ",3)
print(l)
for i in l:
    print(i)'''

'''l=['Harika','Ganesh','Ruthu']
s=' *'.join(l)
print(s)'''
'''s='ruthwik sai srinivas ankam'
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())'''

'''s='RuThu'
print(s.swapcase())'''

#Reverse string:
#1.slice:
'''s='HARIKA'
print(s[::-1])'''
#2.reverse ():
'''s='HARIKA'
rs=''.join(reversed(s))
print(rs)'''
#for loop:
'''def Reverse(s):
    reverse=' '
    for i in s:
        reverse=i+reverse
    return reverse
s="Ruhtu"
print(Reverse(s))'''

'''s="RUTHU"
rs=''
for i in s:
    rs=i+rs
print(rs)'''

'''s="Durga software solutions"
l=s.split()
print(l)
for i in l[::-1]:
    print(i,end=' ')'''

'''s="Durga software solutions"
l=s.split()
ns=''
for i in l:
    x=i[::-1]
    ns=ns+x+' '
print(ns)'''

'''s="HARIKA"
el=[]
ol=[]
for i in range(len(s)):
    if i%2==0:
        el.append(s[i])
    else:
        ol.append(s[i])
print('Even index char:',el)
print('Odd index char:',ol)'''

'''s='B4A1D3'
al=''
nl=''
for i in s:
    if i.isalpha():
        al=i+al
    else:
        nl=i+nl
x=sorted(al)+sorted(nl)
output=''.join(x)
print(output)'''

'''s='a4b3c2'
res=''
for i in range(0,len(s)-1,2):
    alpha = s[i]
    digit = s[i+1]
    result = alpha*int(digit)
    res = res+result
print(res)'''

'''s='A2B3c4D5'
res=''
for i in range(0,len(s)-1,2):
    alp=s[i]
    dig=s[i+1]
    res=res+(alp*int(dig))
print(res)'''

#list:
#functions and methods in list:
#1.len() fun:,count(),index method():
'''l=[1,12,13,12,12,12,14]
print(len(l))
print(l.count(12))
print(l.index(14))'''
#to add all elements to list up to 100 which are divisible by 10:
#l.append(element):
'''l=[]
for i in range(1,101):
    if i%10==0:
        l.append(i)
print(l)'''
#l.insert(index,element):
'''l=[1,12,13,12,12,12,14]
l.insert(1,222)
print(l)'''
#extended() method:
'''l1=[1,2,3]
l2='HARIKA'
l1.extend(l2)
print(l1)
print(l2)
l1.append("HARIKA")
print(l1)
l1.remove("HARIKA")
print(l1)
print(l1.pop())
print(l1.pop(0))'''
#reverse () method:
'''l1=[1,2,34,5]
l1.reverse()
print(l1)'''
#sort() method:
'''l1=[2,10,4,5,9,6]
l1.sort()
print(l1)'''
'''l1=["HARIKA","Ganesh","Ruthu"]
l1.sort()
print(l1)'''
#aliasing:
'''x=[10,20,30]
y=x
print(id(x))
print(id(y))
print(x is y)
y[1]=111
print(y)
print(x)'''
'''import copy
class Emp:
    def __init__(self,ename,eno):
        self.ename=ename
        self.eno=eno
e1=Emp('HArika',100)
e2=Emp("Ganesh",200)
ori_List=[e1,e2]
dup_List=copy.deepcopy(ori_List)
e3=dup_List[0]
e3.ename='Butte harika'
print(ori_List[0].ename)'''

#cloning:
#using slice ope:
'''x=[10,20,30,40]
y=x[:]
print(id(x))
print(id(y))
y[1]=222
print(x)
print(y)'''
#using copy() fun:
'''x=[10,20,30,40]
y=x.copy()
print(id(x))
print(id(y))
y[1]=999
print(x)
print(y)'''

'''l1=[1,2,3]
l2=[4,5,6]
print(l1+l2)'''
'''l1=[1,2,3]
print(l1*2)'''
'''l1=[1,2,3,4,5]
l1.reverse()
print(l1)'''
'''l1=[20,10,50,90,30]
l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l1.clear()
print(l1)'''

#print squares of 1st 10 numbers:
'''l=[]
for i in range(1,11):
    l.append(i*i)
print(l)'''
#using comprehension;
'''l=[i*i for i in range(1,11)]
print(l)'''
#1st 10 even numbers :
'''l=[i*i for i in range(1,11)]
l2=[x for x in l if x%2==0]
print(l)
print(l2)
l3=[x for x in range(1,11) if x%2==0]
print(l3)'''
'''vowels=['a','e','i','o','u','A','E','I','O','U']
str=input("enter your word: ")
found=[]
for i in str:
    if i in vowels:
        if i not in found:
            found.append(i)
print("vowels in word {} is {}".format(str,found))
print("no.of vowels in {} are {}".format(str,len(found)))'''

'''l=[1,2,3]
l1=[1,2,3,4]
l.extend(l1)
print(l)
l.reverse()'''

'''l=[10,20,30]
t=tuple(l)
print(t)
print(type(t))'''
#t1=(10,20,30,40,20)
#print(len(t1))
#print(t1[0])
#print(t1.index(20))
#print(t1.count(20))
#print(sorted(t1))

'''t1=(11,17,18,20,9,5)
print(sorted(t1,reverse=True))'''

'''w=input("Enter your word:")
s=[]
v=['a','e','i','o','u']
for ele in w:
    if ele in v:
        s.append(ele)
print(s)
print("no of vowels in w:",len(s))'''

rec={}
n=int(input("Enter No.of Student:"))
i=1
while i<=n:
    name=input("Enter student Name:")
    marks=input("Enter % Marks of student:")
    rec[name]=marks
    i=i+1
print("Name of Student","\t","% marks")
for x in rec:
    print('\t',x,'\t\t','\t',rec[x])

