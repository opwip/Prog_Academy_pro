# Task 1
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger(self.__class__.__name__)

    def log(self, message, level=logging.INFO):
        self.logger.log(level, message)


print("HW1 TASK 1")


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


apple = Product("Apple", 5, "Just an Apple")
milk = Product("Milk", 20, "A bottle of 2.6% milk")
cart = Cart()
cart.add_product(apple)
cart.add_product(milk)
cart.add_product(apple)
cart.add_product(apple)
cart.add_product(milk)
print(cart)
print(cart.total_price())

# Task 2
print("HW1 TASK 2")


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
                return "Not in menu"
        except TypeError as error:
            return "Kla"


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


spaghetti = Dish("spaghetti", "Tasty spaghetti", 10)
spaghetti2 = Dish("spaghetti2", "Tasty spaghetti2", -11)
spaghetti3 = Dish("spaghetti3", "Tasty spaghetti3", "11")
pizza_4_cheese = Dish("pizza 4 cheese", "Tasty pizza with 4 cheeses", 40)
soup = Dish("soup", "Tasty soup", 15)
borshc = Dish("borshc", "Tasty borshc", 15)

menu = MenuCategories()

menu.add_category("first meal")
menu.add_category("second meal")
menu.add_category("third meal")

menu.add_dish("first meal", soup)
menu.add_dish("first meal", borshc)
menu.add_dish("second meal", spaghetti)
menu.add_dish("third meal", pizza_4_cheese)

order = Order()
order.add_item(pizza_4_cheese)
order.add_item(borshc)
order.add_item(soup)

print(order.calculate_total())
order.remove_item(borshc)
print(order.calculate_total())
print(menu)

# Task HW2.1
print("HW2 TASK 1")


class Discount:
    def __init__(self, disc):
        if 0 < disc < 1:
            self.disc = disc
        else:
            print("Not a valid % amount. Calculating with 0%")
            self.disc = 0


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

    def get_total_price(self, ordered: Order):
        summa = ordered.calculate_total() * self.discount.discount()
        self.log(f'Customer pay {summa}', logging.INFO)
        return summa


Regular = RegularDiscount(0.05)
Silver = SilverDiscount(0.1)
Gold = GoldDiscount(12)

client1 = Client("Kolya", Silver)
client2 = Client("Ivan", Gold)
print(client1.get_total_price(order))
print(client2.get_total_price(order))
