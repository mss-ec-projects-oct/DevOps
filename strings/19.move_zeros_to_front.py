#!/bin/bash

def move_zeros_to_front(s):
    non_zeros = [ch for ch in s if ch != '0']
    zeros = [ch for ch in s if ch == '0']
    
    result = ''.join(zeros + non_zeros)
    return result

#Example Usage
string = '32400121200'
output = move_zeros_to_front(string)
print(output)

#Notes:
#''.join(str1 + str2)
