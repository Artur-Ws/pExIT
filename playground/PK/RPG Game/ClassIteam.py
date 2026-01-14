class Iteam:
    def __init__(self, name, value, drop_chance):
        self.name = name
        self.value = value
        self.drop_chance = drop_chance

    def add_iteam(self, target):
        target.backpack.append(self)
