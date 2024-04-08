# import tkinter
#
# root = tkinter().Tk()
def sum(a: int, b: int) -> int:
    """
    Сумма чисел
    :param a:
    :param b:
    :return:
    """
    return a + b

sum(1, 2)
print(sum("1", "2"))

razn = sum
print(razn(1, 2))





def decor(fn):
    def begin():
        a = "People"
        print(f"{a}")

    def end():
        a = "Bye bye"
        print(f"{a}")

    def wraper(t = "Hello World"):
        begin()
        fn(t)
        end()
        print()
        # print("<---------->")
        # fn(t)
        # print("<---------->")

    return wraper

@decor
def text(t):
    print(t)


text()
text("lol")





class Property(object):
    "Эмуляция PyProperty_Type() в Objects/descrobject.c"

    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.__doc__ = doc

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self

        if self.fget is None:
            raise AttributeError("нечитаемый атрибут")

        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("не могу установить атрибут")

        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("не могу удалить атрибут")

        self.fdel(obj)


obj = Property(1, 2, 3, 'lol')

print(obj.fget)
print(obj.fset)
print(obj.fdel)
print(obj.__doc__)
print()




class C(object):
    def getx(self):
        return self.__x
    def setx(self, value):
        self.__x = value
    def delx(self):
        del self.__x
    x = property(getx, setx, delx, "Я свойство 'X'.")

ob = C()
ob.setx(10)
print(ob.getx())
print(ob.__doc__)
print(ob.delx())
print(ob.__doc__)











import datetime

dt = datetime.datetime.now()
print(dt.time())
print(dt.date())
print(dt.time())
print(dt.timestamp())

date = datetime.date(year=2024, month=12, day=31)
print(date)



delta = datetime.timedelta(days = 10, hours=10, milliseconds=100000)
print(dt - delta)

print()

import time


st = datetime.datetime.now().timestamp()
print(st, 'start')
end = datetime.datetime.now().timestamp()
print(st - end, "end")



t = time.time()
print(t)
time.sleep(2)
t2 = time.time()
print(t-t2) # ДЛЯ ДЗ