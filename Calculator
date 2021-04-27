def add(num, num2):
    print(num + num2)

def sub(num, num2):
    print(num - num2)

def mult(num, num2):
    print(num * num2)

def div(num, num2):
    print(num / num2)

def funct(function, num, num2):
    switch = {
        0: lambda: add(num, num2),
        1: lambda: sub(num, num2),
        2: lambda: mult(num, num2),
        3: lambda: div(num, num2)
    } [function]()


num = input("Enter a number: ")
num2 = input("Enter another number: ")

try:
    function = input("Choose 0 to add, 1 to subtract, 2 to multiply, or 3 to divide: ")
except KeyError:
    print ("Choose a valid number")

funct(function, num, num2)

