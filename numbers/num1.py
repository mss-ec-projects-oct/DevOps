#!/bin/python3

#1.Python program to Find Odd or Even number
def odd_even(n):
    n=int(n)
    if n % 2 == 0:
        print(f"{n} is a Even number")
    else:
        print(f"{n} is a Odd number")

num = 3.4
odd_even(num)
print("----------------------------------------")
#2. Python program to find Prime number
def prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

start = 1
end = 100
print(f"the prime numbers between {start} and {end} are: ")
for num in range(start, end+1):
    if prime(num):
        print(num, end=' ')
print(' ')
print("----------------------------------------")
#3. Python program to find Fibonacci series upto a given number range
def fibonacci(n):
    a = 0
    b = 1
    fibo = []
    while a <= n:
        fibo.append(a)
        a,b = b,a+b
    return fibo

n = 5
print(f"Fibonacci series upto {n} are: {fibonacci(n)}", end=' ')
print(' ')
print("----------------------------------------")
#4. Python program to swap two numbers without using third variable
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(f"swap of a: {a}")
    print(f"swap of b: {b}")

a=2
b=3
swap(a,b)
print("----------------------------------------")
#5. Python program to Find Factorial on given Number
def fact(n):
    a = 1
    for i in range(1,n+1):
        a = i * a
    return a

n = 6
print(f"factorial of {n} is: {fact(n)}")
print("----------------------------------------")
