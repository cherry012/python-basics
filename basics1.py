#1.wite a program to print your name
print('Charan kumar')

#2.Write a program for single line comment and multi line comment

 #python is a high level programming language

 #multiline comment
'''every expert 
was once a 
beginner'''

#3.Define variables for different data types int,boolean,char,float

a=10
b=True
c='Hy charan'
d=10.5

print(a)
print(b)
print(c)
print(d)

#4.Define the local and global variables with the same name and print both the variables and understand the scope of the variables

a=10
def f1():
    a=888
    print(a)
def f2():
    print(a)

f1()
f2()
#the variable which is declared inside a function is called local variable
#the variable which is declared outside a function is called global variable
#first priority is given for local variable
