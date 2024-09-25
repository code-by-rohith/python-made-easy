def decorator(func):
    def inner(a,b):
        print("before operation")

        func(a,b)

        print("after operation")

    return inner

def add_numbers(a, b):
    print("addition is done ", a + b)

@decorator
def sub_numbers(a, b):
    print("subtraction is done ", a - b)

add_numbers1 = decorator(add_numbers)
add_numbers1(10,20)

sub_numbers(20,10)