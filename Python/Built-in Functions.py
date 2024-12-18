# string Build in Methods/Functions
message = "corona vaccine is ready to use, most of them are more than 90% effective"
print(message)
print(message.capitalize())
Message = message.capitalize()
print(Message)

# dir() function
print(dir(""))
print(dir([]))
print(dir(()))
print(dir({}))

print(message.upper())
print(message.islower())
print(message.isupper())
print(message.find("ready"))
print(message[18:24])
print(message.find("not"))

seq1 = ("192", "168", "40", "90")

print(".".join(seq1))
print("-".join(seq1))

mountains = ["Everest", "Himalaya", "sahyadri", "Alps", "k2", "mt Hood"]
print(mountains)
mountains.append("oregon mount")
print(mountains)
mountains.extend(["Mt Rainer", "satpuda"])
print(mountains)
mountains.insert(2,"Mt Apu")
print(mountains)
mountains.pop()
print(mountains)
mountains.pop(5)
print(mountains)

cntr_emp1 = {"name":"manoj", "skill":"DevOps","code":"1048"}
print(cntr_emp1.keys())
print(cntr_emp1.values())
cntr_emp1.clear()
print(cntr_emp1)
