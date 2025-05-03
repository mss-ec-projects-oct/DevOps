#!/bin/python3

#Python program that prints the characters at even indexes of a string:
def print_even_index(text):
    for i in range(0, len(text), 2):
        print(text[i],end=' ')
    print()

print_even_index("manoj kumar Reddy")
