# class First:
#     pass
#
# f = First()
#
# print(f)






# stack = []

# def push(val):
#     stack.append(val)
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
#
# push(3)
# push(2)
# push(1)
# print(pop())
# print(pop())
# print(pop())






# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
# stackObject = Stack()
# stackObject2 = Stack()
# print(stackObject)
# print(stackObject2)





# class Stack:
#     def __init__(self):
#         self.__stackList = []
#
#     def push1(self, val):
#         self.__stackList.append(val)
#
#     def pop1(self):
#         val = self.__stackList[-1]
#         del self.__stackList[-1]
#         return val
#
# stackObject = Stack()
# stackObject2 = Stack()
# stackObject.push1(3)
# stackObject2.push1(stackObject.pop1())
# print(stackObject2.pop1())
#
# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
#
#     def getSum(self):
#         return self.__sum
#
#     def push(self, val):
#         self.__sum += val
#         Stack.push1(self, val)
#
#     def pop(self):
#         val = Stack.pop1(self)
#         self.__sum -= val
#         return val
#
# stackObject = AddingStack()
# for i in range(5):
#     stackObject.push(i)
#     print(stackObject.getSum())
#
# for i in range(5):
#     print(stackObject.pop())
#
print('\n' * 10)









# class Animals:
#     def __init__(self):
#         print("Это животное умеет ходить.")
#
# class Animal(Animals):
#     def __init__(self):
#         Animals.__init__(self)
#         self.__walk = "Ходит на четырёх лапах."
#         print(self.__walk)
#
#     def meow(self):
#         return print("Умеет мяукать.")
#
# Cat = Animal()
# Cat.meow()
# print('\n' * 3)
#
#
#
#
#
#
#
# class Animals:
#     def __init__(self):
#         print("Это животное умеет ходить.")
#
# class Animal(Animals):
#     def __init__(self, val):
#         Animals.__init__(self)
#         self.__walk = f"Ходит на {val}."
#         print(self.__walk)
#
#     def meow(self, val):
#         return print(f"Умеет {val}.")
#
# Cat = Animal("четырёх лапах")
# Cat.meow("мяукать")






class Animal:
    def __init__(self):
        self.nogi = 0
    def walk(self):
        return print(f"Я хожу на {self.nogi} ногах")

class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.say = "Miya"
    def talk(self):
        return print(self.say)

caty = Cat()
caty.say = "GAV"
caty.talk()
caty.nogi = 4
caty.walk()

