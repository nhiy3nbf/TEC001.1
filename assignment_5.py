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
def prime():
    a = int(input("Enter a number: "))
    b = 0
    for i in range(1, a + 1):
        if a % i == 0:
            b += 1
    if b == 2:
        print(a, "is a prime number.")
    else:
        print(a, "is not a prime number.")
#prime()

#3
def city():
    a = []
    for i in range(5):
        b = input("Enter a city: ")
        a.append(b)
    for o in a:
        print(o)
#city()

#4
#1, 2, 3, 4, 5, 6, 7, 8, 9
def sum():
    a = input("Enter a list of number: ")
    b = 0
    for i in a.split(","):
        b += int(i)
    return b
print(sum())

#5
#1, 2, 3, 4, 5, 6, 7, 8, 9
def odd():
    a = input("Enter list of numbers: ")
    b = []
    for i in a.split(","):
        b.append(int(i))
    c = []
    for o in b:
        if o % 2 == 0:
            c.append(o)
    print("The original:", b)
    print("The cut-down:", c)
#odd()