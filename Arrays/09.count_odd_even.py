#!/bin/python3

def count_odd_even(arr):
    odd_count = 0
    even_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return odd_count, even_count

#Example usage:
array = [1, 3, 5, 7, 8, 2, 4]
odd, even = count_odd_even(array)
print(f"count of odd numbers: {odd} \ncount of even numbers: {even}")
