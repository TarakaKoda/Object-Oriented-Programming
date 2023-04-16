# Duck typing and Easier to ask forgiveness than permission (EAFP)

class Duck:
    def quack(self):
        print("Quack, quack")

    def fly(self):
        print("Flop, flop")


class Person:
    def quack(self):
        print("I'm quacking like a duck")

    def fly(self):
        print("I'm flopping my arms")


def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        print()
        thing.bark()

    except AttributeError as e:
        print(e)


d = Duck()
# quack_and_fly(d)

p = Person()
# quack_and_fly(p)

# Example 1:

person: dict = {

    "name": "srinu",
    "age": 22,
    "salary": 50000
}
# This is a non pythonic way
if "name" in person and "age" in person and "salary" in person:
    print(f'Hi my name is {person["name"]}, im {person["age"]} years old and i have an annual salary of {person["salary"]:,.2f}')
else:
    print(f"Missing some Keys")


# Pythonic way
try:
    print(f"Name: {person['name']}\nAge: {person['age']}\nSalary: {person['Salary']}")
except KeyError as e:
    print(f"Missing {e} key")

# Example 2:

# This is a non pythonic way
my_list = [x for x in range(2)]

if len(my_list) >= 6:
    print(my_list[5])
else:
    print("IndexError")

# Pythonic way:
try:
    print(my_list[5])
except IndexError as e:
    print(f"{e}")
    
# Example from the Python Docs

import os

my_file = "C:\\Users\\PAVAN\\PycharmProjects\\pythonProject1\\Python\\Getting Started with Python\\Minesweeper-with-Tkinter-using-OOP\\settings.py"
# Non Pythonic way
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print(f"File can ot be accessed")

# Pythonic way
try:
    f = open(my_file)
except IOError as e:
    print(f"{e}")
else:
    with f:
        print(f.read())
