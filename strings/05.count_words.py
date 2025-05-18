#!/bin/python3

def count_words(string):
    words = string.split()
    return len(words)

#Example usage
string = "Hello, How are you doing today!"
print(count_words(string))
