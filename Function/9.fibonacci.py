"""def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a=0
        b=1
        for i in range(n-2):
            c= a+b
            a=b
            b=c
        return c"""
def fib(n):
    if n<=0:
        print("incorrect n")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n=int(input("Enter nth term: "))
#print(fibo(n))
print(fib(n))
