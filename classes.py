# Task 1
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)



class Product:
    """
    Defines a Product
    """

    def __init__(self, name, price: float, desc):
        self.name = name
        self.price = price
        self.desc = desc

    def __str__(self):
        return f"{self.name}, cost - {self.price}, description - {self.desc}"


class Cart():
    def __init__(self):
        self.__products = {}

    def add_product(self, product: Product):
        if product not in self.__products.keys():
            self.__products[product] = 1
        else:
            self.__products[product] += 1

    def total_price(self):
        return sum(product.price * amount for product, amount in self.__products.items())

    def __str__(self):
        return "\n".join(f"{amount} {product}" for product, amount in self.__products.items())





class Dish:
    def __init__(self, name, description, price):
        try:
            if price > 0:
                self.name = name
                self.description = description
                self.price = price
        except TypeError as error:
            print(f"{name}: Not a valid price(Wrong data type)")
        else:
            if price <= 0:
                print(f"{name}: Not a valid price(<=0)")

    def __str__(self):
        try:
            try:
                return f'{self.name}: {self.price}'
            except AttributeError as error:
                return f"Not in menu{error}"
        except TypeError as error:
            return f"{error}"


class MenuCategories:
    def __init__(self):
        self.menu = {}

    def add_category(self, name):
        if name not in self.menu:
            self.menu[name] = set()

    def add_dish(self, category, dish):
        if category in self.menu:
            self.menu[category].add(dish)

    def __str__(self):
        s = ''
        for category, dishes in self.menu.items():
            s += f'\n{category}:\n' + '\n'.join(map(str, dishes))
        return s


class Order(LoggingMixin):
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
            self.disc = 0
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


class Client(LoggingMixin):
    def __init__(self, name, discount: Discount):
        super(Client, self).__init__()
        self.name = name
        self.discount = discount

    def get_total_price(self, ordered):
        summa = ordered.calculate_total() * self.discount.discount()
        self.log(f"Total price for {self.name} with {self.discount.disc * 100}% discount")
        return summa

