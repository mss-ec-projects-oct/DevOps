# variable length arguments **kwargs (keyword arguments)
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

time_activity(10,20,30, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
