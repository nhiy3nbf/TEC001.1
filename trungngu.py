def divisible_3():
    a = 0
    while a < 1001:
        if a % 3 == 0:
            print(a)
        a += 1
#divisible_3()

def convert():
    while True:
        b = int(input("Converts inches to centimeters: "))
        if b >= 0:
            print("Converted:", b * 2.54)
        else:
            break
#convert()

def compare():
    a = []
    while True:
        b = input("Enter a number: ")
        if b =='':
            break
        try:
            a.append(int(b))
        except:
            print("Invalid input")
            continue

    print("Smallest:", min(a))
    print("Largest:", max(a))
#compare()

import random
def guess():
    a = random.randint(1, 10)
    while True:
        b = int(input("Guess the number: "))
        if b == a:
            print("Correct")
            break
        elif b > a:
            print("Too high")
        else:
            print("Too low")
#guess()

#The correct username is python and password rules.
def login():
    print("Please enter yor username and password")
    a = 0
    while a < 5:
        b = input("Enter username: ")
        c = input ("Enter password: ")
        if b == 'python' and c == 'rules':
            break
        else:
            a += 1
            print("Wrong username or password, try again")
    if a == 5:
        print("Access Denied")
    else:
        print("Welcome")
#login()

def median():
    a = input("Enter somthing: ")
    b = list(a)
    c = len(b) // 2
    if c % 2 == 0:
        print(b[c:c+1])
        del b[c:c+1]
        print("".join(b))
    else:
        print(b[c])
        del b[c]
        print("".join(b))
#median()

def acronym():
    a = input("Enter somthing: ")
    b = ""
    for i in a.split():
        b = b + i[0]
    print(b.upper())
#acronym()