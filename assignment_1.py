def greet():
    name = input("Write your name: ")
    print("Hello", name)
#greet()

import math
def circumference():
    radius = float(input("Write your radius: "))
    print("Circumference of the circle:", math.pi * radius * 2)
#circumference()

def rectangle():
    length = int(input("Write your length of the rectangle: "))
    width = int(input("Write your width of the rectangle: "))
    print("Perimeter of the rectangle:", length * 2 + width * 2)
    print("Area of the rectangle:", length * width)
#rectangle()

def numbers():
    a = int(input("Write your first numbers: "))
    b = int(input("Write your second numbers: "))
    c = int(input("Write your third numbers: "))
    print("Sum: ", a + b + c)
    print("Product:", a * b * c)
    print("Average:", (a + b + c) / 3)
#numbers()

def medieval():
    talents = 8512 * float(input("Enter talents: "))
    pounds = 425.6 * float(input("Enter pounds: "))
    lots = 13.3 * float(input("Enter lots: "))
    total = talents + pounds + lots

    if total > 1000:
       kg = int(total / 1000)
       g = total - kg * 1000
    else:
        kg = 0
        g = total
    print("The weight in modern units:", kg, "kg and", g, "g")
#medieval()

import random
def password():
    three = ""
    for i in range(3):
        three += str(random.randint(0, 9))
    four = ""
    for i in range(4):
        four += str(random.randint(1, 6))
    print("3 digits password:", three)
    print("4 digits password:", four)
#password()
