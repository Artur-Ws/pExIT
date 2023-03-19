from random import randint
class Character:
    def __init__(self, name, healt_points, strenght, crit_chacne):
        self.name = name
        self.health_points = healt_points
        self.strenght = strenght
        self.crit_chance = crit_chacne
        self.is_alive = True
        self.backpack = []
        
    
    #is it ok to add crit strike like that?
    def get_damage(self, damage, crit_luck):
        crit_randomise = randint(1,100)
        print(f"Attacker crit chance is: {crit_randomise}")
        if crit_luck >= crit_randomise:
            print(f"CRITICAL STRIKE LOADED")
            damage *= 2
            self.health_points = self.health_points - damage
            print(f"{self.name} taken {damage} damage. {self.health_points} health left.")
            if self.health_points <= 0:
                print(f"{self.name} has died.")
                self.is_alive = False
        else:
            print(f"CRITICAL STRIKE NOT LOADED")
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

golden_ring = Iteam("Golden ring", 60, 25)
silver_ring = Iteam("Silver ring", 60, 45)
golden_necklace = Iteam("Golden necklace", 120, 10)
gold_pouch = Iteam("Gold pouch", 10, 60)

player = Character("Player", 100, 25, 50)
enemy1 = Character("Orc", 80, 20, 25)
enemy2 = Character("Goblin", 20, 8, 12)

enemies = [enemy1, enemy2]
items = [golden_ring, silver_ring, golden_necklace, gold_pouch]

while player.health_points > 0:
    print(f"Your backpack contains{[item for item in player.backpack]}")
    action = input("What you want to do? (A - attack)")

    if action.lower() == "a":
        enemies_left = [f"{i+1}: {enemy.name} - HP:{enemy.health_points}, DMG:{enemy.strenght}" for i, enemy in enumerate(enemies)]
        print(enemies_left)
        choice = input(f"Who you want to attack?\n{enemies_left}\n")
        to_attack = enemies[int(choice) - 1]
        to_attack.get_damage(player.strenght, player.crit_chance)
        if to_attack.is_alive:
            player.get_damage(to_attack.strenght, to_attack.crit_chance)

    for i, enemy in enumerate(enemies):
        if not enemy.is_alive:
            enemies.pop(i)
            loot = []
            for item in items:
                luck = randint(1,100)
                print(luck)
                if luck <= item.drop_chance:
                    item.add_iteam(player)


print("GAME OVER")