class Character:
    def __init__(self, name, healt_points, strenght):
        self.name = name
        self.health_points = healt_points
        self.strenght = strenght
        self.is_alive = True
        self.backpack = []
    
    def get_damage(self, damage):
        self.health_points = self.health_points - damage
        print(f"{self.name} taken {damage} damage. {self.health_points} health left.")
        if self.health_points <= 0:
            print(f"{self.name} has died.")
            self.is_alive = False

class Iteam:
    def __init__(self, name, value, drop_chance):
        self.name = name
        self.value = value
        self.drop_chance = drop_chance

    def add_iteam(self, target):
        target.backpack.append(self)

player = Character("Player", 100, 20)
enemy1 = Character("Orc", 80, 25)
enemy2 = Character("Goblin", 20, 8)

enemies = [enemy1, enemy2]

while player.health_points > 0:
    action = input("What you want to do? (A - attack)")

    if action.lower() == "a":
        enemies_left = [f"{i+1}: {enemy.name} - HP:{enemy.health_points}, DMG:{enemy.strenght}" for i, enemy in enumerate(enemies)]
        print(enemies_left)
        choice = input(f"Who you want to attack?\n{enemies_left}\n")
        to_attack = enemies[int(choice) - 1]
        to_attack.get_damage(player.strenght)
        if to_attack.is_alive:
            player.get_damage[to_attack.strenght]

    for i, enemy in enumerate(enemies):
        if not enemy.is_alive:
            enemies.pop(i)

print("GAME OVER")