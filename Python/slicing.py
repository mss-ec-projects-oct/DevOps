planet1 = "Closet of the Sun"

print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

#slicing a string, get a substring from a string
print(planet1[1:4])
print(planet1[:])
print(planet1[:7])
print(planet1[14:])

#slicing tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")

print(devops[0])
print(devops[1])
print(devops[4])

print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

#slicing a List
devops = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]

print(devops[0])
print(devops[1])
print(devops[4])

print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

#Dictionary Example
skills = {"DevOps": ("AWS", "Jenkins", "Python", 1), "Development": ["Java", "NodeJS", ".net"]}

print(skills)
print(skills["DevOps"])
print(skills["Development"])
print(skills["DevOps"][-1])
print(skills["DevOps"][:4])