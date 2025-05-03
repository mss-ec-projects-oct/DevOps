#!/bin/python3

def split_and_sort_letters(s):
    seen_lower = set()
    seen_upper = set()

    for char in s:
        if char.islower():
            seen_lower.add(char)
        elif char.isupper():
            seen_upper.add(char)
    lowercase = ''.join(sorted(seen_lower))
    uppercase = ''.join(sorted(seen_upper))

    return lowercase, uppercase

#Example Usecase
string = "aBACbcEDed"
lower, upper = split_and_sort_letters(string)
print(lower)
print(upper)

#Notes:
#A set is an unordered collection of unique elements.
#❌ set() does not return a list.
#✅ Use list(set(...)) or sorted(set(...)) to get a list if needed.
#char.islower(), char.isupper() returns boolean.
#seen_upper.add(char)
