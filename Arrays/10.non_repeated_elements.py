#!/bin/python3

def non_repeated_elements(arr):
    seen = {}
    for ch in arr:
        if ch not in seen:
            seen[ch] = 1
        else:
            seen[ch] +=1
    #unique_elements = [unq for unq in seen.keys() if seen[unq] == 1]
    unique_elements = [item for item,count in seen.items() if count == 1] 
    return unique_elements

#Example usage:
array = [ 1, 2, 2, 3, 1, 5, 5, 6]
print("non repeated elements are: ", non_repeated_elements(array))
 
