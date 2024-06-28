def remove_duplicates(input_str):
    result = []
    for char in input_str:
        if char not in result:
            result.append(char)
    return ''.join(result)

input_string = "abacdbazdddddddddddddddeeeeeeeeeeeeeeeeeeeeeeeeee"
print(remove_duplicates(input_string))  