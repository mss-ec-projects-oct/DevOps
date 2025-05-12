#!/bin/python3

def count_occurance_of_each_char(s):
    s = s.replace(' ','')
    dic = {}
    for ch in s:
        if ch in dic:
            dic[ch] += 1
        else:
            dic[ch] = 1
    for char,count in dic.items():
        print(f"{char}: {count}")

#Example usage
string = "manoj kumar reddy"
count_occurance_of_each_char(string)
