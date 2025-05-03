#!/bin/python3

def a2b2c3d2(s):
    if not s:
        return ""

    result = []
    count = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)

#Example usage
input_str = "aabbcccdd"
output = a2b2c3d2(input_str)
print(output)

#Notes:
#if not s: => handle edge cases safely and prevent index errors
#List result.append(s[i-1] + str(count)) => ['a2', 'b2', 'c3', 'd2'] 
