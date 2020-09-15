'''
Collaborators: 

'''
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def subtract(a,b):
    return a-b

num1=int(input("inert number: "))
num2=int(input("insert another number: "))
pick=int(input("type 1 to add, 2 to subtract, 3 to multiply, and 4 to divide:  "))

if pick == 1:
    print(add(num1,num2))

elif pick == 2:
    print(subtract(num1,num2))

elif pick == 3:
    print(multiply(num1,num2))
elif pick == 4:
    print(divide(num1,num2))
else:
    print("thats not the right input")