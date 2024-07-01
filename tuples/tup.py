import sys

# 1. Find the size of a tuple in bytes
def tuple_size(t):
    return sys.getsizeof(t)

# 2. Python program to create a list of tuples from given list having number and its cube in each tuple
def create_tuple_list(lst):
    return [(x, x**3) for x in lst]

# 3. Adding Tuple to List and vice – versa
def add_tuple_to_list(tup, lst):
    lst.append(tup)
    return lst

def add_list_to_tuple(lst, tup):
    return tuple(lst) + tup

# 4. Python – Sum of tuple elements
def sum_tuple_elements(tup):
    return sum(tup)

# 5. Update each element in tuple list
def update_tuple_list(lst):
    return [(x+4, y+4, z+4) for x, y, z in lst]

# 6. Multiply Adjacent elements
def multiply_adjacent_elements(tup):
    return tuple(tup[i] * tup[i+1] for i in range(len(tup) - 1))

# Example usage to test each function
t = (1, 2, 3)
print("Size of tuple:", tuple_size(t), "bytes")

lst = [1, 2, 3]
print("List of tuples:", create_tuple_list(lst))

tup = (4, 16, 64)
lst_tuples = [(1, 1), (2, 8), (3, 27)]
print("List after adding tuple:", add_tuple_to_list(tup, lst_tuples))
print("Tuple after adding list:", add_list_to_tuple(lst_tuples, (5, 7, 8)))

tup_sum = (5, 7, 8)
print("Sum of tuple elements:", sum_tuple_elements(tup_sum))

lst_update = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
print("Updated tuple list:", update_tuple_list(lst_update))

tup_mult = (1, 5, 7, 8, 10)
print("Tuple after multiplication:", multiply_adjacent_elements(tup_mult))
