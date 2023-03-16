from datetime import datetime


class Product:
    serial = 10000
    def __init__(self, name, price):
        self.name = name
        self.price = price


    def change_price(self, percentage):
        self.price *= 1 + percentage/100


class Consumable(Product):
    def __init__(self, name, price, expiration):
        super().__init__(name, price)
        self.expiration = datetime.fromisoformat(expiration).date()
        self.serial = 9999

    def __repr__(self):
        return f"Product: {self.name}, price: {self.price}, consumable serial number: {self.serial}, " \
               f"general serial: {super().serial}"

    def is_unexpired(self):
        today = datetime.today().date()
        return True if today <= self.expiration else False

    def __lt__(self, other):
        if isinstance(other, Consumable):
            return self.expiration < other.expiration


class Fruit(Consumable):
    def __init__(self, name, price, expiration, country):
        super().__init__(name, price, expiration)
        self.country = country


shirt = Product("polo", 100)

print(shirt.price)
shirt.change_price(20)
print(shirt.price)

apple = Consumable("Apple", 5, "2023-03-19")

print(apple.is_unexpired())
print(apple.price)
apple.change_price(10)
print(apple.price)

banana = Fruit("banana", 8, "2023-03-18", "Nigeria")

print(banana.price)
banana.change_price(50)
print(banana.price)

print(apple)
print("-"*100)


class BetterList(list):
    def __mul__(self, other):
        return [i * other for i in self]

    def __call__(self, *args, **kwargs):
        print(f"Better list was called, here it is: {self}")


l1 = list((1, 2, 3, 4))
l2 = BetterList((1, 2, 3, 4))
print(l1*3)
print(l2*3)

l2()

print("-"*100)

print(apple < banana)

print(banana)

