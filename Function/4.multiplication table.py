def mul(num,n):
    for i in range(0,n+1):
        print(num,"*",i,"=",num*i)
num=int(input("Enter value to multiply: "))
n=int(input("enter upto which: "))
mul(num,n)