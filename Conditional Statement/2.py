
def print_grade():
    mark = int(input("Enter the mark: "))
    if mark > 90 :
        print("O grade")
    elif mark > 80:
        print("A grade")
    elif mark > 70:
        print("B grade")
    elif mark > 60:
        print("C grade")
    elif mark > 50:
        print("D grade")
    else:
        print("Fail")


def num():
    number = int(input("Enter a number: "))
    for i in range(1, number + 1):
        print(i)

def infinite():
     while True:
        n=int(input("Enter the number "))
        if n<=100:
            break


def even_odd():
    n = int(input("Enter the number: "))
    if n % 2 == 0:
        print(f"The number {n} is even.")
    else:
        print(f"The number {n} is odd.")


def nin():
    number = int(input("Enter a number: "))
    for i in range(1, number + 1):
        if i > 90:
            break
        print(i)
def num1():
    for i in range(1, 5):
        for j in range(i):
            print(i, end=' ')
        print()


def strr():
    a="vikas"
    print(a[::-1])



def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = 5
result = sum_numbers(n)
print(f"The sum of numbers from 1 to {n} is: {result}")

