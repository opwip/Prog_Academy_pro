# Task 1
class Bill:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):
        return self.__getattr__("balance")

    def __setattr__(self, key, value):
        if key == "balance":
            raise AttributeError("NO DIRECT CHANGE")
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == "balance":
            raise AttributeError("NOt exists")
        elif item in self.__dict__:
            return self.__dict__[item]

    def __str__(self):
        return f"{self.__balance}"


Billy = Bill(129)
Billy.weight = 123
print(Billy.weight)
print(Billy)


# Task 2

class User:
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname

    @property
    def first_name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__surname

    def __setattr__(self, key, value):
        if key in ("name", "surname",):
            raise TypeError("No direct change")
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item not in self.__dict__:
            raise AttributeError("Not exists")

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"


Billgates = User("Bill", "Gates")
Billgates._User__name = "Kola"
print(Billgates.__dict__)
print(Billgates)


# Task 3

class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __setattr__(self, key, value):
        if key in ("wight", "height",):
            raise AttributeError("No direct change")
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item not in self.__dict__:
            raise AttributeError("Secret")

    def __str__(self):
        return f"{self.width}, {self.height}"

    def area(self):
        return self.height * self.width


rec = Rectangle(100, 100)
print(rec.area())
print(rec.height)
