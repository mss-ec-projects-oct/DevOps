#!/bin/python3

class Person:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __eq__(self,other):
        if not isinstance(other, Person):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

#Example usage:
person1 = Person("Alice", 30)
person2 = Person("Alice", 30)
person3 = Person(25, "Bob")

print(person1 == person2) #True
print(person1 == person3) #False

# Using as keys in a dictionary (requires __hash__ and __eq__)
people_dic = {person1: "Engineer", person3: "Doctor"}
print(people_dic[person2]) # "Engineer", since person1 == person2
print(person1, person2, person3)
