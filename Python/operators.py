#Arithmetic Operators
x = 2
y = 5

total = x + y
print(total)

total = x - y
print(total)

total = x * y
print(total)

total = y / x
print(total)

total = y % x
print(total)

total = y ** x
print(total)

#comparison operators
a = 30
b = 60

out = a < b
print(out)

out = a > b
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a <= b)
print(out)

out = (a >= b)
print(out)

#Assignment Operators

c = 0
d = 10

c += d  # c = c + d
print(c)

c -= d  # c = c - d
print(c)

#Logical Operators
#and
#or

a = 40
b = 60

y = 3
x = 2

out = (a<b) or (y<x)
print(out)

out = (a>b) or (x>y)
print(out)

out = (a<b) and (x<y)
print(out)

out = not(x < y)
print(out)

#Membership Operator

first_tuple = ("str1", "DevOps", 47, "num1", 1.5)

ans = "DevOps" in first_tuple
print(ans)

ans = "DevOps" not in first_tuple
print(ans)

#Identity Operator
a = 12
b = 15

result = a is b
print(result)

result = a is not b
print(result)
