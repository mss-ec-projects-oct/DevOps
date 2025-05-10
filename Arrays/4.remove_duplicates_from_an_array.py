#!/bin/python3

#Remove Duplicates (Keep Original Order)

arr = [1,2,2,3,4,4,6,5]
arr.sort()
uniq_list = []
seen = set()

for item in arr:
    if item not in seen:
        uniq_list.append(item)
        seen.add(item)

#unique = sorted(uniq_list)
#print(unique)
print(uniq_list)

#Notes:
#======
#sort(): Method for lists only, sorts in place
#Modifies the original list.

#Returns None, not a new list.

#Only works on lists, not other iterables.
#+++++++++++++++++++++++++++++++

#sorted(): Built-in function, returns a new sorted list
#Works on any iterable (lists, tuples, strings, etc.).

#Does not change the original iterable.

#Useful when you need a sorted result but want to keep the original.
