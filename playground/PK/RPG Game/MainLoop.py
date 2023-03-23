from random import randint
from ClassCharakter import Character
from ClassIteam import Iteam


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
        enemies_left = [f"{i+1}: {enemy.name} - HP:{enemy.health_points}, DMG:{enemy.strenght}" 
                        for i, enemy in enumerate(enemies)]
        choice = input(f"Who you want to attack?\n{enemies_left}\n")
        to_attack = enemies[int(choice) - 1]
        
        if to_attack.dodge():
            pass

        else:
            damage = to_attack.critical_strike(player.strenght, player.crit_chance)
            to_attack.get_damage(damage)

        if to_attack.is_alive:

            if player.dodge():
                pass

            else:
                damage = player.critical_strike(to_attack.strenght, to_attack.crit_chance)
                player.get_damage(damage)

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