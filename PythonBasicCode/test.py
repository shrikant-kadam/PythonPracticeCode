# Calculator Code
num1 = int(input("Enter First Number.. = "))
num2 = int(input("Enter Second Number.. = "))
PHYSICS = int(input("PHYSICS Marks = "))
CHEMISTRY = int(input("CHEMISTRY Marks = "))
MATHS = int(input("MATHS Marks = "))


def add():
    print("Addition is : ", num1 + num2)

def sub():
    print("Substraction is : ", num1 - num2)

def mul():
    print("Multiplication is : ", num1 * num2)

def div():
    print("Division is : ", num1 / num2)

def avg():
    print((PHYSICS + CHEMISTRY + MATHS)/3)

Add = add()
Sub = sub()
Mul = mul()
Div = div()
Avg = avg()
