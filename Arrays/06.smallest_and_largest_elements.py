#!/bin/python3

def smallest_largest(arr):
    #1arr = sorted(arr)
    #1return arr[0], arr[-1]
    
    #2return min(arr), max(arr)

    #3
    smallest = largest = arr[0]
    for num in arr:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    
    return smallest, largest

#Example usage:
array = [1,3,6,2,3,10,1]
small,large = smallest_largest(array)
print(f"smallest number: {small} \nlargest number: {large}")


#notes:
#------
#The Python built-in functions min() and max() are used to find the smallest and largest items in an iterable (like a list, tuple, string, etc.) or among two or more arguments.
