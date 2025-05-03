#!/bin/python3

#Python program that removes duplicate letters, but keeps the first occurrence
#set(), .add(char)

def print_unique_characters(text):
    seen = set()
    result = ""
    for char in text:
        if char not in seen or char == " ":
            if char != " ":
                seen.add(char)
            result += char
    print(result)


#Example usage
text="Java Automation Learning"
print_unique_characters(text)

#notes
#---------
#dic = {}
#if "a" not in dic: a is a key not a value 
#   dic[a] = 1
