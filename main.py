import classes

if __name__ == "__main__":

    Product = classes.Product
    Cart = classes.Cart
    Dish = classes.Dish
    MenuCategories = classes.MenuCategories
    Order = classes.Order

    print("HW1 TASK 1")
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

    try:
        Regular = classes.RegularDiscount(0.05)
        Silver = classes.SilverDiscount(0.1)
        Gold = classes.GoldDiscount(12)
        client1 = classes.Client("Kolya", Silver)
        print(client1.get_total_price(order))
        client2 = classes.Client("Ivan", Gold)
        print(client2.get_total_price(order))
    except ValueError:
        pass
