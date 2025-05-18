#!/bin/python3

def are_anagrams(str1,str2):
    str1 = str1.replace(' ','').lower()
    str2 = str2.replace(' ','').lower()

    return sorted(str1) == sorted(str2)

#Example usage:
string1 = "manoj"
string2 = "anojm"

if are_anagrams(string1,string2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
