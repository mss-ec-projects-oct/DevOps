#For loop
PLANET = "Earth"
for i in PLANET:
    print(i)
    print("value of i is",i)
print("Rest of the code")

VACCINES = ("Moderna","Pfizer","Sputnik","Covaxin","Adtazentia")
for vac in VACCINES:
    print(f"{vac} vaccine provides immunization against covid19")

VACCINES = ["Moderna","Pfizer","Sputnik","Covaxin","Adtazentia"]
for vac in VACCINES:
    print(f"{vac} vaccine provides immunization against covid19")

#while loop
x = 0
while x <= 10:
    print("value of x is:", x)
    print("Looping")
    x += 1
print("Rest of the code.")

# Nested Loop
VACCINES = ["Moderna","Pfizer","Sputnik","Covaxin","Adtazentia"]
for vac in VACCINES:
    print("I would like to take a shot of")
    for i in vac:
        print(i)

import time
i = 2
while True:
    print("value of x is:", i)
    print("Looping")
    i *= 2
    time.sleep(1)


