import string

# Print characters from a string that are present at an even index number
def print_chars_at_even_index(str):
    index = 0
    while index < len(str):
        if index % 2 == 0:
            print(str[index])
        index += 1

# Remove first n characters from a string
def remove_first_n_chars(str, count):
    if count > len(str):
        return
    return str[count:]

# Return the count of a given substring from a string
def count_substring(str, substr):
    return str.count(substr)

# Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
def print_pattern(count):
    for num in range(count+1):
        for i in range(num):
            print(num, end=" ")
        print("\n")

# Print a downward half pyramid start pattern
# ******
# *****
# ****
# ***
# **
# *
def print_downward_star_pyramid(count):
    for i in range(count, 0, -1):
        for j in range(i):
            print("*", end="")
        print("\n") 

# Create a string made of the first, middle and last char
def get_first_middle_last(str):
    length = len(str)
    if length <= 3:
        return str
    first = str[0]
    mid = str[length//2]
    last = str[length-1]
    return first+mid+last

# Create a string made of the middle 3 chars
def get_middle_three_chars(str):
    length = len(str)
    if length < 3:
        return None
    mid = length//2
    return str[mid-1:mid+2]
   
# Append a new string in the middle of a given string
def append_into_middle(str1, str2):
    length = len(str1)
    mid = length // 2
    return str1[0:mid]+str2+str1[mid:]

# Create a new string made of the first, middle and last characters of each input string
def create_combination_of_strings(list_of_strings):
    combination_str = ""
    for str in list_of_strings:
        length = len(str)
        combination_str+= "".join([str[0], str[length//2], str[-1]])
    return combination_str

# Arrange string characters such that lowercase letter come first
def make_lowercases_prefix(str):
    list_u = []
    list_l = []
    for c in str:
        if c.islower():
            list_l += [c]
        else:
            list_u += [c]
    return "".join(list_l+list_u)

# Count all letter, digits, special characters from a given string
def group_characters_in_string(a_str):
    char_count = 0
    symbol_count = 0
    number_count = 0
    for c in a_str:
        if c.isalpha():
            char_count += 1
        elif c.isdigit():
            number_count += 1
        else:
            symbol_count += 1
    return a_str + " has " + str(char_count) + " chars " + str(number_count) + " digits " + str(symbol_count) + " symbols."

# String characters balance test, check if all characters of s1 are present in s2
def is_balanced_string(str1, str2):
    for c in str1:
        if not c in str2:
            return False
    return True

# Count all occurences of all characters within a string
def count_char_occurrences(str1):
    char_map = {}
    for c in str1:
        if c in char_map:
            char_map[c] += 1
        else:
            char_map[c] = 1
    return char_map
            
# Reverse a given string
def reverse_string(str1):
    reversed_string = str1[::-1]
    return reversed_string

# Find the last position of a given substring
def get_last_position(str1, substr):
    return str1.rfind(substr)

# Split a string with given char
def split_string(str1, split_char):
    return str1.split(split_char)

# Remove empty strings from a list of strings
def remove_empty_strings(str_list):
    new_list = list(filter(None, str_list))
    return new_list

# Remove all characters except integers 
def remove_characters_keep_integers(str1):
    new_list = [item for item in str1 if item.isdigit()]
    return "".join(new_list)

# Find words with both alphabets and numbers
def find_combination_of_alphabets_numbers(str1):
    str1_list = str1.split()
    result = []
    for s in str1_list:
        if any(c.isalpha() for c in s) and any(c.isdigit() for c in s):
            result += [s]
    return result

# Replace each symbol with given char
def replace_symbols(str1, replace_char):
    for c in string.punctuation:
        str1 = str1.replace(c, replace_char)
    return str1