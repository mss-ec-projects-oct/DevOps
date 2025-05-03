#!/bin/python3

input_str = "Subbu123raj"
alphabets = ''.join([char for char in input_str if char.isalpha()])
digits = ''.join([char for char in input_str if char.isdigit()])

#Print the results
print(alphabets)
print(digits)

#Notes:
#single line ''.join([])
