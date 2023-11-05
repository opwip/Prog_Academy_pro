import loggers
import products


class CartIterator:
    def __init__(self, products: dict):
        self.products = products.items()
        self.index = 0
        self.product_ = []
        self.amount_ = []
        for product, amount in self.products:
            self.product_.append(product)
            self.amount_.append(amount)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.product_):
            self.index += 1
            return f"{self.amount_[self.index - 1]} {self.product_[self.index - 1]}"
        raise StopIteration


class OrderIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1]
        raise StopIteration


class Cart:
    def __init__(self):
        self.__products = {}

    def add_product(self, product: products.Product):
        if product not in self.__products.keys():
            self.__products[product] = 1
        else:
            self.__products[product] += 1

    def __iadd__(self, other):
        if isinstance(other, Cart):
            for key, value in other.__products.items():
                if key in self.__products.keys():
                    self.__products[key] += value
                else:
                    self.__products[key] = value
            return self
        else:
            raise TypeError

    def total_price(self):
        return sum(product.price * amount for product, amount in self.__products.items())

    def __str__(self):
        return "\n".join(f"{amount} {product}" for product, amount in self.__products.items())

    def __iter__(self):
        return CartIterator(self.__products)


class Order(loggers.LoggingMixin):
    def __init__(self):
        super(Order, self).__init__()
        self.order_list = []

    def add_item(self, item):
        self.order_list.append(item)
        self.log("Add dish to order")

    def __iadd__(self, other):
        if isinstance(other, products.Dish):
            self.add_item(other)
            return self
        else:
            raise TypeError

    def remove_item(self, item):
        self.log("Remove dish from order")
        if item in self.order_list:
            self.order_list.remove(item)

    def calculate_total(self):
        return sum(item.price for item in self.order_list)

    def __str__(self):
        return "\n" .join(f"{i}" for i in self.order_list)

    def __getitem__(self, item):
        return self.order_list[item]

    def __len__(self):
        return len(self.order_list)

    def __iter__(self):
        return OrderIterator(self.order_list)


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
