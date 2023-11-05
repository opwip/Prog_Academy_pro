import products
import checkouts

if __name__ == "__main__":
    Product = products.Product
    Cart = checkouts.Cart
    Dish = products.Dish
    MenuCategories = products.MenuCategories
    Order = checkouts.Order
    try:
        print("HW1 TASK 1")
        apple = Product("Apple", 5, "Just an Apple")
        milk = Product("Milk", 20, "A bottle of 2.6% milk")
        tomato = Product("Tomato", 10, "Tomato")
        cart = Cart()
        cart.add_product(apple)
        cart.add_product(milk)
        cart.add_product(apple)
        cart.add_product(apple)
        cart.add_product(milk)
        print(cart)
        print(cart.total_price())
        cart2 = Cart()
        cart2.add_product(apple)
        cart2.add_product(apple)
        cart2.add_product(milk)
        cart2.add_product(tomato)
        cart += cart2
        print(cart)
        for i in cart:
            print("_____________________________________________Test_iter")
            print(i)
    except ValueError:
        print("Not a valid price for a Product")
    # Task 2
    print("HW1 TASK 2")
    try:
        spaghetti = Dish("spaghetti", "Tasty spaghetti", 10)
        spaghetti2 = Dish("spaghetti2", "Tasty spaghetti2", 11)
        spaghetti3 = Dish("spaghetti3", "Tasty spaghetti3", 11)
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
        order2 = Order()
        order2 += spaghetti
        order2 += soup
        for i in order:
            print("_____________________________________________Test_iter")
            print(i)
        print("Test_seq", order[1], "Test_seq")
        print(f"{order2}\n")
        print(f"{order}\n")
        print(order.calculate_total())
        order.remove_item(borshc)
        print(order.calculate_total())
        print(menu)
        print("HW2 TASK 1")
        try:
            Regular = checkouts.RegularDiscount(0.05)
            Silver = checkouts.SilverDiscount(0.1)
            Gold = checkouts.GoldDiscount(0.12)
            client1 = checkouts.Client("Kolya", Silver)
            print(f"{client1.get_total_price(order)} UAH")
            client2 = checkouts.Client("Ivan", Gold)
            print(f"{client2.get_total_price(order)} UAH")
        except ValueError:
            print("Not a valid discount amount")
    except ValueError or AttributeError:
        print("Not a valid price for something")
