#!/bin/python3

def oddeven():
    num=int(input("Enter the number: "))
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

#oddeven()

def prime():
    num=int(input("Enter the number: "))
    if num > 1:
        for i in range(2,int(num ** 0.5) +1):
            if num % i == 0:
                print(f"{num} is not a prime number")
                break
        else:
            print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

#prime()

def fibonacci():
    max_range=int(input("Enter the maximum value for the fibanocci sequence: "))
    print(f"fibanocci sequence upto {max_range}")
    a=0
    b=1
    while a <= max_range:
        print(a,end=' ')
        a,b=b,a+b
#fibonacci()

def swap_two():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(f"Before swapping: a={a} and b={b}")
    a=a+b
    b=a-b
    a=a-b
    print(f"After swapping: a={a} and b={b}")

#swap_two()

def factorial():
    num=int(input("Enter the number: "))
    factorial=1
    if num < 0:
        print("Factorial does not exist for negative numbers.")
    elif num ==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,num+1):
            factorial *= i
        print(f"factorial of {num} is: {factorial}")

#factorial()

def reverse(n):
    reversed_num=0
    is_negative=n<0
    #print(is_negative)  #true/false
    n=abs(n)
    while n !=0:
        digit=n%10
        reversed_num=reversed_num*10+digit
        n//=10
    return -reversed_num if is_negative else reversed_num

#num=int(input("Enter a number: "))
#print(f"Reversed number: {reverse(num)}")

def is_armstrong(num):
    num_str=str(num)
    power=len(num_str)
    total=sum(int(digit) ** power for digit in num_str)
    return total == num

#num=int(input("Enter a number: "))
#if is_armstrong(num):
#    print(f"{num} is an armstrong number.")
#else:
#    print(f"{num} is not an armstrong number.")


def count_digits(n):
    n=abs(n)
    #total=len(str(n))
    #return total
    count=0
    if n==0:
        return 1
    while n>0:
        n //= 10
        count += 1
    return count

#num=int(input("Enter a number: "))
#print("Number of digits",count_digits(num))

def is_palindrome(n):
    #n_str=str(n)
    #return n_str==n_str[::-1]
    original=n
    reverse=0
    while n !=0:
        digit=n%10
        reverse=reverse*10+digit
        n//=10
    return original==reverse
#num=int(input("Enter a number: "))
#if is_palindrome(num):
#    print(f"{num} is a palindrome number")
#else:
#    print(f"{num} is not an palindrome number")

def sum_of_digits(n):
    n_str=str(abs(n)).replace('.','')
    total=sum(int(digit) for digit in n_str if digit.isdigit())
    return total
   # digit=0
   # while n!=0:
      #  digit+=n%10
     #   n//=10
    #return digit
num=int(input("Please enter a num: "))
print(f"sum of digits in a {num}: {sum_of_digits(num)}")
