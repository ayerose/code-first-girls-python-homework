
from unittest import TestCase, main
from shop import buy_item


class PurchaseItemFunction(TestCase):
    def test_not_in_shop(self):
        shop = {
            "Book": 7,
            "Lamp": 15,
            "Tablet": 399
        }

        item = "Banana"
        money_available = 100
        expected = "Invalid input: You either entered an invalid item or we don't sell it."
        self.assertEqual(buy_item(item, money_available), expected)

    def test_purchase_item_and_exit(self):
        item = "Book"
        money_available = 100
        expected = ["Here's your Book!", "Thanks for visiting us. Bye!"]
        self.assertEqual(buy_item(item, money_available), expected)

    def test_can_afford_item(self):
        item = "Lamp"
        money_available = 100
        expected = "Here's your Lamp!"
        self.assertEqual(buy_item(item, money_available), expected)

    def test_cannot_afford_item(self):
        item = "Tablet"
        money_available = 100
        expected = ["You can't afford that, sorry.", "Do you have more money? -> 'y' or 'n'"]
        self.assertEqual(buy_item(item, money_available), expected)


if __name__ == "__main__":
    main()