#1
def sorting():
    a = []
    while True:
        b = input("Enter number: ")
        if b == "":
            break
        a.append(int(b))
    a.sort(reverse=True)
    print("Five greatest numbers sorted in descending order:", a[0:5])
#sorting()

#2
def season():
    a = ("winter", "spring", "summer", "autumn")
    b = int(input("Enter number of months: "))
    print("Season: ", a[(b % 12)//3])
#season()

#3
def name():
    a = set()
    while True:
        b = input("Enter a name: ")
        if b == "":
            break
        elif b in a:
            print("Existing name")
        else:
            print("New name")
            a.add(b)
    print ("Names entered:", a)
#name()

#4
import re
def frequency():
    a = input("Enter text: ")
    b = re.findall('[a-z]+', a.lower())
    c = {}
    for o in b:
        if o in c:
            c[o] += 1
        else:
            c[o] = 1
    print("The frequency of a word in the text:", c)
frequency()

#5
def odd():
    a = input("Enter list of numbers: ")
    b = []
    for i in a.split():
        b.append(int(i))
    c = []
    for o in b:
        if o % 2 == 0:
            c.append(o)
    print("The original:", b)
    print("The cut-down:", c)
#odd()

