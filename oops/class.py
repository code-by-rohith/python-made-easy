#1

def basic_class():
  class MyClass:
    x = 5
  p1 = MyClass()
  print(p1.x)
basic_class()

#2


def lam(n):
    return lambda x: x * n
n = int(input("Enter a number: "))
s = lam(n)
w=int(input("Enter a number :"))
result = s(w)     
print(result)
