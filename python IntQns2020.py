#3

'''my_dict={'fruit_Names':('apple,mango,orange,guava')}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())'''

#5
'''class Human:
    def __init__(self,name,age):
        self.name=name
        self.age=age
h=Human('Harika',30)
print(h.name)
print(h.age)'''

'''class human:
    name=None
    age=None
    def get_Name(self):
        print("Enter your Name:")
        self.name=input()
    def get_Age(self):
        print("Enter your age:")
        self.age=input()
    def put_Name(self):
        print("Your name is:",self.name)
    def put_Age(self):
        print("Your Age is:",self.age)
person1=human()
person1.get_Name()
person1.get_Age()
person1.put_Name()
person1.put_Age()'''

#6.
'''class Student:
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.subject=subject
    def print_Stu(self):
        print("Name of student :",self.name)
        print("Age of student :",self.age)
        print("Subject :",self.subject)
stu1=Student('Ruthu',7,'Math')
stu1.print_Stu()'''

#7.
'''class Fruit:
    def __init__(self):
        print('I am a fruit')

class Citrus(Fruit):
    def __init__(self):
        super().__init__()
        print('I am citrus')
lemon=Citrus()'''

#8.

'''import numpy as np
a=np.array([1,2,3])
print(a)
b=np.array([[1,2,3],[4,5,6]])
print(b)'''
#9
'''import numpy as np
a=np.zeros((5,5))
print(a)'''
#10.
'''import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.sum((a,b),axis=0)
print(c)'''

'''import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
c=np.sum((a,b),axis=1)
print(c)'''

import numpy as np
x=np.array([12,43,2,100,54,5,68])
y=print(x[np.argsort(x)[-2:][::-1]])