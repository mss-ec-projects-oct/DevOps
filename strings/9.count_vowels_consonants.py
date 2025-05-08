#!/bin/python3

def count_vowels_and_consonants(s):
    s = s.replace(' ','')
    vowels = "aeiouAEIOU"
    count_v = 0
    count_c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                count_v += 1
            else:
                count_c += 1
    
    return count_v, count_c

#Example usage:
string = "Apple1 "
vowels,consonants = count_vowels_and_consonants(string)
print("count of vowels: ",vowels)
print("count of consonants: ", consonants)

#Notes:
#--------
#vowels is in string, not require list.
#spaces handle: s.replace(' ','')
#char isalpha() cheack to avoid numbers.
