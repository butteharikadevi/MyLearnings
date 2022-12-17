'''import sys
class Customer:
    Bankname='SBI'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print("Balance amount after deposit is",self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print("Insufficient Funds .....can't perform withdraw operation...")
            sys.exit()
        self.balance=self.balance-amt
        print("Avilable balance after withdraw is : ",self.balance)
print("Welcome to",Customer.Bankname)
name=input("Enter your Name :")
c=Customer(name)
while True:
    print('d-deposit \nw-withdraw \ne-exit')
    option=input("Enter your option : ")
    if option=='d' or option=='D':
        amt=float(input("Enter Your amount : "))
        c.deposit(amt)
    elif option=='w' or option=='W':
        amt = float(input("Enter Your amount : "))
        c.withdraw(amt)
    elif option=='e' or option=='E':
        print("Thanks for Banking....")
        sys.exit()
    else:
        print(" Invalid option...Please enter valid option...")'''
import re
import sys
import time

'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print('HI',self.name)
        print('Your Marks are : ',self.marks)
    def grade(self):
        if self.marks>=60:
            print('You got 1st Grade')
        elif self.marks>=50:
            print('You got 2nd Grade')
        elif self.marks>=35:
            print('You got 3rd Grade')
        else:
            print('You are Failed')
n=int(input("Enter number of Students : "))
for i in range(n):
    name=input("Enter Student name : ")
    marks=int(input("Enter student Marks :"))
    s=Student(name,marks)
    s.display()
    s.grade()'''

'''class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("Enter No.of Students : "))
for i in range(n):
    s=Student()
    name=input("Enter student name : ")
    s.setName(name)
    marks=int(input("Enter marks of student : "))
    s.setMarks(marks)
    print('Hi ',s.getName())
    print('Your Mark are :',s.getMarks())
    print()'''

'''class Animal:
    legs=4
    @classmethod
    def walk(cls,name):
        print("{} walk with {} legs...".format(name,cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')'''

#IMP Program in Interview room:
'''class Test:
    count=0
    def __init__(selfs):
        Test.count +=1
    @classmethod
    def noOfObjects(cls):
        print("No of Objects created Are :",cls.count)
t1=Test()
t2=Test()
t5=Test()
t4=Test()
t3=Test()
Test.noOfObjects()'''

#or

'''class Test:
    count=0
    def __init__(self):
        Test.count+=1

    def noOfObj():
        print("No of Objects Created : ",Test.count)
t1=Test()
t2=Test()
t3=Test()
Test.noOfObj()'''


#Static Method example:

'''class Math:
    @staticmethod
    def sum(x,y):
        print("The Sum is :",x+y)

    @staticmethod
    def product(x,y):
        print("The product is :",x*y)

    @staticmethod
    def average(x,y):
        print("The average is : ",(x+y)/2)

Math.sum(30,20)
Math.product(30,20)
Math.average(30,20)'''

'''class Employee:
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal

    def Display(self):
        print('Employee number :',self.eno)
        print('Employee name :',self.ename)
        print('Employee salary :',self.esal)

class Test:
    def Modiify(emp):
        emp.esal=emp.esal+1000
        emp.ename = "Mrs: "+emp.ename
        emp.Display()
e=Employee(1,"aaaa",10000)
Test.Modiify(e)'''

'''class Outer:
    def m1(self):
        print("Outer class method")
    class Inner:
        def m2(self):
            print("Inner class method")
o=Outer()
o.m1()
i=o.Inner()
i.m2()'''


'''class Person:
    def __init__(self):
        print('Person class constructor')
        self.name='Harika'
        self.db=self.Dob()

    def display(self):
        print('Name :',self.name)
    class Dob:
        def __init__(self):
            print('Dob class Constructor')
            self.dd=28
            self.mm=8
            self.yy=1990
        def display(self):
            print('Dob is {}/{}/{}'.format(self.dd,self.mm,self.yy))
p=Person()
p.display()
p.db.display()'''

'''import sys
class Employee:
    def __init__(self,ename,eno,edb,edepno):
        self.ename=ename
        self.eno=eno
        self.edb=edb
        self.edepno=edepno
    def Display(self):
        print('Employee Name is :',self.ename)
        print("Employee No is :",self.eno)
        print("Employee DOB is :",self.edb)
        print("Employee Dep No is:",self.edepno)
    def addEmployee():
        ename = input("Enter emp name : ")
        eno = int(input("enter emp no :"))
        edb = input("enter emp dob :")
        edepno = int(input("Enter emp dep no : "))
        e = Employee(ename, eno, edb, edepno)
        return e
    def FindEmp(empList,eid):
        for emp in empList:
            if eid==emp.eno:
                emp.Display()


empList = []

print("Welcome to Employee management applicaiton \n Please choose your option \n ")
while True:
    option = int(input("1 for Add employee \n2 for Display employees \n3 for find Employee \n4 for exit"))
    if option == 1:
        e = Employee.addEmployee()
        empList.append(e)
    elif option == 2:
        for emp in empList:
            emp.Display()
    elif option==3:
        empno=int(input("Enter employee number: "))
        Employee.FindEmp(empList,empno)

    elif option==4:
        sys.exit()

    else:
        print('please enter valid option')'''

'''class Human:
    def __init__(self):
        self.name='Harika'
        self.head=self.Head()
        self.brain=self.Brain()
    def display(self):
        print('Hello',self.name)

    class Head:
        def talk(self):
            print('Talking.....')
    class Brain:
        def think(self):
            print('Thinking....')
h=Human()
h.display()
h.head.talk()
h.brain.think()'''
'''import time
class Test:
    def __init__(self):
        print("Object initilization...")
    def __del__(self):
        print("Fulfilling last wish and perform cleanup activities...")
t1=Test()
t2=t1
t3=t2
del t1
time.sleep(5)
print('End of Application')'''
'''import time
class Test:
    def __init__(self):
        print("Constructor Execution")
    def __del__(self):
        print("Destructor Execution")
t1=Test()
del t1
time.sleep(5)
print('END')'''

'''import time
class Test:
    def __init__(self):
        print("Constructor Execution....")
    def __del__(self):
        print("Destructor Execution....")
t1=Test()
t2=t1
t3=t2
del t1
time.sleep(10)
print("Object not yet Destroyed after deleting t1...")
del t2
time.sleep(10)
print("Object not yet Destroyed after deletiong t2...")
print("I am trying to delete t3 also..")
del t3'''

'''class Test:
    def __init__(self):
        print("constructor Execution")
    def __del__(self):
        print("Destructor Execution")
l1=[Test(),Test(),Test()]
time.sleep(5)
del l1
 time.sleep(7)
print("End of Application...")'''

'''import sys
class Test:
    pass
t1=Test()
t2=t1
t3=t1
t4=t1
del t1
print(sys.getrefcount(t2))'''

'''class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color

    def getinfo(self):
        print("Car Name :{} ,Model :{},color : {}".format(self.name,self.model,self.color))

class Employee:
    def __init__(self,ename,eno,car):
        self.ename=ename
        self.eno=eno
        self.car=car

    def empinfo(self):
        print("Employee name :",self.ename)
        print("Employee Number :",self.eno)
        print("Car Info:")
        self.car.getinfo()
c=Car('Innova','2010X','Red')
e=Employee('Harika',100,c)
e.empinfo()'''

'''class X:
    a=10
class Y(X):
    pass
y=Y()
print(y.a)'''

'''class X:
    a=10
    def __init__(self):
         self.b=888
        print("Constructor....")
    def m1(self):
        print("Parent class Instance Method...")
    @classmethod
    def m2(cls):
        print("Parent class class method")
    @staticmethod
    def m3():
        print("Parent class Static Method")
class Y(X):
    a=7777
    def __init__(self):
        print("Child class constructor...")
y=Y()
print(y.a)
y.m1()
y.m2()
y.m3()'''

'''class X:
    a=10
    def __init__(selfs):
        print("Parent class constructor....")
    def m1(self):
        print(" parent class Instance Method...")
    @classmethod
    def m2(cls):
        print("Parent class method...")
    @staticmethod
    def m3():
        print("parent static method...")'''
'''class Y(X):
    a=777
    def __init__(selfs):
        super().__init__()
        print("child class constructor....")
        print(super().a)
        print(Y.a)

    def m1(self):
        super().m1()
        print("child class Instance Method...")
    @classmethod
    def m2(cls):
        print("child class method...")
    @staticmethod
    def m3():
        print("child static method...")

y=Y()
y.m1()
y.m2()
y.m3()'''

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def EatNDrink(self):
        print("Biryani Eating and 7up Drinking...")
class SE(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def Work(self):
        print("Python coding is like Drinking chilled Drink..")
s=SE('Harika',30,100,10000)
print(s.name,s.age,s.eno,s.esal)'''

'''class A:
    def m1(self):
        self.x=10
class B(A):
    def m1(self):
        super().m1()
        self.a=20
    def disp(self):
        print(self.a)
        print(self.x)


b=B()
b.m1()
b.disp()'''

'''class P:
    def __init__(self):
        self.a=10
class C(P):
    def __init__(self):
        super().__init__()
        self.a=20

        print(self.a)
c=C()'''

'''class P:
    a=10
    def __init__(self):
        self.b=20
    

p1=P()
p2=P()
print(p1.a,p1.b,p2.a,p2.b)'''

#1.SINGLE inheritance:

'''class P:
    def m1(self):
        print("parent class method")
class C(P):
    def m2(self):
        print("child class method")
c=C()
c.m1()
c.m2()'''

#Multilevel inheritance:
'''class GF:
    def m1(self):
        print('Land')
class F(GF):
    def m2(self):
        print('cash')
class U(F):
    def m3(self):
        print("Enjoy......")
u=U()
u.m1()
u.m2()
u.m3()'''

#Hierarchical inheritance:

'''class P:
    def m1(self):
        print('Parent...')
class C1(P):
    def m2(self):
        print('Child1...')
class C2(P):
    def m3(self):
        print('Child2...')
c1=C1()
c1.m1()
c1.m2()
c2=C2()
c2.m1()
c2.m3()'''
'''import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for match in matcher:
    count+=1
    print("Match is available at start index :",match.start())
print("the no of occurrences:",count)'''
'''import re
count=0
pattern=re.compile('bb')
matcher=pattern.finditer('abaababa')
for match in matcher:
    count=count+1
    print("match is  available at start index : ",match.start())
print("No of occurrences :",count)'''

'''import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for m in matcher:
    count+=1
    print("start : {},end : {},group : {}".format(m.start(),m.end(),m.group()))
print("The No of Occurrences :",count)'''
'''import re
count=0
matcher=re.finditer('ab','abaababa')
for m in matcher:
    count=count+1
    print('Start : {},end : {},group :{}'.format(m.start(),m.end(),m.group()))
print("The No of Occurrences",count)'''


'''import re
matcher=re.finditer('[abc]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('[^abc]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('[a-z]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('[0-9]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('[a-zA-Z0-9]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('[^a-zA-Z0-9]','a7b@k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('\s','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('\S','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('\d','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('\D','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('\w','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('\W','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('.','a7b @k9z')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('a','abaabaaab')
for m in matcher:
    print(m.start(),'....',m.group())'''


'''import re
matcher=re.finditer('a+','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('a*','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('a?','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('a{3}','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('a{2,3}','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('a{1,3}','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''
'''import re
matcher=re.finditer('[ ^a]','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
matcher=re.finditer('^a','abaabaaab')
for m in matcher:
    print(m.start(),'.....',m.group())'''


'''import re
matcher=re.finditer('a$','abaabaaaa')
for m in matcher:
    print(m.start(),'.....',m.group())'''

'''import re
s=input("Enter pattern to check: ")
m=re.match(s,'abcdefghij')
if m!=None:
    print("Match is available at the beginning of the string")
    print("Start Index :{} and end Index :{}".format(m.start(),m.end()))
else:
    print("match is not available at the begnning of the string")'''
'''import re
s=input("enter pattern to check : ")
m=re.fullmatch(s,'abcdefghij')
if m!=None:
    print("Full string Matched ")
else:
    print("Full String not Matched")'''

'''import re
s=input("Enter target string..:")
m=re.search(s,'abaabaaab')
if m!=None:
    print("Match is available...")
    print("First occurrence at start index {} and end Index {} ".format(m.start(),m.end()))
else:
    print("Match is not available...")'''

'''import re
l=re.findall('[0-9]','a7b6k9z')
print(l)'''

'''l=re.findall('[a-z]','a2bc37z')
print(l)'''

'''l=re.findall('\W','@adc#gf$ mn*')
print(l)'''
'''import re
matcher=re.finditer('ab','abcdaabaab')
for m in matcher:
    print(m.start(),m.end(),m.group())'''
'''import re
matcher=re.finditer('\d','ab3f5@nn&')
for m in matcher:
    print(m.start(),m.end(),m.group())'''
'''import re
s=re.sub('\d','****','a1b2c3d4')
print(s)'''
'''import re
t=re.subn('\d','***','a2b3c4d5e10')
print("The result of String after replacing",t[0])
print("the No of replacements :",t[1])'''
'''import re
l=re.split('-','28-08-1990')
print(l)'''
'''import re
l=re.split('\.','www.butte.harika.com')
print(l)
for i in l:
    print(i)'''
'''import re
s='learning pythos is very Easy..'
res=re.search('^learn',s)
if res!=None:
    print("Target string starts with Learn")
else:
    print("Target string not starts with Learn")'''

'''import re
s='Learning python is very easy'
res=re.search('easy$',s)
if res!=None:
    print("Target  string Ends with easy")
else:
    print("Target string not ends with easy")'''

'''import re
s='Learning python is very easy'
res=re.search('Easy$',s,re.IGNORECASE)
if res!=None:
    print("Target  string Ends with easy")
else:
    print("Target string not ends with easy")'''
'''import re
s=input("Enter Identifier to validate : ")
m=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if m!=None:
    print(s,'is a valid Identifier ')
else:
    print(s,'is not a valid Identifier')'''

'''import re
s=input('Emnter Mobile Number to validate:')
m=re.fullmatch('[6-9]\d{9}',s)
if m!=None:
    print(s,'is the valid mobile  number')
else:
    print(s,"is the invalid mobile  number")'''
'''import re
s=input('Enter mobile number for validate:')
if len(s)==10:
    m=re.fullmatch('[6-9]\d{9]',s)
elif len(s)==11:
    m=re.fullmatch('[0][6-9]\d{9}',s)
elif len(s)==12:
    m=re.fullmatch('[9][1][0][6-9]\d{9}')
elif len(s)==13:
    m=re.fullmatch('[+][9][1][6-9]\d{9}',s)
if m!=None:
    print(s,'is the valid mobile  number')
else:
    print(s,"is the invalid mobile  number")'''

'''import re
f1=open('C:\\Users\\Admin\\Documents\\Python regx\\newfilemobnum.txt','r')
f2=open('C:\\Users\\Admin\\Documents\\Python regx\\output.txt','w')
for line in f1:
    list1=re.findall('[6-9]\d{9}',line)
    for number in list1:
        f2.write(number+'\n')
    list2=re.findall('[0][6-9]\d{9}',line)
    for number in list2:
        f2.write(number+'\n')
print("Extract numbers from newfilemobnum into output file")
f1.close()
f2.close()'''
'''import re,urllib
import urllib.request
sites=['http://google.com','http://rediff.com']
for s in sites:
    print('Searching....',s)
    u=urllib.request.urlopen(s)
    text=u.read()
    title=re.findall("<title>.*</title>",str(text),re.IGNORECASE)
    print(title[0])'''

'''import re,urllib
import urllib.request
u=urllib.request.urlopen("https://www.redbus.in/info/contactus")
text=u.read()
numbers=re.findall('[+][9][1][0-9]{10}',str(text))
for n in numbers:
    print(n)'''

'''import re
s=input("Enter mail Id to check for Validation : ")
m=re.fullmatch('\w[a-zA-z0-9._]*@gmail[.]com',s)
if m!=None:
    print("Given Mail Id is valid one")
else:
    print("Given mail id is invalid one")'''


'''import re
s=input("Enter mail Id to check for Validation : ")
m=re.fullmatch('\w[a-zA-z0-9._]*@[a-z0-9]+[.][a-z]+',s)
if m!=None:
    print("Given Mail Id is valid one")
else:
    print("Given mail id is invalid one")'''

'''import re
s=input("Enter mail Id to check for Validation : ")
m=re.fullmatch('\w[a-zA-z0-9._]*@(gmail|rediffmail)[.]com',s)
if m!=None:
    print("Given Mail Id is valid one")
else:
    print("Given mail id is invalid one")'''

'''import re
s=input("Enter Registration number :")
n=re.fullmatch('TS[012][0-9][A-Z]{2}\d{4}',s)
if n!=None:
    print('Valid Registration Number')
else:
    print('Invalid Registration Number')'''

'''import re
s=input("Enter mail Id to check for validation:")
m=re.fullmatch('\w[a-zA-Z0-9_.]*@[a-z0-9]+[.][a-z]+',s)
if m!=None:
    print("valid ID")
else:
    print('Invalid ID')'''

'''import re
s=open("C:\\Users\\Admin\\Documents\\Python regx\\newfilemobnum.txt",'r')
for line in s:
    m=re.findall("(www[.][a-zA-Z0-9]+[.]com|http://[a-zA-Z0-9]+[.]com).",line)
    for n in m:
        print(n)'''

'''class P1:
    def m1(self):
        print('P1 Method')
class P2:
    def m1(self):
        print('P2 Method')
class C(P1,P2):
    pass
c=C()
c.m1()'''

'''class P1:
    def m1(self):
        print('P1 Method')
class P2:
    def m1(self):
        print('P2 Method')
class C(P2,P1):
    pass
c=C()
c.m1()'''

'''class P1:
    def m1(self):
        print('P1 Method')
class P2:
    def m1(self):
        print('P2 Method')
class C(P1,P2):
    def m1(self):
        print("Child Method")
c=C()
c.m1()'''

'''class D:
    pass
class E:
    pass
class F:
    pass
class B(D,E):
    pass
class C(D,F):
    pass
class A(B,C):
    pass
print(A.mro())'''

class A:pass
class B:pass
class C:pass
class Z:pass
class X(A,B):pass
class Y(B,C):pass
class P(X,Y,C,Z):pass
print(P.mro() )