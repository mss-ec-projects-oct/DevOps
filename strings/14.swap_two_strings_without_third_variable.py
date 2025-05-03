#!/bin/bash

# swap two strings without using a third variable
def swap_two_strings(string1,string2):
    string1 = string1 + string2
    string2 = string1[:len(string1) - len(string2)]
    string1 = string1[len(string2):]
    
    print("string1", string1)
    print("string2", string2)

#Example usage
string1 = "manoj"
string2 = "peddamallu"
swap_two_strings(string1,string2)
