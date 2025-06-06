#1.Python program to Find Odd or Even number  
```
def odd_even(n):
    n=int(n)
    if n % 2 == 0:
        print(f"{n} is a Even number")
    else:
        print(f"{n} is a Odd number")

num = 3.4
odd_even(num)
```
#2. Python program to find Prime number  
```
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
```
#3. Python program to find Fibonacci series upto a given number range  
```
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
```
#4. Python program to swap two numbers without using third variable  
```
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    print(f"swap of a: {a}")
    print(f"swap of b: {b}")

a=2
b=3
swap(a,b)
```
#5. Python program to Find Factorial on given Number  
```
def fact(n):
    a = 1
    for i in range(1,n+1):
        a = i * a
    return a

n = 6
print(f"factorial of {n} is: {fact(n)}")
```
#6. Python program to Reverse Number  
```
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
```
#7. Python program to find Armstrong Number  
```
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
```
#8. Python program to find number of digits in given number  
```
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
```
#9. Python program to find Palindrome number  
```
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
```
#10. Python program to calculate the sum of digits of a number
```
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        x = n % 10
        total += x
        n //= 10
    return total
n = -12345
print(f"sum of digits {n}: {sum_of_digits(n)}")
```
