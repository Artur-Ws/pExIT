from random import randint


class Character:
    def __init__(self, name, health_points, strength):
        self.name = name
        self.health_points = health_points
        self.strength = strength
        self.is_alive = True
        self.backpack = []

    def get_damage(self, damage):
        self.health_points = self.health_points - damage
        print(f"{self.name} taken {damage} damage. {self.health_points} health left.")
        if self.health_points <= 0:
            print(f"{self.name} has died.")
            self.is_alive = False


class Item:
    def __init__(self, name, value, drop_chance):
        self.name = name
        self.value = value
        self.drop_chance = drop_chance

    def add_item(self, target):
        target.backpack.append(self)


golden_ring = Item("Golden ring", 60, 25)
silver_ring = Item("Silver ring", 30, 45)
golden_necklace = Item("Golden necklace", 120, 10)
gold_pouch = Item("Gold pouch", 10, 60)

player = Character("Player", 100, 20)
enemy1 = Character("Orc", 80, 25)
enemy2 = Character("Goblin", 20, 8)

enemies = [enemy1, enemy2]
items = [golden_ring, silver_ring, golden_necklace, gold_pouch]

while player.health_points > 0:
    print(f"Your backpack contains {[item.name for item in player.backpack]}")

    action = input("What you want to do? (A - attack)\n")
    if action.lower() == "a":
        enemies_left = [f"{i+1}: {enemy.name} (HP:{enemy.health_points} DMG:{enemy.strength})" for i, enemy in enumerate(enemies)]
        choice = input(f"Who you want to attack?\n{enemies_left}\n")
        to_attack = enemies[int(choice) - 1]
        to_attack.get_damage(player.strength)
        if to_attack.is_alive:
            player.get_damage(to_attack.strength)

    for i, enemy in enumerate(enemies):
        if not enemy.is_alive:
            enemies.pop(i)
            loot = []
            for item in items:
                luck = randint(1, 100)
                print(luck)
                if luck <= item.drop_chance:
                    item.add_item(player)
print("GAME OVER")

# for nr, i in enumerate(enemies):
#     print(f"{nr+1}: {i.name}")
