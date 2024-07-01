# 1. Find the sum of all items in a dictionary
def sum_of_values(d):
    total = 0
    for value in d.values():
        total += value
    return total

# 2. Get size of a Dictionary in Python
def dictionary_size(d):
    return len(d)

# 3. Remove all duplicates from a given sentence
def remove_duplicates(sentence):
    words = sentence.split()
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    return ' '.join(unique_words)

# 4. Sort a dictionary by value (ascending and descending)
def sort_dict_by_value(d, ascending=True):
    sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=not ascending)
    sorted_dict = {}
    for item in sorted_items:
        sorted_dict[item[0]] = item[1]
    return sorted_dict

# 5. Change value of a key in a nested dictionary
def change_nested_dict_value(d, key_path, new_value):
    keys = key_path.split('.')
    current = d
    for key in keys[:-1]:
        current = current[key]
    current[keys[-1]] = new_value
    return d

# 6. Check if a Given Key Already Exists in Dictionary
def key_exists(d, key):
    return key in d

# 7. Merge two Python dictionaries
def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged

# 8. Iterate over dictionaries using for loops
def iterate_over_dict(d):
    for key, value in d.items():
        print(f"Key: {key}, Value: {value}")

# 9. Count frequency of List Items using Dictionary
def count_frequency(lst):
    freq = {}
    for item in lst:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

# 10. Get Keys with Maximum and Minimum Value in a Dictionary
def max_min_keys(d):
    max_value = max(d.values())
    min_value = min(d.values())
    max_keys = []
    min_keys = []
    for key, value in d.items():
        if value == max_value:
            max_keys.append(key)
        if value == min_value:
            min_keys.append(key)
    return max_keys, min_keys

# 11. Drop empty Items from a given Dictionary
def drop_empty_items(d):
    return {key: value for key, value in d.items() if value}

# 12. Print the Sum of Key Value Pairs in a Given Dictionary
def sum_key_value_pairs(d):
    total = 0
    for value in d.values():
        total += value
    return total

# 13. Convert a dictionary to a list of (key, value) tuples
def dict_to_tuples(d):
    return list(d.items())


# Example usage and testing of functions
# Example for each function
d = {'a': 100, 'b': 200, 'c': 300}
print("Sum of values:", sum_of_values(d))
print("Size of dictionary:", dictionary_size(d))

sentence = "Python is great and Java is also great"
print("Remove duplicates:", remove_duplicates(sentence))

print("Sorted by value (ascending):", sort_dict_by_value(d))
print("Sorted by value (descending):", sort_dict_by_value(d, ascending=False))

nested_dict = {'a': {'b': {'c': 10}}}
change_nested_dict_value(nested_dict, 'a.b.c', 20)
print("Changed nested dict:", nested_dict)

print("Key 'b' exists:", key_exists(d, 'b'))

d1 = {'a': 100, 'b': 200}
d2 = {'c': 300}
print("Merged dictionaries:", merge_dicts(d1, d2))

print("Iterating over dictionary:")
iterate_over_dict(d)

lst = [1, 2, 2, 3, 4, 1, 4, 5, 5, 6, 7, 7]
print("Frequency of list items:", count_frequency(lst))

print("Keys with max and min value:", max_min_keys(d))

d_empty = {'a': 100, 'b': None, 'c': 300, 'd': ''}
print("Drop empty items:", drop_empty_items(d_empty))

print("Sum of key-value pairs:", sum_key_value_pairs(d))

d1_tuples = {"one": 11, "two": 22, "three": 33, "four": 44, "five": 55}
print("Convert dictionary to list of tuples:", dict_to_tuples(d1_tuples))
