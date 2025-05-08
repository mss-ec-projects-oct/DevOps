#!/bin/python3

def first_last_elements_array(arr):
    if not arr:
        return none,none
    
    return arr[0], arr[-1]

#Example usage:
array_list = [10, 20, 30, 40, 50]
first, last = first_last_elements_array(array_list)

print("First element: ",first)
print("Last element: ",last)


#Notes:
#if not arr:
