import random

def time_activity(*args, **kwargs):
    #print(args)
    #print(kwargs)
    min = sum(args) + random.randint(0,60)
    print(min)
    #print(kwargs.keys())
    choice = random.choice(list(kwargs.keys()))
    print(choice)
    print(f"you have to spent {min} minutes for {kwargs[choice]}")

def order_food(min_order, *args):
        print(f"you have ordered: {min_order}")
        for item in args:
            print(f"you have ordered: {item}")
        print("your food will be delivered in 30 mins: ")
        print("Enjoy the party")

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