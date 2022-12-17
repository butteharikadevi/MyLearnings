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

s='mississippi'
d={}
for e in s:
    if e in d:
        d[e]=d[e]+1
    else:
        d[e]=1
print(d)
