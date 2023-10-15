# Task 1
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

class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price


class MenuCategory:
    def __init__(self, name, *dishes):
        self.category = {
            name: dishes
        }


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

first_meal = MenuCategory("first meal", soup, borshc)
second_meal = MenuCategory("second meal", spaghetti)
third_meal = MenuCategory("third meal", pizza_4_cheese)

order = Order()
order.add_item(pizza_4_cheese)
order.add_item(borshc)
order.add_item(soup)

print(order.calculate_total())
order.remove_item(borshc)
print(order.calculate_total())
