
def prime(num):
    if num == 0:
        print("0 is neither prime nor composite")
    elif num == 1:
        print("1 is neither prime nor composite")
    elif num < 0:
        print("Negative numbers cannot be prime or composite")
    elif num == 2:
        print("2 is a prime number")
    else:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, "is a prime number")
        else:
            print(num, "is not a prime number")
num = int(input("Enter a number: "))
prime(num)