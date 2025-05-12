#!/bin/python3

def bubble_sort(arr):
    print("original array:",arr)
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                #swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        #print(j,arr)

        if not swapped:
            break

    return arr

#Example Usage:
arr = [2, 1, 4, 2, 4, 6, 1]
sorted_arr = bubble_sort(arr)
print("Optimized Buble sorted array: ",sorted_arr)

#notes:
#1st itreation: Largest element is sorted (6) then,4,4...
