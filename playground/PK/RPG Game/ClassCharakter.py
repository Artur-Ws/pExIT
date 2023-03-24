from random import randint


class Character:
    def __init__(self, name, health_points, strenght, crit_chacne, agility, defend, mana_points):
        self.name = name
        self.health_points = health_points
        self.strenght = strenght
        self.crit_chance = crit_chacne
        self.agility = agility
        self.defend = defend
        self.mana_points = mana_points
        self.toxicity = 0
        self.is_alive = True
        self.backpack = []
        self.equipment = []
    #is it ok to add crit strike like that?
    def get_damage(self, damage):
        self.health_points = self.health_points - self.reduced_damage(damage)
        print(f"{self.name} taken {self.reduced_damage(damage)} damage. {self.health_points} health left.")

        if self.health_points <= 0:
            print(f"{self.name} has died.")
            self.is_alive = False

    def critical_strike(self, damage, crit_luck):
        crit_randomise = randint(1,100)
        print(f"Attacker crit chance is: {crit_randomise}") 

        if crit_luck >= crit_randomise:
            print(f"CRITICAL STRIKE LOADED")
            damage *= 2
            return damage

        else:
            print(f"Critical strike not loaded")
            return damage

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
    
    def health_add(self, health_addion, toxicity):
        self.health_points += health_addion
        self.toxicity_add(toxicity)
    
    def mana_add(self, mana_addion, toxicity):
        self.mana_points += mana_addion
        self.toxicity_add(toxicity)

    def toxicity_add(self, toxicity):
        self.toxicity += toxicity
        if self.toxicity < 0:
            self.toxicity = 0
        
        # self.potion_used(player)

    # def potion_used(self,player):
    #     player.backpack.pop(self)
    #     print('Potion used')
