class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy

    def __str__(self):
        return f"{self.name} is in {self.galaxy}"


sun = Star("Sun", "Milky Way")
sun2 = Star("Sun2", "Milky Way")

print(sun)
print(sun2)


class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class TrackedVehicle(LandVehicle):
    pass


print(issubclass(TrackedVehicle, Vehicle))

myVehicle = Vehicle()
myLandVehicle = LandVehicle()
myTrackedVehicle = TrackedVehicle()

for obj in [myVehicle, myLandVehicle, myTrackedVehicle]:
    for cls in [Vehicle, LandVehicle, TrackedVehicle]:
        print(isinstance(obj, cls), end="\t")
    print()


class SampleClass:
    def __init__(self, val):
        self.val = val


ob1 = SampleClass(0)
ob2 = SampleClass(2)
ob3 = ob1
ob3.val += 1
print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)
print(ob1.val, ob2.val, ob3.val)
str1 = "Mary had a little "
str2 = "Mary had a little lamb"
str1 += "lamb"
print(str1 == str2, str1 is str2)


class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)
    # а можно тупа pass


obj = Sub("Andy")
print(obj)


class Super:
    def __init__(self):
        self.supVar = 11


class Sub(Super):
    def __init__(self):
        super().__init__()
        self.subVar = 12


obj = Sub()
print(obj.subVar)
print(obj.supVar)


class Level1:
    varia1 = 100

    def __init__(self):
        self.var1 = 101

    def fun1(self):
        return 102


class Level2(Level1):
    varia2 = 200

    def __init__(self):
        super().__init__()
        self.var2 = 201

    def fun2(self):
        return 202


class Level3(Level2):
    varia3 = 300

    def __init__(self):
        super().__init__()
        self.var3 = 301

    def fun3(self):
        return 302


obj = Level3()
print(obj.varia1, obj.var1, obj.fun1())
print(obj.varia2, obj.var2, obj.fun2())
print(obj.varia3, obj.var3, obj.fun3())


class SuperA:
    varA = 10

    def funA(self):
        return 11


class SuperB:
    varB = 20

    def funB(self):
        return 21


class Sub(SuperA, SuperB):
    pass


obj = Sub()
print(obj.varA, obj.funA())
print(obj.varB, obj.funB())


class One:
    def doit(self):
        print("Do it form One")

    def doanything(self):
        self.doit()


class Two(One):
    def doit(self):
        print("Do it from Two")


one = One()
two = Two()
one.doanything()
two.doanything()
















