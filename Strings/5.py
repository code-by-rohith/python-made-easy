def reverse_words_loop(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

def reverse_words_stack(s):
    words = s.split()
    reversed_words = []
    for word in words:
        stack = []
        for char in word:
            stack.append(char)
        reversed_word = ''
        while stack:
            reversed_word += stack.pop()
        reversed_words.append(reversed_word)
    return ' '.join(reversed_words)

def reverse_words_reverse_method(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

def reverse_words_slicing(s):
    words = s.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return ' '.join(reversed_words)

def print_even_length_words(s):
    words = s.split()
    for word in words:
        if len(word) % 2 == 0:
            print(word)

def has_letter_and_number(s):
    has_letter = False
    has_number = False
    for char in s:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        if has_letter and has_number:
            return True
    return False

def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

input_string = "Hello World Python Programming 123"
print("Original String:", input_string)

print("\n1. Reverse words in the string using Loop:")
print("Result:", reverse_words_loop(input_string))

print("\n2. Reverse words in the string using Stack:")
print("Result:", reverse_words_stack(input_string))

print("\n3. Reverse words in the string using Reverse method:")
print("Result:", reverse_words_reverse_method(input_string))

print("\n4. Reverse words in the string using Slicing:")
print("Result:", reverse_words_slicing(input_string))

print("\n5. Even length words in the string:")
print_even_length_words(input_string)

print("\n6. Check if the string has at least one letter and one number:")
print("Result:", has_letter_and_number(input_string))

print("\n7. Remove all duplicates from the string:")
print("Result:", remove_duplicates(input_string))
