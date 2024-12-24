# Defining Functions
def add(arg1, arg2):
    total = arg1 + arg2
    return total

out = add(2, 3)
print(out)
print(add(5, 7))

def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)
adder(10, 15)
print(adder(10,20))


def summ(arg):
    x = 0
    for i in arg:
        x = x + i
    return x

out = summ([10,20,30])
print(out)

#Default Argument
def greetings(MSG="Morning"):
    print(f"Good {MSG}")
    print("Welcome to the function")
greetings()
greetings("Evening")

# keyword Arguments
def vac_feedback(vac, efficacy):
    print(f"{vac} vaccine is having {efficacy}% efficacy")
    if (efficacy>50) and (efficacy<=75):
        print("seems not so effective, needs more trail.")
    elif (efficacy>75) and (efficacy<90):
        print("can consider this vaccine.")
    elif efficacy >= 90:
        print("Sure, will take the shot.")
    else:
        print("needs many more trails")

#vac_feedback("pfizer", 95)
#vac_feedback(45,"unknown")
vac_feedback(efficacy=45, vac="unknown")

