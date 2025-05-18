#!/bin/python3

import itertools

def find_permutations(s):
    perms = itertools.permutations(s)
    return [''.join(p) for p in perms]

#Example usage
string = "abca"
permutations = find_permutations(string)

print("all permutations: ")
for p in permutations:
    print(p)
