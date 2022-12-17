'''import threading
print("Current Executing thread :",threading.current_thread().name)'''

#Creating Thread without using class:
import time

'''from threading import *
def display():
    print("This Code(Display method) is executed by :",current_thread().name)
t=Thread(target=display)
t.start()
print("This code is executed by:",current_thread().name)'''

'''from threading import *
def display():
    for i in range(10):
        print("child thread")
        print()
t=Thread(target=display)
t.start()
for i in range(10):
    print("Main Thread")'''

#Creating thread by extanding thread class:
'''from threading import *
class myThread(Thread):
    def run(self):
        for i in range(10):
            print("Child Thread-1")
t=myThread()
t.start()
for i in range(10):
    print("Main Thread-1")'''

#Creating thread without extanding thread class:
'''from threading import  *
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread-2")
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(10):
    print("Main Thread-2")'''

'''from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("Child Thread Executed by:",current_thread().name)
obj=Test()
t1=Thread(target=obj.display)
t2=Thread(target=obj.display)
t3=Thread(target=obj.display)
t4=Thread(target=obj.display)
t1.start()
t2.start()
t3.start()
t4.start()'''

#PROGRAM with out using multi threading:

'''import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:",n*n)
numbers=[1,2,3,4,5,6]
startTime=time.time()
doubles(numbers)
squares(numbers)
endTimme=time.time()
print("The Total time taken :",endTimme-startTime)'''

#program using thread:

'''from threading import *
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print("Double:",2*n)
        print()
def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print("Square:",n*n)
        print()
numbers=[1,2,3,4,5,6]
startTime=time.time()
t1=Thread(target=doubles,args=(numbers,))
t2=Thread(target=squares,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endTimme=time.time()
print("Total time taken by using thread:",endTimme-startTime)'''

#how to get and set names of thread:

'''from threading import *
print('Current thread name:',current_thread().name)
current_thread().name='harika'
print("Current thread name:",current_thread().name)'''

#thread Identification  number:ident

'''from threading import *
def display():
    print("Child Thread",current_thread().ident)

t=Thread(target=display)
t.start()
print("Main thread Identification Number:",current_thread().ident)
print("Child thread Identification number :",t.ident)'''

#program to know about no of active threads active_count()

'''from threading import *
import time
def display():
    print(current_thread().name,'started....')
    time.sleep(2)
    print(current_thread().name,'ended....')
print('The No.of active threads:',active_count())
t1=Thread(target=display,name='Child Thread-1')
t2=Thread(target=display,name='Child Thread-2')
t3=Thread(target=display,name='Child Thread-3')
t4=Thread(target=display,name='Child Thread-4')
t1.start()
t2.start()
t3.start()
t4.start()
print('The No.of active threads:',active_count())
time.sleep(6)
print('The No.of active threads:',active_count())'''

#program to know the information of all active threads:enumerate()

'''from threading import *
import time
def display():
    print(current_thread().name,'started...')
    time.sleep(3)
    print(current_thread().name,'ended....')
t1=Thread(target=display,name='Child Thread-1')
t2=Thread(target=display,name='Child Thread-2')
t3=Thread(target=display,name='Child Thread-3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print(t.name)
print('After 10 sec sleeping....')
time.sleep(10)
l=enumerate()
for t in l:
    print(t.name)'''

#join() method:

'''from threading import *
import time
def display():
    for i in range(10):
        print('Sita Thread')
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join()
for i in range(10):
    print("Ram Thread")'''

'''from threading import *
import time
def display():
    for i in range(10):
        print('Sita Thread')
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join(10)
for i in range(10):
    print("Ram Thread")'''

#Daemon:
'''from threading import *
print(current_thread().daemon)
current_thread().daemon=True
print(current_thread().daemon)'''

'''from threading import *
def job():
    print("child Thread")
t=Thread(target=job)
print()
print(current_thread().daemon)
print(t.daemon)
t.daemon=True
t.start()
print(t.daemon)'''
#operator overloading:

'''class Books:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self, other):
        return  self.pages+other.pages
    def __sub__(self, other):
        return self.pages-other.pages

b1=Books(100)
b2=Books(200)
print("The Total No.of Pages:",b1+b2)
print("difference",b2-b1)'''

#overloading >,<= operators for student object:
'''class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __le__(self, other):
        return self.marks<=other.marks
s1=Student('Ruthu',200)
s2=Student("Harika",100)
print('s1>s2',s1>s2)
print('s1<=s2',s1<=s2)'''

#overriding:
#Method overriding:
'''class P:
    def property(self):
        print("Land+cash+gold+power")
    def marry(self):
        print("Appalamma")
class C(P):
    def marry(self):
        print("Katrina kaif")
c=C()
c.property()
c.marry()'''

'''class P:
    def property(self):
        print("Land+cash+gold+power")
    def marry(self):
        print("Appalamma")
class C(P):
    def marry(self):
        super().marry()
        print("Katrina kaif")
c=C()
c.property()
c.marry()'''

#Constructor overriding:
'''class P:
    def __init__(self):
        print("Parent class constructor....")
class C(P):
    pass
c=C()'''

'''class P:
    def __init__(self):
        print("Parent class Constructor.......")

class C(P):
    def __init__(self):
        print("Child class Constructor.....")
c=C()'''

'''class P:
    def __init__(self):
        print("Parent class Constructor.......")

class C(P):
    def __init__(self):
        super().__init__()
        print("Child class Constructor.....")
c=C()'''

'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal

    def Display(self):
        print("EMP Name:",self.name)
        print("EMP age:",self.age)
        print("EMp NUm:",self.eno)
        print("EMP Sal:",self.esal)
e=Employee("Harika",30,1234,40000)
e.Display()'''


'''from abc import *
class Vechicle:
    @abstractmethod
    def getNoOfWheels(self):
        pass'''

'''from abc import *
class DBInterface(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class Oracle(DBInterface):
    def connect(self):
        print("Connecting to oracle DataBase...")
    def disconnect(self):
        print("DisConnecting to oracle DataBase...")
class Mysql(DBInterface):
    def connect(self):
        print("Connecting to Mysql DataBase...")
    def disconnect(self):
        print("DisConnecting to Mysql DataBase...")
class SyBase(DBInterface):
    def connect(self):
        print("Connecting to sybase DataBase...")
    def disconnect(self):
        print("DisConnecting to sybase DataBase...")
dbname=input("Enter Database name:")
classname=globals()[dbname]
x=classname()
x.connect()
x.disconnect()'''

#private variable:

'''class Test:
    def __init__(self):
        self.x=10
t=Test()
print(t.x)'''

'''class Test:
    def __init__(self):
        self.__x=10
t=Test()
print(t.x)'''

'''class Test:
    def __init__(self):
        self.__x=10
t=Test()
print(t.__x)'''

'''class Test:
    def __init__(self):
        self.__x=10
    def m1(self):
        print(self.__x)
t=Test()
t.m1()'''

'''class Test:
    def __init__(self):
        self.__x=10
t=Test()
print(t._Test__x)'''

#__str__(self):

'''class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def __str__(self):
        return "This is the Student with name:{} and with Rollno:{}".format(self.name,self.rollno)
s1=Student("Harika",2)
s2=Student("Ruthwik",1)
print(s1)
print(s2)'''

'''from threading import *
import time
def wish(name):
    for i in range(10):
        print("Good Evening:",end='')
        time.sleep(5)
        print(name)
t=Thread(target=wish,args=('Ruthwik',))
t.start()'''

'''from threading import *
import time
l=Lock()
def wish(name):
    l.acquire()
    for i in range(10):
        print('Good Morning:',end='')
        time.sleep(3)
        print(name)
    l.release()
t1=Thread(target=wish,args=('Ruthu',))
t2=Thread(target=wish,args=('Tinku',))
t1.start()
t2.start()'''

'''from threading import *
import time
s=Semaphore()
def wish(name):
    s.acquire()
    for i in range(10):
        print("Good Morning:",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Harika',))
t2=Thread(target=wish,args=('Ganesh',))
t3=Thread(target=wish,args=('Ruthu',))
t1.start()
t2.start()
t3.start()'''

from threading import *
import time
s=Semaphore(3)
def wish(name):
    s.acquire()
    for i in range(10):
        print("Good Morning:",end='')
        time.sleep(2)
        print(name)
    s.release()
t1=Thread(target=wish,args=('Harika',))
t2=Thread(target=wish,args=('Ganesh',))
t3=Thread(target=wish,args=('Ruthu',))
t1.start()
t2.start()
t3.start()