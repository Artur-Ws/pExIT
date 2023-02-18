"""
Look at given list of items. There is exactly one piece of each listed item on store shelf.

Implement a shopping function for customers to buy products. You code should: print all available products in the shop,
allow user to add products to their cart, until customer decides to end shopping, or all products from shop
will be chosen. Each time customer want to add product to cart, program should check if such item is available
in the shop, if it is, program should add this item to customer cart, then it should be removed from store list.

At the end of shopping function should return customer cart list, and list with shop remaining products.


"""

shop_contains = ["banana", "apple", "water", "milk", "bread", "pasta", "rice", "juice", "cookies", "peanuts"]


def shopping(available_products):
    customer_cart = []

    return customer_cart, available_products


chosen_products, left_in_shop = shopping(shop_contains)

print(f"In your cart: {chosen_products} \nLeft in shop: {left_in_shop}")
