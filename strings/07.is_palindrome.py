#!/bin/python3

def is_palindrome(s):
    s = s.replace(' ','').lower()
    return s == s[::-1]

#Example usage:
text = "Madam"

if is_palindrome(text):
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")
