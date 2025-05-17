#!/bin/python3

def duplicate_char(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    duplicates = [(char,count) for char,count in freq.items() if count > 1]
    return duplicates

#Example uage
string = "Hello World"
print("Duplicate characters: ", duplicate_char(string))
