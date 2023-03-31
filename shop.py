shop = {
  "Book": 7,
  "Lamp": 15,
  "Tablet": 399
}

money_available = 100

def items_in_shop():
    for item, price in shop.items():
        print(f"{item}: £{price:.2f}")

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
