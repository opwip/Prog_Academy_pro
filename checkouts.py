import loggers
import products


class Cart():
    def __init__(self):
        self.__products = {}

    def add_product(self, product: products.Product):
        if product not in self.__products.keys():
            self.__products[product] = 1
        else:
            self.__products[product] += 1

    def total_price(self):
        return sum(product.price * amount for product, amount in self.__products.items())

    def __str__(self):
        return "\n".join(f"{amount} {product}" for product, amount in self.__products.items())


class Order(loggers.LoggingMixin):
    def __init__(self):
        super(Order, self).__init__()
        self.order_list = []

    def add_item(self, item):
        self.order_list.append(item)
        self.log("Add dish to order")

    def remove_item(self, item):
        self.log("Remove dish from order")
        if item in self.order_list:
            self.order_list.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.order_list)


class Discount:
    def __init__(self, disc):
        if 0 < disc < 1:
            self.disc = disc
        else:
            raise ValueError("Not a valid % amount. Calculating with 0%")

    def discount(self):
        raise NotImplementedError


class RegularDiscount(Discount):
    def discount(self):
        return 1 - self.disc


class SilverDiscount(Discount):
    def discount(self):
        return 1 - self.disc


class GoldDiscount(Discount):
    def discount(self):
        return 1 - self.disc


class Client(loggers.LoggingMixin):
    def __init__(self, name, discount: Discount):
        super(Client, self).__init__()
        self.name = name
        self.discount = discount

    def get_total_price(self, ordered):
        summa = ordered.calculate_total() * self.discount.discount()
        self.log(f"Total price for {self.name} with {self.discount.disc * 100}% discount")
        return summa
