#!/bin/python3

def find_missing_number(array):
    n = len(array) + 1
    total = n * (n+1) // 2

    return total - sum(array)

#Example usage
arr = [1,2,4,5]
print("Missing number is: ",find_missing_number(arr))

#notes:
#// return interger
