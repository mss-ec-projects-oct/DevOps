#Python program to Reverse Number
def rev_num(n):
    #n = str(n)
    #return n[::-1]
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

n = 12345
print(f"reverse number of {n} is: {rev_num(n)}")
print("-------------------------------")
#Python program to find Armstrong Number
def armstrong(n):
    n = str(n)
    count = len(n)
    total = sum(int(i) ** count for i in n)
    return total

n = 153
if n == armstrong(n):
    print(f"{n} is a Armstrong number")
else:
    print(f"{n} is not a Armstrong number")
print("-------------------------------")
#Python program to find number of digits in given number
def no_of_digits(n):
    n = abs(n)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count
n = -123
print(f"no of digits in {n} is {no_of_digits(n)}")
print("-------------------------------")
#Python program to find Palindrome number
def palindrome(n):
    a = n
    rev_num = 0
    if a < 0:
        return False
    while a > 0:
        last_digit = a % 10
        rev_num = rev_num * 10 + last_digit
        a //= 10
    return n == rev_num
n = 1221
if palindrome(n):
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")
print("-------------------------------")
#Python program to calculate the sum of digits of a number
