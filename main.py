# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#1st program:

'''def cal(a,b):
    m=a*b
    s1=m+100
    s2=s1/5
    return m,s1,s2
f=cal(100,7)
for i in f:
    print(i)

g=cal(10,7)
for i in g:
    print(i)'''

#2nd program:

'''def sunday(name,age,p):
    name=(name+' ')*4
    age=-20*age
    p=(p*100)//100
    return name,age,p

f=sunday('harika',30,80)
for i in f:
    print(i)
    print('=========')'''

'''print('Butte',end=' ')
print("Harika",end=' ')
print("Devi")

print('Harika','devi','Butte',sep='\n')'''

def learnPython(name):
    marks=int(input("Enter Your Marks:" ))
    if name=='suresh':
        print("suresh your marks are: 567")
    perMarks=marks//1000
    if perMarks>60:
        print("{} your are passed and promoted to next class".format(name))
    else:
        print('{} you are failed and you not promoted to next class'.format(name))
    return perMarks
f=learnPython('suresh')
print(f)

