from random import randint


class Character:
    def __init__(self, name, healt_points, strenght, crit_chacne, agility, defend):
        self.name = name
        self.health_points = healt_points
        self.strenght = strenght
        self.crit_chance = crit_chacne
        self.agility = agility
        self.defend = defend
        self.is_alive = True
        self.backpack = []
        
    #is it ok to add crit strike like that?
    def get_damage(self, damage, crit_luck):
        crit_randomise = randint(1,100)
        print(f"Attacker crit chance is: {crit_randomise}")

        if crit_luck >= crit_randomise:
            print(f"CRITICAL STRIKE LOADED")
            damage *= 2
            self.health_points = self.health_points - self.reduced_damage(damage) #self.health_points = self.health_points - (damage * 2) #not working
            print(f"{self.name} taken {self.reduced_damage(damage)} damage. {self.reduced_damage(damage)} health left.")

            if self.health_points <= 0:
                print(f"{self.name} has died.")
                self.is_alive = False

        else:
            print(f"CRITICAL STRIKE NOT LOADED")
            self.health_points = self.health_points - self.reduced_damage(damage)
            print(f"{self.name} taken {self.reduced_damage(damage)} damage. {self.health_points} health left.")
            if self.health_points <= 0:
                print(f"{self.name} has died.")
                self.is_alive = False
        
    def dodge(self):
        dodge_luck = randint(1,100)
        print(f"Dodge luck: {dodge_luck}")
        
        if self.agility >= dodge_luck:
            print(f"{self.name} DODGE!")
            return True
        
        else:
            print(f"{self.name} Not dodged")
            return False
        
    def reduced_damage(self, damage):
        damage = damage * (1 - (self.defend/100))
        return damage


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

player = Character("Player", 100, 25, 50, 50, 50)
enemy1 = Character("Orc", 80, 20, 25, 25, 25)
enemy2 = Character("Goblin", 20, 8, 12, 12, 12)
enemy3 = Character("Sponge Bob", 1000, 1, 75, 75, 75)

enemies = [enemy1, enemy2, enemy3]
items = [golden_ring, silver_ring, golden_necklace, gold_pouch]

while player.health_points > 0:
    print(f"Your backpack contains{[item for item in player.backpack]}")
    action = input("What you want to do? (A - attack)")

    if action.lower() == "a":
        enemies_left = [f"{i+1}: {enemy.name} - HP:{enemy.health_points}, DMG:{enemy.strenght}" for i, enemy in enumerate(enemies)]
        choice = input(f"Who you want to attack?\n{enemies_left}\n")
        to_attack = enemies[int(choice) - 1]
        
        if to_attack.dodge():
            pass

        else:
            to_attack.get_damage(player.strenght, player.crit_chance)

        if to_attack.is_alive:

            if player.dodge():
                pass

            else:
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