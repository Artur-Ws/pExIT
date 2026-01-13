from random import randint
from ClassCharakter import Character
from ClassItem import Item
from ClassItem import Potion
from ClassItem import Armor
from ClassItem import Weapon


potion1 = Potion('Health potion', 50, 20, 20, 40, 0)
potion2 = Potion('Mana potion', 50, 20, 20, 0, 40)
potion3 = Potion('Beer', 10, 10, -30, 0, 0)

golden_ring = Item("Golden ring", 60, 25)
silver_ring = Item("Silver ring", 60, 45)
golden_necklace = Item("Golden necklace", 120, 10)
gold_pouch = Item("Gold pouch", 10, 60)

player = Character("Player", 100, 25, 50, 50, 50, 0)
enemy1 = Character("Orc", 80, 20, 25, 25, 25, 0)
enemy2 = Character("Goblin", 20, 8, 12, 12, 12, 0)
enemy3 = Character("Sponge Bob", 1000, 1, 75, 75, 75, 0)

potion1.add_iteam(player)
potion2.add_iteam(player)
potion3.add_iteam(player)

enemies = [enemy1, enemy2, enemy3]
items = [golden_ring, silver_ring, golden_necklace, gold_pouch]

while player.health_points > 0:
    print(f"Your backpack contains{[item for item in player.backpack]}")
    action = input("What you want to do? (A - attack, D - drink potion)")

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

    elif action.lower() == "d":
        drink = input("What do you want to drink (H - health potion, M - mana potion, B - beer)")
        if drink.lower() == "h":
            if potion1.is_in_equipment(player.backpack):
                print("MMM ... It's looks like liquid shit... YMM ... and taste even better!")
                player.health_add(potion1.health_addion, potion1.toxicity)
                potion1.potion_used(player)
                print(f"player's HP:{player.health_points}, toxcity: {player.toxicity}")
            
            else:
                print("Potion unavailable")

        elif drink.lower() == "m":
            if potion2.is_in_equipment(player.backpack):
                print("OHH ... Urine ... HMM ... but blue?!")
                player.health_add(potion2.health_addion, potion2.toxicity)
                potion2.potion_used(player)
                print(f"player's MP:{player.health_points}, toxcity: {player.toxicity}")

            else:
                print("Potion unavailable")

        elif drink.lower() == "b":
            if potion3.is_in_equipment(player.backpack):
                print("Ahh... Kuflowe...")
                player.toxicity_add(potion3.toxicity)
                potion3.potion_used(player)
                print(f"player's toxcity: {player.toxicity}")
              
            else:
                print("Potion unavailable")

        else:
            print("Wrong action")
    
    else:
        print("Wrong action")     


print("GAME OVER")
