#1
class car:
    def __init__(self, rn, ms):
        self.rn = rn
        self.ms = ms
        self.cs = 0
        self.td = 0
#2
    def accelerate(self, speed):
        self.cs = self.cs + speed
        if self.cs > self.ms:
            self.cs = self.ms
        elif self.cs < 0:
            self.cs = 0
#3
    def drive(self, hours):
        distance = self.cs * hours
        self.td += distance
#4
import random
a = []
for i in range(1,11):
    b = car(f"ABC-{i}", random.randint(150, 200))
    a.append(b)
c = True
while c == True:
    for b in a:
        b.accelerate(random.randint(-10, 15))
        b.drive(1)
        if b.td >= 10000:
            c = False
a.sort(key=lambda d: d.td, reverse=True)
for b in a:
    print(f"Registration number: {b.rn}, Maximum speed: {b.ms}, Final current speed: {b.cs}, Final travelled distance: {b.td}")

#test
#a = car("ABC-123", 142)
#print("Registration number:", a.rn)
#print("Maximum speed:", a.ms, "km/h")
#a.accelerate(30)
#a.drive(1.5)
#a.accelerate(70)
#a.accelerate(50)
#a.accelerate(-200)
#print("Final current speed:", a.cs, "km/h")
#print("Final travelled distance:", a.td)