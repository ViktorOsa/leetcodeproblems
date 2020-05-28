"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    """Your code goes here."""
    l_bound = 0
    r_bound = len(input_array) - 1
    while l_bound <= r_bound:
        mid_index = l_bound + (r_bound - l_bound)//2
        if value == input_array[mid_index]:
            return mid_index
        elif input_array[mid_index] > value: # go left
            r_bound = mid_index - 1
        elif input_array[mid_index] < value: # go right
            l_bound = mid_index + 1
            
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))