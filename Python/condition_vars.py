"""
This script will implement our knowledge on
conditions and different datatypes
"""

DevOps = ["Jenkins", "Ansible","Bash","Puppet","Docker","Kubernetes"]
Development = ("Java", "Nodejs", "Angularjs", ".net")
cntr_emp1 = {"Name": "Santa","Skill":"Block chain","Code": 1024}
cntr_emp2 = {"Name": "Rocky", "Skill": "AI", "Code": 1218}

usr_skill = input("Enter your desired skill: ")
#print(usr_skill)

#check in the database if we have this skill

if usr_skill in DevOps:
    print(f"we have {usr_skill} in the DevOps Team.")
elif usr_skill in Development:
    print(f"we have {usr_skill} in the Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"we have contract employees with {usr_skill} skill.")
else:
    print("skill not found")
    print("Please check if you have entered value in capatalise or check the spelling")