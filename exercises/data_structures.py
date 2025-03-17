import math
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

# Remove and add items in a list
def remove_add_item_in_list(a_list, remove_index, add_index):
    length = len(a_list)
    if not any(a_list) or remove_index > length or add_index >  length:
        return
    removed_item = a_list.pop(remove_index)
    after_add = a_list.insert(add_index, removed_item)
    a_list += [removed_item]

    return a_list

# Slice list into 3 equal chunks and reverse each chunk
def slice_and_reverse(a_list):
    length = len(a_list)
    if length == 0:
        return
    chunk_size =  math.ceil(length / 3)
    chunk_list = []
    for i in range(0, length, chunk_size):
        chunk  = a_list[i:i+chunk_size]
        chunk_list += [chunk[::-1]]
    return chunk_list

# Make the element from both lists in a pair
def pair_lists(list_1, list_2):
    if not any(list_1) or not any(list_2):
        return
    pair_list = list(zip(list_1, list_2))
    return pair_list

# Find intersection of two sets and remove them from 1st set
def intersection_of_sets(set_1, set_2):
    intersection = set_1.intersection(set_2)
    for item in intersection:
        set_1.remove(item)
    return set_1, set_2

# Check if a set is a subset or superset of another, and remove found elements
def clear_subset(set_1, set_2):
    if set_1.issubset(set_2):
        set_1.clear()
    if set_2.issubset(set_1):
        set_2.clear()
    return set_1, set_2

# Check in alist if the key from dict exists, if not delete from list
def key_exists(list_1, dict_1):
    value_list = dict_1.values()
    list_1[:] = [item for item in value_list if item in list_1]
    return list_1

# Add unique items to a list from dict
def add_items(dict_1):
    list_1=[]
    value_list = dict_1.values()
    for item in value_list: 
        if item not in list_1:
            list_1.append(item)
    return list_1 
