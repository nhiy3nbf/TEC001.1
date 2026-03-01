#1
def course():
    a = input("Write your course codes: ")
    if len(a) == 6:
        if a[0:3].isupper():
            if a[3:6].isdigit():
                print("Ok")
                return True

            else:
                return False
        else:
            return False
    else:
        return False
#course()

#2
def check(a):
    b = ["a", "b", "c", "d", "e", "f"]
    for i in b:
        if a == i or a == i.upper():
            return True
def hexcolor():
    a = input("Enter your hexcolor: ")
    b = 0
    if len(a) == 7:
        if a[0] == "#":
            for i in a[1:]:
                if i.isdigit():
                    b += 1
                elif check(i) == True:
                    b += 1
                else:
                    print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
    if b == 6:
        print("Valid")
#hexcolor()

#3
import re
def total():
    a = input("Enter a paragraph: ")
    b = re.findall('[0-9]+', a)
    print(b)
    c = 0
    for i in b:
        c = c + int(i)
    print(c)
#total()

#4
def sdt():
    a =input("Enter a document: ")
    print(re.sub(r'[0-9]{10}|\+84[0-9]+', '[REDACTED]', a))
sdt()