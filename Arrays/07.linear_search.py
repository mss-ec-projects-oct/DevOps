#!/bin/python3

def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1

#Example usage:
array = [10,40,15,25,30,75]
target = int(input("Enter the element to search for:"))

index = linear_search(array,target)

if index != -1:
    print(f"Element found at index {index}")
else:
    print("Element not found in the array")
