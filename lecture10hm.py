import math


# Task 1
class Figure:
    def area(self):
        raise NotImplemented

    def perimeter(self):
        raise NotImplemented


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


class Triangle(Figure):
    def __init__(self, side1, side2, base, height):
        self.side1 = side1
        self.side2 = side2
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.height * self.base

    def perimeter(self):
        return self.base + self.side2 + self.side1


if __name__ == "__main__":
    figures = [Circle(10), Rectangle(10, 10), Triangle(3, 5, 4, 5)]
    for i in figures:
        print(i.area())
        print(i.perimeter())


# Task 2
class PaymentMethod:
    def pay(self):
        raise NotImplemented


class CreditCard(PaymentMethod):

    def pay(self):
        return f"CreditCard"


class BankTransfer(PaymentMethod):

    def pay(self):
        return f"Bank transfer"


class DigitalMoney(PaymentMethod):
    def pay(self):
        return f"Digital Money"


class PaymentProcessor:
    def __init__(self, *args):
        self.methods = args

    def pay_process(self, method: PaymentMethod):
        if method in self.methods:
            return f"Success payment by {method.pay()}"
        else:
            return f"{method.pay()} is not supported"


if __name__ == "__main__":
    digital = DigitalMoney()
    bank = BankTransfer()
    cred = CreditCard()
    processor = PaymentProcessor(digital, bank)
    print(processor.pay_process(bank))
    print(processor.pay_process(cred))
    print(processor.pay_process(digital))
