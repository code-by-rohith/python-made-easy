# Basic Lambda Functions
lambda1 = lambda x: x + 1  # Adds 1 to x
lambda2 = lambda x, y: x * y  # Multiplies x and y
lambda3 = lambda s: s.upper()  # Converts string s to uppercase
lambda4 = lambda x: x % 2 == 0  # Checks if x is even
lambda5 = lambda x: x ** 2  # Squares x

# Outputs
print(f"lambda1: {lambda1(5)}")  # Outputs: 6
print(f"lambda2: {lambda2(4, 5)}")  # Outputs: 20
print(f"lambda3: {lambda3('hello')}")  # Outputs: HELLO
print(f"lambda4: {lambda4(4)}")  # Outputs: True
print(f"lambda5: {lambda5(3)}")  # Outputs: 9

# Intermediate Lambda Functions
lambda6 = lambda a, b: (a + b) / 2  # Calculates average of a and b
lambda7 = lambda lst: [x ** 2 for x in lst]  # Squares each element in list
lambda8 = lambda x: 'Even' if x % 2 == 0 else 'Odd'  # Checks if x is even or odd
lambda9 = lambda s: s[::-1]  # Reverses string s
lambda10 = lambda x, y: x if x > y else y  # Returns the maximum of x and y

# Outputs
print(f"lambda6: {lambda6(4, 8)}")  # Outputs: 6.0
print(f"lambda7: {lambda7([1, 2, 3])}")  # Outputs: [1, 4, 9]
print(f"lambda8: {lambda8(5)}")  # Outputs: Odd
print(f"lambda9: {lambda9('hello')}")  # Outputs: olleh
print(f"lambda10: {lambda10(5, 7)}")  # Outputs: 7

# Advanced Lambda Functions
lambda11 = lambda x: (lambda y: x + y)(5)  # Adds 5 to x
lambda12 = lambda f: lambda x: f(f(x))  # Applies function f twice
lambda13 = lambda x: (lambda y: y * x)(10)  # Multiplies x by 10
lambda14 = lambda f: lambda x: x if f(x) else -x  # Returns x if f(x) is True, else -x
lambda15 = lambda *args: sum(args)  # Sums all arguments

# Outputs
print(f"lambda11: {lambda11(3)}")  # Outputs: 8
print(f"lambda12: {lambda12(lambda x: x + 1)(2)}")  # Outputs: 4
print(f"lambda13: {lambda13(2)}")  # Outputs: 20
print(f"lambda14: {lambda14(lambda x: x > 0)(5)}")  # Outputs: 5
print(f"lambda15: {lambda15(1, 2, 3, 4)}")  # Outputs: 10

# Higher-order Lambda Functions
lambda16 = lambda x: (lambda y: (x, y))  # Returns a lambda that pairs x with y
lambda17 = lambda x: (lambda f: f(x))(lambda y: y ** 2)  # Applies f to x, where f squares its argument
lambda18 = lambda f: lambda x: f(x) + 1  # Returns a lambda that applies f to x and adds 1
lambda19 = lambda f: lambda x: f(f(f(x)))  # Applies function f three times
lambda20 = lambda x: (lambda f: f(x))(lambda y: y + 2)  # Applies a lambda that adds 2 to x

# Outputs
print(f"lambda16: {lambda16(5)(10)}")  # Outputs: (5, 10)
print(f"lambda17: {lambda17(4)}")  # Outputs: 16
print(f"lambda18: {lambda18(lambda x: x * 2)(3)}")  # Outputs: 7
print(f"lambda19: {lambda19(lambda x: x + 1)(2)}")  # Outputs: 5
print(f"lambda20: {lambda20(5)}")  # Outputs: 7

# Lambda with Filter and Map
lambda21 = lambda lst: list(filter(lambda x: x > 0, lst))  # Filters positive numbers
lambda22 = lambda lst: list(map(lambda x: x * 2, lst))  # Doubles each number
lambda23 = lambda lst: list(map(lambda x: x if x % 2 == 0 else 0, lst))  # Replaces odd numbers with 0
lambda24 = lambda lst: list(map(lambda x: x ** 0.5, lst))  # Square root of each number
lambda25 = lambda lst: list(filter(lambda x: x % 2 != 0, lst))  # Filters odd numbers

# Outputs
print(f"lambda21: {lambda21([1, -1, 2, -2])}")  # Outputs: [1, 2]
print(f"lambda22: {lambda22([1, 2, 3])}")  # Outputs: [2, 4, 6]
print(f"lambda23: {lambda23([1, 2, 3, 4])}")  # Outputs: [0, 2, 0, 4]
print(f"lambda24: {lambda24([1, 4, 9])}")  # Outputs: [1.0, 2.0, 3.0]
print(f"lambda25: {lambda25([1, 2, 3, 4])}")  # Outputs: [1, 3]

# Lambda with Reduce
from functools import reduce
lambda26 = lambda lst: reduce(lambda x, y: x + y, lst)  # Sums all numbers in the list
lambda27 = lambda lst: reduce(lambda x, y: x * y, lst)  # Multiplies all numbers in the list
lambda28 = lambda lst: reduce(lambda x, y: x if x > y else y, lst)  # Finds the maximum in the list
lambda29 = lambda lst: reduce(lambda x, y: x + y / len(lst), lst, 0)  # Calculates average of the list
lambda30 = lambda lst: reduce(lambda x, y: x if x < y else y, lst)  # Finds the minimum in the list

# Outputs
print(f"lambda26: {lambda26([1, 2, 3, 4])}")  # Outputs: 10
print(f"lambda27: {lambda27([1, 2, 3, 4])}")  # Outputs: 24
print(f"lambda28: {lambda28([1, 2, 3, 4])}")  # Outputs: 4
print(f"lambda29: {lambda29([1, 2, 3, 4])}")  # Outputs: 2.5
print(f"lambda30: {lambda30([1, 2, 3, 4])}")  # Outputs: 1

# Advanced Applications
lambda31 = lambda lst: [(lambda x: x ** 2)(x) for x in lst]  # List comprehension with lambda
lambda32 = lambda x, y: (lambda a: lambda b: a + b)(x)(y)  # Nested lambdas to add x and y
lambda33 = lambda x: (lambda f: f(x))(lambda y: y ** 3)  # Applies lambda that cubes x
# Corrected lambda34 function
lambda34 = lambda x: (lambda f: f(x + 2))(lambda z: z)  # Corrected complex nested lambda
lambda35 = lambda x: (lambda y: (lambda z: y(z))(x))(lambda a: a * a)  # Lambda inside lambda inside lambda

# Outputs
print(f"lambda31: {lambda31([1, 2, 3])}")  # Outputs: [1, 4, 9]
print(f"lambda32: {lambda32(3, 6)}")  # Outputs: 9
print(f"lambda33: {lambda33(2)}")  # Outputs: 8
print(f"lambda34: {lambda34(3)}")  # Outputs: 5
print(f"lambda35: {lambda35(5)}")  # Outputs: 25

# Lambda with Generators
lambda36 = lambda n: (lambda gen: [x for x in gen])(range(n))  # Generator to list
lambda37 = lambda n: (lambda gen: [x for x in gen])(range(0, n, 2))  # Even numbers generator
lambda38 = lambda n: (lambda gen: [x for x in gen if x % 2 == 0])(range(n))  # Even numbers from range
lambda39 = lambda n: (lambda gen: [x ** 2 for x in gen])(range(n))  # Squares of numbers in range
lambda40 = lambda n: (lambda gen: [x for x in gen if x % 2 != 0])(range(n))  # Odd numbers from range

# Outputs
print(f"lambda36: {lambda36(5)}")  # Outputs: [0, 1, 2, 3, 4]
print(f"lambda37: {lambda37(10)}")  # Outputs: [0, 2, 4, 6, 8]
print(f"lambda38: {lambda38(10)}")  # Outputs: [0, 2, 4, 6, 8]
print(f"lambda39: {lambda39(5)}")  # Outputs: [0, 1, 4, 9, 16]
print(f"lambda40: {lambda40(10)}")  # Outputs: [1, 3, 5, 7, 9]
