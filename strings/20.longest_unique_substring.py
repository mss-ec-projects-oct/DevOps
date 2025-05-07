#!/bin/python3

def longest_unique_substring(s):
    start = 0
    max_len = 0
    seen = {}

    for end,char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1 #slicing first a
        seen[char] = end #add to the dictionary
        current_len = end - start + 1 #bca =3
        if current_len > max_len:
            max_len = current_len
            max_substr = s[start:end+1]

    return max_substr, max_len

#Example usage:
inp_str = "abcabcbb"
substr,length = longest_unique_substring(inp_str)

print("Longest substring: ",substr)
print("Length: ",length)


#abcab
