#!/bin/python3

def move_zeros_to_end(s):

    non_zero_char = [char for char in s if char != '0']
    count_zero = s.count('0')
    result = ''.join(non_zero_char) + '0' * count_zero

    return result

#Example usage
string = "324000121200"
output = move_zeros_to_end(string)
print(output)

#Notes:
#str.count('char')
