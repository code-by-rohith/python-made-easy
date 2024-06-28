def print_numbers_up_to_n(n):
    for i in range(1, n + 1):
        print(i)

def print_numbers_skip_divisible_by_10(n):
    for i in range(1, n + 1):
        if i % 10 == 0:
            continue
        print(i)

def print_numbers_exit_at_90(n):
    for i in range(1, n + 1):
        if i > 90:
            break
        print(i)

def sum_numbers_up_to_n(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print("Sum of numbers from 1 to", n, "is:", total_sum)

def infinite_loop_with_break():
    i = 1
    while True:
        print("Inside infinite loop, iteration:", i)
        i += 1
        if i > 10:
            break

def for_loop_print_n_numbers(n):
    for i in range(1, n + 1):
        print(i)

def for_loop_sum_n_numbers(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i
    print("Sum of numbers from 1 to", n, "is:", total_sum)

def print_pattern():
    for i in range(1, 5):
        for j in range(i):
            print(i, end=" ")
        print()

print("1. Printing numbers up to n:")
print_numbers_up_to_n(10)

print("\n2. Printing numbers up to n, skipping those divisible by 10:")
print_numbers_skip_divisible_by_10(20)

print("\n3. Printing numbers up to n, exiting the loop if i > 90:")
print_numbers_exit_at_90(100)

print("\n4. Sum of numbers up to n:")
sum_numbers_up_to_n(5)

print("\n5. Infinite loop with break:")
infinite_loop_with_break()

print("\n6. For loop to print numbers from 1 to n:")
for_loop_print_n_numbers(5)

print("\n7. For loop to sum numbers from 1 to n:")
for_loop_sum_n_numbers(5)

print("\n8. Printing the pattern:")
print_pattern()
