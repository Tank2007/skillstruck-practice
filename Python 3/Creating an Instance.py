"""
class Person:    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species


userinput_name = input("Enter a name: ")
user_input_age = input("Enter your age: ")
user_input_gender = input("Enter your gender: ")


userinput_name2 = input("Enter a name: ")
user_input_age2 = input("Enter your age: ")
user_input_gender2 = input("Enter your gender: ")






p1 = Person(userinput_name, user_input_age, user_input_gender)
p2 = Person(userinput_name2, user_input_age2, user_input_gender2)

print("Person 1: " +p1.name + " " + p1.age + " " + p1.gender)
print("person 2: " +p2.name + " " + p2.age + " " + p2.gender)"""



'''class Hat:
    def __init__(self, kind, color, material):
        self.kind = kind 
        self.color = color
        self.material = material

myObject = Hat(kind="Fedora", color="Black", material="Wool")

print("hat: " + myObject.kind + " " + myObject.color + " " + myObject.material)'''

'''class pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

myObject = pet(name="Tango", species="green neck parrot", age="4")
myObject2 = pet(name="cricket", species="", age="2")
myObject3 = pet(name="tiki", species="green_cheek_conure", age="3")

print("pet: " + myObject.name + " " + myObject.species + " " + myObject.age)

print("pet: " + myObject2.name + " " + myObject2.species + " " + myObject2.age)

print("pet: " + myObject3.name + " " + myObject3.species + " " + myObject3.age)'''


class vacation:
    def __init__(self, location, activity , food):
        self.location = location
        self.activity = activity
        self.food = food
myObject = vacation(location="Poland", activity="looking_around", food="Pierogi")

myObject2 = vacation(location="germany", activity="looking_around", food="Rouladen ")

myObject3 = vacation(location="estoina", activity="looking_around", food="rye_bread")

print("Vacation: " + myObject.location + " " + myObject.activity + " " + myObject.food)

print("Vacation: " + myObject2.location + " " + myObject2.activity + " " + myObject2.food)

print("Vacation: " + myObject3.location + " " + myObject3.activity + " " + myObject3.food)