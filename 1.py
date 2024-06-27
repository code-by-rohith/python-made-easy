def first():
    a=55
    b=22
    c=a+b
    print(c)
    d=c*a
    print(d)
    if d>a:
        cc=d*3.142
        cc+=34
        cc-=20
        print(float(cc))

def second():
    exam_st_date = (11, 12, 2014)
    print("The Examination will start from : ",exam_st_date[0],"/",exam_st_date[1],"/",exam_st_date[2])

def circle():
    r=1.1
    pi=3.142
    area =r*pi
    print("Area of the circle is : ",area)

def triangle():
    a=int(input("Enter the length  :"))
    b=int(input("Enter the breadth : "))
    c=(a*b)/2
    print("Area of triangle is ",c)

def swap():
    a=4
    b=9
    print("before swap a : ",a)
    print("before swap b : ",b)
    temp=a
    a=b
    b=temp
    print("after swap a : ",a)
    print("after  swap a : ",b)

def reverse():
    n=int(input("Enter the number :"))
    
    reverse=0
    while n>0:
        s=n%10
        reverse=reverse*10+s
        n=n//10
    print(reverse)
reverse()

