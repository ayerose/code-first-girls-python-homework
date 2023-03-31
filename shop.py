# Tasks:
#
# 1. Create a dictionary with a minimum of 3 items and prices
# a. One of the items needs to cost more than £100
# 2.Customer’s available money is £100
# 3.Welcome the customer and display the items and their prices, along with an option to “exit”
# 4.Accept the option as an input, an invalid input should raise a ValueError
# 5.If the customer can afford it, print out a message saying “Here’s your {item}!”
# 6.The user should be then greeted out of the shop, and the program terminated.
# 7.If the customer cannot afford it, note the attempt and ask if they have more money, if they do and enter the amount it should be added to the balance.
# 8.The purchase should be tried a maximum of 3 items, if it fails a custom error should be raised and the customer will exit the shop.
#


shop = {
  "Book":  7,
  "Lamp": 15,
  "Tablet": 399
}

money_available = 100

def items_in_shop():
    for item, price in shop.items():
        print(f"{item}: £{price:.2f}")

def buy_item(item, money_available):
    try:
        print("Hi, welcome to the shop. Here are our items and their prices:")
        items_in_shop()

        attemps = 0
        while attemps < 3:
            item = input("Please enter the item you would like to buy or type 'exit' to leave: ")
            if item.lower() == "exit":
                break
            if item not in shop:
                raise ValueError("You either entered an invalid item or we don't sell it.")
            if shop[item] <= money_available:
                print(f"Here's your {item}!")
                break
                money_available -= shop[item]
                attemps += 1
            else:
                print("You can't afford that, sorry.")
                add_money = input("Do you have more money? -> 'y' or 'n'")
                if add_money == "y":
                    add_money = float(input("Please enter the amount: "))
                    money_available += add_money
        else:
            raise ValueError("Purchase tried a maximum of 3 items")

    except ValueError as exc:
        print("Invalid input: %s" % exc)

    finally:
        print("Thanks for visiting us. Bye!")
