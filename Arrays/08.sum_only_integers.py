#!/bin/python3

def sum_only_integers(arr):
    #sum only integers
    #total = sum(int(x) for x in arr if x.isdigit()) #work for strings since ''.isdigit()
    total = sum(x for x in arr if isinstance(x, int))
    return total

#Example usage
arr = [1, 10, '#', '$', 'A', 4]
output = sum_only_integers(arr)
print("sum of only integers: ", output)

#Notes:
#isinstance(x, int) checks if the element is an integer.
#   if isinstance(x, str):
#   x = 5.5
#   if isinstance(x, (int, float)):  # Tuple of types
#       print("x is a number")

#The sum() function adds only those elements.
