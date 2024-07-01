def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
num1=int(input("Enter number1: "))
num2=int(input("Enter number2: "))
op=input("Enter operation(add/subtract/multiply/divide): ")
op1=op.lower()
if op1 == "add":
    print(add(num1,num2))
elif op1 == "subtract":
    print(subtract(num1,num2))
elif op1 == "multiply":
    print(multiply(num1,num2))
elif op1 == "divide":
    print(divide(num1,num2))