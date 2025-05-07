#!/bin/python3

#Two input arrays
arr1 = [1,2,3,4,5]
arr2 = [3,4,5,6,7]

#convert to sets and find intersection
common = list(set(arr1) & set(arr2))

print("common elements:", common)

#Notes:
#Set Operators:
#---------------
#1.Union(|)
#Combines all unique elements from both sets
#{1,2,3} | {3,4,5} -> {1,2,3,4,5}

#2.Intersection(&)
#Returns elements common to both sets.
#{1,2,3} & {2,3,4} -> {2,3}

#3.Difference(-)
#Elements in A but not in B.
#{1,2,3} - {2,3,4} -> {1}

#4.Symmetric Difference(^)
#Elements in A or B but not both.
#{1,2,3} ^ {2,3,4} -> {1,4}

#5.Subset(<=)
#True if A is a subset of B.

#6.Superset(>=)
#True if A is a superset of B.

