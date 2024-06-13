# *args
def add(*args):
    summ = 0
    for i in args:
        summ += i
    return summ


print(add(3, 4, 5))


# **kwargs
def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


calculate(5, add=5, mul=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Audi", model="A8")
print(my_car.make)
print(my_car.model)
