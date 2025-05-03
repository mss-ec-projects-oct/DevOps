#!/bin/python3

#string.replace(' ','')

def remove_space_from_given_string(text):
    return text.replace(' ','')

#Example Usage:
string = input("Enter a string with spaces: ")
result = remove_space_from_given_string(string)
print("String without spaces: ", result)



#Notes:
#-----
#1.convert list to string:
#   str = ''.join(my_list)
