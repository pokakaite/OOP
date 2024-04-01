# class Car:
#     counter = 0
#     def __init__(self, name = "Vaz", year = 2000):
#         self.__name = name
#         self.__year = year
#         Car.counter += 1
#         # не self.counter += 1, чтобы сработало
#
#     def editName(self):
#         self.__name = input("Укажите имя - ")
#
#     def editYear(self):
#         self.__year = input("Укажите год - ")
#
#     def showName(self):
#         print(self.__name)
#
#     def showYear(self):
#         print(self.__year)
#
# auto1 = Car(year = 2020, name = "Gaz11")
# print(auto1.__dict__, auto1.counter)
# auto2 = Car(year = 2020, name = "Gaz22")
# print(auto2.__dict__, auto2.counter)
# auto3 = Car(year = 2020, name = "Gaz33")
# print(auto3.__dict__, auto3.counter)


# print(auto1.__dict__, auto1.counter)
# print(auto2.__dict__, auto2.counter)
# print(auto3.__dict__, auto3.counter)

# print(auto.__dict__)
# print(auto._Car__name)
# # print(auto.__year) защищенный
# print(auto._Car__year)
#
# auto.color = "green"
#
# print(auto.color)
#
# auto.__status = 'good'
# print(auto.__status)
# print(auto.__dict__)

# auto1 = Car()
# print(auto1.__dict__)




# class ExampleClass:
#     def __init__(self, val):
#         if val % 2 != 0:
#             self.a = 1
#         else:
#             self.b = 2
#
# exampleObject = ExampleClass(1)

# print(exampleObject.a)



# try:
#     print(exampleObject.b)
# except AttributeError:
#     print("error")



# if hasattr(exampleObject, 'b'):
#     print(exampleObject.b)
#
# if hasattr(exampleObject, 'a'):
#     print(exampleObject.a, 'wdd')



# class ExampleClass:
#     a = 1
#     def __init__(self):
#         self.b = 2
#
# exampleObject = ExampleClass()
#
# print(hasattr(exampleObject, 'b'))
# print(hasattr(exampleObject, 'a'))
# print(hasattr(ExampleClass, 'b'))
# print(hasattr(ExampleClass, 'a'))



class Car:
    counter = 0
    year = 1950
    color = 'green'
    price = 20000
    def __init__(self, name = "Vaz", year = 2000):
        self.__name = name
        self.__year = year
        self.status = "good"
        Car.price = 30000
        Car.counter += 1
        # не self.counter += 1, чтобы сработало

    def editName(self):
        self.__name = input("Укажите имя - ")

    def editYear(self):
        self.__year = input("Укажите год - ")

    def showName(self):
        print(self.__name)

    def showYear(self):
        print(self.__year)

auto = Car()
print(Car.year)
print(Car.price)
print(hasattr(Car, 'status'))
print(hasattr(auto, 'status'))
print(hasattr(Car, 'price'))
print(hasattr(auto, 'price'))
print(hasattr(Car, 'color'))
print(hasattr(auto, 'color'))
auto.showYear()




# class Classy:
#     varya = 1
#     def __init__(self):
#         self.var = 2
#
#     def method(self):
#         pass
#
#     def __hidden(self):
#         pass
#
# obj = Classy()
# print(obj.__dict__)
# print(Classy.__dict__)



# class Classy:
#     pass
#
# print(Classy.__name__)
#
# obj = Classy()
# print(type(obj).__name__)



class Calc:
    pass
    def __str__(self, a, b):
        return a * b

c = Calc()
print(c.__str__(2, 3))













