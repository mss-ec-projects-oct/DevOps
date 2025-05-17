#!/bin/python3

def rev_each_word(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

#Example usage
string = "Hello World!"
print('rev_each_word is: ', rev_each_word(string))
