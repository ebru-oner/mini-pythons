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

