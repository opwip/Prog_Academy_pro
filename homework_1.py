# Task 1
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


class Cart:
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
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price}'


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


class Order:
    def __init__(self):
        self.order_list = []

    def add_item(self, item):
        self.order_list.append(item)

    def remove_item(self, item):
        if item in self.order_list:
            self.order_list.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.order_list)


spaghetti = Dish("spaghetti", "Tasty spaghetti", 10)
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
        self.disc = disc

    def discount(self):
        return 1 - self.disc


class RegularDiscount(Discount):
    def discount(self):
        return 1 - self.disc


class SilverDiscount(Discount):
    def discount(self):
        return 1 - self.disc


class GoldDiscount(Discount):
    def discount(self):
        return 1 - self.disc


class Client:
    def __init__(self, name, discount: Discount):
        self.name = name
        self.discount = discount

    def get_total_price(self, ordered: Order):
        return ordered.calculate_total() * self.discount.discount()


Silver = SilverDiscount(0.1)
Gold = GoldDiscount(0.2)
Regular = RegularDiscount(0.05)

client1 = Client("Kolya", Silver)
client2 = Client("Ivan", Gold)
print(client1.get_total_price(order))
print(client2.get_total_price(order))
