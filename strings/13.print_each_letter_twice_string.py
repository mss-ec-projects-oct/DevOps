#!/bin/python3

#Print each letter twice from a given string

def print_each_letter_twice(text):
    double = ''.join([a * 2 for a in text])
    return double

#Eample usage:
text="hello"
print(print_each_letter_twice(text))


#Notes:
#-------
#list = [a * 2 for a in text]

