#!/usr/bin/python
def add2():
    x=int(raw_input("\nEnter 1st number : "))
    y=int(raw_input("Enter 2nd number : "))
    print "Sum = ",x+y

def add3():
    x=int(raw_input("\nEnter 1st number : "))
    y=int(raw_input("Enter 2nd number : "))
    z=int(raw_input("Enter 3rd number : "))
    print "Sum = ",x+y+z

print "MENU:-\n1. Add 2 numbers\n2. Add 3 numbers"
ch=int(raw_input("Enter your choice : "))
if (ch==1):
    add2()
elif (ch==2):
    add3()
else:
    print "Invalid Choice"
