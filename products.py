class Product:
    """
    Defines a Product
    """

    def __init__(self, name, price: float, desc):
        if isinstance(price, int | float) and price > 0:
            self.name = name
            self.desc = desc
            self.price = price
        else:
            raise ValueError("Not a valid price for a Product")

    def __str__(self):
        return f"{self.name}, cost - {self.price}, description - {self.desc}"


class Dish:
    def __init__(self, name, description, price):
        if isinstance(price, int | float) and price > 0:
            self.name = name
            self.description = description
            self.price = price
        else:
            raise ValueError("Not a valid price for a Dish")

    def __str__(self):
        if self.name:
            return f'{self.name}: {self.price}'
        else:
            raise AttributeError("Not in menu")


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
