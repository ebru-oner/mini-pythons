# Check if the first and last number of a list is the same
def compare_list_elements(a_list):
    return a_list[0] == a_list[-1]

# Return numbers divisible by 5 from a list
def get_divisible_by_five(numbers):
    divisible_by_five_list = []
    for num in numbers:
        if num % 5 == 0:
            divisible_by_five_list += [num]
    return divisible_by_five_list

# Given two lists merge them so that new list has even numbers from list 1 and odd number from list2
def merge_lists(list1, list2):
    merged_list = []
    for num in list1:
        if num % 2 == 0:
            merged_list += [num]

    for num in list2:
        if num % 2 != 0:
            merged_list += [num]

    return merged_list
